import dns.resolver


domain_for_search= ""
def FindSPF(domain_for_search):

# Add error handling here!
      tmpList = domain_for_search.split(".")
      domain_for_search = tmpList[1]+"."+tmpList[2]

      answer=dns.resolver.query(domain_for_search,"TXT")
      for data in answer:

        if "v=spf1" in data.to_text():
          print (data)
          return(1)
      else:
          return(0)
