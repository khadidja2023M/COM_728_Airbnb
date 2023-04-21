#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tui module

#Create a starting function that will indicate the start of the programme.
def started(msg = ""): 
    #Display a line of dashes for separation.
    #The code \033[1;34 and \033[0m to display the dashes in bleu colour. 
    dashes = ('\033[1;34m#\033[0m')*85
    print(dashes)
    print(f"Operation started: {msg}...\n")
    
#Create a completed function that will indicate the end of the programme.    
def completed():
    print("Operation completed.")
    dashes = ('\033[1;34m#\033[0m')*85
    print(dashes)
    
#Create a main menu to give the user a chance to choose what he wants to do.    
def main_menu():
    print(f"""Please select which menu would you like:\n
    {"[first]":<6} : Retrieve data.\n   
    {"[second]":<6} : Analyse data.\n
    {"[third]":<6} : visualise data.\n
    {"[exit]":<6} : Exit the programme.""")
    print('  ')
    #Input for the user to enter his selection.
    selection = input('Your selection: ')
    #lower if the user enter capital letter and strip to remove the spaces. 
    return selection.strip().lower() 
                  
#error function to handle the errors.
def error():
        #The code \033[31m and \033[0m are used to change the colour of the print function to red.
        red_satrt ='\033[31m'
        red_end ='\033[0m'
        print(f"{red_satrt}Invalid Selection!{red_end}")
        print(' ')

#this function display the results of the function listing by id in the retrieve module as a dictionnary.       
def display_listing_by_id(ID):
    #The code \033[1;30m and \033[0m are used to change the headings to dark black color. 
    print(f"\033[1;30mHost name\033[0m : {ID[0]}\n\033[1;30mDescription\033[0m : {ID[1]}\n\033[1;30mHost location\033[0m : {ID[2]}\n\033[1;30mHost since\033[0m : {ID[3]}")
    
#this function display the results of the function listing for specified location in the retrieve module as a dictionnary.       
def display_listing_for_specified_location(location):
    print(f"\033[1;30mHost name\033[0m : {location[0]}\n\033[1;30mProperty type\033[0m : {location[1]}\n\033[1;30mPrice\033[0m : {location[2]}\n\033[1;30mMinimum nights\033[0m : {location[3]}\n\033[1;30mMaximum nights\033[0m : {location[4]}\n") 
    print('-'*50)
    
#this function display the results of the function listing by property type in the retrieve module as a dictionnary.   
def display_listing_by_property_type(property_type):
    print(f"\033[1;30mRoom type\033[0m : {property_type[0]}\n\033[1;30mAccommodates\033[0m : {property_type[1]}\n\033[1;30mBathrooms\033[0m : {property_type[2]}\n\033[1;30mBedroom\033[0m : {property_type[3]}\n\033[1;30mBeds\033[0m : {property_type[4]}\n")
    print('-'*50)

#this function display the results of the function listing by location in the retrieve module as a dictionnary.            
def display_listing_by_location(Location):
    print(f"\033[1;30mReview scores cleanliness\033[0m : {Location[0]}\n\033[1;30mReview scores communication\033[0m : {Location[1]}\n\033[1;30mReview scores checkin\033[0m : {Location[2]}\n\033[1;30mReview scores rating\033[0m : {Location[3]}\n") 
    print('-'*50)
                    

