from mimetypes import init
import requests

class ProcessOne:
  def __init__(self, code="1000001", n="15000"):
    self.code = code
    self.n = n
    self.response = None


  def send_message(self):
    resposta = requests.get('http://localhost:5000/processo2',
      params={
        "code": self.code,
        "n": self.n
      }
    )
    self.response = (resposta.text)

  def wait_callback(self):
    if (self.response):
      msg = self.response.split("&")

      print(f"Key: {msg[0]}")
      print(f"Tempo: {msg[1]}")
