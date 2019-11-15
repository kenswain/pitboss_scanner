import socket
import modules
from modules import domain_name

def get_address(url):
    host = domain_name.get_domain_name(url)
    host = str(host)
    ip = socket.gethostbyname(host)
    ip = str(ip)
    return ip
