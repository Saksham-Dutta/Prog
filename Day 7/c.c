#include<stdio.h>
 int sumOfDigits(int num){
    if(num==0){
        return 0;
    }
    return(num % 10)+ sumOfDigits(num/10);
}
int main(){
    int number;
    printf("Enter an integer");
    scanf("%d",&number);
    if (number<0){
        number=-number;
    }
    int result=sumOfDigits(number);
    printf("Th sum of digits is %d\n:" ,result);
    


}


 





