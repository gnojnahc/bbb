#성적이 아니라 이수/미이수의 연관관계를 표현 Ex : A과목 이수와 B과목이수의 연관관계
#학과나 신입생,재학생 구분없이 전체 학생의 이수/미이수의를 데이터로


import pandas as pd

df = pd.read_csv('./z연관관계/1. 19년도-과정이수및평가점수.csv',encoding='cp949')
df.drop(columns=['학생구분','학과','학년','반','A과목점수','B과목점수','C과목점수','D과목점수','E과목점수',], inplace=True)
df
df.isnull().sum() # 결측치 확인 =>확인결과 결측치없음.

#파이썬은 1을 참, 0을 거짓으로 인식
df['A과목이수'].replace({2:0}, inplace=True)
df['B과목이수'].value_counts()
df['B과목이수'].replace({2:0}, inplace=True)
df['B과목이수'].value_counts() 
df['C과목이수'].replace({2:0}, inplace=True) 
df['C과목이수'].value_counts() 
df['D과목이수'].replace({2:0}, inplace=True) 
df['D과목이수'].value_counts() 
df['E과목이수'].replace({2:0}, inplace=True) 
df['E과목이수'].value_counts() 

import matplotlib.pyplot as plt
import matplotlib

f, ax = plt.subplots(1,2, figsize= (10,5))
df['A과목이수'][df['B과목이수']==1].value_counts().plot.pie(explode =[0,0.1],
    autopct='%1.1f%%', ax = ax[0], shadow =True)
#explode는 부채꼴이 파이 차트의 중심에서 벗어나는 정도를 설정
#autopct는 부채꼴 안에 표시될 숫자의 형식을 지정
#shadow를 True로 설정하면, 파이 차트에 그림자가 표시
df['A과목이수'][df['C과목이수']==1].value_counts().plot.pie(explode =[0,0.1],
    autopct='%1.1f%%', ax = ax[1], shadow =True)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 8
ax[0].set_title('A와B과목 이수자')
ax[1].set_title('A와C과목 이수자')
plt.show()



















f, ax = plt.subplots(1,2, figsize= (10,5))
df['A과목이수'][df['D과목이수']==1].value_counts().plot.pie(explode =[0,0.1],
    autopct='%1.1f%%', ax = ax[0], shadow =True)
#explode는 부채꼴이 파이 차트의 중심에서 벗어나는 정도를 설정
#autopct는 부채꼴 안에 표시될 숫자의 형식을 지정
#shadow를 True로 설정하면, 파이 차트에 그림자가 표시
df['A과목이수'][df['E과목이수']==1].value_counts().plot.pie(explode =[0,0.1],
    autopct='%1.1f%%', ax = ax[1], shadow =True)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 8
ax[0].set_title('A와D과목 이수자')
ax[1].set_title('A와E과목 이수자')
plt.show()



#상관계수 데이터 파일 저장
df_corr = df.corr(method='pearson')
df_corr
df_corr.to_csv('./z연관관계/df_corr.csv',index=False)

#특정 과목 사이에 상관계수 구하기
df['A과목이수'].corr(df['B과목이수']) #0.5376188249848205
df['A과목이수'].corr(df['C과목이수']) #0.40596757703420383
df['A과목이수'].corr(df['D과목이수']) #0.5446359588415658
df['A과목이수'].corr(df['E과목이수']) #0.5338852283551629

#산점도로 상관분석 시각화하기
import seaborn as sns
sns.pairplot(df, hue='A과목이수')
plt.show()
sns.pairplot(df, hue='B과목이수')
plt.show()