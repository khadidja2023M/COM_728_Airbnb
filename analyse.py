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
    print(' ')
    #This code will set the no truncate for Pandas.
    pd.set_option("display.max_columns", None)#show all cols.
    pd.set_option("display.max_rows", None)#show full rows 
    pd.set_option("display.max_colwidth", None)#show full width of showing cols.
    pd.set_option("expand_frame_repr", False)#print cols side by side as it's supposed to be
    data = pd.read_csv(file_path, parse_dates=[0], dayfirst=True, infer_datetime_format=True)
    return data
    
# In[ ]:

#This function display the menu of analyse selection.
def analyse_menu():
    print(f"""select which menu would you like:
    {"[1]":<6} : The most popular amenities that Airbnb guests are looking for.\n 
    {"[2]":<6} : The average price of stay in each location.\n
    {"[3]":<6} : The average review scores rating for each location.\n
    {"[4]":<6} : The average price for host is superhost and host not superhost.\n 
    {"[5]":<6} : Go back to main menu.""")
    print(' ')
    menu_selection = input('your selection: ')
    return menu_selection.strip() 

# In[5]:

#This function displays The most popular amenities.  
def popular_amenities(data):
    tui.started("Display the top 10 most popular amenities")
    print(' ')
    data_amenities = data['amenities']
    #Create an empty dictionnary.
    amenities = {}
    #For each list in data amenties.
    for amenity in data_amenities:
        #The list amenity is a sring, eval function separats the elememts.
        amenity = eval(amenity)
        #For each element in the list.
        for x in amenity:
            #If the element dosent exist in the list his count is 1.
            if x not in amenities:
                amenities[x]=1
            else:
                #If the element existe in the list keep adding to get the count of the word.
                amenities[x]+=1
    #Sort the dictionnary and put it in a list to use indexing to get the first 10 amenities.           
    sort_amenities = list(sorted(amenities.items(), key = lambda item:item[1], reverse = True))
    print(f'\033[1;30mThe most popular amenities are\033[0m:{sort_amenities[0:10]}')            
    tui.completed()
    
# In[9]:

#This function displays the average price of stay in each location.      
def average_price_location(data):
    tui.started('Display average price by location:')
    print(' ')
    #Groupby function groups data by host location and get the average price of each group using the mean function 
    average_stay_location = data.groupby('host_location', as_index=False)['price'].mean()
    #Add a column of mean and set the data to columns.
    average_stay_location.columns = ['host_location','mean_price']
    average_stay_location['mean_price'] = average_stay_location['mean_price'].apply(lambda x:round(x,3))
    #Use string format to write in bold.
    print(f'\033[1;30mThe average stay in each location\033[0m:\n')
    #Use display function instead of print function to show the result without traucate. 
    display(average_stay_location)
    tui.completed() 

#In[11]:

#This function displays the average review scores rating for each location.      
def average_review_location(data):
    tui.started('Display the average review scores rating:')
    print(' ')
    #Groupby function groups data by host location and get the average review score of each group using the mean function.
    average_review_location = data.groupby('host_location', as_index=False )['review_scores_location'].mean()
    average_review_location.columns = ['host_location','mean_review']
    average_review_location['mean_review'] = average_review_location['mean_review'].apply(lambda x:round(x,3))
    print(f'\033[1;30mThe average review rate score for each location is\033[0m:\n')
    display(average_review_location)
    tui.completed()

# In[16]:

#This function Analyses the average price for host is superhost and host not superhost.
def average_price_host_is_superhost(data):
    tui.started('Display average price for host is superhost:')
    print(' ')
    #Groupby function groups data by host is superhost and get the average price of each group using the mean function.
    average_price = data.groupby(['host_is_superhost'])['price'].mean()
    #Get the count of each group to compart the average price of the two groupes.
    not_super_count = data.loc[data.host_is_superhost == False,['host_is_superhost']].count()
    superhost_count = data.loc[data.host_is_superhost == True,['host_is_superhost']].count()
    #Display two numbers after the decimal for the price.
    print(f"\033[1;30mThe number of not suprhost is\033[0m:{not_super_count.values} with the average price of:{average_price.values[0]:.2f}")
    print(f"\033[1;30mThe number of suprhost is\033[0m:{superhost_count.values} with the average price of:{average_price.values[1]:.2f}")
    tui.completed()   


# In[ ]:




