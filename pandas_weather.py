import numpy as np
import pandas as pd

global df

def header(msg):
  print('-'*100)
  print('[ ' + msg + ' ]')
  print('-'*100)

def my_init():
  header("create Data Frame with hardcoded data")
  global df
  df = pd.DataFrame(
      [['Jan',58,42,74,22,2.95],
      ['Feb',61,45,78,26,3.02],
      ['Mar',65,48,84,25,2.34],
      ['Apr',67,50,92,28,1.02],
      ['May',71,53,98,35,0.48],
      ['Jun',75,56,107,41,0.11],
      ['Jul',77,58,105,44,0.0],
      ['Aug',77,59,102,43,0.03],
      ['Sep',77,57,103,40,0.17],
      ['Oct',73,54,96,34,0.81],
      ['Nov',64,48,84,30,1.7],
      ['Dec',58,42,73,21,2.56]],
      index = [0,1,2,3,4,5,6,7,8,9,10,11],
      columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])


def examples():
    header("examples function")

    header("df-  dtype")
    print(df.dtypes)

    header("df-shape() - tells number of rows & columns")
    print(df.shape)
    
    header(" df.describe() - display stats - mean, std, min, max, % of distribution")
    print(df.describe())
    
    header("disply header, df.head()")
    print(df.head(3))
    
    header("disply last 3 rows, df.tail(3)")
    print(df.tail(3))
    
    header("disply data types, df.dtypes")
    print(df.dtypes)
    
    header("disply index, df.index")
    print(df.index)
    
    header("disply column names, df.columns")
    print(df.columns)
    
    header("disply data values, df.values")
    print(df.values)
    
    header("disply data types, df.dtypes")
    print(df.dtypes)
    
    header(" df.count() - gives count of non-null values of each column")
    print(df.count())
    
    header(" df.min() - min values of each column")
    print(df.min())
    
    header(" df.min() - max values of each column")
    print(df.max())
    
    header(" df.std() - standard diviation values of each column")
    print(df.std())
    
    header(" df.median() - median values of each column")
    print(df.median())
    
    header(" df.mean() - mean values of each column")
    print(df.mean())
    
    header(" df.corr() - correlation values of each column")
    print(df.corr())

    header(" Sorting by column name")
    print(df.sort_values('record_high', ascending=False))


def slice_records():
  header("Data Frame slice")
  
  header("Data Frame - display single col by col name")
  print(df.avg_low)

  header("Data Frame - display single col by []")
  print(df['avg_low'])

  header("Data Frame - slice multiple rows nos")
  print(df[2:4])
  
  header("Data Frame - slice multiple column names")
  print(df[['avg_low', 'avg_high']])

  header("Data Frame - slice multi row nos & multi col names")
  print(df.loc[2:5, ['avg_low', 'avg_high']])

  header("Data Frame - slice single row nos & multi col names")
  print(df.loc[9, ['avg_low', 'avg_high']])

  header("Data Frame - slice single row nos & multi col nos")
  print(df.iloc[3:6, [0,4]])


def filter():
  header("filter function")
  header("Data Frame - filter - (df[df.avg_high>70] ")
  print(df[df.avg_high>70])
  
  header("Data Frame - filter - (df[df.avg_high>70] ")
  print(df[df['month'].isin(['Jun', 'Jul', 'Aug'])])
  

def assign():
    header("DF Assign: df.loc[9,['avg_precipitation']] = 101.3")
    df.loc[9,['avg_precipitation']] = 101.3
    print(df.iloc[9:11])
    
    header("DF Assign: df.loc[9,['avg_precipitation']] = np.nan")
    df.loc[9,['avg_precipitation']] = np.nan
    print(df.iloc[9:11])
    
    header("DF Assign: df.loc[:,'avg_low'] = np.array([5] * len(df))")
    df.loc[:,'avg_low'] = np.array([5] * len(df))
    print(df.head())
    
    header("DF Assign: df['avg_day'] = (df.avg_low + df.avg_high) / 2")
    df['avg_day'] = (df.avg_low + df.avg_high) / 2
    print(df.head())


def rename_col():
    header(" rename column ")
    df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)
    print(df.head())
    

def iterate():
    header(" iterate for loop")
    for index, row in df.iterrows():
        print (index, row["month"], row["avg_high"])
    
    header(" save to csv file")
    df.to_csv('foo.csv')
    
    
my_init()
#examples()
#slice_records()
#filter()
#assign()
rename_col()
iterate()

