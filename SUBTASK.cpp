#include<bits/stdc++.h>
using namespace std;

int main() 
{
    int t;
    cin>> t;
    while(t--) 
    {
        int n,m,k;
        cin>>n>>m>>k;
        
        int a[n] , ans = 0 , counter = 0 , cnt = 0;
        bool first = false;
        for (int i =0 ; i < n;i++) 
        {
            cin>>a[i];
        }
        for(int i =0 ; i <n ;i++) 
        {
            if(a[i] == 1 && counter <= m) 
            {
                counter++;       
                cnt ++;
            }
            else if(a[i]== 0 && counter <= m && first == false)
            {
                break;
            }
            if(counter == m) 
            {
                first = true;
                counter = 0;
            }
        }
        if(cnt == n) 
        {
            cout<<100<<std::endl;
        }else if(first == true ) 
        {
            cout<<k<<std::endl;
        }
        else 
        {
            cout<<0<<std::endl;
        }
    }
    return 0;
}