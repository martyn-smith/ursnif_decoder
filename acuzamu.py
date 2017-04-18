"""
"""

def foo(ciphertext):
    key = "xz.~^7;>od-DF )}uS1[=cU`mGWis3MT4{N%9Zq2/Ew(&+vkV:l\!hKp8fCOAR6?0|nYbI_LtPB'H<Q$Xy\"aJ@g#j5],*re"
    key = (" " * 32) + key
    #print ([ord(ciphertext[i]) - 32 for i in range(0, len(ciphertext))])
    plaintext = ''.join([key[ord(x)] for x in ciphertext])
    return (ciphertext[0:4] + "...   " + plaintext)

print(foo('P~})sbs')) #"Verdana"
print(foo('ZU~5O-11g-5~}h;Y;5sh~""')) #"check SSL certificate: "
print(foo('-----iR~s<~-Js;h""""""')) #"please wait"
print(foo('UhhWQHHh}0URs}bs*8s50}s""5!H;8vHR(v(""v;Y')) #some URL (http!)
print(foo('UhhWQHHv0s8sh~b""5(8HW}0~dsHR(v(""v;Y'))
print(foo('UhhWQHHW}~Y8sF0s""5(8Hf50<0);HR(v(""v;Y'))
print(foo('B(-;bh~}b~h-s55~<<""-?0}b-(YY-sbq-Y;}~JsRR-(}-sbh;*N;}0<-<(YhJs}~-sb)-h}q-svs;b""'))
print(foo('I}}(}'))
print(foo('?U~-Y;R~-;<-5(}}0Wh~)-sb)-5sbb(h-d~-(W~b~)'))
print(foo('15};Wh;bv"",;R~1q<h~8[dx~5h'))
print(foo('u~5U(-(YY'))
print(foo('W;bu-G2""2G""@@""G=-*b-2-*J-G```-\'-B6g')) #ping 21.12.44.23 -n 1 -w 2000 NUL - that's a DoD address...
print(foo('<hs}h-'))
print(foo('[W~b'))
