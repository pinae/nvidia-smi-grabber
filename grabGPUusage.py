#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import subprocess
import time

values = []
try:
    while True:
        p = subprocess.Popen(["nvidia-smi"], stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        gpu_usage = int(out.splitlines()[8][56:].split(b"%")[0])
        values.append(gpu_usage)
        print("GPU usage {:2.1%}".format(gpu_usage / 100), end="\r")
        time.sleep(0.005)
except KeyboardInterrupt:
    with open("values.csv", 'w') as f:
        f.write("\n".join([str(v) for v in values]))
    print("")
    print("captured " + str(len(values)) + " values.")
    # print(", ".join([str(v) for v in values]))
