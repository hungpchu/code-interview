#include<stdio.h>
#include<stdlib.h>
#include<math.h>


double averageVelocity(double distance, double time);
double averageAcceleration(double currentVelo, double initialVelo, double time);
double force( double mass, double acceleration);


int main(int argc, char **argv){


	if (argc != 5){

	fprintf(stderr, "Usage: %s distance time initialVelo mass\n", argv[0]);
	exit(1);

	}


	double distance = atof(argv[1]);
	double time = atof(argv[2]);
	double initialVelo = atof(argv[3]);
	double mass = atof(argv[4]);
        double currentVelo =  averageVelocity(distance, time);

	printf("average velocity = %f\n", averageVelocity(distance, time));
	printf("Average Acceleration = %f\n", averageAcceleration(currentVelo, initialVelo,time));
	printf(" Force =  %f\n", force(mass, averageAcceleration(currentVelo,initialVelo,time)));


}


double averageVelocity(double distance, double time){

return distance/time;

}

double averageAcceleration(double currentVelo, double initialVelo, double time){

return (currentVelo - initialVelo)/time;
}

double force( double mass, double acceleration){

return mass*acceleration;
}


