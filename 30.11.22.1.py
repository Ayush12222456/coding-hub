#line,split("")
ans=0
file=open("30.11.22.file.txt",'r')
while True:
          line=file.readline()
          if line=="":
            break
          line=line.split(" ")
          line=line[:-1]
          for i in line:
            ans+=int(i)
print(ans)
file.close()