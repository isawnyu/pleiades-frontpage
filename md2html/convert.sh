#! /bin/bash

set -e 	# exit at first error

usage='\n\nUsage:\nconvert.sh [source/md/filename] [template/filename] [output/html/filename]\n'

if [[ -z $1 || -z $2 || -z $3 ]]; then
	printf "FATAL: Invalid command line arguments.$usage\n" 1>&2
	exit 64		# sysexits.h: command line usage error
fi 
if [[ ! -e $1 ]]; then
	printf "FATAL: Source file $1 does not exist.$usage\n"
	exit 66		# sysexits.h: cannot open input
else
	echo "source file: $1"
fi
if [[ ! -e $2 ]]; then
	printf "FATAL: template file $2 does not exist.$usage\n"
	exit 66		# sysexits.h: cannot open input
else
	echo "template file: $2"
fi
if [[ -e $3 ]]; then
	echo "WARNING: output file $3 will be overwritten; copying to $3.bak."
	cp $3 "$3.bak"
fi
echo "output file: $3"

# position ourselves at top of working tree so relative paths work as expected
origdir=$(PWD)
topdir=$(git rev-parse --show-toplevel)
cd $topdir

# make sure we have venv we need
projpath=$(echo $topdir | sed -E  's/(.*)\/[A-Z]\/(.*)/\2/')
virtualenvpath=~/Envs/$(echo ${projpath} | sed 's/\//-/g')
if [[ -z $VIRTUAL_ENV ]]; then
	activatepath=${virtualenvpath}/bin/activate
	source ${activatepath}
elif [[ $VIRTUAL_ENV != $virtualenvpath ]]; then
	origvenv=$VIRTUAL_ENV
	deactivate
	activatepath=${virtualenvpath}/bin/activate
	source ${activatepath}
	echo "$VIRTUAL_ENV activated"
else
	origvenv=$VIRTUAL_ENV
fi

# perform the conversion
set -v
python md2html/mdid.py < $1 | python md2html/mdlinks.py | python -m markdown --noisy -e utf-8 -o xhtml5 -x markdown.extensions.extra -x markdown.extensions.meta -x markdown.extensions.abbr -x sections | python md2html/htmlfill.py -t $2 -m $1  > $3
set +v

# restore original location and venv
cd $origdir
if [[ ! -z $origvenv && $origvenv != $VIRTUAL_ENV ]]; then
	deactivate
	source ${origvenv}
fi
