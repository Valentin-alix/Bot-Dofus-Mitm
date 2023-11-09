import os
from pathlib import Path
import sys
from dotenv import load_dotenv

from decompile_code_source import get_as_scripts


ROOT_DIR = str(Path(__file__).parent.parent)
sys.path.append(ROOT_DIR)


from dofus_unpack.d2i_unpack import d2i_unpack
from dofus_unpack.d2o_unpack import d2o_unpack
from init_bdd import init_bdd


if __name__ == "__main__":
    load_dotenv()

    get_as_scripts()

    os.system("python app/network/protocol/build_protocol.py")

    resources_path = os.path.join(Path(__file__).parent.parent.parent, "resources")

    print(os.path.join(resources_path, "from_d2o"))
    d2o_unpack(
        os.environ.get("D2O_FOLDER"),
        output_folder=os.path.join(resources_path, "from_d2o"),
    )
    d2i_unpack(
        os.environ.get("D2I_FILE"), os.path.join(resources_path, "from_d2i.json")
    )
    # d2p_unpack(os.environ.get("D2P_FOLDER"))
    # d2p_unpack(os.environ.get("D2P_FOLDER2"))

    init_bdd()
