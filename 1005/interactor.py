import sys, random
test_case_fifo = sys.argv[1]
with open(test_case_fifo, 'r') as f:
    test_case = f.readline().split()

# test case:
num_nums, num_queries = map(int, test_case)

print(f"{num_nums} {num_queries}", flush=True)

a = list(range(num_nums))
random.shuffle(a)
# print(a, flush=True)

while(num_queries > 0):
    try:
        req = input().split()
        if req[0] == 'a':
            ans = list(map(int, req[1:]))
            if len(ans) != num_nums:
                print(-1, flush=True)
                sys.exit(1)
            for i in range(num_nums-1):
                if a[ans[i]] >= a[ans[i+1]]:
                    print(-1, flush=True)
                    sys.exit(1)
            print(1, flush=True)
            sys.exit(0)

        used = set()
        fail = False
        results = []
        if int(req[1]) > num_nums//2:
            print(-1, flush=True)
            sys.exit(0)

        for i in range(int(req[1])):
            cmp = input().split()
            if cmp[0] == cmp[2] or cmp[0] in used or cmp[2] in used:
                print(-1, flush=True)
                sys.exit(1)
            used.add(cmp[0])
            used.add(cmp[2])
            # print(cmp)
            if cmp[1] == '<':
                results.append(1 if a[int(cmp[0])] < a[int(cmp[2])] else 0)
            else:
                results.append(1 if a[int(cmp[0])] > a[int(cmp[2])] else 0)
        
        print(' '.join([str(int(x)) for x in results]), flush=True)

    except Exception as err:
        # print(type(err))
        # print(err.args)
        # print(err)
        print(-1, flush=True)
        sys.exit(1)
    
    num_queries -= 1

print(-1, flush=True)
sys.exit(1)