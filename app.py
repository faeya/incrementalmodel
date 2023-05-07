from flask import Flask, url_for, redirect, request, g, session
from flask.templating import render_template
import utils
import pandas as pd


app = Flask(__name__)
app.secret_key = 'archi'
@app.route('/')
def index():
    session['origin']=1
    return render_template("index.html",result="")


@app.route('/', methods=['POST'])
def home():
    action=request.form['action']
    if action=='Reset':
        for key in list(session.keys()):
            session.pop(key) 
        print('right here')
        return render_template("index.html",result = None, url=None, action=action, filename=None,df=None,data=None,filenamelist=None,count=None)
    if 'count' not in session:
        session['count']=0
    if request.files.get('File'):
        file = request.files['File']
        filename = file.filename
        if 'filenamelist' in session:
            if filename not in session['filenamelist']:
                session['filenamelist'].append(filename.split(".")[0])
                session['count']+=1
        else:
            session['filenamelist']=[]
            session['filenamelist'].append(filename.split(".")[0])
            session['count']=1
        df = pd.read_excel(file) 
        URL=df['URL'].to_list()
        Category=df['Category'].to_list()
        dictionary=dict(zip(URL, Category))
        url=None
    else:
        url=request.form['url']
        dictionary=None
        filename=None
        file=None
    if 'dict' in session:
        data=session.get('dict')
    else:
        data=dict()
    if 'filenamelist' in session:
        filenamelist=session.get('filenamelist')
    else:
        filenamelist=None
    count=session.get('count')
    urlNumber,data=utils.perform_action(data,action,url,file,filename,dictionary,filenamelist,count)
    session['dict']=data
    return render_template("index.html",result = None, url=url, action=action, filename=filename,data=data,filenamelist=filenamelist,count=count,urlNumber=urlNumber)
    # count=0
    # if 'df' not in session:
    #     session['cCount'] = 0
    # url=None
    # filename=None
    # df=None
    # result=None
    # category=None
    # action=request.form['action']
    # if action=='Add More':
    #     return render_template("index.html",result = category, url=url, action=action, filename=filename,df=df,count=session['cCount'])

    # url = request.form['url']
    
    
    #     else:
    #         merged_df = pd.concat([session['df'], df], axis=0)
    #         session['df'] = merged_df.to_json()
        
    #     # perform function
    # category = utils.url_classification(url)
        
    # if action=='Check Category':
    #     return render_template("index.html",result = category, url=url, action=action, filename=filename,df=df, count=int(session['cCOunt']))
            

    #     # return output
    # return render_template("index.html",result = category, url=url, action=action, filename=filename,df=df,count=session['cCount'])
  



if __name__ == '__main__':
    app.run(debug=True)
