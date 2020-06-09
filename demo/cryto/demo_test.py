import hashlib
import requests
str='zr111111hg'
md5=hashlib.md5()
md5.update(str.encode('UTF-8'))
pwd=md5.hexdigest()
print(pwd)
payload={"mobile":"13588000000","password":pwd}
r=requests.post('http://121.41.14.39:2001/token/token',data=payload)
print(r.json())
