 #!/usr/bin/bash


g++ -std=c++17 ./submissions/ac.cpp -O3 -o ./submissions/aco3.out

export CASE=2
for i in $(seq 11 11);
do
    python3 ./submissions/gen.py  200000 10000 > "./data/case$CASE/$i.in";
    # python3 ./submissions/gen_rand.py 20 20 100 > "./data/case$CASE/$i.in";
    cat "./data/case$CASE/$i.in" | ./submissions/aco3.out > "./data/case$CASE/$i.out";
done