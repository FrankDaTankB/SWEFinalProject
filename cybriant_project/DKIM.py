import dns.resolver


domain_for_search= ""
DKIMString="._domainkey."
DKIMSelector=""


def FindDKIM(domain_for_search,DKIMString,DKIMSelector):
      answer=dns.resolver.query(DKIMSelector+DKIMString+domain_for_search,"TXT")
      for data in answer:

        if "v=DKIM1" in data.to_text():
          print (data)
          return(1)
        else:
          return(0)


#example of how to call this funtion
#domain_for_search= "agari.com"
#DKIMSelector="s1024"
#print(FindDKIM(domain_for_search,DKIMString,DKIMSelector,count))
#This will return the DKIM record as well as a 1 for pass, 0 for fail.
#"s1024._domainkey.agari.com" --final string for query
