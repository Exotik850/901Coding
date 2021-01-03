import socket
import subprocess as cmd
commit_message = input("Commit Message: ")
REPO = "C:/Users/ExO/Desktop/901Coding/.git"
HOST = "104.200.18.207"
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # s.connect((HOST, PORT))
  def git_push():
    try:
      cmd.run(["git", "add", "."])
      cmd.run(["git", "commit", "-m", commit_message])
      cmd.run(["git", "push", "origin", "main"])
      # repo = git.Repo(REPO)
      # repo.git.add(update=True)
      # repo.index.commit(commit_message)
      # # repo.git.push()
      # origin = repo.remote(name='origin')
      # origin.push()
      # s.send(b"PUSHED")
    except:
        print('Some error occured while pushing the code')
    
  git_push()