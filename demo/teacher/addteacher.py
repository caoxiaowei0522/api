import requests
url='http://localhost/api/mgr/sq_mgr/'
dict={
    'Content-Type':'application/x-www-form-urlencoded'
}
payload={
    'action':'add_teacher',
    'data':'''{
    "username":"caoxiaowei",
    "password":"123456",
    "realname":"caoxiaowei",
    "desc":"李世民老师",
    "courses":[{"id":1493,"name":"高中物理00013"},{"id":1494,"name":"高中物理00015顶顶1111"}],
    "display_idx":1
}'''
}
re=requests.post(url,headers=dict,data=payload)
print(re.json())