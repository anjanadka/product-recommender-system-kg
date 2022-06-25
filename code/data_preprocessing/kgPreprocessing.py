import pandas as pd
import json
import numpy as np
df_video = pd.read_json('Video_Games.json', lines=True)
df_meta = pd.read_json('meta_Video_Games.json', lines=True)
df=df_video[0:5000]
df_m=df_meta[0:500]
du=pd.read_table("uList.txt",sep='\t')
du=du[['u.A21ROB4YDOZA5P','5']]
du=du.to_dict(orient='index')
dp=pd.read_table("pList.txt",sep='\t')  #product index table
#user index table
print(dp)
dp=dp[['p.0439381673','6']]
dp=dp.to_dict(orient='index')
du1={}
dp1={}
dc={}
du={}
dp={}
rel={'reviews':1 , 'also_buy':2 , 'also_view':3, 'category':4}
ctp=pd.read_table("cList.txt") # category index table
ctp={'video games':0}
print(ctp)
ctp1={}
k=7  #index value
kg = pd.read_csv("kgPartial2.txt",sep="\t",header=None)
print(ctp1)

for i in df.index:
  ku="u."+str(df['reviewerID'][i])
  kp="p."+str(df['asin'][i])
  r=df['overall'][i]
  if r>=2.5:
    if ku not in du.keys():
      du[ku]=k
      du1[ku]=k
      k+=1
    if kp not in dp.keys():
      dp[kp]=k
      dp1[kp]=k
    k+=1
    kg.loc[len(kg.index)] = [du[ku], 1, dp[kp]]  #r=1 : relation 1 -->
                                                #user reviews product 


rel=df_m['also_view']

for i in df_m.index:
  kp="p."+df_m['asin'][i]
  r=df_m['category'][i]
  if kp not in dp.keys():
    dp[kp]=k
    dp1[kp]=k
    k+=1
  for j in r:
    if j== '</span></span></span>':
      break
    else:
        if j not in ctp.keys():  
          ctp[j]=k
          ctp1[j]=k
          k+=1
        kg.loc[len(kg.index)] = [dp[kp], 4, ctp[j]] #product - category graph
  ab=df_m['also_buy'][i]
  for j in ab:
    kab="p."+j
    if kab not in dp.keys():
      dp[kab]=k
      dp1[kab]=k
      k+=1
    kg.loc[len(kg.index)] = [dp[kp], 2, dp[kab]]  #2--also buy
  av=df_m['also_view'][i]
  for j in av:
    kav="p."+j
    if kav not in dp.keys():
      dp[kav]=k
      dp1[kav]=k
      k+=1
    kg.loc[len(kg.index)] = [dp[kp], 3, dp[kav]]  #3--also view

np.savetxt('kgPartial.txt', kg.values, fmt='%d')

with open("uList.txt", 'a') as f: 
    for key, value in du1.items(): 
        f.write('%s\t%s\n' % (value, key))
with open("pList.txt", 'a') as f: 
    for key, value in dp1.items(): 
        f.write('%s\t%s\n' % (value ,key))
with open("cList.txt", 'w') as f: 
    for key, value in ctp.items(): 
        f.write('%s\t%s\n' % (value ,key))


