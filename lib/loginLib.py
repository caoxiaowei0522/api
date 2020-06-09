#用户登录
import requests
from config import HOST
def loginlib(username,password):
    dict1={'Content-Type':'application/x-www-form-urlencoded'}
    payload={
        "username":f"{username}",
        "password":f"{password}"
    }
    re=requests.post(f'{HOST}/api/mgr/loginReq',headers=dict1,data=payload)
    return re.cookies['sessionid']