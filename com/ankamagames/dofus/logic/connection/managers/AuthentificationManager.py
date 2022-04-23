from argparse import ArgumentError
import os
from com.ankamagames.dofus.BuildInfos import BuildInfos
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager__verifyKey import (
    AuthentificationManager__verifyKey,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import (
    IdentificationMessage,
)
from com.ankamagames.dofus.network.types.version.Version import Version
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.hurlan.crypto.symmetric.AESKey import AESKey
from com.hurlan.crypto.symmetric.CBCMode import CBCMode
from com.hurlan.crypto.symmetric.NullPAd import NullPad
from com.hurlan.crypto.symmetric.PKCS1 import PKCS1
from com.hurlan.crypto.symmetric.PSAKey import RSACipher
from com.hurlan.crypto.symmetric.SimpleIVMode import SimpleIVMode
from Cryptodome.PublicKey import RSA

logger = Logger(__name__)
ROOTDIR = os.path.dirname(__file__)


class AuthentificationManager(metaclass=Singleton):
    _verifyKey = AuthentificationManager__verifyKey.create()
    AES_KEY_LENGTH = 32
    _publicKey: str = None
    _salt: str = None
    gameServerTicket: str = None
    _AESKey: ByteArray = None
    nextToken: str = None
    tokenMode: bool = None
    username: str = None
    _password = None
    _certificate = None

    def initAESKey(self):
        self._AESKey = AESKey.generateRandomAESKey(self.AES_KEY_LENGTH)

    def setSalt(self, salt: str) -> None:
        if len(salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(salt) < 32:
            salt += " "
        self._salt = salt

    def setPublicKey(self, enc_publicKey: list[int]):
        baSignedKey = ByteArray.from_int8Arr(enc_publicKey)
        rsacipher = RSACipher(self._verifyKey, PKCS1())
        ba_pubKey = ByteArray()
        if not rsacipher.verify(baSignedKey, ba_pubKey):
            raise Exception("Pubkey Sign validation failed!")
        self._publicKey = (
            "-----BEGIN PUBLIC KEY-----\n"
            + str(ba_pubKey)
            + "\n-----END PUBLIC KEY-----"
        )

    def getCanAutoConnectWithToken(self) -> bool:
        return self.nextToken != None

    def setCredentials(self, username, password):
        self.username = username
        self._password = password

    def setToken(self, token: str):
        self._token = token
        self.username = "   "

    def getIdentificationMessage(self) -> IdentificationMessage:
        imsg = NetworkMessage.from_json(
            {
                "__type__": "IdentificationMessage",
                "autoconnect": False,
                "credentials": self.getAuthCredentials(),
                "failedAttempts": [],
                "lang": "fr",
                "serverId": 0,
                "sessionOptionalSalt": 0,
                "useCertificate": False,
                "useLoginToken": True,
                "version": {
                    "__type__": "Version",
                    "build": BuildInfos.VERSION.build,
                    "buildType": BuildInfos.VERSION.buildType,
                    "code": BuildInfos.VERSION.code,
                    "major": BuildInfos.VERSION.major,
                    "minor": BuildInfos.VERSION.minor,
                },
            }
        )
        return imsg

    def getAuthCredentials(self) -> list[int]:
        baIn = ByteArray()
        baIn += bytes(self._salt, "utf")
        baIn += self._AESKey
        baIn += len(self.username).to_bytes(1, "big")
        baIn += bytes(self.username, "utf")
        baIn += bytes(self._token, "utf")
        rsa_key = RSA.importKey(bytes(self._publicKey, "utf"))
        rsacipher = RSACipher(rsa_key, PKCS1())
        baOut = rsacipher.encrypt(baIn)
        return baOut.to_int8Arr()

    def decodeWithAES(self, byteArrayOrVector) -> ByteArray:
        aescipher = SimpleIVMode(CBCMode(AESKey(self._AESKey), NullPad()))
        result = ByteArray()
        result.writeByteArray(self._AESKey, 0, 16)

        if type(byteArrayOrVector) == list:
            for i in byteArrayOrVector:
                result.writeByte(i, signed=True)

        else:
            if not isinstance(byteArrayOrVector, ByteArray):
                raise ArgumentError(
                    "Argument must be a bytearray or a vector of int/uint"
                )
            result.writeByteArray(byteArrayOrVector)

        aescipher.decrypt(result)
        return result
