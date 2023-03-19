s = input()
a,t = 1,1

for i in range(1, len(s)):
    if (s[i] == s[i-1]):
        t+=1
    else:
        a = t if a<t else a
        t=1
print(a)
