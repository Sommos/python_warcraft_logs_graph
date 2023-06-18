import pandas as pd
import matplotlib.pyplot as plt
import re
import mplcursors
import os

# function to format the full amount tooltip text on mouse hover
def format_tooltip_text(sel):
    index = sel.target.index
    return f"{df['Shortened Amount'].iloc[index]}"

# save the .csv file path to a variable
csv_path = 'datasets/lava_waves_dmg_taken.csv'
# turns off the warning for chained assignment
pd.set_option('mode.chained_assignment', None)
# read the csv file, and set the variable name to df (dataframe)
df = pd.read_csv(csv_path)

# extract the shortened version of the full number from the "Amount" column using regular expressions
df['Shortened Amount'] = df['Amount'].str.extract('(\d+)', expand = False).astype(float)
# extract the percentage from the "Amount" column using regular expressions
df['Percentage'] = df['Amount'].str.extract('(\d+\.\d+)%', expand = False).astype(float)
# sort the dataframe by the values of the column "Percentage"
df.sort_values(by = 'Percentage', inplace = True, ascending = True)

# create the bar plot
plt.figure(figsize = (14, 8))
# swap x and y axes using the barh() function
plt.barh(df['Name'], df['Percentage'])  
plt.xlabel('Percentage', fontweight = 'bold')  
plt.ylabel('Name', fontweight = 'bold') 
plt.title('Damage Taken from Lava Waves', fontweight = 'bold')
# remove x-axis ticks
plt.xticks([])

# save the damage taken plot as a png file to the figs folder
plt.savefig('figs/lava_waves_dmg_taken.png', bbox_inches = 'tight')

# iterate through the values of the column "Percentage" and place the percentage value inside the bar
for i, value in enumerate(df['Percentage']):
    plt.text(value / 2, i, f"{value:.2f}%", ha = 'center', va = 'center')

# create the mouse cursor for the plot, and connect it to the format_tooltip_text() function
mouse_cursor = mplcursors.cursor(hover = True)
mouse_cursor.connect("add", lambda sel: sel.annotation.set_text(format_tooltip_text(sel)))

plt.show()

# create the bar plot for hits
plt.figure(figsize = (14, 8))
plt.barh(df['Name'], df['Hits'])
plt.xlabel('Hits', fontweight = 'bold')
plt.ylabel('Name', fontweight = 'bold')
plt.title('Hits from Lava Waves', fontweight = 'bold')
# remove x-axis ticks
plt.xticks([])

# save the hits plot as a png file to the figs folder
plt.savefig('figs/lava_waves_hits_taken.png', bbox_inches = 'tight')

# iterate through the values of the column "Percentage" and place the percentage value inside the bar
for i, value in enumerate(df['Hits']):
    plt.text(value / 2, i, f"{value}", ha = 'center', va = 'center')

mouse_cursor = mplcursors.cursor(hover = True)

plt.show()