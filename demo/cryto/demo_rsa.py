import rsa
#待加密的字符串
str='111111'
#实例化加密对象
(pubkey,privkey)=rsa.newkeys(1024)
print(pubkey)
#公钥加密1
pwd1=rsa.encrypt(str.encode('utf-8'),pubkey)
print('加密后结果1为：',pwd1.hex())
#公钥加密2
pwd2=rsa.encrypt(str.encode('utf-8'),pubkey)
print('加密后结果2为：',pwd2.hex())
#私钥解密1
depwd1=rsa.decrypt(pwd1,privkey)
print('解密后的结果1为：',depwd1.decode())
#私钥解密1
depwd2=rsa.decrypt(pwd2,privkey)
print('解密后的结果2为：',depwd2.decode())