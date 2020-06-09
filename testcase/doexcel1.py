import requests
import xlrd
import json
import time
from lib.excelmanage import readExcel,getnewexcel
from lib.loginLib import loginlib
from config import path1,path,savepath,savepath1
def excutXLTestCase2():
    sessionID = loginlib('auto', 'sdfsdfsdf')
    cookie = {'sessionid': sessionID}
    list = readExcel(path, 2)
    newworbook= getnewexcel(path)
    worksheet=newworbook.get_sheet(2)
    for i in range(0,len(list)):
        row = list[i]  # 获取一行记录
        headers = json.loads(row[11])  # 获取请求头-并转dict
        payload = json.loads(row[5])  # 获取请求体内容-并转dict
        test = json.loads(row[6])  # 获取断言结果-并转dict
        r = None  # 预先定义响应对象
        # 3. 请求url、请求头、data数据都从Excel中获取（课程新增除外）
        if row[10] == 'get':
            r = requests.get(row[9], params=payload, headers=headers, cookies=cookie)
        elif row[10] == 'delete':
            r = requests.delete(row[9], data=payload, headers=headers, cookies=cookie)
        elif row[10] == 'post':
            randomStr = str(int(time.time() * 10000))  # 时间戳
            time.sleep(0.001)  # 睡眠时间
            data = row[5].replace('{{courseName}}', randomStr)  # 课程名称-替换
            # 添加部分参数
            payload = {
                "action": "add_course",
                "data": data
            }
            r = requests.post(row[9], data=payload, headers=headers, cookies=cookie)
        try:
            # 4. 结果写回Excel中
            dictBody = r.json()
            if dictBody['retcode'] == test['code']:
                worksheet.write(i + 1, 7, 'PASS')
            else:
                worksheet.write(i + 1, 7, 'FAIL')
                if 'reason' in dictBody.keys():
                    worksheet.write(i + 1, 8, dictBody['reason'])
        except:
            worksheet.write(i + 1, 7, 'FAIL')
            worksheet.write(i + 1, 8, '异常')
        # 5. 保存excel
    newworbook.save(savepath1)
excutXLTestCase2()