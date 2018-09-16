#include <iostream>
#include <vector>
using namespace std;


bool makeThreeGroups( vector<int> num ) {

    bool result = false;
    
    int oneThird = 0, numSize = 0, i ,j, numb1 = 0, numb = 0, sum = 0, sum1 = 0;

    numSize = num.size() + 1;

    // calculate the sum of all number
    for (i = 0; i < num.size(); i++){
        sum1 += num.at(i);

    }

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

    // only true if sum can divide 3
    if ( sum1 % 3 == 0) {

        oneThird = (sum1 / 3);

        // first case for twoThird value
        bool number[oneThird + 1][numSize];

        // initialize bool array
        for (i = 0; i < oneThird + 1; i++) {

            for (j = 0; j < numSize; j++) {

                number[i][j] = false;

            }
        }
        
        // num = 0 -> whole column of 0 is false
        for (i = 1; i < oneThird + 1; i++) {

            number[i][0] = false;

        }

        // sum = 0 -> whole row of 0 is true
        for (j = 0; j < numSize; j++) {

            number[0][j] = true;

        }
        
        for (j = 1; j < numSize; j++) {
            for (i = 0; i < oneThird + 1; i++) {
                // true condition
                if (number[i][j - 1] == true) {
                   
                    number[i][j] = true;

                    if (i + num.at(j - 1) <= oneThird) {
                        number[i + num.at(j - 1)][j] = true;
                    }
                }

                    // false condition
                else if (number[i][j] != true) {
                    number[i][j] = false;
                }


            }
        }
        
        result = number[oneThird ][numSize - 1];

        // if the result from the first array is true then delete all element created 1/3 sum
        if (result == true) {

            for (j = 0; j < numSize; j++) {
                if (number[oneThird][j] == true) {

                    numb = num.at(j - 1);
                    numb1 = oneThird - num.at(j - 1);
                    sum += numb;
                    num.erase(num.begin() + (j - 1));
                    break;
                }
            }

            while (sum < oneThird) {

                for (j = 0; j < numSize; j++) {
                    if (number[numb1][j] == true) {
                        numb1 = numb1 - num.at(j - 1);
                        numb = num.at(j - 1);
                        sum += numb;
                        num.erase(num.begin() + (j - 1));
                        break;
                    }
                }
            }
            
            numSize = num.size() + 1;

            for (i = 0; i < oneThird + 1; i++) {

                for (j = 0; j < numSize; j++) {

                    number[i][j] = false;

                }
            }
            
            // num = 0 -> whole column of 0 is false
            for (i = 1; i < oneThird + 1; i++) {

                number[i][0] = false;

            }

            // sum = 0 -> whole row of 0 is true
            for (j = 0; j < numSize; j++) {

                number[0][j] = true;

            }
            
            for (j = 1; j < numSize; j++) {
                for (i = 0; i < oneThird + 1; i++) {
                    // true condition
                    if (number[i][j - 1] == true) {

                        number[i][j] = true;

                        if (i + num.at(j - 1) <= oneThird) {
                            number[i + num.at(j - 1)][j] = true;
                        }
                        
                    }

                        // false condition
                    else if (number[i][j] != true) {
                        number[i][j] = false;
                    }
                    
                }
                
            }

            result = number[oneThird ][numSize - 1];
      
        }
        
    }
    
    return result;
}


int main(){
vector<int> num = {5,4,8,1,6,4};


cout<<"Result of make3Group = "<<makeThreeGroups(num)<<endl;

}
