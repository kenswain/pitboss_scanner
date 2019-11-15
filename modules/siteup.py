#from modules import domain_name
import urllib.error
import urllib.request

def get_site_status(url):
    try:
        con = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        return 'down'
    else:
        return 'up'
