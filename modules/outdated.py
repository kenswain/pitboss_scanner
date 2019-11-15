import os 
from modules import domain_name

def get_outdated(url):
    command = "nikto -host " + url + ' ' + '-Plugins "outdated"'
    process = os.popen(command)
    results = str(process.read())
    return results