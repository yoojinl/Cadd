#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands, sys, os, re, shutil
from os import path
from stat import *

if len(sys.argv) < 3:
    print "Usage example:"
    print "python script.py /usr/bin/gdb /my/folder\n"
    exit(1)

file_name = sys.argv[1]
dest_folder = sys.argv[2]

if not path.isdir(dest_folder):
    print "Error:", dest_folder, "is not a directory."
    exit(1)

ldd_result = commands.getstatusoutput("ldd %s" % file_name)

exit_code = ldd_result[0]
if exit_code:
    print "Command error: ldd %s" % file_name
    print "Error: exit code of ldd %s\n" % exit_code
    exit(1)

depends = re.findall('(/.*) ', ldd_result[1])

print "Copy to", dest_folder
for dep in depends:
    shutil.copy(dep, path.join(dest_folder, path.basename(dep)))
    print "--", dep, '...'

print "Copy", file_name
dest_file_name = path.join(dest_folder, path.basename(file_name))
shutil.copy(file_name, dest_file_name)

script = "#!/bin/sh\n\
env LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(dirname $(readlink -f $0)) $(dirname $(readlink -f $0))/%s $@\n" % path.basename(file_name)

script_name = dest_file_name + '.sh'
f_script = open(script_name, 'w')
f_script.write(script)

os.chmod(script_name, S_IMODE(os.stat(script_name).st_mode) | S_IXUSR)

print "Done"
