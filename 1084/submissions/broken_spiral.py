n=int(input());l=t=x=0;r=b=n-1;q,k,v,u=26,range,chr,65;m=[[' ']*n for _ in k(n)]
def o(a,b):global x;m[a][b]=v(u+x%q);x+=1
while x<n*n:
 for i in k(l,r+1):o(t,i)
 for i in k(t+1,b+1):o(i,r)
 for i in k(r-1,l-1,-1):o(b,i)
 for i in k(b-1,t,-1):o(i,l)
 l+=1;r-=1;t+=1;b-=1
w=2*n-1;z="+ "+w*"="+" +";print(z)
for i in range(n):
 print(2*i*" ",'\\'+' '.join(m[i][i::]),"|")
print((w+3)*' '+'+')