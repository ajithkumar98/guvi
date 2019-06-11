#include <stdio.h>

int main() {
	//code
	int r,c;
	scanf("%d %d",&r,&c);
	int mat[r][c];
	int map[1000]={0};
	for(int i=0;i<r;i++){
	    for(int j=0;j<c;j++){
	        scanf("%d ",&mat[i][j]);
	        if(mat[i][j]==0){
	            map[i]++;
	        }
	    }
	}
	for(int i=0;i<r;i++){
	    for(int j=0;j<c;j++){
	        if(map[i]==0)
	        printf("%d ",mat[i][j]);
	        else
	        printf("0 ");
	    }
	    printf("\n");
	}
}
