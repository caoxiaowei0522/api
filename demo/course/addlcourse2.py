import  requests
url='http://localhost/apijson/mgr/sq_mgr/'
dict1={'Content-Type':'application/json'}
payload='''
{
  "action" : "add_course_json",
  "data": {
    "name":"初中化学442",
    "desc":"初中化学课程",
    "display_idx":"4"
  }
}
'''
re=requests.post(url,headers=dict1,data=payload.encode(encoding='UTF-8'))
print(re.text)