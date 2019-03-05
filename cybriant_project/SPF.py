import dns.resolver #import the module
import checkdmarc
domain_For_Search= ""








class SPFChecker :
def Check_SPF2(self, domain_For_Search):
    myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
myAnswers = myResolver.query(domain_For_Search, "TXT") #Lookup the 'A' record(s) for google.com
for rdata in myAnswers: #for each response
    print (rdata) #print the data

    def Check_SPF_backup (self, domain_For_Search):
return    search_result=(checkdmarc.get_spf_record(domain, nameservers=None, timeout=6.0))
