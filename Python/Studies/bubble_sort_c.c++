void bubbleSort(int arr[],int size){
    int tmp;                          
    int i;
    int j;
    for (i=0; i<size-1; i++) {
        for (j=0; j<size-1-i; j++){
            int next = j+1;
            if (arr[next] < arr[j]) {          
                tmp = arr[j];                   
                arr[j] = arr[next];
                arr[next] = tmp;
            }
        }
    }
}