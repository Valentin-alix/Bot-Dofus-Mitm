import json
import os
import com.ankamagames.dofus.Constants as Constants

ROOTDIR = os.path.dirname(__file__)

if not os.path.exists(Constants.PROTOCOL_SPEC_PATH):
    raise Exception(f"{Constants.PROTOCOL_SPEC_PATH} file not found")

with open(Constants.PROTOCOL_SPEC_PATH, "r") as fp:
    D2PROTOCOL = json.load(fp)


class ProtocolSpec:
    @staticmethod
    def getTypeSpecById(id):
        if str(id) not in D2PROTOCOL["type_by_id"]:
            raise Exception(f"Type id {id} not found in known types ids")
        return D2PROTOCOL["type_by_id"][str(id)]

    staticmethod

    def getClassSpecById(id):
        if str(id) not in D2PROTOCOL["msg_by_id"]:
            raise Exception(f"msg id {id} not found in known msg ids")
        return D2PROTOCOL["msg_by_id"][str(id)]

    @staticmethod
    def getClassSpecByName(name):
        return D2PROTOCOL["type"][name]
