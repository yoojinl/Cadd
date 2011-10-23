## Copying all dynamic library dependencies

## Example

    $ python cadd.py /usr/bin/gdb /home/user/dest
    Copy to /home/user/dest
    -- /lib/libreadline.so.6 ...
    -- /lib/libncurses.so.5 ...
    -- /lib/libz.so.1 ...
    -- /lib/libm.so.6 ...
    -- /usr/lib/libpython2.6.so.1.0 ...
    -- /lib/libexpat.so.1 ...
    -- /lib/libdl.so.2 ...
    -- /lib/libc.so.6 ...
    -- /lib/libssl.so.0.9.8 ...
    -- /lib/libcrypto.so.0.9.8 ...
    -- /lib/libpthread.so.0 ...
    -- /lib/libutil.so.1 ...
    -- /lib64/ld-linux-x86-64.so.2 ...
    Copy /usr/bin/gdb
    Done

    $ tree dest/
	dest/
	|-- gdb
	|-- gdb.sh
	|-- ld-linux-x86-64.so.2
	|-- libcrypto.so.0.9.8
	|-- libc.so.6
	|-- libdl.so.2
	|-- libexpat.so.1
	|-- libm.so.6
	|-- libncurses.so.5
	|-- libpthread.so.0
	|-- libpython2.6.so.1.0
	|-- libreadline.so.6
	|-- libssl.so.0.9.8
	|-- libutil.so.1
	`-- libz.so.1
	
	0 directories, 15 files


now you can run the gdb

    $ ./dest/gdb.sh
    Could not find platform independent libraries <prefix>
    Could not find platform dependent libraries <exec_prefix>
    Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
    'import site' failed; use -v for traceback
    GNU gdb (GDB) 7.1-ubuntu
    Copyright (C) 2010 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
    and "show warranty" for details.
    This GDB was configured as "x86_64-linux-gnu".
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    (gdb)
