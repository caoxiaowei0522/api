import requests
dict={
    'Content-Type':'application/x-www-form-urlencoded'
}
payload={'action':'delete_teacher','id':259}
url='http://localhost/api/mgr/sq_mgr/'
re=requests.delete(url,headers=dict,data=payload)
print(re.json())