import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def get_subnet(ip):
    parts = ip.split('.')
    return '.'.join(parts[:3])

def is_same_network(ip1, ip2):
    return get_subnet(ip1) == get_subnet(ip2)