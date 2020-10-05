from http.client import HTTPConnection

def dorequest(url):
  conexion = HTTPConnection(url)
  conexion.request('GET', '/')
  resultado = conexion.getresponse()
  contenido = resultado.read()
  print(contenido)

url = input("Introduce la url: ")
dorequest(url)