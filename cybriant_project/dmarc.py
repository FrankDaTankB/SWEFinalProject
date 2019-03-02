import checkdmarc
def check_Dmarc(self, domain_For_Search):

return checkdmarc.get_dmarc_record(domain_For_Search, include_tag_descriptions=False, nameservers=None, timeout=6.0))
