from flask import Flask, send_file, escape
from flask_cors import CORS,cross_origin
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

app=Flask(__name__)
cors=CORS(app,resourses={r"/api/*":{"origins":"*"}})
cases = pd.read_csv('confirmed.csv')
deaths = pd.read_csv('deaths.csv')
latest = pd.read_csv('latest.csv')

@app.route('/latest/<ck>')
@cross_origin()
def latest_(ck):
    print('CK:',ck)
    i=latest[latest['Combined_Key']==ck].index[0]
    print(i)
    s = str(latest.loc[i,'Combined_Key'])+'<hr>Cases: '+str(latest.loc[i,'Confirmed'])+'<br>Deaths:'+str(latest.loc[i,'Deaths'])+'<br>Recovered:'+str(latest.loc[i,'Recovered'])+'<br>Active:'+str(int(latest.loc[i,'Active']))+'<hr>Incidence Rate:<br>'+str(latest.loc[i,'Incidence_Rate'])+'<br><br>Case Fatality Ratio:<br>'+str(latest.loc[i,'Case-Fatality_Ratio'])
    print(s)
    return s


@app.route('/cases/<ck>')
def case(ck):
    ck=str(ck)
    print(ck)
    d=cases[cases['Combined_Key']==ck].iloc[0]
    print(d)
    y=np.array(d.iloc[5:])
    x=np.arange(len(y))
    
    fig,ax=plt.subplots(1,1)
    ax.grid()
    ax.plot(x,y)
    fig.savefig('cases.png')
    plt.close(fig)
    time.sleep(1)
    return send_file('cases.png',mimetype='image/png')

@app.route('/deaths/<ck>')
def death(ck):
    ck=str(ck)
    print(ck)
    d=deaths[deaths['Combined_Key']==ck].iloc[0]
    print(d)
    y=np.array(d.iloc[5:])
    x=np.arange(len(y))
    
    fig,ax=plt.subplots(1,1)
    ax.grid()
    ax.plot(x,y)
    fig.savefig('deaths.png')
    plt.close(fig)
    time.sleep(1)
    return send_file('deaths.png',mimetype='image/png')

if __name__  ==  "__main__":
    app.run()
    
