import checkdmarc

domain_for_search=""
count=0
def DMARCFound(domain_for_search, count):

      answer=checkdmarc._query_dmarc_record(domain_for_search, nameservers=None, timeout=6.0)
      for data in answer:

        if "v=DMARC1;" in answer:
          return(1)
        else:
          return(0)


#print(PrintandGoogle("youtube.com",count))    this is an example call of the function


print(checkdmarc._query_dmarc_record(domain_for_search, nameservers=None, timeout=6.0))


def showDMARC(domain_for_search):

      print(checkdmarc._query_dmarc_record(domain_for_search, nameservers=None, timeout=6.0))
