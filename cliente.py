import socket


HOST = "127.0.0.1"

PUERTO= 5000




cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PUERTO)) 

while True:
    mensaje = input("Mensaje (vacío para salir): ")
    if not mensaje:
        break
    
    cliente.sendall(mensaje.encode("utf-8"))
    datos = cliente.recv(1024)
    respuesta = datos.decode("utf-8")
    print("Servidor dice:", respuesta)


cliente.close()
print("Se desconectó del servidor")
