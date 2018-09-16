#include<iostream>

using namespace std;


unsigned long long int pellNumber( unsigned long long int number ){

    int i;
    // initialize previousResult = 0 and currentResult = 1
    unsigned long long  int previousResult = 0, currentResult = 1, result = 0;
cout<<"list of number  = "<<previousResult<<"  "<<currentResult<<"  ";
    // calculate pellNumber until number times
    for( i = 0; i < number - 1; i++ ){

        result = currentResult + previousResult;
        // update previousResult and currentResult for the future clacualtion of result
        previousResult = currentResult;
        currentResult = result;
       cout<<"  "<<result<<" "; 
    }

   return result;
}





int main(){


       
	cout<<pellNumber(9)<<endl;
}
