#!/usr/bin/env python3
import os
import json
import argparse
import sys
global volId
global ioType
global bwValue
global iopsValue
global group_report
global fio_output_file

parser = argparse.ArgumentParser(description='Please add fio option to fio_full_bench.    py')
parser.add_argument('-v', '--volId', required=False, help='Pass this info for reading the volId to parse')
parser.add_argument('-t', '--ioType', required=True, help='ioType read/write/mixed')
parser.add_argument('-g', '--groupReport', required=False, help='Json logged as group report = 1 or 0')

args = parser.parse_args()
if(args.volId is not None):
    volId = int(args.volId, 0)
else:
    volId = 1

if(args.ioType is not None):
    ioType = args.ioType

if(args.groupReport is not None):
    group_report = int(args.groupReport, 0)
else:
    group_report = 1

if(group_report == 1):
    job_pos = 0
else:
    job_pos = volId

fio_output_file = "/tmp/fio_output.json"

with open(str(fio_output_file)) as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()
    if(ioType == "read" or ioType == "randread"):
        bwValue = data['jobs'][job_pos]['read']['bw']
        iopsValue = data['jobs'][job_pos]['read']['iops']
        print(bwValue, iopsValue)
    if(ioType == "write" or ioType == "randwrite"):
        bwValue = data['jobs'][job_pos]['write']['bw']
        iopsValue = data['jobs'][job_pos]['write']['iops']
        print(bwValue, iopsValue)
    if(ioType == "readwrite"):
        bwValue = data['jobs'][job_pos]['read']['bw']
        iopsValue = data['jobs'][job_pos]['read']['iops']
        print(bwValue, iopsValue)
        bwValue = data['jobs'][job_pos]['write']['bw']
        iopsValue = data['jobs'][job_pos]['write']['iops']
        print(bwValue, iopsValue)

