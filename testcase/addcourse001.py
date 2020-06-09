from lib.courseLib import addcourse,listcourse
from lib.loginLib import loginlib
import time
sessionID=loginlib('auto','sdfsdfsdf')
coursename='大学英语'+str(int(time.time()*10000))
relist=listcourse(1,100,sessionID)
print(relist)
ret=addcourse(coursename,'课程描述','0',sessionID)
print(ret)
if ret['retcode']==0:
    print('-----pass--------------')
    relist1 = listcourse(1, 100, sessionID)
    print(relist1)
    if len(relist['retlist'])+1==len(relist['retlist']):
        print('>>>>>新增课程测试通过')
        print(">>>>>新增课程测试通过2")
    if relist['total'] + 1 == relist1['total']:
            print(">>>>>新增课程测试通过3")