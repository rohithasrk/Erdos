#include <iostream>
#include <string>
using namespace std;

string toBin(long long int a){
	string s="";
	while(a>0){
		string r= to_String(a%2);
		s=r+s;
		a=a/2;
	}
return s;
}

int main(){
	cout<<toBin(10);
}
