#include<iostream>
using namespace std;

int stringRepeat(string A, string B){
      
    int lengthA = A.length();
    int lengthB = B.length();
    int i = 0,j = 0;
    int count = 1;

    while(i < lengthB){
               
	       j= 0;
	       while (j < lengthA ){
		  

			if ( A[j] == B[i]  && j == lengthA - 1) {
                        
				count++;
				
                        }

			j++;
			i++;
					
		}
	

     				
       
    }

    if ( count == 1){

	    count = -1;
    }

    return count;



}	


int main(){

           
	string A = "abcdef";
	string B = "abcabcdabcd";

	cout<<"count = "<<stringRepeat(A,B)<<endl;

}
