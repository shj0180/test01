import subprocess


obj = subprocess.Popen('ls',shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE
                       )
res = obj.stdout.read()
print(res.decode('utf-8'))










