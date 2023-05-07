from flask import session
import pandas as pd
import json

def url_classification(url):
    return 'ok'

def perform_action(data,action,url,file,filename,dictionary,filenamelist,count):
    if url!=None:
        if url in data.keys():
            cat=data[url]
            n=filenamelist.index(cat)
            return n+1,data
        else:
            return 'False',data
    if action=='Check Clusters':
        if dict!=None:
            print(data)
            print(dictionary)
            data.update(dictionary)
        return None,data
    
