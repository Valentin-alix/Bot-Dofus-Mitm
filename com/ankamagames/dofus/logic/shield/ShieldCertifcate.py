import base64
from hashlib import md5, sha256
import os
import re
from com.ankamagames.dofus.logic.shield.ShieldSecureLevel import ShieldSecureLevel
from com.ankamagames.dofus.network.types.secure.TrustCertificate import TrustCertificate
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.AESKey import AESKey
from com.hurlan.crypto.symmetric.ECBMode import ECBMode
from flash.Capabilities import Capabilities


logger = Logger(__name__)


class ShieldCertifcate:
    HEADER_BEGIN: str = "SV"

    HEADER_V1: str = HEADER_BEGIN + "1"

    HEADER_V2: str = HEADER_BEGIN + "2"

    HEADER_V3: str = HEADER_BEGIN + "3"

    HEADER_V4: str = HEADER_BEGIN + "4"

    version: int

    id: int

    content: str

    useBasicNetworkInfo: bool

    useAdvancedNetworkInfo: bool

    useBasicInfo: bool

    useUserInfo: bool

    filterVirtualNetwork: bool

    def __init__(self, version: int = 4):
        super().__init__()
        if version == 1:
            self.useAdvancedNetworkInfo = False
            self.useBasicNetworkInfo = False
            self.useBasicInfo = False
            self.useUserInfo = False
            self.filterVirtualNetwork = False
        if version == 2:
            self.useAdvancedNetworkInfo = True
            self.useBasicNetworkInfo = True
            self.useBasicInfo = True
            self.useUserInfo = True
            self.filterVirtualNetwork = False
        if version in [3, 4]:
            self.useAdvancedNetworkInfo = False
            self.useBasicNetworkInfo = True
            self.useBasicInfo = True
            self.useUserInfo = True
            self.filterVirtualNetwork = True
        self.version = version

    @classmethod
    def fromRaw(
        cls, data: ByteArray, output: "ShieldCertifcate" = None
    ) -> "ShieldCertifcate":
        result: ShieldCertifcate = output if output is not None else ShieldCertifcate()
        data.position = 0
        header: str = data.readUTFBytes(3)
        if header[:2] != cls.HEADER_BEGIN:
            header = cls.HEADER_V1
        if header == cls.HEADER_V1:
            result.version = 1
            data.position = 0
            result.id = data.readUnsignedInt()
            result.content = data.readUTF()
            result.useAdvancedNetworkInfo = False
            result.useBasicNetworkInfo = False
            result.useBasicInfo = False
            result.useUserInfo = False
            result.filterVirtualNetwork = False
        if header == cls.HEADER_V2:
            result.version = 2
            result.id = data.readUnsignedInt()
            result.useAdvancedNetworkInfo = True
            result.useBasicNetworkInfo = True
            result.useBasicInfo = True
            result.useUserInfo = True
            result.filterVirtualNetwork = False
            result.content = result.decrypt(data)
        if header in [cls.HEADER_V3, cls.HEADER_V4]:
            result.version = 4 if header == cls.HEADER_V4 else 3
            result.id = data.readUnsignedInt()
            infoLen = data.readShort()
            for _ in range(infoLen):
                name = data.readUTF()
                value = data.readBoolean()
                logger.debug(f"{name} = {value}")
                setattr(result, name, value)
            result.content = result.decrypt(data)
        logger.debug("Certificat V{} : {}".format(result.version, result.content))
        return result

    @property
    def secureLevel(self) -> int:
        pass

    @secureLevel.setter
    def secureLevel(self, level: int) -> None:
        if level == ShieldSecureLevel.LOW:
            self.useAdvancedNetworkInfo = False
            self.useBasicNetworkInfo = False
            self.useBasicInfo = False
            self.useUserInfo = False
            self.filterVirtualNetwork = False
        if level == ShieldSecureLevel.MEDIUM:
            self.useAdvancedNetworkInfo = False
            self.useBasicNetworkInfo = False
            self.useBasicInfo = True
            self.useUserInfo = True
            self.filterVirtualNetwork = False
        if level == ShieldSecureLevel.MAX:
            self.useAdvancedNetworkInfo = True
            self.useBasicNetworkInfo = True
            self.useBasicInfo = True
            self.useUserInfo = True
            self.filterVirtualNetwork = True

    @property
    def hash(self) -> str:
        return self.getHash()

    @property
    def reverseHash(self) -> str:
        return self.getHash(True)

    def serialize(self) -> ByteArray:
        result: ByteArray = ByteArray()
        if self.version == 1:
            raise Exception("No more supported")

        if self.version == 2:
            result.writeUTF(self.HEADER_V2)
            result.writeUnsignedInt(self.id)
            result.writeUTF(self.content)

        if self.version in [3, 4]:
            result.writeUTF(self.HEADER_V4 if self.version == 4 else self.HEADER_V3)
            result.writeUnsignedInt(self.id)
            info = [
                "useBasicInfo",
                "useBasicNetworkInfo",
                "useAdvancedNetworkInfo",
                "useUserInfo",
            ]
            result.writeShort(len(info))
            for i in range(len(info)):
                result.writeUTF(info[i])
                result.writeBoolean(self[info[i]])
                result.writeUTF(self.content)
        return result

    def toNetwork(self) -> TrustCertificate:
        certif: TrustCertificate = TrustCertificate()
        hash: str = sha256(
            bytes.fromhex(self.getHash()) + self.content.encode()
        ).hexdigest()
        certif.init(self.id, hash)
        return certif

    def decrypt(self, data: ByteArray) -> str:
        key: ByteArray = ByteArray()
        hex_hash = self.getHash(True)
        key.writeByteArray(bytes.fromhex(hex_hash))
        aesKey: AESKey = AESKey(key)
        ecb: ECBMode = ECBMode(aesKey)
        data_base64 = data.readUTFBytes(data.remaining())
        data_bytes = base64.b64decode(data_base64)
        cryptedData: ByteArray = ByteArray(data_bytes)
        try:
            ecb.decrypt(cryptedData)
        except Exception as e:
            logger.error("Certificat V2 non valide (clef invalide)", exc_info=True)
            raise
        cryptedData.position = 0
        return cryptedData.decode("utf-8")

    def getHash(self, reverse: bool = False) -> str:
        data: list = []
        if self.useBasicInfo:
            data.append(Capabilities.cpuArchitecture)
            if Capabilities.os == "Windows 10" and self.version < 4:
                data.append("Windows 8")
            elif "Darwin" in Capabilities.os and self.version > 3:
                data.append("Mac OS")
            else:
                logger.debug("cert version : {}".format(self.version))
                data.append(Capabilities.os)
            data.append(Capabilities.maxLevelIDC)
            data.append(Capabilities.language)
        if self.useUserInfo:
            try:
                data.append(os.getlogin())
            except Exception as e:
                logger.error("User non disponible.")
        if reverse:
            data.reverse()
        data_str = ",".join(data)
        logger.debug(f"data before Hash : {data_str}")
        hash = md5(data_str.encode()).hexdigest()
        return hash

    # def traceInfo(self, target, maxDepth:int = 5, inc:str = "") -> None:
    #    logger.info("-----------")
    #    logger.info("active : " + target.active)
    #    logger.info("hardwareAddress : " + target.hardwareAddress)
    #    logger.info("name : " + target.hardwareAddress)
    #    logger.info("displayName : " + target.displayName)
    #    logger.info("parent : " + target.parent)
    #    if target.parent and maxDepth:
    #       self.traceInfo(target.parent,maxDepth--,inc + "...")
