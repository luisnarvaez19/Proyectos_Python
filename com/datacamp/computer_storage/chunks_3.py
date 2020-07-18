import pandas as pd


# LEYENDO CHUNKS WITH CHUNKSIZE

filename = 'NYC_taxi_2013_01.csv'  #  200000 registros

for chunk in pd.read_csv(filename, chunksize=50000):
    print('type: %s shape %s' % (type(chunk), chunk.shape))

# EXAMINING A CHUNK

chunk.shape

'''
  (49999, 14)
'''
chunk.info
'''
 <class 'pandas.core.frame.DataFrame'>
RangeIndex: 49999 entries, 150000 to 199998
Data columns (total 14 columns):
medallion 49999 non-null object
...
dropoff_latitude 49999 non-null float64
dtypes: float64(5), int64(3), object(6)
memory usage: 5.3+ MB
'''


# FILTERING A CHUNK

is_long_trip = (chunk.trip_time_in_secs > 1200)

chunk.loc[is_long_trip].shape

'''
  (5565, 14)
'''

# CHUNKING AND FILTERING TOGETHER


def filter_is_long_trip(data):
    "Returns DataFrame filtering trips longer than 20 minutes"
    is_long_trip = (data.trip_time_in_secs > 1200)
    return data.loc[is_long_trip]

chunks = []
for chunk in pd.read_csv(filename, chunksize=1000):
    chunks.append(filter_is_long_trip(chunk))

#  ESTOS DOS SON FRAGMENTOS QUE HACEN LO MISMO

chunks = [filter_is_long_trip(chunk)
    for chunk in pd.read_csv(filename,
    chunksize=1000) ]

# USING PD.CONCAT

len(chunks)
'''
  200
'''
lengths = [len(chunk) for chunk in chunks]
lengths[-5:] # Each has ~100 rows

'''
  [115, 147, 137, 109, 119]
'''
long_trips_df = pd.concat(chunks)
long_trips_df.shape

'''
  (21661, 14)
'''
# PLOTTING THE FILTERED RESULTS

import matplotlib.pyplot as plt
long_trips_df.plot.scatter(x='trip_time_in_secs',
                           y='trip_distance');
plt.xlabel('Trip duration [seconds]');
plt.ylabel('Trip distance [miles]');
plt.title('NYC Taxi rides over 20 minutes (2013-01-01to 2013-01-14)');
plt.show();


'''

OTRO EJEMPLO PARA PLOTEAR


# Print length of DataFrame df

len(df)

# Call df.plot.line with x='Year' and y='value'
df.plot.line(x='Year', y='value')
plt.ylabel('% Urban population')

# Call plt.show()
plt.show()



'''

