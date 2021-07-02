import os
import subprocess
import re
import psutil
import elasticsearch
from elasticsearch import Elasticsearch
import json

#Average CPU Load on Machine

statistics = {}


physical_and_logical_cpu_count = os.cpu_count()
statistics['physical_and_logical_cpu_count'] = physical_and_logical_cpu_count


cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
statistics['cpu_load'] = cpu_load


#Send and Retrieve Data from ElasticSearch

def send_data_to_es(data):
    es = Elasticsearch(['localhost:9200'])
    res = es.index(index='metrics',doc_type='metrics_data',body=data)
    print(res)
    
def get_data_from_es():
    es = Elasticsearch(['localhost:9200'])
    r = es.search(index="metrics",body={"query": {"match":{'Name':'Performance_Metrics'}}})
    print(r)
    print(type(r))
    print(r["hits"]["hits"][0]["_source"])
    
data = {"Name":"Performance_Metrics","CPU-Load":cpu_load,"Virtual-Memory-Percent":psutil.virtual_memory().percent,"Disk-Usage-Percent":psutil.disk_usage(os.sep).percent}

send_data_to_es(data)
