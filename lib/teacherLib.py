import requests
from config import HOST
#添加老师
def addteacher(username,password,realname,desc,id,display_idx,name):
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'action': 'add_teacher',
        'data': f'''{{
        "username":"{username}",
        "password":"{password}",
        "realname":"{realname}",
        "desc":"{desc}",
        "courses":[{{"id":'{id}',"name":"{name}"}},{{"id":'{id}',"name":"{name}"}}],
        "display_idx":{display_idx}
    }}'''
    }
    re = requests.post(url=f'{HOST}/api/mgr/sq_mgr/', headers=dict, data=payload)
    try:
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#删除老师
def deleteteacher(id):
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'action': 'delete_teacher', 'id': id}
    re = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=dict, data=payload)
    try:
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#列出老师
def listteacher(pagenum,pagesize):
    payload = {
        'action': 'list_teacher',
        'pagenum': pagenum,
        'pagesize': pagesize
    }
    re = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload)
    try:
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#修改老师
def modifyteacher(id,username,password,realname,desc,cid,cname):
    payload = {
        'action': 'modify_teacher',
        'id': id,
        'newdata': f"""{{
        "username":"{username}",
        "password":"{password}",
        "realname":"{realname}",
        "desc":"{desc}",
        "courses":[{{"id":'{cid}',"name":"{cname}"}},{{"id":'{cid}',"name":"{cname}"}}],
        "display_idx":1
    }}
    """
    }
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    re = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=dict, data=payload)
    try:
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}