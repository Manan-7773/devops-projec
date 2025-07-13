from redhat/ubi8
	
	
workdir /myapp
copy app.py  app.py
copy requirement.txt requirement.txt
run yum install  python3 -y &&  pip3 install -r requirement.txt
cmd ["python3" ,"app.py"]
