#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//function prototypes + documentation (comments)

/**
 * This function computes the factorial,
 * n! = n * (n-1) * (n-2) ... 3 * 2 * 1
 */
long factorial(int n);
double sine(int sign, int x, int n);
int main(int argc, char **argv) {

  if(argc != 3) {
    fprintf(stderr, "Usage: %s x n\n", argv[0]);
    exit(1);
  }

  double x = atof(argv[1]);
  int n = atoi(argv[2]);
int sign = 1;
  double result = 0.0;

  //compute sin(x) using a taylor series out to n terms
 
  result = sine(sign,x, n);
  printf("sin(%f) = %f\n", x, result);

  return 0;
}

double sine(int sign, int x, int n){
 int i;
  double sum = 0.0;
  for(i=0; i<n; i++) {
    sum += (sign * pow(x, 2*i+1) / factorial(2*i+1));
    sign *= -1;
  }
return sum;

}
//function definition(s)

long factorial(int n) {
  long result = 1, i;
  for(i=2; i<=n; i++) {
    result *= i;
  }
  return result;
}
