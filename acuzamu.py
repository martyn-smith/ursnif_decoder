"""
"""

def decode(ciphertext):
    key = ''.join([(" " * 32), "xz.~^7;>od-DF )}uS1[=cU`mGWis3MT4{N%9Zq2/Ew(&+",
                    "vkV:l\!hKp8fCOAR6?0|nYbI_LtPB'H<Q$Xy\"aJ@g#j5],*re"])
    plaintext = ''.join([key[ord(x)] for x in ciphertext])
    return (ciphertext[0:4] + "...   " + plaintext)

print(decode('P~})sbs')) #"Verdana"
print(decode('ZU~5O-11g-5~}h;Y;5sh~""')) #"check SSL certificate.."
print(decode('-----iR~s<~-Js;h""""""')) #"please wait......"
print(decode('UhhWQHHh}0URs}bs*8s50}s""5!H;8vHR(v(""v;Y')) #"http://truhlarna-macura..cz/img/logo..gif"
print(decode('UhhWQHHv0s8sh~b""5(8HW}0~dsHR(v(""v;Y')) #"http://guamaten..com/prueba/logo..gif"
print(decode('UhhWQHHW}~Y8sF0s""5(8Hf50<0);HR(v(""v;Y')) #"http://prefmaqua..com/_cusudi/logo..gif"
print(decode('B(-;bh~}b~h-s55~<<""-?0}b-(YY-sbq-Y;}~JsRR-(}-sbh;*N;}0<-<(YhJs}~-sb)-h}q-svs;b""')) #"No internet access.. Turn off any firewall or anti-virus software and try again..""
print(decode('I}}(}')) #"Error"
print(decode('?U~-Y;R~-;<-5(}}0Wh~)-sb)-5sbb(h-d~-(W~b~)')) #"The file is corrupted and cannot be opened"
print(decode('15};Wh;bv"",;R~1q<h~8[dx~5h')) #"Scripting..FileSystemObject"
print(decode('u~5U(-(YY')) #"@echo off"
print(decode('W;bu-G2""2G""@@""G=-*b-2-*J-G```-\'-B6g')) #"pin@ 21.12.44.23 -n 1 -w 2000 NUL"
print(decode('<hs}h-')) #"start"
print(decode('[W~b')) #"Open"
