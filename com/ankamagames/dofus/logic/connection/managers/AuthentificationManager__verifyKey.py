from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from Cryptodome.PublicKey import RSA
import com.ankamagames.dofus.Constants as Constants


class AuthentificationManager__verifyKey:
    VERIFY_KEY_PATH = (
        Constants.BINARY_DATA_DIR
        / "115_com.ankamagames.dofus.logic.connection.managers.AuthentificationManager__verifyKey_com.ankamagames.dofus.logic.connection.managers.AuthentificationManager__verifyKey.bin"
    )

    def create() -> RSA.RsaKey:
        with open(AuthentificationManager__verifyKey.VERIFY_KEY_PATH, "rb") as fp:
            return RSA.import_key(fp.read())
