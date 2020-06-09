import requests
url='http://localhost/api/mgr/sq_mgr/'
payload={
    'action':'modify_course',
    'id':'2171',
    'newdata':"""{
  "name":"初中化学999",
  "desc":"初中化学课程",
  "display_idx":"4"
}"""
}
dict = {
    'Content-Type':'application/x-www-form-urlencoded'
}
re=requests.put(url,headers=dict,data=payload)
print(re.json())