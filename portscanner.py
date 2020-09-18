import socket
from queue import Queue
import threading

target = "127.0.0.1"
queue = Queue()
open_port = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1,1024):
            queue.put(port)
    elif mode == 1:
        for port in range(1,49512):
            queue.put(port)
    elif mode == 1:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        result = portscan(port)
        if result:
            print("Port {} is open".format(port))
            open_port.append(port)

def run_scanner(threads,mode):
    get_ports(mode)
    thread_list = []

    for t in range(100):
        thread = threading.Thread(target = worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are: ",open_port)

run_scanner(100,1)
