import socket
import subprocess as cmd

def git_pull():
  try:
    cmd.run(["git", "pull"])
  except:
      print('Some error occured while pulling the code')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname()
PORT = 9999
sock.bind((HOST, PORT))

sock.listen()
conn, addr = sock.accept()
with conn:
  while True:
    data = conn.recv(1024)
    if not data:
      break
    else:
      if data == b"PUSHED":
        git_pull()


