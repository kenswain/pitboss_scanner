from tld import get_fld


### grab fld
def get_domain_name(url):
    tld_domain = get_fld(url)
    return tld_domain

