import dns.resolver


bls = ["zen.spamhaus.org","cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de",
    "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcannibal.org", "bl.spamcop.net",
    "xbl.spamhaus.org", "pbl.spamhaus.org", "dnsbl-1.uceprotect.net", "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net", "db.wpbl.info"]



myIP = ""

#0.0.0.0-255.255.255.255
def check_black_lists(myIP):
    count=0
    for bl in bls:
        try:
            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            print ('IP: %s IS listed in %s (%s: %s)' %(myIP, bl, answers[0], answer_txt[0]))
            count+=1
        except dns.resolver.NXDOMAIN:
            print ('IP: %s is NOT listed in %s' %(myIP, bl))
    return(count)
def check_Ip_Range(ipA, ipB, ipC):
    count=0
    for x in range(ipB, ipC):
        count+=check_black_lists(ipA+str(x))
    return(count)


#myIP="4.4.4.12"
#check_black_lists(myIP)
#example of how to call the range version of the Lookup
#An ip has 4 sections, provide the first three as the first input, then the lower 4th section, then the higher 4th section.
#check_Ip_Range("4.4.4.",12,15)

#output will look like this
#IP: 4.4.4.12 IS listed in zen.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.12")
#IP: 4.4.4.12 is NOT listed in cbl.abuseat.org
#IP: 4.4.4.12 is NOT listed in virbl.dnsbl.bit.nl
#IP: 4.4.4.12 is NOT listed in dnsbl.inps.de
#IP: 4.4.4.12 is NOT listed in ix.dnsbl.manitu.net
#IP: 4.4.4.12 is NOT listed in dnsbl.sorbs.net
#IP: 4.4.4.12 is NOT listed in bl.spamcannibal.org
#IP: 4.4.4.12 is NOT listed in bl.spamcop.net
#IP: 4.4.4.12 is NOT listed in xbl.spamhaus.org
#IP: 4.4.4.12 IS listed in pbl.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.12")
#IP: 4.4.4.12 is NOT listed in dnsbl-1.uceprotect.net
#IP: 4.4.4.12 is NOT listed in dnsbl-2.uceprotect.net
#IP: 4.4.4.12 is NOT listed in dnsbl-3.uceprotect.net
#IP: 4.4.4.12 is NOT listed in db.wpbl.info
#IP: 4.4.4.13 IS listed in zen.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.13")
#IP: 4.4.4.13 is NOT listed in cbl.abuseat.org
#IP: 4.4.4.13 is NOT listed in virbl.dnsbl.bit.nl
#IP: 4.4.4.13 is NOT listed in dnsbl.inps.de
#IP: 4.4.4.13 is NOT listed in ix.dnsbl.manitu.net
#IP: 4.4.4.13 is NOT listed in dnsbl.sorbs.net
#IP: 4.4.4.13 is NOT listed in bl.spamcannibal.org
#IP: 4.4.4.13 is NOT listed in bl.spamcop.net
#IP: 4.4.4.13 is NOT listed in xbl.spamhaus.org
#IP: 4.4.4.13 IS listed in pbl.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.13")
#IP: 4.4.4.13 is NOT listed in dnsbl-1.uceprotect.net
#IP: 4.4.4.13 is NOT listed in dnsbl-2.uceprotect.net
#IP: 4.4.4.13 is NOT listed in dnsbl-3.uceprotect.net
#IP: 4.4.4.13 is NOT listed in db.wpbl.info
#IP: 4.4.4.14 IS listed in zen.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.14")
#IP: 4.4.4.14 is NOT listed in cbl.abuseat.org
#IP: 4.4.4.14 is NOT listed in virbl.dnsbl.bit.nl
#IP: 4.4.4.14 is NOT listed in dnsbl.inps.de
#IP: 4.4.4.14 is NOT listed in ix.dnsbl.manitu.net
#IP: 4.4.4.14 is NOT listed in dnsbl.sorbs.net
#IP: 4.4.4.14 is NOT listed in bl.spamcannibal.org
#IP: 4.4.4.14 is NOT listed in bl.spamcop.net
#IP: 4.4.4.14 is NOT listed in xbl.spamhaus.org
#IP: 4.4.4.14 IS listed in pbl.spamhaus.org (127.0.0.11: "https://www.spamhaus.org/query/ip/4.4.4.14")
#IP: 4.4.4.14 is NOT listed in dnsbl-1.uceprotect.net
#IP: 4.4.4.14 is NOT listed in dnsbl-2.uceprotect.net
#IP: 4.4.4.14 is NOT listed in dnsbl-3.uceprotect.net
#IP: 4.4.4.14 is NOT listed in db.wpbl.info
