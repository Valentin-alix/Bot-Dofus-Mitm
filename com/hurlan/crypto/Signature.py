import hashlib
import traceback
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.SignatureKey import SignatureKey
from Cryptodome.PublicKey import RSA
from com.hurlan.crypto.symmetric.PKCS1 import PKCS1
from com.hurlan.crypto.symmetric.PSAKey import RSACipher


class SignatureError(Exception):
    pass


class Signature:
    ANKAMA_SIGNED_FILE_HEADER: str = "AKSF"
    SIGNATURE_HEADER: str = "AKSD"

    def __init__(self, key1: SignatureKey, key2: RSA.RsaKey):
        self.key1 = key1
        self.key2 = key2

    def verify(self, input: ByteArray) -> ByteArray:
        headerSize = input.readUnsignedShort()
        if headerSize != len(self.ANKAMA_SIGNED_FILE_HEADER):
            input.position = 0
            headerPosition = input.remaining() - len(self.ANKAMA_SIGNED_FILE_HEADER)
            input.position = headerPosition
            header = input.readUTFBytes(len(self.ANKAMA_SIGNED_FILE_HEADER))
            if header == self.ANKAMA_SIGNED_FILE_HEADER:
                return self.verifyV2Signature(input, headerPosition)
        else:
            header = input.readUTFBytes(len(self.ANKAMA_SIGNED_FILE_HEADER))
            if header == self.ANKAMA_SIGNED_FILE_HEADER:
                return self.verifyV1Signature(input)
        raise SignatureError("Invalid header")

    def verifyV2Signature(self, input: ByteArray, headerPosition: int) -> bool:
        if not self.key2:
            raise SignatureError("No key for self signature version (2)")
        try:
            input.position = headerPosition - 4
            signedDataLenght = input.readShort()
            input.position = headerPosition - 4 - signedDataLenght
            cryptedData = input.readBytes(0, signedDataLenght)
            rsaceipher = RSACipher(self.key2, PKCS1())
            sigData = ByteArray()
            if not rsaceipher.verify(cryptedData, sigData):
                return False
            sigData.position = 0
            sigHeader = sigData.readUTF()
            if sigHeader != self.SIGNATURE_HEADER:
                return None
            sigVersion = sigData.readByte()
            sigData.readInt()
            sigData.readInt()
            sigFileLenght = sigData.readInt()
            if sigFileLenght != headerPosition - 4 - signedDataLenght:
                return None
            hashType = sigData.readByte()
            sigHash = sigData.readUTF()
            input.position = 0
            output = input.readBytes(0, headerPosition - 4 - signedDataLenght)
            if hashType == 0:
                contentHash = hashlib.md5(output).hexdigest()
            elif hashType == 1:
                contentHash = hashlib.sha256(output).hexdigest()
            else:
                return None
            if sigHash != contentHash:
                return None
        except Exception as e:
            traceback.print_exc()
            return None
        return output

    def verifyV1Signature(self, input: ByteArray) -> bytearray:
        len: int = 0
        try:
            len = input.readInt()
            sigData = input.readBytes(0, len)
        except Exception as e:
            raise SignatureError("Invalid signature format, not enough data.")

        try:
            decryptedHash = ByteArray()
            rsacipher = RSACipher(self.key1, PKCS1())
            rsacipher.verify(sigData, decryptedHash)
        except Exception as e:
            return None

        decryptedHash.position = 0
        ramdomPart = decryptedHash.readByte()
        for i in range(len(decryptedHash)):
            decryptedHash[i] ^= ramdomPart

        contentLen: int = decryptedHash.readUnsignedInt()
        testedContentLen: int = input.remaining()
        signHash: str = decryptedHash.readUTFBytes(decryptedHash.remaining())[1:]
        output = ByteArray(input.readBytes())
        contentHash: str = hashlib.md5(
            output.readUTFBytes(output.remaining())
        ).hexdigest()[1:]
        if signHash and signHash == contentHash and contentLen == testedContentLen:
            return output
        else:
            return None
