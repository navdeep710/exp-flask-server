#Simple http wrapper over queue

this flask is good for experimentation , where items can be queued/dequeued at runtime

# To Run

python server/queryserver.py
---
TO ADD

curl http://localhost:5000/putvalues
random values will be put into the queue

TO GET 

curl -X POST 'http://localhost:5000/getvalues?numvals=5'


