import  requests
url='http://localhost/api/mgr/sq_mgr/'
dict={
    'Content-Type':'application/x-www-form-urlencoded'
}
payload={
    'action':'add_course',
    'data':"""{
  "name":"初中化学1",
  "desc":"初中化学课程1",
  "display_idx":"3"
}"""
}
re=requests.post(url,headers=dict,data=payload)
print(re.json())