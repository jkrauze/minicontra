#!/bin/sh

LICENSE_FILE_EXT='.LICENSE'

find . -name "*$LICENSE_FILE_EXT" | while read file
do
	echo "\`${file::-8}\`"
	echo
	head -n1 "$file"
	echo "\`\`\`"
	tail -n+2 "$file"
	echo "\`\`\`"
done
