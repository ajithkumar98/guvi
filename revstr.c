#include <stdio.h>
#include<string.h>
int main() {
	char str[1001];
	while(scanf("%s ",str)>0){
	    for(int i=strlen(str)-1;i>=0;i--){
	        printf("%c",str[i]);
	    }
	    printf(" ");
	}
}
