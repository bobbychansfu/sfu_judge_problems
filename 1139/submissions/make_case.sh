 #!/usr/bin/bash


g++ -std=c++17 ./ac.cpp -O2 -o ./ac.out

export CASE=1
for i in $(seq 1 10);
do
    python3 gen.py 20 10 50  ../data/case$CASE/gen.py > "../data/case$CASE/$i.in";
    cat "../data/case$CASE/$i.in" | ./ac.out > "../data/case$CASE/$i.out";
done