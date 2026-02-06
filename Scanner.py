import socket
import threading
from queue import Queue
from datetime import datetime

# 1. Define the target
target = input("Enter the IP address to scan (e.g., 127.0.0.1): ")

# 2. Print a banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

# 3. Create a lock for printing so text doesn't get messy
print_lock = threading.Lock()

# 4. Define the port scanning function
def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait 1 second max
        con = s.connect((target, port))
        with print_lock:
            print(f"[+] Port {port} is OPEN")
        con.close()
    except:
        pass # Port is closed or unreachable

# 5. Threading to make it fast
def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

q = Queue()

# Create 30 threads (workers)
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# 6. Assign ports 1 to 1000 to be scanned
for worker in range(1, 1001):
    q.put(worker)

q.join()
print("Scanning completed.")