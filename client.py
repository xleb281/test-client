import socket
import time
import platform
import psutil
import os 
import shutil


server_address = ('localhost', 12345) # укажите адрес и порт сервера
processes = psutil.process_iter()
connected = False
while not connected:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server_address)
        connected = True
        print('Connected to server')
    except ConnectionRefusedError:
        print('Connection failed, retrying in 5 seconds...')
        time.sleep(5)

while True:
    data = client.recv(1024).decode()
    
    if data == "stop":
        message = "stop"
        client.send(message.encode())
        exit()
    elif data == "info":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        message = "IP:" + ip_address + ";  name:" + socket.gethostname() + ";  system version:" + platform.version()
        client.send(message.encode())
    elif data == "programs":
        processes = psutil.process_iter()
        client.send(processes.encode())

    else:
        message = "Error command: " + data
        client.send(message.encode())

client.close()
