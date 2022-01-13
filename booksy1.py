#!/usr/bin/env python
# coding: utf-8

# In[54]:


#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[26]:


#import csv file as dataframe
bestseller = pd.read_csv(r'C:\Users\Declan\Downloads\amazon_bs_20102020.csv')
#view the header of the dataframe
print(bestseller.head)


# In[27]:


#Check for missing values
print(bestseller.info())


# In[28]:


#summary statistics
print(bestseller.describe())


# In[29]:


#Sorting the DataFrame based on the number of customer reviews
print(bestseller.sort_values("Num_Customers_Rated", ascending=False))


# In[30]:


#Create subset callled bestsellersub with columns year, rank and book_title
Bestsellersub = bestseller[["Year", "Rank", "Book_Title"]]
print(Bestsellersub.info())


# In[31]:



#print a subset of bestsellersub where Rank = 1
print(Bestsellersub[Bestsellersub["Rank"] == 1])


# In[32]:


#Create a DF called Bestauthors with Rank, Book_Title and Author
Bestauthor = bestseller[["Year", "Rank", "Book_Title", "Author"]]
#Subset rows to show authors who had a ranking of 1 only
print(Bestauthor[Bestauthor["Rank"] == 1])


# In[33]:


# Create DF with columns Author and Rating using .loc and filter on the highest rating value 4.9
Bestrating = bestseller.loc[:, ["Author", "Rating"]]
Rating = Bestrating[Bestrating["Rating"] == 4.9]
print(Rating)


# In[34]:


#Count the number of times authors appear with the rating of 4.9
print(Rating["Author"].value_counts(sort=True))


# In[35]:


#code for loop that adds a column title_length
for lab, row in bestseller.iterrows() :
    bestseller.loc[lab, "Title_Length"] = len(row["Book_Title"])
    


# In[36]:


#Print header of bestseller with new Column
print(bestseller.head())


# In[37]:


#Grouped the data by rank and the average price of the book
print(bestseller.groupby("Rank")["Price"].mean())


# In[38]:


# Grouped by Rank and the average number of customer reviews
print(bestseller.groupby("Rank")["Num_Customers_Rated"].mean())


# In[39]:


# Summarise ranking based on average price and average rating
print(bestseller.groupby("Rank")["Price", "Num_Customers_Rated"].mean())


# In[40]:


#Set the index of bestseller to rank and assign to bestseller_rank
Bestseller_rank = bestseller.set_index("Rank")
print(Bestseller_rank.head())


# In[41]:


#Create a list called Rankings that contains "1" and "100"
Rankings = [1, 100]


# In[42]:


#use .loc to subset bestseller_rank for rows where it matches the ranking list
print(Bestseller_rank.loc[Rankings])


# In[43]:


#Select books that cost above the average price
print(bestseller[bestseller["Price"] > 10.85])


# In[44]:


#Select books that are between price of 15.80 and 152
Price = bestseller["Price"]
Pricebet = np.logical_and(Price >= 15.80, Price <= 152)
Pricehigh = bestseller[Pricebet]
print(Pricehigh)


# In[45]:


#Create list of Authors with highest rating of 4.9
Topbook =bestseller.groupby('Author').mean().Rating.sort_values(ascending=False)
#print Author over 4.9
print(Topbook[Topbook>=4.9])


# In[46]:


# Chart no. of ratings of top books
ratings=bestseller.groupby('Book_Title').sum().Num_Customers_Rated.sort_values(ascending=False).head(10)
print(ratings)


# In[56]:


#plot barchart
sns.barplot(data=ratings.to_frame().reset_index(), y='Book_Title', x='Num_Customers_Rated')
sns.despine(top=1, left=1, right=1)
plt.ylabel('')
plt.title('Top 10 Books by Number of Ratings', fontweight='bold', fontsize=14)
print(plt.show())


# In[61]:


# Chart no. of ratings of authors
authratings=bestseller.groupby('Author').sum().Num_Customers_Rated.sort_values(ascending=False).head(10)
print(authratings)
#plot barchart
sns.barplot(data=authratings.to_frame().reset_index(), y='Author', x='Num_Customers_Rated')
sns.despine(top=1, left=1, right=1)
plt.ylabel('')
plt.title('Top Authors by Number of Ratings', fontweight='bold', fontsize=14)
print(plt.show())


# In[110]:


#Scatter plot to view rating against Number of customers ratings
bestseller.plot(x="Rating", 
                y="Num_Customers_Rated", 
                kind="scatter")
plt.show()


# In[112]:


#histogram showing price of no. 1 rank books and no.100 rank books
bestseller[bestseller["Rank"] == 1]["Price"].hist()
bestseller[bestseller["Rank"] == 100]["Price"].hist()
plt.legend([1, 100])
plt.show()


# In[77]:


#histogram showing prices in 2010 and 2020
bestseller[bestseller["Year"] == 2010]["Price"].hist()
bestseller[bestseller["Year"] == 2020]["Price"].hist()
plt.legend([2010, 2020])
plt.ylabel('No. of Books')
plt.xlabel('Price')
plt.show()


# In[103]:


#Top 10 Books for 2010 and 2020 by Price
year2010 = bestseller[bestseller["Year"] == 2010].head(10)
year2020 = bestseller[bestseller["Year"] == 2020].head(10)
fig, ax = plt.subplots()
ax.plot(year2010["Rank"], year2010["Price"], marker="o")
ax.plot(year2020["Rank"], year2020["Price"], marker="o")
plt.ylabel('Price')
plt.xlabel('Rank 1-10')
plt.legend([2010, 2020])
plt.title('Comparison Top 10 Books 2010/2020 by Price', fontweight='bold', fontsize=14)
plt.show()


# In[109]:


#Top 10 Books by Number of Customer Ratings across all years in Subplots
year2010 = bestseller[bestseller["Year"] == 2010].head(10)
year2011 = bestseller[bestseller["Year"] == 2011].head(10)
year2012 = bestseller[bestseller["Year"] == 2012].head(10)
year2013 = bestseller[bestseller["Year"] == 2013].head(10)
year2014 = bestseller[bestseller["Year"] == 2014].head(10)
year2015 = bestseller[bestseller["Year"] == 2015].head(10)
year2016 = bestseller[bestseller["Year"] == 2016].head(10)
year2017 = bestseller[bestseller["Year"] == 2017].head(10)
year2018 = bestseller[bestseller["Year"] == 2018].head(10)
year2019 = bestseller[bestseller["Year"] == 2019].head(10)
year2020 = bestseller[bestseller["Year"] == 2020].head(10)
fig, ax = plt.subplots(4,1, sharey=True)
ax[0].plot(year2010["Rank"], year2010["Rating"], marker="o", color='b')
ax[0].plot(year2011["Rank"], year2011["Rating"], marker="o", color='r')
ax[0].plot(year2012["Rank"], year2012["Rating"], marker="o", color='g')
ax[0].legend([2010, 2011, 2012])
ax[1].plot(year2013["Rank"], year2013["Rating"], marker="o", color='b')
ax[1].plot(year2014["Rank"], year2014["Rating"], marker="o", color='r')
ax[1].plot(year2015["Rank"], year2015["Rating"], marker="o", color='g')
ax[1].legend([2013, 2014, 2015])
ax[2].plot(year2016["Rank"], year2016["Rating"], marker="o", color='b')
ax[2].plot(year2017["Rank"], year2017["Rating"], marker="o", color='r')
ax[2].plot(year2018["Rank"], year2018["Rating"], marker="o", color='g')
ax[2].legend([2016, 2017, 2018])
ax[3].plot(year2019["Rank"], year2010["Rating"], marker="o", color='b')
ax[3].plot(year2020["Rank"], year2020["Rating"], marker="o", color='r')
ax[3].legend([2019, 2020])
ax[3].set_ylabel("Cust. Ratings")
ax[3].set_xlabel("Rank 1-10")
plt.show()


# In[ ]:




