#include <cstdlib>
#define THRESHOLD 32

void quickSort(int arr[],int size){
   quickSort(arr,0,size-1);
}

void quickSort(int arr[], int left, int right){
   if(right-left <= THRESHOLD){
      insertionSort(arr,left,right);
   }
   else{
      int i = partition(arr,left,right);
      quickSort(arr,left,i-1);
      quickSort(arr,i+1,right);
   }
}

/*performs the insertion sort algorithm on array from index left to index right inclusive.*/
void insertionSort(int arr[],int left,int right){
   int curr;
   int i, j;
   for(i=left+1;i<=right;i++){
      curr=arr[i];
      for(j=i;j>left && arr[j-1] > curr;j--){
         arr[j]=arr[j-1];
      }
      arr[j]=curr;
   }
}

int partition(int array[],int left, int right){

  //choose a random index between left and right inclusive
   int location = left + (rand()%(right-left+1));

   //get the pivot
   int pivot = array[location];

   //move the pivot out of the way by swapping with
   //last value of partition
   array[location] = array[right];
   array[right] = pivot;            //move the pivot out of the way


   int i=left-1;
   for(int j=left;j<right;j++){
      if(array[j]<=pivot){
         i=i+1;
         int tmp=array[i];
         array[i]=array[j];
         array[j]=tmp;
      }
   }

   //restore pivot so that it is just after i
   int tmp=array[i+1];
   array[i+1]=array[right];
   array[right]=tmp;
   return i+1;
}