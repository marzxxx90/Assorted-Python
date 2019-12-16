from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['192.168.1.176'])

#for i in range(10):

 #   doc = {
  #      'timestamp': "".,
   #     'loan_amt': "",
	#	'branch': ""
    #}

    #res = es.index(index="test-01", doc_type='cbs', body=doc)
    #print(res['result'])

    
	#pass
	
	
doc = {
	'timestamp': datetime.now(),
	'loan_amt': "1500",
	'branch': "Gensan"
}

res = es.index(index="test-01", doc_type='cbs', body=doc)
print(res['result'])
print("Please see output")