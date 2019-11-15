import csv
import os



def checkfile():
    firstrow = ['traget', 'domain_name', 'ip_address', 'siteup', 'whois', 'robots', 'outdated', 'nmap_scan']
    if not os.path.exists('findings.csv'):
        command = 'touch findings.csv'
        process = os.popen(command)
        with open('findings.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(firstrow)
            csvFile.close

def write_findings(target, domain_name, ip_address, siteup, whois, robots, outdated, nmap_scan):
    findings = [target, domain_name, ip_address, siteup, whois, robots, outdated, nmap_scan]
    with open('people1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(findings)
        csvFile.close()