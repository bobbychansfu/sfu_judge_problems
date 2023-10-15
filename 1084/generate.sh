#!/bin/bash
dir=$1
fin="data/$dir/$2.in"
fout="data/$dir/$2.out"
echo "$2" > "$fin"; cat "$fin" | python3 submissions/broken_spiral.py > "$fout"
