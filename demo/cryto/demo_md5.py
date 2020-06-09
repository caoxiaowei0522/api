import hashlib
str='123456'
md5=hashlib.md5()
md5.update(str.encode('utf-8'))
print(md5.hexdigest())