import requests
from config import HOST
from lib.loginLib import loginlib
#新增课程
def addcourse(name,desc,display_idx,SessionID):
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'action': 'add_course',
        'data': f"""{{
      "name":"{name}",
      "desc":"{desc}",
      "display_idx":"{display_idx}"
    }}"""
    }
    cookie = {'sessionid': SessionID}
    try:
        re = requests.post(f'{HOST}/api/mgr/sq_mgr/',
                           headers=dict, data=payload,cookies=cookie)
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#列出课程
def listcourse(pagenum,pagesize,SessionID):
    cookie = {'sessionid': SessionID}
    payload = {
        'action': 'list_course',
        'pagenum': pagenum,
        'pagesize': pagesize
    }
    try:
        re = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload,cookies=cookie)
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#删除课程
def deletecourse(id,SessionID):
    cookie = {'sessionid': SessionID}
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'action': 'delete_course', 'id': id}
    try:
        re = requests.delete(url=f'{HOST}/api/mgr/sq_mgr/', headers=dict,
                         data=payload,cookies=cookie)
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#4.修改课程
def modifycourse(id,name,desc,display_idx,SessionID):
    cookie = {'sessionid': SessionID}
    payload = {
        'action': 'modify_course',
        'id': id,
        'newdata': f"""{{
      "name":"{name}",
      "desc":"{desc}",
      "display_idx":"{display_idx}"
    }}"""
    }
    dict = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        re = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=dict, data=payload,cookies=cookie)
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#5.新增课程2
def add2course(name,desc,display_idx,SessionID):
    cookie = {'sessionid': SessionID}
    dict = {'Content-Type': 'application/json'}
    payload = {
        'action': 'add_course_json',
        'data': {"name": name, "desc": desc, "display_idx": display_idx}
    }
    try:
        re = requests.post(f'{HOST}/apijson/mgr/sq_mgr/',
                       headers=dict,json=payload,cookies=cookie)
        return re.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

if __name__ == '__main__':
    SessionID = loginlib('auto', 'sdfsdfsdf')
    addcourse('123','22','123','SessionID')