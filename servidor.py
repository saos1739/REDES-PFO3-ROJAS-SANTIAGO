import socket
import threading
from concurrent.futures import ThreadPoolExecutor



HOST = "127.0.0.1"

PUERTO= 5000

def procesar(texto): 
    print("Procesando en:", threading.current_thread().name)
    return texto.upper()
    

def correr_cliente(conexion, direccion_cliente):
    print("Se conecto correctamente", direccion_cliente)
    while True:                                  
        datos = conexion.recv(1024)
        if not datos:
            break
        texto = datos.decode("utf-8")
        print("Recibí:", texto)
        future = pool.submit(procesar, texto) 
        resultado = future.result()             
        conexion.sendall(resultado.encode("utf-8"))
    conexion.close()
    print("Se desconectó", direccion_cliente)


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PUERTO))
servidor.listen() 
print(f"Escuchando en {HOST}:{PUERTO}")
pool = ThreadPoolExecutor(max_workers=4)


while True:
    conexion, direccion_cliente = servidor.accept()
    threading.Thread(
        target=correr_cliente,
        args=(conexion, direccion_cliente),
        daemon=True,
    ).start()


   