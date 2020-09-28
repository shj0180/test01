import paramiko
import os

def hello():
    print('hello 172.16.206.144')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='172.16.206.144', port=22, username='root', password='!QAZ2wsx3edc')

# 执行命令
stdin, stdout, stderr = ssh.exec_command(hello())
# 获取命令结果
result = stdout.read()

ssh.get_transport()


print(result)
# 关闭连接
ssh.close()

def get():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.16.206.144', port=22, username='root', password='!QAZ2wsx3edc',timeout=100)
    stdin, stdout, stderr = ssh.exec_command(hello())
    stdin, stdout, stderr = ssh.exec_command("cd /app;sh sf.sh")
    ssh.close()

#
# dir=r'D:\'
# for root,dirs,files in os.walk(dir)
# 	for file in files:
# print os.path.join(root,file)
#















