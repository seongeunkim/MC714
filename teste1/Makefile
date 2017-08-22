run:
	gcc -o seq seq.c
	gcc -o multithread multithread.c -lpthread
	gcc -o sharedMultiprocess sharedMultiprocess.c
	time ./seq 64
	time ./multithread 64 2
	time ./multithread 64 4
	time ./multithread 64 6
	time ./multithread 64 8
	time ./sharedMultiprocess 64 2
	time ./sharedMultiprocess 64 4
	time ./sharedMultiprocess 64 6
	time ./sharedMultiprocess 64 8