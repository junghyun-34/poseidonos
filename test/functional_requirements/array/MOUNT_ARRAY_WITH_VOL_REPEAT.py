#!/usr/bin/env python3
import subprocess
import os
import sys
sys.path.append("../")
sys.path.append("../../system/lib/")

import json_parser
import pos
import cli
import api
import UNMOUNT_ARRAY_WITH_VOL_MOUNTED

ARRAYNAME = UNMOUNT_ARRAY_WITH_VOL_MOUNTED.ARRAYNAME


def execute():
    out = UNMOUNT_ARRAY_WITH_VOL_MOUNTED.execute()
    code = 0
    repeat = 30
    for i in range(0, repeat):
        print("TEST(" + str(i + 1) + ")")
        out = cli.mount_array(ARRAYNAME)
        print("mount: " + out)
        code = json_parser.get_response_code(out)
        if code != 0:
            return out
        out = cli.unmount_array(ARRAYNAME)
        print("unmount: " + out)
        code = json_parser.get_response_code(out)
        if code != 0:
            return out
    return out


if __name__ == "__main__":
    api.clear_result(__file__)
    out = execute()
    ret = api.set_result_by_code_eq(out, 0, __file__)
    pos.kill_pos()
    exit(ret)
    