#include <stdio.h>

int main(void) {
	long long int num;
	scanf("%lld",&num);
	if(num>0){
		printf("Positive");
	}
	else if(num<0){
		printf("Negative");
	}
	else if(num==0){
		printf("Zero");
	}
}

