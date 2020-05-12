#!/usr/bin/env python3.7
import os
import sys

arg = sys.argv
f_name = "mailto.py"
cmd = "mailto"

path = "~/bin"
if os.path.isdir(path):
  pass
else:
  os.system("mkdir ~/bin")
  os.system("echo 'export PATH=$PATH":$HOME/bin'" >> ./.profile")
os.system("chmod +x "+f_name)
os.system("mv {} {}".format(f_name, cmd))
os.system("cp {} ~/bin".format(cmd))

