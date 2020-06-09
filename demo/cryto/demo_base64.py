import base64
#待加密的字符串
str='111111'

#base6编码
pwd=base64.b64encode(str.encode('UTF-8'))
print(pwd)

#base64解码
bstr=base64.b64decode(pwd)
print(bstr.decode('UTF-8'))