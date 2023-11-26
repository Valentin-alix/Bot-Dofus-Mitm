import os
import shutil
from pathlib import Path


def get_as_scripts():
    output_as_scripts = os.path.join(
        Path(__file__).parent.parent.parent, "resources", "code_source"
    )
    selected_classes = "com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++"
    if os.path.exists(output_as_scripts):
        shutil.rmtree(output_as_scripts)
    os.system(
        f'java -jar "{os.environ.get("FFDECJAR_PATH")}"\
        -config parallelSpeedUp=0 -selectclass {selected_classes}\
        -export script "{output_as_scripts}" "{os.environ.get("DOFUS_INVOKER")}"'
    )
