
import subprocess
from rich.console import Console

print = Console().print

def send_imessage(reciever_contact: str, message: str):
    res = subprocess.run(["osascript", "-e", "message_sender.scpt"], stderr=subprocess.PIPE)
    print(res)
    
    if res.returncode != 0:
        print(res.stderr.decode('utf-8'))
    
send_imessage("bishopandrew49@gmail.com", "Testing")