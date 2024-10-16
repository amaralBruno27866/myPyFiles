void selectionSort(int arr[],int size){
    int i,j;
    int min;  //index of smallest value in the unsorted array

    for(int i=0;i<size-1;i++){
        min=i;
        for(int j=i+1;j<size;j++){
            if(arr[j] < arr[min]){
                min=j;
            }
        }
        if(min!=i){
            int tmp=arr[min];
            arr[min]=arr[i];
            arr[i]=tmp;
        }
    }
}