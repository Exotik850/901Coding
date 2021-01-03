import socket
import subprocess as cmd

def git_pull():
  try:
    cmd.run(["git", "pull"])
  except:
      print('Some error occured while pulling the code')

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
PORT = 9090
socket.bind((HOST, PORT))

socket.listen()
conn, addr = socket.accept()
with conn:
  while True:
    data = conn.recv(1024)
    if not data:
      break
    else:
      if data == b"PUSHED":
        git_pull()


