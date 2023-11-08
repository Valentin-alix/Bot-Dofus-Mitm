import sys, json, os

from d2o_reader.pydofus.d2i import D2I


def d2i_unpack(input_file, output_file=os.path.join("output", "i18n_fr.json")):
    d2i_input = open(input_file, "rb")
    json_output = open(output_file, "w", encoding="utf-8")

    d2i = D2I(d2i_input)
    data = d2i.read()

    json.dump(data, json_output, indent=2, ensure_ascii=False)

    d2i_input.close()
    json_output.close()
