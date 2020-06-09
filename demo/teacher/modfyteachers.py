import requests
url='http://localhost/api/mgr/sq_mgr/'
payload={
    'action':'modify_teacher',
    'id':'259',
    'newdata':"""{
    "username":"caoxiaowei123",
    "password":"123456",
    "realname":"caoxiaowei",
    "desc":"李世民老师",
    "courses":[{"id":1493,"name":"高中物理00013"},{"id":1494,"name":"高中物理00015顶顶1111"}],
    "display_idx":1
}
"""
}
dict = {
    'Content-Type':'application/x-www-form-urlencoded'
}
re=requests.put(url,headers=dict,data=payload)
print(re.json())