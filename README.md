# Flask Server
Simple http wrapper over queue  

this http based queue is good for experimentation , where items can be queued/dequeued at runtime

_To Start the Server_

`python server/queryserver.py`


_TO ADD_

`curl http://localhost:5000/putvalues`  
random values will be put into the queue  

_TO GET_ 

`curl -X POST 'http://localhost:5000/getvalues?numvals=5'`


