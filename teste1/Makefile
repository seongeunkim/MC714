run:
	gcc -o seq seq.c
	gcc -o multithread multithread.c -lpthread
	gcc -o sharedMultiprocess sharedMultiprocess.c
	time ./seq 64
	time ./multithread 64 4
	time ./sharedMultiprocess 64 4