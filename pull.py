import socket
import git

def git_pull():
  try:
    repo = Repo("/var/www/html/901Coding/.git")
    origin = repo.remote(name='origin')
    origin.pull()
  except:
      print('Some error occured while pulling the code')

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
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


