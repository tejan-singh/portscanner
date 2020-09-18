import socket

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
            worker(port)

    elif mode == 2:
        for port in range(1,49512):
            worker(port)

    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            worker(port)

    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            worker(port)

def worker(port):
    port = port
    result = portscan(port)
    if result:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

mode = int(input(" Press 1 for reserved ports \n Press 2 for all ports \n Press 3 for Critical ports \n Press 4 for manual ports \n"))
target = input("Enter Target IP: ")
get_ports(mode)
