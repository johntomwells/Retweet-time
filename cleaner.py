# John Wells
# Takes Data from workbook jungle:
# which is retweet data
# averages # of retweets for each minute

import xlrd
import csv

# open workbook
wd = xlrd.open_workbook("jungle.xlsx")
# declare working sheet
jungle = wd.sheet_by_index(0)

# reads col of time
timestamp = jungle.col_values(2)
rows = len(timestamp) # size of sheet

def main():
    cleanboys = [] # initialize new list
    for x in range(rows):
        rt_cut = jungle.cell(x, 3).value    # iterate retweets
        time_cut = jungle.cell(x, 2).value  # times
        if rt_cut <= 300000: # unhealthy outliers from initial excel runthrough
            cleanboy = [time_cut, rt_cut]
            cleanboys.append(cleanboy)  # add to new list of only timestamps and retweets

    # create clean, new file for plotting
    with open('cleanboys_retweets.csv', 'wb') as f:
    	writer = csv.writer(f)
    	writer.writerow(["time","retweet count"])
    	writer.writerows(cleanboys)

main()
