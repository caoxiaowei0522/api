import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
def send_email():
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(r'C:\Users\caowei\Desktop\20200601\bysms\htmlReport.html','r').read(), 'html' ))  # 添加html格式邮件正文（会丢失css格式）
    msg['From'] = '1746637603@qq.com'  # 发件人
    msg['To'] = '7175290@qq.com'  # 收件人
    msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码
    att1 = MIMEText(open(r'C:\Users\caowei\Desktop\20200601\bysms\htmlReport.html', 'r').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)
    smtp = smtplib.SMTP_SSL('smtp.qq.com')  # smtp服务器地址 使用SSL模式
    smtp.login('1746637603@qq.com', 'kiulxtzquvxxccfc')  # 用户名和密码
    smtp.sendmail("7175290@qq.com", msg.as_string())
    smtp.quit()
