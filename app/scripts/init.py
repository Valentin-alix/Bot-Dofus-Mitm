import os
import sys
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = str(Path(__file__).parent.parent.parent)
sys.path.append(ROOT_DIR)

from app.scripts.decompile_code_source import get_as_scripts
from app.scripts.generate_python_class import (
    launch_generator,
)
from dofus_unpack.d2i_unpack import d2i_unpack
from dofus_unpack.d2o_unpack import d2o_unpack
from init_bdd import init_bdd

if __name__ == "__main__":
    load_dotenv()

    get_as_scripts()
    os.system(
        f"python {os.path.join(Path(__file__).parent.parent, 'network', 'protocol', 'build_protocol.py')}"
    )
    launch_generator()

    resources_path = os.path.join(Path(__file__).parent.parent.parent, "resources")
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
