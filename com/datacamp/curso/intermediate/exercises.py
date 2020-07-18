'''

        INTERMEDIATE PYTHON


'''

# Line plot
# Exercise 1

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()



# Exercise 2

# Print the last item of gdp_cap (Gross domestic product), and life_exp (Life expectation)
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()


# Exercise 3

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


# Exercise 4

# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop,life_exp)

# Show plot
plt.show()



# Histogram
# Exercise 5
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()


# Exercise 6

# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()


# Exercise 7
# Histogram of life_exp, 15 bins
plt.hist(life_exp,bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,bins=15)

# Show and clear plot again
plt.show()
plt.clf()


# Customize your plots
# Exercise 8

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()




# Exercise 9

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()




# Exercise 10
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


# Exercise 11

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha= 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


# Exercise 12

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)
#plt.text()

# Show the plot
plt.show()




#  Dictionaries
# Exercise 13

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(ind_ger)
print(capitals[ind_ger])



# Exercise 14

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin','norway':'oslo' }

# Print europe
print(europe)



# Exercise 15
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])



# Exercise 16

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland']= 'warsaw'

# Print europe
print(europe)



# Exercise 17
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)


# Exercise 18

# Dictionary of dictionaries
europe = {'spain': {'capital':'madrid', 'population':46.77 },
           'france': {'capital':'paris', 'population':66.03 },
           'germany': {'capital':'berlin', 'population':80.62 },
           'norway': {'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome' ,'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data


# Print europe
print(europe)


#  Pandas
# Exercise 19

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)




# Exercise 20

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)




# Exercise 21

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)



# Exercise 22

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])


# Exercise 23

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations (rows)
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])



# Exercise 24

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])


# Exercise 25
# Import cars data
'''
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True

'''
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars['drives_right']['MOR'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'],['country','drives_right']])


# Exercise 26

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars['drives_right'])

# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])



#  Comparisons
# Exercise 27

# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
'pyscript' == 'PyScript'


# Compare a boolean with an integer
True == 1


# Exercise 28
# Comparison of integers
x = -3 * 6


# Comparison of strings
y = "test"


# Comparison of booleans
print(x >= -10)

print('test' <= y)

print(True > False)


# Exercise 29
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)


# Exercise 30

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen > 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2 * my_kitchen < 3 * your_kitchen)


# Exercise 31
x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))  (False)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10) )

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11) )


#   IF   ELIF   ELSE
# Exercise 32
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit":
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print('big place!')


# Exercise 33

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")





# Exercise 34

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif (area > 10):
    print("medium size, nice!")
else :
    print("pretty small.")


#   Filtering dataframes
# Exercise 35

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)



# Exercise 36
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars[cars['drives_right']])



# Exercise 37
'''
Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
Use cpc in combination with a comparison operator and 500. You want to end up with a boolean
 Series that's True if the corresponding country has a cars_per_cap of more than 500 and
  False otherwise. Store this boolean Series as many_cars.
Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
Print out car_maniac to see if you got it right.



'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cars[cpc >500]
print(many_cars)
# car_maniac = cars[many_cars]

# La respuesta anterior esta mala
# La respuesta buena es:

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)





# Exercise 38

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between =  np.logical_and(cpc > 100, cpc < 500)

medium = cars[between]

# Print medium
print(medium)


#  Ciclo while
# Exercise 39
# Initialize offset
offset = 8

# Code the while loop
while offset > 0:
    print("correcting...")
    offset -= 1
    print(offset)

#  Whiles and fors
# Exercise 39

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset -= 1
    else:
        offset += 1

    print(offset)




# Exercise 40

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for elem in areas:
    print(elem)



# Exercise 41
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, height in enumerate(areas) :
    print('room '+str(index)+': '+str(height))



# Exercise 42

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for elem in house:
    print('the ' + elem[0] + ' is ' + str(elem[1]) + ' sqm')


# Loop over dictionary
# Exercise 43
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print('the capital of ' + key + ' is ' + str(value))



# Exercise 44

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x)+' inches')

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)



# Exercise 45

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
# US
# cars_per_cap              809
# country         United States
# drives_right             True
# Name: US, dtype: object
# AUS
# cars_per_cap          731
# country         Australia
# drives_right        False
# Name: AUS, dtype: object
# JPN
# cars_per_cap      588
# country         Japan
# drives_right    False
# Name: JPN, dtype: object
# IN
# cars_per_cap       18
# country         India
# drives_right    False
# Name: IN, dtype: object
# RU
# cars_per_cap       200
# country         Russia
# drives_right      True
# Name: RU, dtype: object
# MOR
# cars_per_cap         70
# country         Morocco
# drives_right       True
# Name: MOR, dtype: object
# EG
# cars_per_cap       45
# country         Egypt
# drives_right     True
# Name: EG, dtype: object


# Exercise 46

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ': ' + str(row['cars_per_cap']) )


'''
Use a for loop to add a new column, named COUNTRY, that contains a uppercase version
 of the country names in the "country" column. 
 You can use the string method upper() for this.
'''
# Exercise 47
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab,'COUNTRY'] = str(row['country']).upper()

# Print cars
print(cars)



# Exercise 48   (Lo mismo que antes y sin for)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)


print(cars)

#  RANDOM NUMBERS
# Exercise 49

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


# Exercise 50
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
np.random.randint(1,7)

# Use randint() again
np.random.randint(1,7)


# Exercise 51
'''
    Roll the dice. Use randint() to create the variable dice.
    Finish the if-elif-else construct by replacing ___:
    If dice is 1 or 2, you go one step down.
    if dice is 3, 4 or 5, you go one step up.
    Else, you throw the dice again. The number of eyes is the number of steps you go up.
    Print out dice and step. Given the value of dice, was step updated correctly?
    
'''
# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice == 3 or dice == 4 or dice == 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


# Exercise 52
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the for
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()


# Exercise 53

# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


# Visualize all walks
# Exercise 54

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()



# Exercise 55
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()




# Exercise 56



# Exercise 57



# Exercise 58



# Exercise 59



# Exercise 60

