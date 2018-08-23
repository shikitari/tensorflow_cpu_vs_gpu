#!/usr/bin/env bash

PYTHON="multiply_sample.py"
FILE="report_"
EXT=".txt"
POSTFIX="data"

if [ $# -ge 1 ]; then
    POSTFIX=$1
fi

OUTPUT=${FILE}${POSTFIX}${EXT}
echo "" > $OUTPUT

echo "output: $OUTPUT"

for i in $(cat list.txt);
do
  echo $i
  gtime -f "%e" python $PYTHON $i &>> $OUTPUT
done
