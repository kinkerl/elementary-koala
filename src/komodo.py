#!/usr/env python
# sudo apt-get install python-configobj OR 
# easy_install configobj

import subprocess
import os
from configobj import ConfigObj

CONFIGDIR = '../config'

configs = os.listdir(CONFIGDIR)


for chapter in configs:
  config = ConfigObj(os.path.join(CONFIGDIR, chapter))
  
  for group in config:
    for element in config[group]:
	cmd = []
	cmd.append("kwriteconfig")
	cmd.append("--file")
	cmd.append(chapter)
	cmd.append("--group")
	cmd.append(group)
	cmd.append("--key")
	cmd.append(element)
	cmd.append(config[group][element])
	print ' '.join(cmd)
	#p = subprocess.call(cmd)
