#include<bits/stdc++.h>
#define f(a,b,c,d,e)for(i=a;e>0?i<b:i>b;x++)m[c][d]=65+x%26,i+=e;
using namespace std;int n,l,t,x,r,b,i;main(){cin>>n;auto m=vector<vector<char>>(n,vector<char>(n));r=b=n-1;while(x<n*n){f(l,r+1,t,i,1)f(t+1,b+1,i,r,1)f(--r,l-1,b,i,-1)f(--b,t,i,l,-1)++l,++t;}string z(2*n-1,'=');z="+ "+z+" +\n";cout<<z;for(auto r:m){cout<<"| ";for(auto p:r)cout<<p<<" ";puts("|");}cout<<z;}