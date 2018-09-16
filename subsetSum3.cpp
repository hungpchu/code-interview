#include <iostream>
#include <vector>
using namespace std;


bool subsetSum3( vector<int> num, int sum ) {

    bool result = false;
    
    int oneThird = 0, numSize = 0, i ,j, numb1 = 0, numb = 0;

    numSize = num.size() + 1;


    // sort the number in increasing order
    for ( i = 0; i < num.size(); i++) {

        for ( j = i + 1; j <= num.size() - 1; j++) {

            // if the element of array containing ending number of interval is bigger
            // then put it to the right os that array
            if (num.at(i) < num.at(j)) {

                // have the increasing order of the array with swap
                swap(num.at(i), num.at(j));


            }
        }
    }


       bool number[sum + 1][numSize];


        for (i = 0; i < sum + 1; i++) {

            for (j = 0; j < numSize; j++) {

                number[i][j] = false;

            }
        }
        // num = 0 -> whole column of 0 is false
        for (i = 1; i < sum + 1; i++) {

            number[i][0] = false;

        }

        // sum = 0 -> whole row of 0 is true
        for (j = 0; j < numSize; j++) {

            number[0][j] = true;

        }
        
        for (j = 1; j < numSize; j++) {
            for (i = 0; i < sum + 1; i++) {
                // true condition
                if (number[i][j - 1] == true) {
                   
                    number[i][j] = true;

                    if (i + num.at(j - 1) <= sum) {
                        number[i + num.at(j - 1)][j] = true;
                    }
                }

                    // false condition
                else if (number[i][j] != true) {
                    number[i][j] = false;
                }


            }
        }
        
        result = number[sum ][numSize - 1];

   
    
    return result;
}


int main(){

	vector<int> num = {3,3,5, 1,2,3};
	int sum = 11;

       cout<<" resut = "<<subsetSum3(num,sum)<<endl;
}
