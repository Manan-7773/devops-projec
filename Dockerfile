from redhat/ubi8
workdir /myapp
copy app.py  app.py
copy requirment.txt requirment.txt

cmd ["python3" ,"app.py"]
