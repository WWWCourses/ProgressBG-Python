import os
import subprocess

res = subprocess.check_output(["date","+60"])

print(res)

