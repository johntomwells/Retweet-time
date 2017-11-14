import numpy, csv, matplotlib
matplotlib.use
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight') # poach style of 538

# reads cleaned data from cleaner.py, puts in dataframe
clean = pd.read_csv(
    filepath_or_buffer = "cleanboys2_retweets.csv",
    sep = ",",
    na_values = ["N/A"],
    dtype = {"Row Labels": "long32", "Sum of Retweet count": "float32"}
)

ax = clean.plot("Row Labels", "Sum of retweet count")
ax.set_xlabel("Time")
ax.set_ylabel("Retweets")
plt.show()
