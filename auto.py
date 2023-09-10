#!/usr/bin/python3
import subprocess
import sys

filename = sys.argv[1]

with open(filename,"w") as newfile:
  newfile.write(r"#!/usr/bin/python3")

resualt = subprocess.run(["chmod","+x",filename],capture_output=True)

if resualt:
  print("File created with exe permission")
else:
  print("File not created")
