#!/bin/sh

error() {
    echo >&2 "$@"
}

if [ $# -ne 2 ]; then
	printf "Usage: %s /bin/ls /my/folder\n" "$0"
	exit 1
fi

FILE_NAME="$1"
DST_DIR="$2"

if [ ! -f "$FILE_NAME" ]; then
	error "$FILE_NAME does not exists"
fi

if [ ! -d "$DST_DIR" ]; then
	error "$DST_DIR does not exists or not a directory"
	exit 1
fi
if [ ! -w "$DST_DIR" ]; then
	error "$DST_DIR does not writable"
	exit 1
fi

LDD_OUTPUT="$(ldd "$FILE_NAME" 2>&1)"
LDD_RC=$?
if [ $LDD_RC -ne 0 ]; then
	error "ldd fails with exit code $LDD_RC"
	if [ -n "$LDD_OUTPUT" ]; then
		error "ldd output was: $LDD_OUTPUT"
	fi
	exit 1
fi

echo "Copy to $DST_DIR"

echo "$LDD_OUTPUT" | grep -o '/[^ ]*' | while read LIB; do
	cp "$LIB" "$DST_DIR"
	echo "-- $LIB..."
done

echo "Copy $FILE_NAME"
cp "$FILE_NAME" "$DST_DIR"

SH_SCRIPT_NAME="$DST_DIR/$(basename "$FILE_NAME").sh"

cat </dev/null >"$SH_SCRIPT_NAME" <<EOF
#!/bin/sh
CURRENT_DIR="\$(dirname \$(readlink -f \$0))"
env LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$CURRENT_DIR \$CURRENT_DIR/$(basename "$FILE_NAME") "\$@"
EOF

chmod 755 "$SH_SCRIPT_NAME"

echo 'Done'
