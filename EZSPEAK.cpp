#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    string s;
	    cin>>s;
	    int count=0;
	    bool flag = false;
	    for(int i=0;i<n;i++)
	    {
	        if(s[i]=='a'|| s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
	        {
	            count=0;
	            continue;
	        }
	        else
	        {
	            count++;
	            if(count==4)
	            {
	                flag = true;
	                break;
	            }
	        }
	    }
	        if(!flag)
	        cout<<"YES"<<endl;
	        else
	        cout<<"NO"<<endl;
	    
	}
	return 0;
}
