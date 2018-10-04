#include <vector>

#include <cmath>
#include <iostream>
#include <vector>

using namespace std;


int ourQuickSelect( vector<int> arrayOfNumber , int position ) {

    vector<int> arrayOfNumberSmallerThanPivot;
    vector<int> arrayOfNumberBiggerThanPivot;

    int pivotIndex, pivot, index, number;
    int startingIndex = 0;
    static int countCompare = 0;
    static int smallestValue = 0;

    int size = arrayOfNumber.size();

    // set the first element of the vector as the pivot
    pivot = arrayOfNumber.at(startingIndex);
    // pivot's index is the starting index
    pivotIndex = startingIndex;

    // loop from the index = 1 to size - 1
    for (index = startingIndex + 1; index < size; index++) {

        // if the element in the vector is smaller than the pivot
        if (arrayOfNumber.at(index) < pivot) {

            // increase the pivotIndex
            pivotIndex++;

            // initialize the value of that element to the number
            number = arrayOfNumber.at(index);

            // store that number in the arrayOfNumberSmallerThanPivot
           // arrayOfNumberSmallerThanPivot.push_back(number);
            // increase the countCompare
            countCompare++;

            // if the element in the vector is bigger than the pivot
        } else if (arrayOfNumber.at(index) > pivot) {

            number = arrayOfNumber.at(index);

            // store that number in the arrayOfNumberBiggerThanPivot
           // arrayOfNumberBiggerThanPivot.push_back(number);

            countCompare++;

        }
    }

   // if the pivot's index = position
    if (pivotIndex == position - 1) {

        // the smallestValue is the position's number
        smallestValue = arrayOfNumber.at(pivotIndex);

    // if the pivot's index > position
    } else if (pivotIndex > startingIndex + position - 1) {

      // go to the arrayOfNumberSmallerThanPivot and recursively find the wanted value since the position will be on the left
        ourQuickSelect(arrayOfNumber, position);

        // if the pivot's index < position
    } else {

        // go to the arrayOfNumberBiggerThanPivot and recursively find the wanted value since the position will be on the right
        ourQuickSelect(arrayOfNumber, position - 1 - pivotIndex);

    }

    // return the number of comparisions
    return countCompare;
    
}

int main(){


vector<int> num = {9,7,8,5,6,3,4,1,2};

cout<<" result ="<<ourQuickSelect(num,4)<<endl;

for ( int i = 0 ; i < num.size(); i++){
cout<<num[i]<<" ";
}

}
