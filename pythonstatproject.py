import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#from matplotlib.ticker import FuncFormatter


# line graph
df = pd.read_csv('C:/Users/president/Desktop/covidproject/covid-datasett.csv')
df_line = df.groupby(['WHO Region'])[['Cases - cumulative total', 'Deaths - cumulative total']].sum().reset_index()
df_line.plot(x='WHO Region', y=['Cases - cumulative total', 'Deaths - cumulative total'], kind='line')
plt.xlabel('WHO Region')
plt.ylabel('Total Cases/Deaths')
plt.xticks(rotation=90)
plt.title('Cases and Deaths per Region')
plt.show()

# bar graph showing cases and death for top 30 countries with deaths
df = df[df['Name'] != 'Global']
df_bar = df.groupby(['Name'])[['Cases - cumulative total', 'Deaths - cumulative total']].sum().reset_index().sort_values('Cases - cumulative total', ascending=False).head(30)
df_bar.plot(x='Name', y=['Cases - cumulative total', 'Deaths - cumulative total'], kind='bar')
plt.xlabel('countries')
plt.ylabel('Total Cases/Deaths')
plt.xticks(rotation=90)
plt.title('Cases and Deaths per Countries')
plt.show()

#only eurpoe

df_europe = df[df['WHO Region'] == 'Europe']
df_line = df_europe.groupby(['Name'])[['Cases - cumulative total', 'Deaths - cumulative total']].sum().reset_index().sort_values('Cases - cumulative total', ascending=False).head(20)
df_line.plot(x='Name', y=['Cases - cumulative total', 'Deaths - cumulative total'], kind='line')
plt.xlabel('Name')
plt.ylabel('Total Cases/Deaths')
plt.xticks(rotation=90)
plt.title('Cases and Deaths per country in Europe')
plt.show()




#column_values = df['WHO Region'].values
#print(column_values)

#print(df.iloc[:,0])

# top 30 countries with most cases

df_top30 = df.sort_values(by=['Cases - cumulative total'], ascending=False).head(30)
df_top30['Name'] = df.iloc[:,0]
df_top30.plot(x='Name', y='Cases - cumulative total', kind='bar',title = 'Covid19 : Top 30 Countries with highest cumulative cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()



import matplotlib.pyplot as plt

df_subset = df[['Name', 'Cases - cumulative total', 'Deaths - cumulative total']]

#sort the dataframe
df_subset = df_subset.sort_values(by=['Cases - cumulative total'],ascending=False)

# take first 30 rows
df_top30 = df_subset.head(60)

# create the bar chart
df_top30.plot(kind='bar', x='Name', y='Cases - cumulative total', color='blue', legend=False)

# add labels and title
plt.xlabel('Country')
plt.ylabel('Cumulative Total Cases')
plt.title('Top 30 Countries with Most Cases')

# rotate the x-axis labels to make them more readable
plt.xticks(rotation=90)

# show the chart
plt.show()


#import pandas as pd
#import matplotlib.pyplot as plt

# Load the dataset
#df = pd.read_csv('covid-datasett.csv')

# Group the data by WHO region
#import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/president/Desktop/covidproject/covid-datasett.csv')
df = df[(df['WHO Region'] == 'Western Pacific') | (df['WHO Region'] == 'Europe')]
df_grouped = df.groupby(['WHO Region'])['Cases - cumulative total', 'Deaths - cumulative total'].sum().reset_index()

fig, ax = plt.subplots()
ax.boxplot([df[df['WHO Region'] == 'Western Pacific']['Cases - cumulative total'], df[df['WHO Region'] == 'European']['Cases - cumulative total']], labels=['Asia', 'Europe'], widths=0.3, notch=True)
ax.set_title('Comparison of number of cases in Asia and Europe')
ax.set_ylabel('Number of Cases')

plt.show()

fig, ax = plt.subplots()
ax.boxplot([df[df['WHO Region'] == 'Western Pacific']['Deaths - cumulative total'], df[df['WHO Region'] == 'European']['Deaths - cumulative total']], labels=['Asia', 'Europe'], widths=0.3, notch=True)
ax.set_title('Comparison of number of deaths in Asia and Europe')
ax.set_ylabel('Number of Deaths')

plt.show()

# heat map fo 20 eu countries
df = pd.read_csv('C:/Users/president/Desktop/covidproject/covid-datasett.csv')
df_europe = df[df['WHO Region'] == 'Europe'].sort_values('Deaths - cumulative total', ascending=False).head(20)

sns.heatmap(df_europe.set_index('Name').loc[:, ['Deaths - cumulative total']], annot=True, fmt='d')
plt.xlabel('Deaths')
plt.ylabel('Name')
plt.title('Deaths in Top 20 European Countries')
plt.show()



#print("Country Wise Data shape =",df.shape)
#df.head()
