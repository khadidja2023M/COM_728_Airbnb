#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pprocess module


import tui     
import csv

#create a function to load the data from the file using the csv module.
def load_data(file_path):
    #call started function from tui module to indicate that the operation is started. 
    tui.started("Reading data from file path")
    
    try:
        with open(file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)#skip the headings
            data = [row for row in csv_reader]#list comprehension
        return data
    except IOError:
        print("Error: File not found.")


##This function ask the user to enter the id to get listings in a dictionnary based on the id entered by the user and call display_listing_by_id function from tui module to display the results in a dictionnary.                                  
def listing_by_id(data):
    
    tui.started('listing host name, description, host location and host since by ID')
    ID={}
    input_id=input('enter your ID:')
    for row in data:
        if row[0] == input_id:
            host_name = row[3]
            description = row[2]
            location = row[5]
            host_since = row[4]
            ID['host_name']=row[3]
            ID['description']=row[2]
            ID['location']=row[5]
            ID['host_since']=row[4]
    tui.display_listing_by_id(ID)
    tui.completed()
    
#This function ask the user to enter a location to get listings in a list based on the location entered by the user and call display_listing_for_specified_location function from tui module to display the results in a dictionnary.                              
def listing_for_specified_location(data):

    tui.started('Listing host name, property type, price, minimum nights, and maximum nights of all Airbnb listing for a specified location')
    location=[]
    input_location=input('enter your location:')
    for row in data:
        if row[5]==input_location:
            host_name = row[3]
            property_type = row[13]
            price = row[20]
            minimum_nights = row[21]
            maximum_nights = row[22]
            location.append(host_name)
            location.append(property_type)
            location.append(price)
            location.append(minimum_nights)
            location.append(maximum_nights)
            
    tui.display_listing_for_specified_location(location)
    tui.completed() 
    
#This function ask the user to enter property type to get listings in a dictionnary based on the property type entered by the user and call display_listing_by_proprty_type function from tui module to display the results in a dictionnary.                          
def listing_by_property_type(data):
    tui.started('listing room_type, accomodates, bathrooms, bedroom and beds by property type')
    property_type={}
    type_of_property=input('enter the property type:')
    for row in data:
        if row[13]==type_of_property:
            room_type=row[14]
            accomodates=row[15]
            bathrooms=row[16]
            bedroom=row[17]
            beds=row[18]
            property_type['room_type']=row[14]
            property_type['accomodates']=row[15]
            property_type['bathrooms']=row[16]
            property_type['bedroom']=row[17]
            property_type['beds']=row[18]
            
    tui.display_listing_by_property_type(property_type)        
    tui.completed() 
    
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
            
    tui.display_listing_by_location(Location)            
    tui.completed()
    

#this function display amenities in a list   
def popular_amenities(data):
    tui.started('display the  most popular amenities:')
    popular_amenities=data['amenities'].mode()
    print(f'the most popular amenities are:{popular_amenities.values}')
    tui.completed()
    
#this function display the average price of stay in each location.      
def average_price_location(data):
    tui.started('display average price by location:')
    average_stay_location=data.groupby(['host_location'])['price'].mean()
    print(f'The average stay in each location:\n{average_stay_location}')         
    tui.completed()      
    
#this function display the average review scores rating for each location.      
def average_review_location(data):
    tui.started('display the average review scores rating:')
    average_review_location=data.groupby(['host_location'])['review_scores_location'].mean()
    print(f'The average review rate score for each location is:\n{average_review_location}')
    tui.completed()
    
def average_price_host_is_superhost(data):
    tui.started('display average price for host is superhost:')
    average_price=data.groupby(['host_is_superhost'])['price'].mean()
    print(f"the average price of host is  not super host and host is super_host is:{average_price.values}")
    tui.completed()
                 

    
