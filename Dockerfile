from redhat/ubi8

copy app.py  /app.py
copy requirment.txt /requirment.txt

cmd ["python3" ,"app.py"]
