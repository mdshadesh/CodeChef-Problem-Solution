#include <bits/stdc++.h>
using namespace std;

int main() {
	int T, A, B, sa , sb ;
	cin >> T;
	while(T-- > 0)	{
	    cin >> A >> B;
	    sa=0;
	    sb=0;
	    int i = 1;
	    while(true)
	    {
	        sa = sa + i;
	        if(sa > A ){
	            cout << "Bob" << endl;
	            break;
	        }
	        i++;
	        sb = sb + i;
	        if(sb > B) {
	            cout << "Limak" <<endl;
	            break;
	        }
	        i++;
	    }
	}
	return 0;
}
	       
	        
