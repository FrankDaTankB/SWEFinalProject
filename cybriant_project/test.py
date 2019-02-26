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

def getIPHostname(hostname):
	try:
		return (socket.gethostbyname(hostname)).strip()
	except IOError:
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

#https://www.irongeek.com/homoglyph-attack-generator.php
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

charList=[]
charList.append(['a','A|a|À|Á|Â|Ã|Ä|Å|à|á|â|ã|ä|å|ɑ|Α|α|а|Ꭺ|Ａ|ａ'])
charList.append(['b','B|b|ß|ʙ|Β|β|В|Ь|Ᏼ|ᛒ|Ｂ|ｂ'])
#charList.append(['c','C|c|ϲ|Ϲ|С|с|Ꮯ|Ⅽ|ⅽ|Ｃ|ｃ'])
#charList.append(['d','D|d|Ď|ď|Đ|đ|ԁ|ժ|Ꭰ|ḍ|Ⅾ|ⅾ|Ｄ|ｄ'])
#charList.append(['e','E|e|È|É|Ê|Ë|é|ê|ë|Ē|ē|Ĕ|ĕ|Ė|ė|Ę|Ě|ě|Ε|Е|е|Ꭼ|Ｅ|ｅ'])
#charList.append(['f','F|f|Ϝ|Ｆ|ｆ'])
#charList.append(['g','G|g|ɡ|ɢ|Ԍ|Ꮐ|Ｇ|ｇ'])
#charList.append(['h','H|h|ʜ|Η|Н|һ|Ꮋ|Ｈ|ｈ'])
#charList.append(['i','I|i|l|ɩ|Ι|І|і|ا|Ꭵ|ᛁ|Ⅰ|ⅰ|ｉ'])
#charList.append(['j','J|j|ϳ|Ј|ј|յ|Ꭻ|Ｊ|ｊ'])
#charList.append(['k','K|k|Κ|κ|К|Ꮶ|ᛕ|K|Ｋ|ｋ'])
#charList.append(['l','L|l|ʟ|ι|ا|Ꮮ|Ⅼ|ⅼ|Ｌ|ｌ'])
#charList.append(['m','M|m|Μ|Ϻ|М|Ꮇ|ᛖ|Ⅿ|ⅿ|Ｍ|ｍ'])
#charList.append(['n','N|n|ɴ|Ν|Ｎ|ｎ'])
#charList.append(['o','0|O|o|Ο|ο|О|о|Օ|Ｏ|ｏ'])
#charList.append(['p','P|p|Ρ|ρ|Р|р|Ꮲ|Ｐ|ｐ'])
#charList.append(['q','Q|q|Ⴍ|Ⴓ|Ｑ|ｑ'])
#charList.append(['r','R|r|ʀ|Ի|Ꮢ|ᚱ|Ｒ|ｒ'])
#charList.append(['s','S|s|Ѕ|ѕ|Տ|Ⴝ|Ꮪ|𐐠|Ｓ|ｓ'])
#charList.append(['t','T|t|Τ|τ|Т|Ꭲ|Ｔ|ｔ'])
#charList.append(['u','U|u|μ|υ|Ա|Ս|⋃|Ｕ|ｕ'])
#charList.append(['v','V|v|ν|Ѵ|ѵ|Ꮩ|Ⅴ|ⅴ|Ｖ|ｖ'])
#charList.append(['w','W|w|ѡ|Ꮃ|Ｗ|ｗ'])
#charList.append(['x','X|x|Χ|χ|Х|х|Ⅹ|ⅹ|Ｘ|ｘ'])
#charList.append(['y','Y|y|ʏ|Υ|γ|у|Ү|Ｙ|ｙ'])
#charList.append(['z','Z|z|Ζ|Ꮓ|Ｚ|ｚ'])


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
							print(ip)
							print(( x+"."+tldDomain+"\t"+x+"."+tldDomain+" ["+ip+"]"))
						else:
							x = str(x.encode("idna"))
							print((x+"."+tldDomain+"\t"+x+"."+tldDomain+" [ALERT]"))
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
								print(ip)
								x = str(x)
								print((x+"."+tldDomain+"\t"+x+"."+tldDomain+" ["+ip+"]"))
							else:
								x = str(x)
								print("not Registered")
								print(( x+"."+tldDomain+"\t"+x+"."+tldDomain+" [Not Registered]"))
