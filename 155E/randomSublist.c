#include<iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include<algorithm>
#include<vector>
#include <stdlib.h>
using namespace std;





bool duplicate(vector<int> L){
bool dup = false;
int N = 3;

for (int i = 0; i < N; i++){
	for( int j = 0; j < N; j++){
            if(L[i] == L[j]){

               dup = true;

	    }
	}
  }

return dup;
}



int main(){

 int L[10] = {1,2,3,4,5,56,44,22,45,87};
 int N = 5;
int result[3];
int i = 0, j = 0, index ;
bool dup = true;





srand (time(NULL));
 index = rand() % 10;	

while ( j < N){
		
		 
		
		result[j] = L[index];
		index = rand() % 10;
		j++;
	}






   for( i = 0; i < N ; i++){

for( j = i + 1; j < N ; j++){

if (result[i] > result[j]){


   swap(result[i],result[j]);
   }

}
}
cout<<"[ ";
 for( i = 0; i < N ; i++){



    cout<<result[i]<<" ,";

   }

cout<<" ]";
cout<<endl;


}
