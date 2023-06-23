#include <iostream>
using namespace std;

int main() {
    
    int t;
    cin>>t;
    
    while(t-- ){
        int n;
        cin>>n;
        int acount=0,bcount=0,abcount=0,ocount=0;
        for(int i=0; i<n ; i++){
            string bn;
            cin>>bn;
            
            if(bn=="A" ){
                acount++;
            }
            else if(bn == "B"){
                bcount++;
            }
            else if (bn == "AB"){
                abcount++;
            }
            else{
                ocount++;
            }
        }
     
        long int sum=0;
        if(acount>=bcount){
            sum+=acount;
        }else{
            sum+=bcount;
        }
        sum+=abcount;
        sum+=ocount;
        cout<<sum<<endl;
    }
}