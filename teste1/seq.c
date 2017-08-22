#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define _CONST_ 1048576  // constant to multiply N


// generates random number from 0 to 1000
int random_number() {

	srand(time(NULL)); // initializes random number generator

	return rand()%1001;
}

void fill_and_mean(long long int array[], long long int size) {

	long long int sum = 0;

	for(long long int i = 0; i < size; i++) {
		array[i] = random_number();
		sum += array[i];
	}
	return sum/size;
}

int main(int argc, char *argv[]) {
	
	int N = atoi(argv[1]);
	long long int *array;

	array = malloc((N * _CONST_) * sizeof(long long int));
	int mean_number = fill_and_mean(array, N*_CONST_);
	printf("%d\n", mean_number);


	free(array);

}