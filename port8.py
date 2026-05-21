 
import socket

s = socket.socket()
s.settimeout(5)
 
status = s.connect_ex(("127.0.0.1", 8080))
 
if status == 10061:
    print("[+] Port 8080 is OPEN")
else:
    print(f"[-] Port 8080 is CLOSED")
    print(f"Error Code : {status}")
if status == 10061:
    print("reason:f")
elif status == 10081:  
    print("reason:hn")
elif status == 10041:
    print("reason:")
else:
    print("unknown")  
