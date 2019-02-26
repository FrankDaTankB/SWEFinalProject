#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import argparse
from ipwhois import IPWhois
from itertools import product
import socket
import signal

def dns_timeout(a,b):
	raise Exception("DNS timeout")

# use socket library to get ip address
#documentation: https://docs.python.org/2/library/socket.html
def getIPHostname(hostname):
	try:
		return (socket.gethostbyname(hostname)).strip()
	except IOError:
		# could have a more descriptive error?
		print('Error')

	return None


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def filler(word, from_char, to_char):
   options = [(c,) if c != from_char else (from_char, to_char) for c in word]
   return (''.join(o) for o in product(*options))

def filler_list(word_list, from_char, to_char):
   return_list=[]
   for word in word_list:
      return_list=return_list+list(filler(word,from_char,to_char))
   return return_list


parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('''\
'''))
parser.add_argument("-d", type=str, dest="domain", help="Domain Name")
if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
args = parser.parse_args()

tmpList=(args.domain).split(".")
tmpDomainSplit=(args.domain).split(".")
topDomainList=[]
tldDomain=''

# This is the collection of all the punycode characters we are checking
#https://www.irongeek.com/homoglyph-attack-generator.php
#some of these are still throwing errors
charList=[]
charList.append(['a','À|Á|Â|Ã|Ä|Å|à|á|â|ã|ä|å|ɑ|Α|α|а|Ꭺ|Ａ|ａ'])
charList.append(['b','ß|ʙ|Β|β|В|Ь|Ᏼ|ᛒ|Ｂ|ｂ'])
charList.append(['c','ϲ|Ϲ|С|с|Ꮯ|Ⅽ|ⅽ|Ｃ|ｃ'])
charList.append(['d','Ď|ď|Đ|đ|ԁ|ժ|Ꭰ|ḍ|Ⅾ|ⅾ|Ｄ|ｄ'])
charList.append(['e','È|É|Ê|Ë|é|ê|ë|Ē|ē|Ĕ|ĕ|Ė|ė|Ę|Ě|ě|Ε|Е|е|Ꭼ|Ｅ|ｅ'])
charList.append(['f','F|f|Ϝ|Ｆ|ｆ'])
charList.append(['g','ɢ|Ԍ|Ꮐ|Ｇ|ｇ'])
charList.append(['h','ʜ|Η|Н|һ|Ꮋ|Ｈ|ｈ'])
charList.append(['i','l|ɩ|Ι|І|і|ا|Ꭵ|ᛁ|Ⅰ|ⅰ|ｉ'])
charList.append(['j','ϳ|Ј|ј|յ|Ꭻ|Ｊ|ｊ'])
charList.append(['k','Κ|κ|К|Ꮶ|ᛕ|K|Ｋ|ｋ'])
charList.append(['l','ʟ|ι|ا|Ꮮ|Ⅼ|ⅼ|Ｌ|ｌ'])
charList.append(['m','Μ|Ϻ|М|Ꮇ|ᛖ|Ⅿ|ⅿ|Ｍ|ｍ'])
charList.append(['n','ɴ|Ν|Ｎ|ｎ'])
charList.append(['o','0|O|o|Ο|ο|О|о|Օ|Ｏ|ｏ'])
charList.append(['p','Ρ|ρ|Р|р|Ꮲ|Ｐ|ｐ'])
charList.append(['q','Ⴍ|Ⴓ|Ｑ|ｑ'])
charList.append(['r','ʀ|Ի|Ꮢ|ᚱ|Ｒ|ｒ'])
charList.append(['s','Ѕ|ѕ|Տ|Ⴝ|Ꮪ|𐐠|Ｓ|ｓ'])
charList.append(['t','Τ|τ|Т|Ꭲ|Ｔ|ｔ'])
charList.append(['u','μ|υ|Ա|Ս|⋃|Ｕ|ｕ'])
charList.append(['v','ν|Ѵ|ѵ|Ꮩ|Ⅴ|ⅴ|Ｖ|ｖ'])
#charList.append(['w','ѡ|Ꮃ|Ｗ|ｗ'])
#charList.append(['x','Χ|χ|Х|х|Ⅹ|ⅹ|Ｘ|ｘ'])
#charList.append(['y','ʏ|Υ|γ|у|Ү|Ｙ|ｙ'])
#charList.append(['z','Ζ|Ꮓ|Ｚ|ｚ'])


mutateList=[]
tmpResultList=[]
if len(tmpDomainSplit)==2:
	for char in charList:
		if char[0] in tmpList[0]:
			mutateList.append(char)

	tldDomain=tmpDomainSplit[1]
	wordList=[]
	wordList.append(tmpDomainSplit[0])

	for char in charList:
		if "|" not in char[1]:
			list1=list(filler(wordList[0], char[0],char[1]))
			for x in list1:
				x=str(x)
				if x not in tmpResultList:
					tmpResultList.append(x)
					if x!=tmpDomainSplit[0]:
						x = x.encode("idna")
						ip=getIPHostname(x+str.encode("."+tldDomain))
						if ip!=None:

							print(( x+"."+tldDomain+"\t"+x+"."+tldDomain+" ["+ip+"]"))
						else:
							x = str(x.encode("idna"))
							print((x+"."+tldDomain+"\t"+x+"."+tldDomain+" [Not Registered]"))
		else:
			tmpCharList=char[1].split("|")
			for y in tmpCharList:
				list1=list(filler(wordList[0], char[0],y))
				for x in list1:

					if x not in tmpResultList:
						tmpResultList.append(x)
						if x!=tmpDomainSplit[0]:
							x = x.encode("idna")
							ip=getIPHostname(x+str.encode("."+tldDomain))
							if ip!=None:

								x = str(x)
								print((x+"."+tldDomain+"\t"+x+"."+tldDomain+" ["+ip+"]"))
							else:
								x = str(x)								
								print(( x+"."+tldDomain+"\t"+x+"."+tldDomain+" [Not Registered]"))
