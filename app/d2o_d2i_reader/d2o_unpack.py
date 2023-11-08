import io, sys, os, json
from pathlib import Path

from d2o_d2i_reader.pydofus.d2o import D2OReader, InvalidD2OFile

# python d2o_unpack.py (all files in input folder)
# folder output: ./output/{all files}


def d2o_unpack(
    input_folder, output_folder=os.path.join(Path(__file__).parent, "d2o_output")
):
    for file in os.listdir(input_folder):
        if file in [
            "Items.d2o",
            "ItemSets.d2o",
            "ItemTypes.d2o",
            "ItemSuperTypes.d2o",
        ]:
            file_name = os.path.basename(file)
            d2p_file = open(os.path.join(input_folder, file), "rb")

            print("D2O Unpacker for " + file_name)

            try:
                d2o_reader = D2OReader(d2p_file)
                d2o_data = d2o_reader.get_objects()

                json_output = open(
                    os.path.join(output_folder, file_name.replace("d2o", "json")),
                    "w",
                )
                json.dump(d2o_data, json_output, indent=4)
                json_output.close()
            except InvalidD2OFile:
                pass
