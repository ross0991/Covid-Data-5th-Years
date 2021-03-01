import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import time

data = pd.read_csv('covid-data.csv')
vaccine = pd.read_csv('vaccinedata.csv')

new_cases = data["new_cases"]
total_cases = data["total_cases"]
