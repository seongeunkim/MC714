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

Pelo gráfico, podemos observar que teve uma maior queda no tempo de processamento de _k=2_ para _k=4_ em relação aos outros. Isso se deve pois há uma queda de eficiência na troca dentro dos processadores lógicos.

![alt](https://github.com/seongeunkim/MC714/blob/master/teste1/grafico.png)


### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md] [PlDb] |
| Github | [plugins/github/README.md] [PlGh] |
| Google Drive | [plugins/googledrive/README.md] [PlGd] |
| OneDrive | [plugins/onedrive/README.md] [PlOd] |
| Medium | [plugins/medium/README.md] [PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md] [PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
