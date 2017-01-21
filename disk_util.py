import subprocess as sp

o = sp.check_output("lsscsi")

devices = []
for line in o:
    if line[:4] == "/dev":
        devices.append(line[:4])
