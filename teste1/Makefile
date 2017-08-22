# ----------------------------------------
# Disciplina: MC714 - 2 semestre 2017
# Professor: Lucas Wanner
#
# Nome: Seong Eun Kim
# RA: 177143
#
# Descricao: Makefile para o teste01
# ----------------------------------------


# Compile, execute and get execution time of each program
run:
	gcc -o seq seq.c
	gcc -o multithread multithread.c -lpthread
	gcc -o sharedMultiprocess sharedMultiprocess.c
	time ./seq 64
	time ./multithread 64 4
	time ./sharedMultiprocess 64 4

# Delete executable files
clean:
	rm -f seq multithread sharedMultiprocess