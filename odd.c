#include <stdio.h>

int main() {
	int num;
	scanf("%d",&num);
	if(num<0){
	    printf("invalid");
	}
	else if(num%2==0){
	    printf("Even");
	}
	else{
	    printf("Odd");
	}
	return 0;
}
