#!/bin/sh

#
# Based on find-lang.sh from PLD, which is
# copyright (c) 1998 by W. L. Estes <wlestes@uncg.edu>
#
# Redistribution and use of this software are hereby permitted for any
# purpose as long as this notice and the above copyright notice remain
# in tact and are included with any redistribution of this file or any
# work based on this file.
#

usage () {
cat <<EOF

Usage: $0 TOP_DIR BASE_DIR FILE_BASE_NAME [options]

Language dependent files from: \$TOP_DIR/\$BASE_DIR/lang/,
\$TOP_DIR/\$BASE_DIR/help/ and \$TOP_DIR/\$BASE_DIR/config.info.* are processed.
The result is written in the \$BASE_DIR/* form into the
./\$FILE_BASE_NAME.lang file.

The following extra option is possible:
  --no-help          omit the $TOP_DIR/help directory

EOF
exit 1
}

if [ -z "$1" ] ; then usage
elif [ $1 = / ] ; then
  echo $0: expects non-/ argument for '$1' 1>&2
  exit 1
elif [ ! -d $1 ] ; then
  echo $0: $1: no such directory
  exit 1
else TOP_DIR="`echo $1|sed -e 's:/$::'`"
fi
shift

if [ "$1" = / ] ; then
  echo $0: expects non-/ argument for '$1' 1>&2
  exit 1
elif [ ! -d $TOP_DIR/$1 ] ; then
  echo $0: $1: no such directory
  exit 1
else BASE_DIR="`echo $1|sed -e 's:/$::'`"
fi
shift 1

if [ -z "$1" ] ; then usage
  else NAME=$1
fi
shift 1

HELP=
while test $# -gt 0 ; do
    case "${1}" in
        --no-help )
                HELP=#
                shift
                ;;
    esac
done

find $TOP_DIR/$BASE_DIR/lang |sed '
1i\
%defattr (644,root,root,755)
s:^'"$TOP_DIR"'::
s:^/'$BASE_DIR/lang/'.*/.*::
s:^/'$BASE_DIR/lang/'.*~::
s:^/'$BASE_DIR/lang/'.*\.eucJP::
s:^\(/'$BASE_DIR/lang/'\)\([a-z][a-z]\)\(.*\):%lang(\2) \1\2\3:
s:^\([^%].*\)::
s:%lang(en) ::' > $NAME.lang

find $TOP_DIR/$BASE_DIR/help -name '*.html' |sed '
s:^'"$TOP_DIR"'::
s:^/'$BASE_DIR/help/'.*/.*::
'"$HELP"'s:^\(/'$BASE_DIR/help/'\)\(.*\.\)\([a-z][a-z]\)\(\|_[A-Z][A-Z]\)\(\|\.euc\|\.Big5\)\(\.html\):%lang(\3) \1\2\3\4\5\6:
'"$HELP"'s:^\(/'$BASE_DIR/help/'.*\.html\):%lang(en) \1:
s:^\([^%].*\)::
'"$HELP"'s:%lang(en) ::' >> $NAME.lang

find $TOP_DIR/$BASE_DIR -name 'config.info.*' |sed '
s:^'"$TOP_DIR"'::
s:^/'$BASE_DIR/'.*/.*::
s:^/'$BASE_DIR/'.*\.eucJP::
s:^\(/'$BASE_DIR/config'\.info\.\)\([a-z][a-z]\)\(.*\):%lang(\2) \1\2\3:
s:^\([^%].*\)::' >> $NAME.lang

if [ "$(cat $NAME.lang | egrep -v '(^%defattr|^$)' | wc -l)" -le 0  ]; then
    echo 'Error: international files not found !'
    exit 1
fi
