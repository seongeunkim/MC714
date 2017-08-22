#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <time.h>


#define _CONST_ 1048576  // constant to multiply N

//#define _CONST_ 20  // constant to multiply N

// generates random number from 0 to 1000
int random_number() {

	srand(time(NULL)); // initializes random number generator

	return rand()%1001;
}

void fill_and_mean(int id, long long int *array, long long int *sum, long long int initial_pos, long long int final_pos) {
	long long int curr_sum = 0;

	for(long long int i = initial_pos; i < final_pos; i++) {
		array[i] = random_number();
		curr_sum += array[i];
		//printf("##%lld##", array[i]);
	}
	sum[id] = curr_sum;
	//printf("\n");
}


int main(int argc, char *argv[]) {

	int N = atoi(argv[1]);
	int k = atoi(argv[2]);

	int status;

	// sharing the array that will be filled with the random numbers
	const char *mem_name = "array_mem_share";
	int array_mem = shm_open(mem_name, O_CREAT | O_RDWR, 0666);
	ftruncate(array_mem, N * _CONST_ * 8); // memory size is N*2^20 of 64bit int
	void *array_ptr = mmap(0, N * _CONST_ * 8, PROT_READ | PROT_WRITE, MAP_SHARED, array_mem, 0);
	long long int *array_ptr_util = (long long int *)array_ptr;

	// sharing the array that will be filled with the random numbers
	const char *sum_mem_name = "sum_mem_share";
	int sum_mem = shm_open(sum_mem_name, O_CREAT | O_RDWR, 0666);
	ftruncate(sum_mem, k); // memory size is N*2^20 of 64bit int
	void *sum_ptr = mmap(0, k, PROT_READ | PROT_WRITE, MAP_SHARED, sum_mem, 0);
	long long int *sum_ptr_util = (long long int *) sum_ptr;

	pid_t *pid = malloc(k * sizeof(pid_t));

	for(int i = 0; i < k; i++) {
		pid[i] = fork();

		if (pid[i] == 0) { //son
			long long int initial_pos = (long long int)i*N*_CONST_/k;
			long long int final_pos = (long long int)N*_CONST_*(i+1)/k;
			if(i == k-1) {
				final_pos = N*_CONST_;
			}
			fill_and_mean(i, array_ptr_util, sum_ptr_util, initial_pos, final_pos);
			exit(0);
		} else if (pid[i] < 0) {
			printf("Fork failed.\n");
		}
	}

	long long int sum = 0;

	for(int i = 0; i < k; i++) {
		if(pid[i] > 0) {
			waitpid(pid[i], &status, 0);
			sum += sum_ptr_util[i];
		}
	}

	printf("%lld\n", sum/(N*_CONST_));


	shm_unlink(mem_name);
	shm_unlink(sum_mem_name);

}