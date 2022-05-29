from mimetypes import init
import re
import socket
import sympy
import time

class ProcessThree:
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conexao = None
  
  def get_all_primes(self, data_msg):
    code = int(data_msg[0])
    n = int(data_msg[1])

    print("Codigo inicial: " + str(code))
    print("N: " + str(n))

    i = 0
    prime_count_before = 0
    prime_before = 0

    start = time.time()
    prime_after = (sympy.nextprime(code, ith=n))

    while (True):
        i+=1
        current_value_sub = code-i

        if sympy.isprime(current_value_sub):
            prime_count_before += 1
            if (prime_count_before == n):
                prime_before = current_value_sub
        
        if (prime_before > 0):
          break
  
    finish = time.time()
    return str(prime_before * prime_after) + "&" + str(finish - start)

  def get_message(self):
     while (True):
      data = self.conexao.recv(1024)
      if (data):
        decoded_message = data.decode()
        print(f"Mensagem recebida: {decoded_message}")
        inputs = decoded_message.split("&")

        response = self.get_all_primes(inputs)
        print("Key: " + response)

        self.conexao.sendall(bytes(response, encoding='utf-8'))
        break

  def wait_client(self):
    self.s.bind((socket.gethostname(), 4003))
    print(self.s)
    self.s.listen()
    while True:
      self.conexao, addr = self.s.accept()
      print(f"Cliente conectado: {addr}")
      self.get_message()

