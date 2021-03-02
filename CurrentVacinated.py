import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import time

data = pd.read_csv('csv_Data/covid-data.csv')
vaccine = pd.read_csv('csv_Data/vaccinedata.csv')

new_cases = data["new_cases"]
total_cases = data["total_cases"]

# ireland = data[(data.location == 'Ireland') & (data.date > '2020-11-11')]

# plt.plot(ireland.date, ireper100, "green", label="Ireland")
# plt.ylabel("Cases")
# plt.xlabel("Date")
# plt.savefig("Ireland.png")

ireland = data[(data.location == 'Ireland') & (data.date > '2020-11-11')]
uk = data[(data.location == 'United Kingdom') & (data.date > '2020-11-11')]
ger = data[(data.location == 'Germany') & (data.date > '2020-11-11')]
usa = data[(data.location == 'United States') & (data.date > '2020-11-11')]
brazil = data[(data.location == 'Brazil') & (data.date > '2020-11-11')]


fig, ax = plt.subplots()

#Ireland
ire_total = ireland.new_cases/ireland.population
print(ire_total)
ire_per_100 = ire_total * 100000
plt.plot(ireland.date, ire_per_100, "green", label="Ireland")


#United Kingdom
uk_total = uk.new_cases/uk.population
print(uk_total)
uk_per_100 = uk_total * 100000
plt.plot(uk.date, uk_per_100, "red", label="United Kingdom")

#Germany
ger_total = ger.new_cases/ger.population
print(ger_total)
ger_per_100 = ger_total * 100000
plt.plot(ger.date, ger_per_100, "black", label="Germany")

#United States
usa_total = usa.new_cases/usa.population
print(usa_total)
usa_per_100 = usa_total * 100000
plt.plot(usa.date, usa_per_100, "blue", label="United States")

#Brazil
brazil_total = brazil.new_cases/brazil.population
print(brazil_total)
brazil_per_100 = brazil_total * 100000
plt.plot(brazil.date, brazil_per_100, "yellow", label="Brazil")



#Get Results
plt.title("Christmas Data per 100, 000")
plt.ylabel("Cases")
plt.xlabel("Date")
fig.autofmt_xdate()
plt.xticks(np.arange(0, len(ireland), 20))
plt.legend(loc="upper left")
# plt.savefig("graphs/christmas_data.png")


#Homework create for +2 coutries
#Japan And India For The Month Of June

japan = data[(data.location == 'Japan') & (data.date < '2020-12-01')]
india = data[(data.location == 'India') & (data.date < '2020-12-01')]

fig, ax = plt.subplots()

japan_total = japan.new_cases/japan.population
japan_per_100 = japan_total * 100000
plt.plot(japan.date, japan_per_100, "yellow", label="Japan")

india_total = india.new_cases/india.population
india_per_100 = india_total * 100000
plt.plot(india.date, india_per_100, "red", label="India")

plt.title("June Data per 100, 000")
plt.ylabel("Cases")
plt.xlabel("Date")
fig.autofmt_xdate()
plt.xticks(np.arange(0, len(india), 20))
plt.legend(loc="upper left")
plt.savefig("graphs/India_japan_rates_per_100,000.png")