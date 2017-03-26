import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)
    
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

res = raw_input('Qual o endereço do servidor? ')

print "Coletando dados do servidor..."
socket.connect (res)

# Inscrição nos filtros desejados
topicSegmento = 'filtro1'
topicProduto = 'produto1'
topicValor = '10001'
socket.setsockopt(zmq.SUBSCRIBE, topicSegmento)
socket.setsockopt(zmq.SUBSCRIBE, topicProduto)
socket.setsockopt(zmq.SUBSCRIBE, topicValor)

# Processa até 10 topicos
total_value = 0
for update_nbr in range (10):
    string = socket.recv()
    topicFilter, messageData = string.split()
    print "Topico: %s, Mensagem: %s" % (topicFilter, messageData)

    

      
