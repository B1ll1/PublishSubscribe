Link do projeto no GitHub: 

Windows:

Passo 1 - Download do python: https://www.python.org/downloads/release/python-2713/

Passo 2 - Acessar a pasta C:\Python27\Scripts e executar o comando pip install pyzmq

Passo 3 - instalar ngrok
Baixe o executável para seu windows em https://ngrok.com/download depois extraia em uma pasta que se lembre qual é

Passo 4 - subir o servidor
clique com o botal direito no arquivo publishServer.py e escolha Edit with IDLE
clique na aba Run > Run Module

Passo 5 - abrir a porta local com o ngrok
clique duas vezes no executavel do ngrok e rode o comando ngrok tcp 5556, é a porta que o servidor usa

Passo 6 - rodar o client
clique com o botao direito no arquivo subscriberClient.py e escolha Edit with IDLE
clique na aba Run > Run Module
entre com o enderço que o ngrok gerou ao abrir a porta
aguarde as respostas do servidor

Ubuntu:

Passo 1 - Instalar o python

sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python2.7

Passo 2 - instalar o pip

sudo apt-get update
sudo apt-get -y install python-pip

Passo 3 - instalar pyzmq

sudo apt-get install python-zmq

Caso não funcione tente
sudo pip install pyzmq

Passo 4 - instalar ngrok
Baixe o ngrok de https://ngrok.com/download e depois extraia na pasta /usr/local/bin, feito isso crie uma conta no site do ngrok e pegue sua authtoken daí 
rode o comando ngrok authtoken 'seu token' no terminal

Passo 5 - subir o servidor
python publisherServer.py

Passo 6 - abrir a porta local com o ngrok 
rode o comando ngrok tcp 5556, é a porta que o servidor usa
 
Passo 7 - rodar o client
python subscriberClient.py
entre com o endereço que o ngrok retornar para você no terminal
aguarde as respostas do servidor


