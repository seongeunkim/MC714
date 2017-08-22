# Teste 01

Este teste teve como objetivo estudar a diferença de desempenho em processos e threads e a versão sequencial. Para isso, foi testado o tempo de execução para preencher um vetor de inteiros com números aleatórios de 0 a 1000 e calcular a sua média de três formas:
- Versão sequencial
- Versão multithread
- Versão multiprocesso

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
Assim, comparando-se o tempo real de processamento, vemos que a versão multiprocesso possui maior desempenho, seguida pela versão multithread e, por fim, a versão sequencial. 

| ![alt](https://github.com/seongeunkim/MC714/blob/master/teste1/grafico.png) |
|:--:| 
| *Gráfico do número de threads/processos pelo tempo de processamento em segundos* |

Pelo gráfico, podemos observar que quanto o maior número de processos e threads (_k_), menor o tempo de execução, pois o problema é altamente paralelizável. Vemos, também, que há uma maior queda no tempo de processamento de _k=2_ para _k=4_ em relação às demais variações de _k_. Isso se deve possivelmente pois há uma queda de eficiência na troca dentro dos processadores lógicos.
