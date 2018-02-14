#include <iostream>
using namespace std;



int main(){
	int x = 21 , y , z ;
	while(x != 1)
	{
		cout<<"Enter a number(Player 1):"<<endl;
		cin>>y;
		if(y>3 || y < 0 || y >= x)
		{
			cout<<"Error"<<endl;
			break;
		}
		else
		{
			x = x - y ;
			cout<<x<<endl;
			if (x == 1){
				cout<<"Player 2 losess"<<endl;
				break;
			}
			else
			{
				cout<<"Enter a number(Player 2):"<<endl;
		        cin>>z;
				if(z > 3 || z < 0 || z >=x )
				{
					cout<<"Error"<<endl;
					break;
				}
				x = x - z ;
				cout<<x<<endl;
				if (x == 1){
				    cout<<"Player 1 losess"<<endl;
					break;
			    }
			}
		}

	}
	return 0;
}
