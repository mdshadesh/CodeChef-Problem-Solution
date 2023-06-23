#include <bits/stdc++.h>
using namespace std;

int main() 
{
  int t;
  cin>>t;
  while(t--)
  {
      int n;
      cin>>n;
      int trn=0;
      unordered_map<int,int>mp;

      while(n--)
      {
          int c,v;
          cin>>c>>v;
          if(c<=8)  
          {
              if(mp[c]<v)
              {
                  trn-=mp[c];
                  mp[c]=v;
                  trn+=mp[c];
              }
          }
      }
    cout<<trn<<"\n";
  }
	return 0;
}
