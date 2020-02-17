import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("10.234.56.78", port=22, username="supriya", password="abcd")

stdin, stdout, stderr = client.exec_command('ls -ltr')

# stdin : To send the command to the program
# stdout : To receive the output
# stderr :  To receive the error

output = stdout.readlines()

print ('\n'.join(output))
