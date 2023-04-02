#!/usr/bin/env python
# coding: utf-8

# In[11]:


#plot module 


import tui 
import matplotlib.pyplot as plt 
import pandas as pd





# In[12]:


#This function displays the menu of visualisation selection.
def plot_menu():
    print(f"""select which menu whoud you like:
    {"[1]":<6}:The proportion of number of bedrooms of Airbnb listing using pie chart.\n 
    {"[2]":<6}:The number of listings for each room type using bar chart.\n  
    {"[3]":<6}:The relationship between accommodates and price using scatter plot rating.\n
    {"[4]":<6}:Subplots of airbnb prices from 2019 -2022.\n  
    {"[5]":<6}:The relation between host response time and number of reviews.\n
    {"[exit]":<6}:Exit the programme.                
    """)
    menu_selection=input('your selection: ')
    return menu_selection.strip().lower()     




# In[13]:


#This function displays the proportion of number of bedrooms of Airbnb listing using pie chart. 
def number_bedrooms(data):
    tui.started('Display the propportion of number of Airbnb listing using pie chart.')
    #Group the data by bedrooms.
    bedrooms_group = data.groupby('bedrooms').size()
    #convert to list.
    bedrooms_group_list =bedrooms_group.index.tolist()
    #convert to list.
    bedrooms_list = bedrooms_group.tolist()
    fig = plt.figure(figsize=(10, 6))
    plt.pie(bedrooms_list ,labels=bedrooms_group_list, autopct='%1.1f%%')# display percentage on Pie chart.
    plt.title("The proportion of number of bedrooms of Airbnb")
    plt.legend(loc="best", bbox_to_anchor=(1.2, 1))
    plt.show()
    tui.completed()



  

   # In[14]:


#This function display the number of listings for each room type using bar chart
def number_listing(data):
    tui.started('Display the number of listing for each room type using bar chart')
    #Group the data by room type and get the count of names.
    listing_room_type = data.groupby('room_type')['name'].count()
    #Convert to list.
    y = listing_room_type.tolist()
    room_type_group=data.groupby('room_type').size()
    x = room_type_group.index.tolist()
    fig = plt.figure()
    plt.bar(x, y, label="Number of data")  # plotting the graph
    plt.xlabel("Room type") # create a label for x-axis
    plt.ylabel("The number of listing")  # create a label for y-axis
    plt.title("the number of listings for each room type")  # create a title for your graph
    plt.legend()  # create a legend
    plt.show()  # show the graph
    tui.completed()




# In[10]:


#This function displays the relationship between accommodates and price using scatter plot.
def relation_accommodates_price(data):
    tui.started('The relationship between accommodates and price using scatter plot.')
    fig = plt.figure(figsize=(15, 8))  #Create figure object and set up the size of figure
    #Call the function plt.scatter to display the results using scatter plot. 
    plt.scatter(data["accommodates"], data["price"], marker='D', s=100)
    plt.xlabel('Accommodates')
    plt.ylabel('Price')
    plt.title('Accommodates vs Price')#The title.
    plt.show()#Show function to show the graph.
    tui.completed()


# In[ ]:


#This function display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).

def prices_specified_years(data):
    tui.started('Airbnb prices from 2019 - 2022 using subplots.')
    #Change the host since type from string to datetime.
    data['host_since'] = pd.to_datetime(data['host_since'])
    #Filter the years to just four years from 2019 to 2022 using query.
    filter_per_year_2019 = data.query("host_since >= '2019-01-01' and host_since < '2019-12-31'")
    filter_per_year_2020 = data.query("host_since >= '2020-01-01' and host_since < '2020-12-31'")
    filter_per_year_2021 = data.query("host_since >= '2021-01-01' and host_since < '2021-12-31'")
    filter_per_year_2022 = data.query("host_since >= '2022-01-01' and host_since < '2022-12-31'")
    #Group each year by month using dt.month and get the average price using mean function.
    group_by_month_year2019=filter_per_year_2019.groupby(filter_per_year_2019.host_since.dt.month)['price'].mean() 
    group_by_month_year2020=filter_per_year_2020.groupby(filter_per_year_2020.host_since.dt.month)['price'].mean()
    group_by_month_year2021=filter_per_year_2021.groupby(filter_per_year_2021.host_since.dt.month)['price'].mean()
    group_by_month_year2022=filter_per_year_2022.groupby(filter_per_year_2022.host_since.dt.month)['price'].mean()
    #Transforme x and y to lists to display the results using index and tolist function.
    x1=group_by_month_year2019.index.tolist()
    y1=group_by_month_year2019.tolist()
    x2=group_by_month_year2020.index.tolist()
    y2=group_by_month_year2020.tolist()
    x3=group_by_month_year2021.index.tolist()
    y3=group_by_month_year2021.tolist()
    x4=group_by_month_year2022.index.tolist()
    y4=group_by_month_year2022.tolist()
    #The plt.supbplots function displays multiple graphs.
    figure, axes = plt.subplots(4,1, figsize=(17,7))#Set the number of rows and columns and the figure size.
    #Plot each graph.
    axes[0].plot(x1, y1)
    axes[1].plot(x2, y2)
    axes[2].plot(x3, y3)
    axes[3].plot(x4, y4)
    figure.suptitle("Airbnb prices from 2019 - 2022")#Set one title for the four years.
    #Set a title for each graph.
    axes[0].set(title="Average price in year19", xlabel='months year19',ylabel='prices')
    axes[1].set(title="Average price in year20", xlabel='months year20',ylabel='prices')
    axes[2].set(title="Average price in year21", xlabel='months year21',ylabel='prices')
    axes[3].set(title="Average price in year22", xlabel='months year22',ylabel='prices')
    plt.show()
    tui.completed()
   

   


      #The function displays the relation between host response and the number of reviews.
def relation_response_reviews(data):
    tui.started('The relation between host response time and the number of reviews.')
    fig = plt.figure(figsize=(15,8)) #Create figure object and set up the size of figure
    #data["host_response_rate"] is the x and data["number_of_reviews"] is the y.
    plt.scatter(data["host_response_rate"], data["number_of_reviews"], marker='D', s=100)
    plt.xlabel('host_response_rate')
    plt.ylabel('number_of_reviews')
    plt.title('host_response_rate vs number_of_reviews ')
    plt.show()
    tui.completed()            
# In[ ]:


#


