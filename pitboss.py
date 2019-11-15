import argparse
import modules
from modules.general import *
from modules.domain_name import *
from modules.host_scan import *
from modules.ip_address import *
from modules.outdated import *
from modules.robots import *
from modules.whois import *
from modules.siteup import *
from modules.write_csv import *
import csv



ROOT_DIR = "Targets"
creat_dir(ROOT_DIR)

#Setting up parsers for arguments
parser = argparse.ArgumentParser("Looking for command line arguments of domain names")
parser.add_argument('-d', default='None', type=str, help='The is the full domain name you are looking up')
parser.add_argument('-t', default='None', type=str, help='This is the target name.')

args = parser.parse_args()
full_domain = args.d
target = args.t
if full_domain.startswith("http://"):
    full_domain = full_domain
else:
    full_domain = "http://" + full_domain

def gather_info(full_url):
    creat_dir(ROOT_DIR)
    print("Getting IP Address")
    print("")
    ipaddress = get_address(full_url)
    print("")
    print("Getting Domain Name")
    print("")
    domainname = get_domain_name(full_url)
    print("")
    print("Performing Whois")
    print("")
    whois = get_whois(domainname)
    print("")
    print("Downloading Robots.txt file")
    print("")
    robots_txt = get_robots_txt(full_url)
    print("")
    print("Starting Nmap Scan")
    print("")
    nmap = get_nmap(ipaddress)
    print("")
    print("Starting Nikto outdated Scan")
    print("")
    outdated = get_outdated(domainname)
    print("")
    print("Checking site status")
    print("")
    sitestatus = get_site_status(full_url)
    report(ipaddress, domainname, robots_txt, nmap, whois, outdated, sitestatus)
    
def report(ipaddress, domainname, robots_txt, nmap, whois, outdated, sitestatus):
    project_dir = ROOT_DIR + "/" + target
    creat_dir(project_dir)
    write_file(project_dir + "/ipaddress.txt", ipaddress)
    write_file(project_dir + "/domainname.txt", domainname)
    write_file(project_dir + "/robots.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/outdated.txt", outdated)
    write_file(project_dir + "/status.txt", sitestatus)
    checkfile()
    write_findings(target, domainname, ipaddress, sitestatus, whois, robots_txt, outdated, nmap)

if full_domain != 'None' and target != 'None':
    gather_info(full_domain)
else:
    print("You must enter both a target and FQDN to start scan.", "Please use --help for more information", sep="\n\n")