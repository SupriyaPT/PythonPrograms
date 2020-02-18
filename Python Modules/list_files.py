import os
os.system("ls -latr")


import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('raspberry.lan', username='irfan', password='my_strong_password')

stdin, stdout, stderr = client.exec_command('ls -l')

for line in stdout:
    print (line.strip('\n'))

client.close()
