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
    print(">>>>>新增课程测试通过1")
    relist = listcourse(1, 100, sessionID)
    print(relist)