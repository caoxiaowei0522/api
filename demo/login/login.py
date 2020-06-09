import requests
url='http://localhost//api/mgr/loginReq'
dict={
    'Content-Type':'application/x-www-form-urlencoded'
}
payload={
    'username':'auto',
    'password':'sdfsdfsdf'
}
re=requests.post(url,headers=dict,data=payload)
print(re.cookies)