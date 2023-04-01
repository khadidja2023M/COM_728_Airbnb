#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#retrieve module

import os
import tui     
import csv

#create a function to load the data from the file using the csv module.
def load_data_csv(file_path):
    #call started function from tui module to indicate that the operation is started. 
    tui.started("Reading data from file path using csv module.")
    #Use tray and except to handle the error.
    
    with open(file_path, encoding='utf-8')as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)#skip the headings
        data = [row for row in csv_reader]#list comprehension
        return data

        
#create menu function that will allow the user to retreive data 
def retrieve_menu():
    
    print(f"""select which menu whoud you like:
    
    {"[1]":<6}:List name of listing, host name, description, host location, host since by host id.\n 
    
    {"[2]":<6}:List host name, property type, price, minimum_nights and maximum_nights by location.\n
    
    {"[3]":<6}:List room type, accommodates, bathrooms, bedroom and beds for a specified property type.\n
    
    {"[4]":<6}:List review scores of cleanliness, checkin, communication and rating by location.\n                 
    
    {"[exit]":<6}:Exit the programme.
    """)
          
      
    menu_selection=input('your selection: ')
    return menu_selection.strip().lower() 
        

                 
##This function ask the user to enter the id to get listings in a dictionnary based on the id entered by the user and call display_listing_by_id function from tui module to display the results in a dictionnary.                                  
def listing_by_id(data):
    
    tui.started('listing host name, description, host location and host since by ID')
    ID=[]
    input_id=input('enter your ID:')
    
    for row in data:
        if row[0] == input_id:
            host_name = row[3]
            description = row[2]
            location = row[5]
            host_since = row[4]
            ID.append(host_name)
            ID.append(description)
            ID.append(location)
            ID.append(host_since)
            
    if len(ID)!=0:
        tui.display_listing_by_id(ID)
        tui.completed()
    else:
        print('Invalid ID')
#This function ask the user to enter a location to get listings in a list based on the location entered by the user and call display_listing_for_specified_location function from tui module to display the results in a dictionnary.                              
def listing_for_specified_location(data):
    tui.started('Listing host name, property type, price, minimum nights, and maximum nights of all Airbnb listing for a specified location')
    location=[]
    input_location=input('enter your location:')
    
    for row in data:
        if row[5]==input_location:
            host_name=row[3] 
            property_type=row[13]
            price=row[20]
            minimum_nights=row[21]
            maximum_nights=row[22]
            location.append(host_name)
            location.append(property_type)
            location.append(price)
            location.append(minimum_nights)
            location.append(maximum_nights)
    if len(location)!=0:
        tui.display_listing_for_specified_location(location)  
        tui.completed()
    else:
        print('Invalid location')             
                    
    
    
#This function ask the user to enter property type to get listings in a list based on the property type entered by the user and call display_listing_by_proprty_type function from tui module to display the results in a dictionnary.                          
def listing_by_property_type(data):
    tui.started('listing room type, accommodates, bathrooms, bedroom and beds by property type')
    property_type=[]
    type_of_property=input('enter the property type:')
    for row in data:
        if row[13]==type_of_property:
            room_type=row[14]
            accommodates=row[15]
            bathrooms=row[16]
            bedroom=row[17]
            beds=row[18]
            property_type.append(room_type)
            property_type.append(accommodates)
            property_type.append(bathrooms)
            property_type.append(bedroom)
            property_type.append(beds)
    if len(property_type)!=0:
        tui.display_listing_by_property_type(property_type)   
        tui.completed()
    else:
        print('Invalid property type')             
            
    
    
#This function ask the user to enter location to get listings in a list based on the location entered by the user and call display_listing_by_location function from tui module to display the results in a dictionnary.             
def listing_by_location(data):
    tui.started('listing review scores of cleanliness, checkin, communication and rating : ')
    Location=[]
    input_location=input('enter your location:') 
    for row in data:
        if row[5]==input_location:
            review_scores_cleanliness=row[29]
            review_scores_checkin=row[30]
            review_scores_communication=row[31]
            review_scores_rating=row[27]
            Location.append(review_scores_cleanliness)
            Location.append(review_scores_checkin)
            Location.append(review_scores_communication)
            Location.append(review_scores_rating)
    if len(Location)!=0:
        tui.display_listing_by_location(Location)
        tui.completed()
    else:
        print('Invalid location')        
    

    

            
            
            
           

