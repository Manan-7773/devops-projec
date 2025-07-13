from redhat/ubi8
run yum install -y python3 python3-pip
workdir /myapp
copy app.py  app.py
copy requirement.txt requirement.txt
run pip3 install -r requirmrnt.txt
cmd ["python3" ,"app.py"]
