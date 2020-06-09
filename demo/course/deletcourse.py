import requests
dict={
    'Content-Type':'application/x-www-form-urlencoded'
}
payload={'action':'delete_course','id':2170}
url='http://localhost/api/mgr/sq_mgr/'
re=requests.delete(url,headers=dict,data=payload)
print(re.json())