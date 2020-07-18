from com.datacamp.computer_storage.chunks_3 import filter_is_long_trip
import pandas as pd

filename='NYC_taxi_2013_01.csv'

# FILTERING IN A LIST COMPREHENSION

chunks = [filter_is_long_trip(chunk)
for chunk in pd.read_csv(filename,
chunksize=1000)]   # Tiene corchetes (forma una lista)



# FILTERING & SUMMING WITH GENERATORS (usan una lazy evaluation)


chunks = (filter_is_long_trip(chunk)
    for chunk in pd.read_csv(filename, chunksize=1000))


distances = (chunk['trip_distance'].sum() for chunk in chunks)

sum(distances)

'''
230909.56000000003
'''

# EXAMINING CONSUMED GENERATORS

distances

'''
<generator object <genexpr> at 0x10766f9e8>
'''

next(distances)

'''
StopIteration Traceback (most recent call last)   the generator is exhausting
<ipython-input-10-9995a5373b05> in <module>()
'''

# READING MANY FILES

template = 'yellow_tripdata_2015-{:02d}.csv'
filenames = (template.format(k) for k in range(1,13)) # Generator
for fname in filenames:
    print(fname)   # Examine contents

'''
yellow_tripdata_2015-01.csv
yellow_tripdata_2015-02.csv
yellow_tripdata_2015-03.csv
yellow_tripdata_2015-04.csv
...
yellow_tripdata_2015-09.csv
yellow_tripdata_2015-10.csv
yellow_tripdata_2015-11.csv
yellow_tripdata_2015-12.csv

'''

#  EXAMINING A SAMPLE DATAFRAME

df = pd.read_csv('yellow_tripdata_2015-12.csv', parse_dates=[1, 2])
df.info() # Columns deleted from output

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71634 entries, 0 to 71633
Data columns (total 19 columns):
VendorID 71634 non-null int64
tpep_pickup_datetime 71634 non-null datetime64[ns]
tpep_dropoff_datetime 71634 non-null datetime64[ns]
passenger_count 71634 non-null int64
...
...
dtypes: datetime64[ns](2), float64(12), int64(4), object(1)
memory usage: 10.4+ MB

'''

#  EXAMINING A SAMPLE DATAFRAME

def count_long_trips(df):
    df['duration'] = (df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds
    is_long_trip = df.duration > 1200
    result_dict = {'n_long':[sum(is_long_trip)], 'n_total':[len(df)]}
    return pd.DataFrame(result_dict)


#  AGGREGATING WITH GENERATORS

def count_long_trips(df):
    df['duration'] = (df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds
    is_long_trip = df.duration > 1200
    result_dict = {'n_long':[sum(is_long_trip)], 'n_total':[len(df)]}
    return pd.DataFrame(result_dict)

template = 'yellow_tripdata_2015-{:02d}.csv'
filenames = [template.format(k) for k in range(1,13)] # Listcomp
dataframes = (pd.read_csv(fname, parse_dates=[1,2])
                for fname in filenames) # Generator
totals = (count_long_trips(df) for df in dataframes) # Generator
annual_totals = sum(totals) # Consumes generators


#  COMPUTING THE FRACTION  OF LONG TRIPS

print(annual_totals)

'''
    n_long n_total
    0 172617 851390
    
'''

fraction = annual_totals['n_long'] / annual_totals['n_total']
print(fraction)

'''
    0 0.202747
    dtype: float64
    
'''


'''
# Define the generator: dataframes
dataframes = (pd.read_csv(file) for file in filenames)

# Create the list comprehension: monthly_delayed
monthly_delayed = [pct_delayed(df) for df in dataframes]

# Create the plot
x = range(1,13)
plt.plot(x, monthly_delayed, marker='o', linewidth=0)
plt.ylabel('% Delayed')
plt.xlabel('Month - 2016')
plt.xlim((1,12))
plt.ylim((0,100))
plt.show()


'''