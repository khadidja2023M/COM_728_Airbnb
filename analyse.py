#!/usr/bin/env python
# coding: utf-8

# In[34]:


#analyse module

import tui
import pandas as pd 

#read csv file using pandas.
def load_data_pandas(file_path):
    #call started function from tui module to indicate that the operation is started. 
    tui.started("Reading data from file path using pandas module.")
    data = pd.read_csv(file_path)
    return data
    



# In[ ]:


#This function display the menu of analyse selection.
def analyse_menu():
    print(f"""select which menu would you like:
    {"[1]":<6}:The most popular amenities that Airbnb guests are looking for.\n 
    {"[2]":<6}:The average price of stay in each location.\n
    {"[3]":<6}:The average review scores rating for each location.\n
    {"[4]":<6}:The average price for host is superhost and host not superhost.\n 
    {"[exit]":<6}:Exit the programme.""")
    menu_selection = input('your selection: ')
    return menu_selection.strip().lower() 




# In[5]:


#This function displays The most popular amenities.  
def popular_amenities(data):
    tui.started("Display the top 10 most popular amenities")
    data_amenities =data['amenities'] 
    amenities={}
    for amenity in data_amenities:
        amenity=eval(amenity)
        for x in amenity:
            if x not in amenities:
                amenities[x]=1
            else:
                amenities[x]+=1
    sort_amenities = list(sorted(amenities.items(), key=lambda item:item[1],reverse=True))
    print(f'The most popular amenities are:{sort_amenities[0:10]}')            
    tui.completed()
  


 # In[9]:


#This function displays the average price of stay in each location.      
def average_price_location(data):
    tui.started('display average price by location:')
    #Groupby function groups data by host location and get the average price of each group using the mean function 
    average_stay_location = data.groupby(['host_location'])['price'].mean()
    print(f'The average stay in each location:\n{average_stay_location}')         
    tui.completed() 




# In[11]:


#This function displays the average review scores rating for each location.      
def average_review_location(data):
    tui.started('display the average review scores rating:')
    #Groupby function groups data by host location and get the average review score of each group using the mean function.
    average_review_location = data.groupby(['host_location'])['review_scores_location'].mean()
    print(f'The average review rate score for each location is:\n{average_review_location}')
    tui.completed()



# In[16]:

#This function Analyses the average price for host is superhost and host not superhost.

def average_price_host_is_superhost(data):
    tui.started('display average price for host is superhost:')
    #Groupby function groups data by host is superhost and get the average price of each group using the mean function.
    average_price = data.groupby(['host_is_superhost'])['price'].mean()
    #Get the count of each group to compart the average price of the 2 groupes.
    not_super_count=data.loc[data.host_is_superhost ==False,['host_is_superhost']].count()
    superhost_count=data.loc[data.host_is_superhost ==True,['host_is_superhost']].count()
    print(f"The number of not suprhost is:{not_super_count.values} with the average price of:{average_price.values[0]:.2f}") 
    print(f"The number of suprhost is:{superhost_count.values} with the average price of:{average_price.values[1]:.2f}")
    tui.completed()   


# In[ ]:




