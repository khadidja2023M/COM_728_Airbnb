#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Main module 
#Import the modules 
import tui
import retrieve        
import os    
import analyse
import plot



#The main function, which control the programme.
def run():
    #Ask the user to enter the file path.
    file_path = input("Enter the file path: ")
    #A main loop keeps looping until user enter exit in the main menu.
    running = True
    while running:
        #Call the function main menu from tui module.
        selection = tui.main_menu()
        
        if selection== 'first':
            data =[]
            #Use os to check file path , call the function load data in the retrieve module.
            #if the path exist the data will be load using csv.
            if os.path.exists(file_path):
                data=retrieve.load_data_csv(file_path)
                tui.completed()
            #Nested loop 
            running=True
            while running:
                #Call retrieve menu function from retrieve module(sub menu).
                menu_selection=retrieve.retrieve_menu()
                if  menu_selection == '1':
                    #display listing by id function called from retrieve module.
                    retrieve.listing_by_id(data)
                elif menu_selection == '2':
                    retrieve.listing_for_specified_location(data)
                elif menu_selection == '3':
                    retrieve.listing_by_property_type(data)
                elif menu_selection == '4':
                    retrieve.listing_by_location(data)
                elif menu_selection == 'exit':
                    #If the user enter exit the loop will stop.
                    break
                #The error function called from the tui module to handle the error in case the user
                #enter someting different than the options.
                else:
                    tui.error()
                
            #If file path entered from the user dosen't exist print envalid file path.    
            else: 
                print('envalid file path')
            
        #Second option of the main loop.            
        elif selection=='second':
            #Use load data function from analyse module using pandas.
            data=analyse.load_data_pandas(file_path)
            tui.completed()
            #Nested loop 
            running=True
            while running:
                #Call retrieve menu function from retieve module(sub menu).
                menu_selection = analyse.analyse_menu()
                if menu_selection == '1':
                    analyse.popular_amenities(data)
                elif menu_selection == '2':
                    analyse.average_price_location(data)
                elif menu_selection == '3':
                    analyse.average_review_location(data)
                elif menu_selection == '4':
                    analyse.average_price_host_is_superhost(data)
                elif menu_selection == 'exit':
                
                    break
                else:
                    tui.error()
        #Third  option of the main loop.           
        elif selection=='third':        
            data=analyse.load_data_pandas(file_path)
            tui.completed()
            running=True
            while running:
                menu_selection = plot.plot_menu()
                if menu_selection == '1':
                    plot.number_bedrooms(data)
                elif menu_selection == '2':
                    plot.number_listing(data)
                elif menu_selection == '3':
                    plot.relation_accommodates_price(data)
                elif menu_selection == '4':
                    plot.prices_specified_years(data)
                elif menu_selection == '5':
                    plot.relation_response_reviews(data)
                elif menu_selection == 'exit':
                    break
                else:
                    tui.error()
        #If the user enter exit the main loop will stop, so the programme will stop.            
        elif selection == 'exit':
            break
        else:
            tui.error()
            
         
   
            

if __name__== "__main__":
    
#Call run fonction to run the programme.
    run()




# In[5]:


import pandas as pd
data=pd.read_csv('Airbnb_UK_2022.csv')
data.head(5)


# In[ ]:


data['host_since'][0]


# In[ ]:


int(data['host_since'][0][-2:])


# In[ ]:


data['year']=data['host_since'].apply(lambda x: x[-2:]).astype('int')


# In[ ]:


new_data=data[data['year'].between(19,22)]


# In[ ]:


new_data.head()


# In[ ]:


x=new_data['year']
x


# In[ ]:


year19=new_data.loc[new_data.year ==19, ['year','price']]
year19


# In[ ]:


year20=new_data.loc[new_data.year ==20, ['year','price']]
year20


# In[ ]:


year21=new_data.loc[new_data.year ==21, ['year','price']]
year21


# In[ ]:


year22=new_data.loc[new_data.year ==22, ['year','price']]
year22


# In[ ]:


x1=year19.groupby('year').size().sort_values(ascending=False)

x1


# In[ ]:


year_group=year19.groupby('year').size()
print(type(year19))


# In[ ]:


y1=year19['price']
y1


# In[ ]:


data19=new_data[new_data['year'] == 19]


# In[ ]:


data20=new_data[new_data['year'] == 20]


# In[ ]:


data21=new_data[new_data['year'] == 21]


# In[ ]:


data22=new_data[new_data['year'] == 22]
data22.head(3)


# In[ ]:


data19['price']


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

def prices_specified_years():
    data['host_since'][0]
    int(data['host_since'][0][-2:])
    data['year']=data['host_since'].apply(lambda x: x[-2:]).astype('int')
    new_data=data[data['year'].between(19,22)]
    year19=new_data.loc[new_data.year ==19, ['year','price']]
    
    data21=new_data[new_data['year'] == 21]
    data22=new_data[new_data['year'] == 22]
    figure, axes= plt.subplots(1,4, figsize=(10,5))

    axes[0].plot(data19['year'], data19['price'])
    axes[1].plot(data20['year'], data20['price'])
    axes[2].plot(data21['year'], data21['price'])
    axes[3].plot(data22['year'], data22['price'])
    plt.show()   
prices_specified_years()    


# In[ ]:





# In[ ]:




