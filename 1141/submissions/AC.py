n = int(input())
nums = list(input())

if n % 2 == 1:
    ans = ''.join(sorted([nums[i] for i in range(n) if i % 2 == 0])[::-1])
    print(ans)
else:
    nums = list(map(int, nums))
    C = [0 for _ in range(9)]
    for i in range(n // 2):
        C[9-nums[2*i]] += 1
    M = C[:]
    for j in range(n-1, 0, -2):
        C[9-nums[j]] += 1
        C[9-nums[j-1]] -= 1
        M = max(M, C[:])
    ans = ''
    for i in range(9):
        ans += chr(ord('9')-i) * M[i]
    print(ans)
