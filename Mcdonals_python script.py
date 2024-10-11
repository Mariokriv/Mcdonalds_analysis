# %% [markdown]
# # McDonalds helath review
# ### -Mario Krivosic-

# %%
#import necceseary libraries for extraction and reforming csv into database 
import pandas as pd
import kagglehub
import sqlite3
import matplotlib.pyplot
%matplotlib inline



# %%
#Get data from computer 
Mcdonalds_data = pd.read_csv(r"C:\\Users\mario\downloads\menu\menu.csv")
Mcdonalds_data.shape

# %%
#Create conection to sqlite 3 for database creation and add McDonaldds to it
conn  = sqlite3.connect('Mcdonalds.db')
Mcdonalds_data.to_sql('Mcdonalds_nutrition', conn)

# %%
#Utilise pandas to add it to a database for manipulation check first row
df = pd.read_sql("Select * from Mcdonalds_nutrition", conn)
df.head()

# %%
#Get simple data overview before diving in 
df.describe(include = 'all')


# %% [markdown]
# # Begin assesment of sodium content in foods 

# %%
#Import graphical data base to find any visual trends and dig deeper \
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sbs

# %%
#create categorical scatterplot of the sodium contents in different foods 
plot = sbs.swarmplot(x="Category", y = 'Sodium', data=df)
plt.setp(plot.get_xticklabels(), rotation=70) #make sure lables are evenly spread
plt.title('Sodium by food')
plt.show()

# %% [markdown]
# ### Finding max sodium items
# 

# %%
#FInd max sodium present in dataset 
df['Sodium'].describe()

# %%
#Find coloumn with max sodium locatio
df['Sodium'].idxmax()

# %%
#FInd this coloumn to find the food item associated
df.loc[82, 'Item']

# %% [markdown]
# # Finding relationship betwen fat and protien 
# 
# 

# %%
#Showcase relationship utilising graph and scipy package 
from scipy.stats import pearsonr
x = df['Protein']
y = df['Total Fat']

pearson_corr, p_value = pearsonr(x, y)  #get values 

plot = sbs.jointplot(x="Protein", y="Total Fat", data=df) #create graph

plt.annotate(f'Pearson r: {pearson_corr:.2f}\nP-value: {p_value:.2g}', 
             xy=(0.1, 0.9), 
             xycoords='axes fraction', 
             fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

#annotate graph

# %% [markdown]
# There is a significant p-value which shows these values are correlated, and judging by the plot this is a positvely skewed correlation

# %%
#Boxplot of suger values
plot = sbs.set_style('darkgrid')
ax = sbs.boxplot(x=df["Sugars"])

# %%



