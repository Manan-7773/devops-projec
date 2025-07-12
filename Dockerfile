from redhat/ubi8

copy app.py  /app.py

cmd ["python3" ,"app.py"]
