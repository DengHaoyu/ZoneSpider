#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int MAXN = 100010;
inline char nc(){
	static char buf[100000],*p1=buf,*p2=buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
#ifdef BEYONDSTARS
#define nc getchar
#endif
template <typename T>
inline void read(T &x){
	x = 0;T f = 1;
	char c = nc();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
	x*=f;
}
char psk[200]="kNh*bQZj7JuIQJ3EqBfnV0M4z*BhuWjilEgQkNac6QM_";
int main(){
	long long has = 5381;
	int len = strlen(psk);
	for(int i = 0;i<len;i++){
		has+=(has<<5)+psk[i];
	}
	long long hash = has&0x7fffffff;
	cout<<hash;
	return 0;
}

