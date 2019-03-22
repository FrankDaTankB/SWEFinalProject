import dns.resolver


domain_for_search= ""
count=0
def FindSPF(domain_for_search, count):

      answer=dns.resolver.query(domain_for_search,"TXT")
      for data in answer:

        if "v=spf1" in data.to_text():
          print (data)
          return(1)


#print(FindSPF(domain_for_search,count))            How to call the function
#This will return the SPF record as well as a 1 for pass, nothing for fail.
