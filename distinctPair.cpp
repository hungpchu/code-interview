#include<iostream>
using namespace std; 
  
int countPairsWithDiffK(int arr[], int n, int k) 
{ 
    int count = 0; 
      
    // Pick all elements one by one 
    for (int i = 0; i < n; i++) 
    {        
        // See if there is a pair of this picked element 
        for (int j = i+1; j < n; j++) 
            if (arr[i] - arr[j] == k || arr[j] - arr[i] == k ) 
                  count++; 
    } 
    return count; 
} 
  
// Driver program to test above function 
int main() 
{ 
    int arr[] =  {1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 1, 9}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int k = 10; 
    cout << "Count of pairs with given diff is "
         << countPairsWithDiffK(arr, n, k); 
    return 0; 
} 
