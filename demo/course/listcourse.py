import requests
url='http://localhost/api/mgr/sq_mgr/'
payload={
    'action':'list_course',
    'pagenum':1,
    'pagesize':20
}
reponse=requests.get(url,params=payload)
print(reponse.json())