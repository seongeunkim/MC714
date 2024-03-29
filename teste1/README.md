# Teste 01

### Introdução
Este teste teve como objetivo estudar a diferença de desempenho em processos e threads e a versão sequencial. Para isso, foi testado o tempo de execução para preencher um vetor de inteiros com números aleatórios de 0 a 1000 e calcular a sua média de três formas:
- Versão sequencial
- Versão multithread
- Versão multiprocesso

### Dados
Ao executarmos as três aplicações para um vetor de 2^26 números inteiros de 64 bits, com _k = 4_, obtivemos o seguinte resultado:
```sh
time ./seq 64
499
0.99 real         0.74 user         0.22 sys
time ./multithread 64 4
500
0.90 real         2.06 user         0.32 sys
time ./sharedMultiprocess 64 4
500
0.40 real         0.92 user         0.27 sys
```

Para melhor avaliarmos o desempenho do multithreading e do multiprocessing, construímos um gráfico do tempo de processamento pelo número de processos e threads.

| ![alt](/Users/seongeunkim/Dropbox (Personal)/MC714/teste1) |
|:--:|
| *Gráfico do número de threads/processos pelo tempo de processamento em segundos* |

### Análise
Com os valores obtidos na execução do programa, pudemos comparar o tempo real de processamento e ver que a versão multiprocesso possui maior desempenho, seguida pela versão multithread e, por fim, a versão sequencial.

Pelo gráfico, podemos observar que quanto o maior número de processos e threads (_k_), menor o tempo de execução, pois o problema é altamente paralelizável. Vemos, também, que há uma maior queda no tempo de processamento de _k=2_ para _k=4_ em relação às demais variações de _k_. Isso se deve possivelmente pois há uma queda de eficiência na troca dentro dos processadores lógicos.

### Conclusão
Nesse primeiro trabalho foi possível estudar a pertinência do uso de multithreads e multiprocessadores em algoritmos, pois observou-se melhor desempenho na sua execução em relaçao à versão sequencial.
