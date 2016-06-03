#include <iostream>
#include <cmath>
using namespace std;

double f(int n,long long int y){
	double z = sqrt((n*(y*y)+1));
	return z;
}

bool pfsq(int n){
	double sqt = sqrt(n);
	if (int(sqt)==sqt) return true;
	else return false;
}

int main(){
	long long int lfX=1;
	int N=1;
	for(int n=2;n<100000;n++){
		if(!pfsq(n)){
			long long int y=1;
			while(int(f(n,y))!=f(n,y)){
				double nex=f(n,y+1);
				if(int(nex)==nex){
					if(nex>lfX){ lfX=nex; N=n;}
				}
				y++;
			}
		}
	}
	//cout<<pfsq(626)<<endl;
	//cout<<f(2,3)<<endl;
	cout<<N<<endl;
	cout<<lfX<<endl;
}
