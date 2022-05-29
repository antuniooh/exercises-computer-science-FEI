from mimetypes import init
import socket

class ProcessTwo:
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conexao = None
  
  @staticmethod
  def validate_message(data_msg):
    response = None
    print(data_msg)
    if (len(data_msg) > 1):
      code = int(data_msg[0])
      n = int(data_msg[1])

      if ((code) > 10000000):
        if (n <= 15000 and n > 5000 ):
          response = str(data_msg[0]) + "&" + str(data_msg[1])
        else:
          response = "Error: Invalid n -> 5000 < n < 15000"
      else:
        response = "Error: Invalid code - > code > 1000000"
    else:
      response = "Error: Number of args is invalid"
    
    return response

  def wait_response(self, socket):
    while (True):
      dados = socket.recv(1024)
      if (dados):
        print("Resposta do servidor: " + str(dados.decode()))
        return dados.decode()

  def get_message(self, request):
    if (request):
      inputs = []
      inputs.append(int(request.args.get('code')))
      inputs.append(int(request.args.get('n')))

      response = ProcessTwo.validate_message(inputs)

      if "Error" in response:
        return response
      else:
        socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_s.connect((socket.gethostname(), 4003))
        socket_s.sendall(bytes(response))

        response_process_3 = self.wait_response(socket_s)
        return response_process_3
      
