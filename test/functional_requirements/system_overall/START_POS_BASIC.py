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
import pos_util

def execute():
    pos_util.kill_process("poseidonos")
    pos_util.pci_rescan()
    pos.start_pos()

if __name__ == "__main__":
    api.clear_result(__file__)
    execute()
    out = cli.get_pos_info()
    ret = api.set_result_by_code_eq(out, 0, __file__)
    pos.kill_pos()
    exit(ret)