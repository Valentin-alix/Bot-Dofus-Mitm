from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from Cryptodome.PublicKey import RSA


class SignatureKey:
    PUBLIC_KEY_HEADER: str = "DofusPublicKey"
    PRIVATE_KEY_HEADER: str = "DofusPrivateKey"

    @staticmethod
    def import_key(input: ByteArray):
        header: str = input.readUTF()
        if (
            header != SignatureKey.PUBLIC_KEY_HEADER
            and header != SignatureKey.PRIVATE_KEY_HEADER
        ):
            raise Exception("Invalid public or private header")
        if header == SignatureKey.PUBLIC_KEY_HEADER:
            N = input.readUTF()
            N = int.from_bytes(bytes(N, "utf"), "big")
            E = input.readUTF()
            E = int.from_bytes(bytes(E, "utf"), "big")
            return RSA.RsaKey(n=N, e=E)
