#!/bin/bash
dir=$1
fin="data/$dir/$2.in"
fout="data/$dir/$2.out"
cat "$fin" | python3 submissions/decrypt.py > "$fout"
