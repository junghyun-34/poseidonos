#!/usr/bin/env python3
import subprocess
import os
import sys
sys.path.append("../lib/")
sys.path.append("../array/")
import json_parser
import pos
import cli
import test_result
import json
import MOUNT_ARRAY_NO_SPARE


def set_result(detail):
    code = json_parser.get_response_code(detail)
    result = test_result.expect_false(code)

    with open(__file__ + ".result", "w") as result_file:
        result_file.write(result + " (" + str(code) + ")" + "\n" + detail)

def execute():
    MOUNT_ARRAY_NO_SPARE.execute()
    wrong_dev = "wrong_dev"
    out = cli.add_device(wrong_dev, MOUNT_ARRAY_NO_SPARE.ARRAYNAME)
    return out

if __name__ == "__main__":
    test_result.clear_result(__file__)
    out = execute()
    set_result(out)
    pos.kill_pos()