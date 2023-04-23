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
    print(' ')
    #empty list to store data.
    data = []
    with open(file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)#skip the headings.
        data = [row for row in csv_reader]#list comprehension to append the list data with each row.
        return data
        
#create menu function that will allow the user to retreive data 
def retrieve_menu():
    print(f"""Select which menu whoud you like:\n
    {"[1]":<6}:List name of listing, host name, description, host location, host since by host id.\n 
    {"[2]":<6}:List host name, property type, price, minimum_nights and maximum_nights by location.\n
    {"[3]":<6}:List room type, accommodates, bathrooms, bedroom and beds for a specified property type.\n
    {"[4]":<6}:List review scores of cleanliness, checkin, communication and rating by location.\n                 
    {"[5]":<6}:Go back to the main menu.""") 
    print(' ')
    menu_selection = input('Your selection : ')
    return menu_selection.strip() 
                         
#This function ask the user to enter the id to get listings in a dictionnary based on the id entered by the user and call display_listing_by_id function from tui module to display the results in a dictionnary.                  
def listing_by_id(data):
    #call started function from the tui module.
    tui.started('listing host name, description, host location and host since by ID')
    print(' ')
    #Create an empty list to store the results.
    ID=[]
    #Ask the user to enter the id .
    input_id=input('Enter the ID : ')
    print(' ')
    for row in data:
        #If the input_id equal to the id  append the list ID with host name, description, location and host since.
        if  row[0] == input_id:
            host_name = row[3]
            description = row[2]
            location = row[5]
            host_since = row[4]
            ID.append(host_name)
            ID.append(description)
            ID.append(location)
            ID.append(host_since)
    #This if statement to handle the error incase the user enters a wrong id.        
    if len(ID) != 0:#If the list is not empty display it.
        tui.display_listing_by_id(ID)#Call a function from the tui module to display the results as a dictionnary.
        print(' ')
        tui.completed()#Call the function completed from the tui module to indicate the end of the operation.
    else:
        print(' ')
        red_satrt ='\033[31m'
        red_end ='\033[0m'
        #In case the id is wrong the list is empty prints invalid ID.
        print(f"{red_satrt}Invalid ID!, please try again{red_end}")
        print(' ')
        
#This function ask the user to enter a location to get listings in a list based on the location entered by the user and call display_listing_for_specified_location function from tui module to display the results in a dictionnary.                              
def listing_for_specified_location(data):
    tui.started('Listing host name, property type, price, minimum nights, and maximum nights of all Airbnb listing for a specified location')
    print(' ')
    #Create four empty lists.
    host_name_list = []
    property_type_list = []
    price_list = []
    minimum_nights_list = []
    maximum_nights_list = []
    #Ask the user to enter the location.
    input_location = input('Enter the location : ')
    print(' ')
    #If user input equal to one of the locations.
    for row in data:
        if  row[5].lower() == input_location.lower():
            host_name = row[3] 
            property_type = row[13]
            price = row[20]
            minimum_nights = row[21]
            maximum_nights = row[22]
            #Append each list with the information needed.
            host_name_list.append(host_name)
            property_type_list.append(property_type)
            price_list.append(price)
            minimum_nights_list.append(minimum_nights)
            maximum_nights_list.append(maximum_nights)        
    location=[host_name_list, property_type_list, price_list, minimum_nights_list, maximum_nights_list]
    #If the list not empty.
    if len(host_name_list) != 0:
        location = [host_name_list, property_type_list, price_list, minimum_nights_list, maximum_nights_list]
        #For loop to get each element.
        for i in range(len(host_name_list)):
            location = [host_name_list[i], property_type_list[i], price_list[i], minimum_nights_list[i],maximum_nights_list[i]]
            tui.display_listing_for_specified_location(location) 
        print(' ')    
        tui.completed()
    else:
        print(' ')
        red_satrt ='\033[31m'
        red_end ='\033[0m'
        print(f"{red_satrt}Invalid location!, please try again{red_end}")
        print(' ')
                       
    
#This function ask the user to enter property type to get listings in a list based on the property type entered by the user and call display_listing_by_proprty_type function from tui module to display the results in a dictionnary.                          
def listing_by_property_type(data):
    tui.started('listing room type, accommodates, bathrooms, bedroom and beds by property type')
    print(' ')
    room_type_list = list()
    accommodates_list = list()
    bathrooms_list = list()
    bedroom_list = list()
    beds_list = list()
    type_of_property = input('Enter the property type : ')
    print(' ')
    for row in data:
        if  row[13].lower() == type_of_property.lower():
            room_type = row[14]
            accommodates = row[15]
            bathrooms = row[16]
            bedroom = row[17]
            beds = row[18]
            room_type_list.append(room_type)
            accommodates_list.append(accommodates)
            bathrooms_list.append(bathrooms)
            bedroom_list.append(bedroom)
            beds_list.append(beds)
    if len(room_type_list) != 0:
        property_type = [room_type_list,accommodates_list,bathrooms_list,bedroom_list,beds_list]
        for i in range(len(room_type_list)):
            property_type = [room_type_list[i], accommodates_list[i], bathrooms_list[i], bedroom_list[i], beds_list[i]]
            tui.display_listing_by_property_type(property_type)
        print('  ')
        tui.completed()
    else:
        print(' ')
        red_satrt ='\033[31m'
        red_end ='\033[0m'
        print(f"{red_satrt}Invalid property type, please try again{red_end}")
        print(' ')
                
#This function ask the user to enter location to get listings in a list based on the location entered by the user and call display_listing_by_location function from tui module to display the results in a dictionnary.             
def listing_by_location(data):
    tui.started('listing review scores of cleanliness, checkin, communication and rating : ')
    print(' ')
    review_scores_cleanliness_list = []
    review_scores_checkin_list = []
    review_scores_communication_list = []
    review_scores_rating_list = []
    input_location = input('Enter the location : ')
    print(' ')
    for row in data:    
        if  row[5].lower() == input_location.lower():
            review_scores_cleanliness = row[29]
            review_scores_checkin = row[30]
            review_scores_communication = row[31]
            review_scores_rating = row[27]
            review_scores_cleanliness_list.append(review_scores_cleanliness)
            review_scores_checkin_list.append(review_scores_checkin)
            review_scores_communication_list.append(review_scores_communication)
            review_scores_rating_list.append(review_scores_rating)
    if len(review_scores_cleanliness_list) != 0:
        Location = [review_scores_cleanliness_list,  review_scores_checkin_list, review_scores_communication_list, review_scores_rating_list]
        for i in range(len(review_scores_cleanliness_list)):
            Location = [review_scores_cleanliness_list[i],  review_scores_checkin_list[i], review_scores_communication_list[i], review_scores_rating_list[i]]
            tui.display_listing_by_location(Location)
        print(' ')    
        tui.completed()
    else:
        print(' ')
        red_satrt ='\033[31m'
        red_end ='\033[0m'
        print(f"{red_satrt}Invalid location!, please try again{red_end}")
        print(' ')


