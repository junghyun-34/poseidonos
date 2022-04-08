#!/usr/bin/env python3
import subprocess
import os
import sys
sys.path.append("../")
sys.path.append("../../system/lib/")
sys.path.append("../device_management/")

import json_parser
import pos
import cli
import api
import SCAN_DEV_BASIC

ONLY_TWO_DATA_DEVS_FOR_RAID5 = "unvme-ns-0,unvme-ns-1"
THREE_DATA_DEVS_FOR_RAID5 = "unvme-ns-0,unvme-ns-1,unvme-ns-2"

def execute():
    SCAN_DEV_BASIC.execute()
    cli.mbr_reset()
    out = cli.create_array("uram0", ONLY_TWO_DATA_DEVS_FOR_RAID5, "unvme-ns-2", "POSArray", "RAID5")
    print (out)
    out = cli.create_array("uram0", THREE_DATA_DEVS_FOR_RAID5, "unvme-ns-3", "POSArray", "RAID5")
    print (out)
    return out

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        pos.set_addr(sys.argv[1])
    api.clear_result(__file__)
    out = execute()
    ret = api.set_result_by_code_eq(out, 0, __file__)
    pos.flush_and_kill_pos()
    exit(ret)