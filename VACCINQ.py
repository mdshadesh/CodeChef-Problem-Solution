#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int sum,add ,n,p,x,y,r,q;
	    cin>>n>>p>>x>>y;
	    int a[n];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	    }
        int time=0 , count=0 , count1=0;
        for(int i=0;i<p;i++){
            if(a[i]==0)
                count++;
            if(a[i]==1)
                count1++;
                
            time=count*x+count1*y;
        }
        cout<<time<<endl;
        	
        }
        return 0;
}
