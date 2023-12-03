import os
file=open('liveones.txt','r')
lines=file.readlines()
for line in lines:
    x=line
    os.system('echo '+x '| waybackurls')
