from redhat/ubi8
run yum install pip3
workdir /myapp
copy app.py  app.py
copy requirment.txt requirment.txt
run pip3 install -r requirmrnt.txt
cmd ["python3" ,"app.py"]
