# -*- coding: utf-8 -*-
#/usr/bin/env python

import commands, sys, re, os, shutil
from stat import *

if len(sys.argv) < 3:
    print "Usage example:"
    print "python script.py /usr/bin/ls /my/folder\n"
    exit(1)

file_name = sys.argv[1]
dest_folder = sys.argv[2]

if not os.path.isdir(dest_folder):
    print "Error:", dest_folder, "is not a directory."
    exit(1)

ldd_result = commands.getstatusoutput("ldd %s" % file_name)

exit_code = ldd_result[0]
if exit_code:
    print "Error: exit code of ldd %s\n" % exit_code
    exit(1)

depends = re.findall('(/.*) ', ldd_result[1])

print "Copy to", dest_folder
for dep in depends:
    shutil.copy(dep, os.path.join(dest_folder, os.path.split(dep)[1]))
    print "--", dep, '...'

print "Copy", file_name
dest_file_name = os.path.join(dest_folder, os.path.split(file_name)[1])
shutil.copy(file_name, dest_file_name)


script = "#/usr/bin/env sh\n\
env LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(dirname $(readlink -f $0)) $(dirname $(readlink -f $0))/gdb\n"

script_name = dest_file_name + '.sh'
f_script = open(script_name, 'w')
f_script.write(script)

os.chmod(script_name, S_IMODE(os.stat(script_name).st_mode) | S_IXUSR)

print "Done"
