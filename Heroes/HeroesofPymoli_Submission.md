
# Heroes of Pymoli - Jeffrey Coen


```python
# Dependencies
import pandas as pd
import numpy as np
```


```python
# Import the file
filename = ('raw_data/purchase_data.json')
heroes_df = pd.read_json(filename)

# Printed in first run through but will remove later
heroes_df.columns

```




    Index(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN'], dtype='object')



# Player Count


```python
# Player Count

# Total Number of Players
total_players = heroes_df["SN"].nunique()

# Create df for total number of players
df_total_players = pd.DataFrame({
    "Total Players": [total_players]
})
df_total_players
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Total)


```python
# Number of Unique Items
unique_items = heroes_df['Item ID'].nunique()

# Average Purchase Price
average_price = round(heroes_df["Price"].mean(), 2)

# Total Number of Purchases
number_of_purchases = heroes_df["Item ID"].count()

# Total Revenue
total_revenue = heroes_df["Price"].sum()

# Build the DF 
df_purchasing_analysis = pd.DataFrame({
    "Number of Unique Items": [unique_items],
    "Average Purchase Price": [average_price],
    "Number of Purchases": [number_of_purchases],
    "Total Revenue": [total_revenue]
})

# Print the DF
df_purchasing_analysis

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>780</td>
      <td>183</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics


```python
# Count of Male Players
male_players = heroes_df.loc[heroes_df["Gender"] == "Male"].nunique()

# Count of Female Players
female_players = heroes_df.loc[heroes_df["Gender"] == "Female"].nunique()

# Count of Other / Non-Disclosed
other_players = heroes_df.loc[heroes_df["Gender"] == "Other / Non-Disclosed"].nunique()

# DF Gender Demographics
df_gender_demographics = pd.DataFrame({
    # Use previous total players int for figuring out the percentage
    "Percentage of Players": [(male_players["SN"]/total_players*100).round(2), 
                              (female_players["SN"]/total_players*100).round(2), 
                              (other_players["SN"]/total_players*100).round(2)],
    "Total Count": [male_players["SN"], female_players["SN"], other_players["SN"]]
    
},index = ['Male', 'Female', 'Other'])

df_gender_demographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Gender)


```python
# Create New DF for gender analysis
df = (heroes_df
      # group DF by gender column
      .groupby(['Gender'], as_index = False)
      .Price
      # Perform calculations as directed by instructions
      .agg({'Count':len, 'Total': 'sum', 'Average': np.mean
           })
     )

# Remove extra decimals as this is currency
df['Average'] = round(df["Average"], 2)

# Print that DF
df


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Count</th>
      <th>Total</th>
      <th>Average</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Female</td>
      <td>136.0</td>
      <td>382.91</td>
      <td>2.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>633.0</td>
      <td>1867.68</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>11.0</td>
      <td>35.74</td>
      <td>3.25</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics



```python
# Create new DF for age, group the age, count how many times each age appears
age_df = (heroes_df
      .groupby(['Age'], as_index = False)
    .SN
      .agg({'Count':len, 
           })
     )
# Remove hash below to show counts of ages
# age_df
```


```python
# Create bins and group names in order to drop ages into categories
bins = [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
group_names = [ '< 10', '10 - 14', '14 - 18', '18 - 22', '22 - 26', '26 - 30', '30 - 34', '34 - 38', '38 - 42', '42 - 46']

```


```python
# Place ages into the categories
categories = pd.cut(age_df['Age'], bins, labels=group_names)
age_df['categories'] = pd.cut(age_df['Age'], bins, labels=group_names)
#age_df
```


```python
# Final age df is meant to merge the new age_df with the first DF, heroes_df
final_age_df = pd.merge(age_df, heroes_df, on = "Age", how="outer")
final_age_df

# Create grouped_age DF to group the categories
grouped_age = (final_age_df
      .groupby(['categories'], as_index = False)
      .Price
      .agg({'Count':len, 'Total': 'sum', 'Average': np.mean, 
           })
     )
grouped_age['Average']=round(df['Average'], 2)
grouped_age.sort_index(by='categories', ascending = True)

```

    /Users/jeffreycoen/anaconda/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:13: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>categories</th>
      <th>Count</th>
      <th>Total</th>
      <th>Average</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10 - 14</td>
      <td>31.0</td>
      <td>83.79</td>
      <td>2.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14 - 18</td>
      <td>111.0</td>
      <td>319.32</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18 - 22</td>
      <td>231.0</td>
      <td>676.20</td>
      <td>3.25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22 - 26</td>
      <td>207.0</td>
      <td>608.02</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26 - 30</td>
      <td>63.0</td>
      <td>187.99</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30 - 34</td>
      <td>46.0</td>
      <td>141.24</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>34 - 38</td>
      <td>37.0</td>
      <td>104.06</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>38 - 42</td>
      <td>20.0</td>
      <td>62.56</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>42 - 46</td>
      <td>2.0</td>
      <td>6.53</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>&lt; 10</td>
      <td>32.0</td>
      <td>96.62</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

       

```

# Top Spenders


```python
#Identify the the top 5 spenders in the game by total purchase value, then list (in a table):

#SN
#Purchase Count
#Average Purchase Price
#Total Purchase Value
```


```python
df = (heroes_df
      .groupby(['SN'], as_index = False)
      .Price
      .agg({'Count':len, 'Total': 'sum', 'Average': np.mean
           })
     )
df['Average']=round(df['Average'], 2)
df.sort_index(by='Total', ascending = False).head(5)
```

    /Users/jeffreycoen/anaconda/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:8: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Count</th>
      <th>Total</th>
      <th>Average</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>538</th>
      <td>Undirrala66</td>
      <td>5.0</td>
      <td>17.06</td>
      <td>3.41</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Saedue76</td>
      <td>4.0</td>
      <td>13.56</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Mindimnya67</td>
      <td>4.0</td>
      <td>12.74</td>
      <td>3.18</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Haellysu29</td>
      <td>3.0</td>
      <td>12.73</td>
      <td>4.24</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Eoda93</td>
      <td>3.0</td>
      <td>11.58</td>
      <td>3.86</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items


```python
#Most Popular Items

#Item ID

#Item Name
#Purchase Count
#Item Price
#Total Purchase Value


    
```


```python
df = (heroes_df
      .groupby(['Item Name'],# 'Price'], 
               as_index = False)
      .Price
      .agg({'Count':len, 'Total': 'sum', #'Prices': ('sum'/len),
           })
     )

df['Price'] = df['Total']/df['Count']
df['Price'] = round(df['Price'], 2)
df.sort_index(by='Count', ascending = False).head(5)

```

    /Users/jeffreycoen/anaconda/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:11: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Count</th>
      <th>Total</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>Final Critic</td>
      <td>14.0</td>
      <td>38.60</td>
      <td>2.76</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Arcane Gem</td>
      <td>11.0</td>
      <td>24.53</td>
      <td>2.23</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11.0</td>
      <td>25.85</td>
      <td>2.35</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Stormcaller</td>
      <td>10.0</td>
      <td>34.65</td>
      <td>3.46</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9.0</td>
      <td>11.16</td>
      <td>1.24</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python

```



# Most Profitable Items


```python
#Most Profitable Items

#Identify the 5 most profitable items by total purchase value, then list (in a table):
#Item ID
#Item Name
#Purchase Count
#Item Price
#Total Purchase Value

df = (heroes_df
      .groupby(['Item Name'], as_index = False)
    .Price
      .agg({'Count':len, 'Total': 'sum', #'Price': ,
           })
     )
df['Price'] = df['Total']/df['Count']
df['Price'] = round(df['Price'], 2)
df.sort_index(by='Total', ascending = False).head(5)
```

    /Users/jeffreycoen/anaconda/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:18: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Count</th>
      <th>Total</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>Final Critic</td>
      <td>14.0</td>
      <td>38.60</td>
      <td>2.76</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Retribution Axe</td>
      <td>9.0</td>
      <td>37.26</td>
      <td>4.14</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Stormcaller</td>
      <td>10.0</td>
      <td>34.65</td>
      <td>3.46</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7.0</td>
      <td>29.75</td>
      <td>4.25</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Orenmir</td>
      <td>6.0</td>
      <td>29.70</td>
      <td>4.95</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```
