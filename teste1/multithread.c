/**
-------------------------------------
Disciplina: MC714 - 2 semestre 2017
Professor: Lucas Wanner

Nome: Seong Eun Kim
RA: 177143

Descricao: Versao multithread
-------------------------------------
**/


#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define _CONST_ 1048576  // constant to multiply N

pthread_mutex_t lock;

struct array_info {
	long long int *array;
	long long int initial_pos;
	long long int final_pos;
	long long int sum;
};


// generates random number from 0 to 1000
int random_number() {

	return rand()%1001;
}

void* fill_and_mean(void *args) {

	long long int sum = 0;
	struct array_info *ptr = args;

	srand(time(NULL)); // initializes random number generator

	for(long long int i = ptr->initial_pos; i < ptr->final_pos; i++) {
		ptr->array[i] = random_number(); // fill array
		sum += ptr->array[i];
	}
	ptr->sum += sum;
	pthread_exit(NULL);
}

int main(int argc, char *argv[]) {

	struct array_info *ptr;
	int N = atoi(argv[1]);
	int k = atoi(argv[2]);
	pthread_t *tid;
	long long int *array;
	long long int sum = 0;

	tid = malloc(k * sizeof(pthread_t));

	ptr = malloc(k * sizeof(struct array_info));

	// alocacao de N * 2^20 inteiros de 64 bits
	array = (long long int*)malloc((N*_CONST_) * sizeof(long long int));

	for(int i = 0; i < k; i++) { 
		ptr[i].array = array; // each thread has a pointer to the array to be filled
		ptr[i].sum = 0; // each thread gets the sum of the elements of the subarrat
		ptr[i].initial_pos = (long long int)i*N*_CONST_/k; // initial index of the subarray
		ptr[i].final_pos = (long long int)N*_CONST_*(i+1)/k; // final index of the subarray - 1
		if(i == k-1) {
			ptr[i].final_pos = (long long int)N*_CONST_;
		}
		pthread_create(&(tid[i]), NULL, fill_and_mean, &ptr[i]);
	}

	for(int i = 0; i < k; i++) {
		pthread_join(tid[i], NULL); // waits for all threads to execute
		sum += ptr[i].sum; // calculates the sum of the sums of the subarrays
	}

	printf("%lld\n", sum/(N*_CONST_));

	free(ptr->array);
	free(tid);
	free(ptr);

}