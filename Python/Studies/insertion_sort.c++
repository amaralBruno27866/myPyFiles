void insertionSort(int arr[],int size){
    int curr;
    int i, j;
    for(i=1;i<size;i++){
        curr=arr[i];
        for(j=i;j>0 && arr[j-1] > curr;j--){
            arr[j]=arr[j-1];
        }
        arr[j]=curr;
    }
}