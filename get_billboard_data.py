from datetime import datetime, timedelta
import billboard
import pandas as pd
import numpy as np

titles=list()
artists=list()
weeks=list()
lastPos=list()
dates=list()
chartPos=list()

#dates for summer 2017
startdate_2017 = '01/05/17 00:00:00'
enddate_2017 = '02/10/17 00:00:00'
#dates for summer 2018
startdate_2018 = '30/04/18 00:00:00'
enddate_2018 = '01/10/18 00:00:00'
#dates for summer 2019
startdate_2019 = '23/04/19 00:00:00'
enddate_2019= '30/09/19 00:00:00'
#dates for summer 2020
startdate_2020= '04/05/20 00:00:00'
enddate_2020= '28/09/20 00:00:00'
#dates for summer 2021
startdate_2021 = '03/05/21 00:00:00'
enddate_2021= '27/09/21 00:00:00'

startdate_2017 = datetime.strptime(startdate_2017, '%d/%m/%y %H:%M:%S')
enddate_2017 = datetime.strptime(enddate_2017, '%d/%m/%y %H:%M:%S')

startdate_2018 = datetime.strptime(startdate_2018, '%d/%m/%y %H:%M:%S')
enddate_2018 = datetime.strptime(enddate_2018, '%d/%m/%y %H:%M:%S')

startdate_2019 = datetime.strptime(startdate_2019, '%d/%m/%y %H:%M:%S')
enddate_2019 = datetime.strptime(enddate_2019, '%d/%m/%y %H:%M:%S')

startdate_2020 = datetime.strptime(startdate_2020, '%d/%m/%y %H:%M:%S')
enddate_2020 = datetime.strptime(enddate_2020, '%d/%m/%y %H:%M:%S')

startdate_2021 = datetime.strptime(startdate_2021, '%d/%m/%y %H:%M:%S')
enddate_2021 = datetime.strptime(enddate_2021, '%d/%m/%y %H:%M:%S')
delta = timedelta(days=7)

#getting the billboard hot-100 songs for 2017
while startdate_2017 <= enddate_2017 :
  t=startdate_2017.strftime('%Y-%m-%d')
  chart = billboard.ChartData('hot-100', date=t)
  for i in range(100):
    chartPos.append(i+1)
    titles.append(chart[i].title)
    artists.append(chart[i].artist)
    weeks.append(chart[i].weeks)
    lastPos.append(chart[i].lastPos)
    dates.append(startdate_2017)
  startdate_2017 += delta

#getting the billboard hot-100 songs for 2018
while startdate_2018 <= enddate_2018 :
  t=startdate_2018.strftime('%Y-%m-%d')
  chart = billboard.ChartData('hot-100', date=t)
  for i in range(100):
    chartPos.append(i+1)
    titles.append(chart[i].title)
    artists.append(chart[i].artist)
    weeks.append(chart[i].weeks)
    lastPos.append(chart[i].lastPos)
    dates.append(startdate_2018)
  startdate_2018 += delta

#getting the billboard hot-100 songs for 2019
while startdate_2019 <= enddate_2019 :
  t=startdate_2019.strftime('%Y-%m-%d')
  chart = billboard.ChartData('hot-100', date=t)
  for i in range(100):
    chartPos.append(i+1)
    titles.append(chart[i].title)
    artists.append(chart[i].artist)
    weeks.append(chart[i].weeks)
    lastPos.append(chart[i].lastPos)
    dates.append(startdate_2019)
  startdate_2019 += delta

#getting the billboard hot-100 songs for 2020
while startdate_2020 <= enddate_2020 :
  t=startdate_2020.strftime('%Y-%m-%d')
  chart = billboard.ChartData('hot-100', date=t)
  for i in range(100):
    chartPos.append(i+1)
    titles.append(chart[i].title)
    artists.append(chart[i].artist)
    weeks.append(chart[i].weeks)
    lastPos.append(chart[i].lastPos)
    dates.append(startdate_2020)
  startdate_2020 += delta  

#getting the billboard hot-100 songs for 2021
while startdate_2021 <= enddate_2021 :
  t=startdate_2021.strftime('%Y-%m-%d')
  chart = billboard.ChartData('hot-100', date=t)
  for i in range(100):
    chartPos.append(i+1)
    titles.append(chart[i].title)
    artists.append(chart[i].artist)
    weeks.append(chart[i].weeks)
    lastPos.append(chart[i].lastPos)
    dates.append(startdate_2021)
  startdate_2021 += delta

#creating the dataset with all four years of songs
df_chartPos=pd.DataFrame(chartPos, columns=["Postion on chart"])
df_titles=pd.DataFrame(titles, columns=["Titles"])
df_artists=pd.DataFrame(artists, columns=["Artists"])
df_weeks=pd.DataFrame(weeks, columns=["Weeks"])
#the tracks position on the previous weeks chart
df_last=pd.DataFrame(lastPos, columns=["lastPosition"])
df_dates=pd.DataFrame(dates, columns=["chart release date"])
df=pd.concat([df_chartPos,df_titles], axis=1)
df=pd.concat([df,df_artists], axis=1)
df=pd.concat([df,df_weeks], axis=1)
df=pd.concat([df,df_last], axis=1)
df=pd.concat([df,df_dates], axis=1)
print(df) 

df.to_csv('SongList.csv')