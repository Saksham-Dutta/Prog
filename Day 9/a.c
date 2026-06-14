#include<stdio.h>
int main(){
    int i,j ,rows;
    printf("Enter the rows from the user");
      scanf("%d",&rows);
    for(i=rows;i>=1;i--){
        for(j=1; j<=i;j++){
            printf("*");
        }
        printf("\n");
    }

}