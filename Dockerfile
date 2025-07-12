from redhat/ubi8
run yum install pip3 -y
workdir /myapp
copy app.py  app.py
copy requirement.txt requirement.txt
run pip3 install -r requirmrnt.txt
cmd ["python3" ,"app.py"]
