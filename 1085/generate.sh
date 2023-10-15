#!/bin/bash
dir=$1
fin="data/$dir/$2.in"
fout="data/$dir/$2.out"
echo "$3 $4 $5 $6" | ./genTestCases > "$fin"
cat "$fin" | ./submissions/sol > "$fout"
