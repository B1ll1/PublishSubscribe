import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:%s' % port)

while True:
    segmentoMercado = ['filtro1', 'filtro2', 'filtro3']
    produto = ['produto1', 'produto2', 'produto3'] 

    
    valor = random.randrange(9999,10005)
    sorteio1 = random.randrange(0,2)
    sorteio2 = random.randrange(0,2)
    
    messageDataSegmento = 'segmento'
    messageDataProduto = 'produto'
    messageDataValor = 'valor'
    
    print ('Segmento Mercado: %s, Produto: %s, Valor: %d' % (segmentoMercado[sorteio1], produto[sorteio2], valor))
    socket.send('%s %s' % (segmentoMercado[sorteio1], messageDataSegmento))
    socket.send('%s %s' % (produto[sorteio2], messageDataProduto))
    socket.send('%d %s' % (valor, messageDataValor))
    time.sleep(1)
