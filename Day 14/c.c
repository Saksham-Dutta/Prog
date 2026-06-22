#include <stdio.h>

void findMinMax(int arr[], int size, int *smallest, int *largest) {
    
    *smallest = arr[0];
    *largest = arr[0];

     
    for (int i=1; i<size;i++) {
        if(arr[i]<*smallest){
        *smallest = arr[i];  
        }
        if(arr[i] > *largest) {
        *largest = arr[i];   
        }
    }
}

int main() {
    int my_list[] = {34, 12, 89, 5, 67, 21};
    
     
    int size = sizeof(my_list) / sizeof(my_list[0]);
    
    int min_val, max_val;

    
    findMinMax(my_list, size, &min_val, &max_val);

    printf("Smallest element: %d\n", min_val);
    printf("Largest element: %d\n", max_val);

    return 0;
}
