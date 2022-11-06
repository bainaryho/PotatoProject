# -*- coding: utf-8 -*-
"""BigdataProjectPotato.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dMuI0Uli9djBhlL5_WuS-cvfFsMNqU0B
"""

import pandas as pd
import numpy as np

#공공데이터 농축산물원천조사가격정보 데이터프레임 생성
df101 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202101.csv')
df102 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202102.csv')
df103 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202103.csv')
df104 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202104.csv')
df105 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202105.csv')
df106 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202106.csv')
df107 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202107.csv')
df108 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202108.csv')
df109 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202109.csv')
df110 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202110.csv')
df111 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202111.csv')
df112 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202112.csv')
df201 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202201.csv')
df202 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202202.csv')
df203 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202203.csv')
df204 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202204.csv')
df205 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202205.csv')
df206 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202206.csv')
df207 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202207.csv')
df208 = pd.read_csv('/content/drive/MyDrive/Colab_Datas/원천조사가격정보_202208.csv')

#데이터 프레임 리스트 생성
dlist = [df101,df102,df103,df104,df105,df106,df107,df108,df109,df110,
         df111,df112,df201,df202,df203,df204,df205,df206,df207,df208]

#불필요한 열 삭제
for i in dlist :
  i.drop(['EXAMIN_SE_CODE','STD_PRDLST_CODE','EXAMIN_PRDLST_CODE','STD_SPCIES_CODE',
              'EXAMIN_SPCIES_CODE','STD_UNIT_CODE','STD_UNIT_NM','BFRT_PRIC','AREA_CODE',
              'STD_MRKT_CODE','EXAMIN_MRKT_CODE','STD_MRKT_NM','EXAMIN_MRKT_NM'],axis=1,inplace=True)

#년도와 월을 구분하는 Month 열 추가
df101['Month'] = "21.01"
df102['Month'] = "21.02"
df103['Month'] = "21.03"
df104['Month'] = "21.04"
df105['Month'] = "21.05"
df106['Month'] = "21.06"
df107['Month'] = "21.07"
df108['Month'] = "21.08"
df109['Month'] = "21.09"
df110['Month'] = "21.10"
df111['Month'] = "21.11"
df112['Month'] = "21.12"
df201['Month'] = "22.01"
df202['Month'] = "22.02"
df203['Month'] = "22.03"
df204['Month'] = "22.04"
df205['Month'] = "22.05"
df206['Month'] = "22.06"
df207['Month'] = "22.07"
df208['Month'] = "22.08"

#데이터 프레임 연결
df =  pd.concat([df101,df102,df103,df104,df105,df106,df107,df108,df109,df110,
         df111,df112,df201,df202,df203,df204,df205,df206,df207,df208],ignore_index = True)

#(결측치)누락이 있는 행 삭제
df.dropna()
df.drop(['EXAMIN_PRDLST_NM','EXAMIN_SPCIES_NM'],axis=1,inplace=True)

#감자 행 추출
dfPotato1 = df.loc[df['STD_SPCIES_NM']=='수미'] #수미감자의
dfPotato1 = dfPotato1.loc[dfPotato1['EXAMIN_NM']=='소비자가격'] #소비자가격 중
dfPotato1 = dfPotato1.loc[dfPotato1['EXAMIN_UNIT_NM']=='100G'] #단위는 100G당
dfPotato1 = dfPotato1.loc[dfPotato1['EXAMIN_GRAD_CODE']==1] # 1등급 감자만

dfPotato2 = df.loc[df['STD_SPCIES_NM']=='수미'] #수미감자의
dfPotato2 = dfPotato2.loc[dfPotato2['EXAMIN_NM']=='소비자가격'] #소비자가격 중
dfPotato2 = dfPotato2.loc[dfPotato2['EXAMIN_UNIT_NM']=='100G'] #단위는 100G당
dfPotato2 = dfPotato2.loc[dfPotato2['EXAMIN_GRAD_CODE']==2] # 2등급 감자만

#1등급 감자와 2등급 감자의 최근 2년간 가격 추세 그래프
import seaborn as sns
sns.set_style('darkgrid') # option: whitegrid, white, dark
sns.lineplot(data=dfPotato1,x='Month',y='TODAY_PRIC')
sns.lineplot(data=dfPotato2,x='Month',y='TODAY_PRIC')