import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import time

data = pd.read_csv('covid-data.csv')
vaccine = pd.read_csv('vaccinedata.csv')

new_cases = data["new_cases"]

total_cases = data["total_cases"]


ireland = data[(data.location == 'Ireland')  & (data.date > '2020-11-11')]
uk = data[(data.location == 'United Kingdom')  & (data.date > '2020-11-11')]
ger = data[(data.location == 'Germany')  & (data.date > '2020-11-11')]
usa = data[(data.location == 'United States')  & (data.date > '2020-11-11')]
brazil = data[(data.location == 'Brazil')  & (data.date > '2020-11-11')]

vireland = vaccine[(vaccine.Country == 'Ireland')]
vuk = vaccine[(vaccine.Country == 'Northern Ireland')]

virelandd = list(vireland.new_vaccinations_smoothed_per_million)
virelanddate = list(vireland.Date)
totalvireland = []
totalire = 0
for case in virelandd:
    totalire += case
    totalvireland.append(totalire)


irelandpopulation = 4937796
irelandpopulation = int(irelandpopulation)
currentdoses = totalire
currentdoses = int(currentdoses)
avgdosesdaily = currentdoses/len(virelandd)
time.sleep(3)
days = 1
lasttotalvireland = totalvireland[len(totalvireland) - 1]
newtotalvireland = [lasttotalvireland]
lastdatevirelanddate = virelanddate[len(virelanddate) - 1]
newdatevireland = [lastdatevirelanddate]
i = 1

while currentdoses < irelandpopulation:
    currentdoses += avgdosesdaily * 1.1
    avgdosesdaily = currentdoses/len(virelandd)
    enddate = str(pd.to_datetime(lastdatevirelanddate, utc=False) + pd.DateOffset(days=i))
    enddate = enddate[:-9]
    newtotalvireland.append(currentdoses)
    newdatevireland.append(enddate)
    i += 1

print(newdatevireland)

vukd = list(vuk.new_vaccinations_smoothed_per_million)
totalvuk = []
totaluk = 0
for case in vukd:
    totaluk += case
    totalvuk.append(totaluk)

fig, ax = plt.subplots()  # Create a figure containing a single axes.

iretotal = ireland.new_cases/ireland.population
#print(iretotal)
ireper100 = iretotal * 100000

plt.plot(ireland.date, ireper100, "green", label="Ireland")

uktotal = uk.new_cases/uk.population
#print(uktotal)
ukper100 = uktotal * 100000

plt.plot(uk.date, ukper100, "red", label="UK")

braziltotal = brazil.new_cases/brazil.population
#print(braziltotal)
brazilper100 = braziltotal * 100000

plt.plot(brazil.date, brazilper100, "yellow", label="Brazil")

usatotal = usa.new_cases/usa.population
#print(usatotal)
usaper100 = usatotal * 100000

plt.plot(usa.date, usaper100, "blue", label="USA")

gertotal = ger.new_cases/ger.population
#print(gertotal)
gerper100 = gertotal * 100000

plt.plot(ger.date, gerper100, "black", label="Germany")

plt.title("Christmas data per 100,000")
plt.ylabel("Cases")
plt.xlabel("Date")
fig.autofmt_xdate()
plt.xticks(np.arange(0, len(ireland), 20))
plt.legend(loc='upper left')
#plt.show()

fig, ax = plt.subplots()  # Create a figure containing a single axes.

#plt.plot(vuk.Date, totalvuk, "red", linewidth=4, label="Northern Ireland")
plt.plot(vireland.Date, totalvireland, "green", linewidth=4, label="Ireland")
plt.plot(newdatevireland, newtotalvireland, "yellow", linewidth=6, label="Projected Vaccines Ireland")

totallen = len(vuk) + len(newdatevireland)
print(totallen)

plt.title("Vaccines Completed To Date")
plt.ylabel("Doses")
plt.xlabel("Date")
fig.autofmt_xdate()
plt.xticks(np.arange(0, len(vuk), 5))
plt.legend(loc='upper left')
plt.show()