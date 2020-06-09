import requests
url='http://localhost/api/mgr/sq_mgr/'
payload={
    'action':'list_teacher',
    'pagenum':1,
    'pagesize':20
}
re=requests.get(url,params=payload)
print(re.json())