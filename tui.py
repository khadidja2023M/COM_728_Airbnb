#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tui module

#create a starting function that will indicate the start of the programme
def started(msg=""):  
    dashes=('#')*75
    print(dashes)
    print(f"Operation started: {msg}...\n")

    
#create a completed function that will indicate the end of the programme
def completed():
    print("Operation completed.")
    dashes=('#')*75
    print(dashes)


#create menu function that will allow the user to retreive data 
def menu():


    print(f"""select which menu would you like:
    
    {"[1]":<6}:List name of listing, host name, description, host location, host since by host id.\n 
    
    {"[2]":<6}:List host name, property type, price, minimum_nights and maximum_nights by location.\n
    
    {"[3]":<6}:List room type, accommodates, bathrooms, bedroom and beds for a specified property type.\n
    
    {"[4]":<6}:List review scores of cleanliness, checkin, communication and rating by location.\n                 
    
    {"[exit]":<6}:Exit the programme.
    """)
          
      
    menu_selection=input('your selection: ')
    return menu_selection.strip().lower() 
          

#error function
def error():  
    print("Invalid Selection!")

#this function display the results of the function listing by id in the process module as a dictionnary.       
def display_listing_by_id(ID):
    print(f"host_name:{ID['host_name']}\ndescription:{ID['description']}\nhost_location:{ID['location']}\nhost_since:{ID['host_since']}")
    
#this function display the results of the function listing for specified location in the process module as a dictionnary.       
def display_listing_for_specified_location(location):
    print(f"host name:{location[0]}\nproperty type:{location[1]}\nprice:{location[2]}\nminimum nights:{location[3]}\nmaximum nights:{location[4]}") 
    
#this function display the results of the function listing by property type in the process module as a dictionnary.   
def display_listing_by_property_type(property_type):
    print(f"room type:{property_type['room_type']}\naccomodates:{property_type['accomodates']}\nbathrooms:{property_type['bathrooms']}\nbedroom:{property_type['bedroom']}\nbeds:{property_type['beds']}")                             
#this function display the results of the function listing by location in the process module as a dictionnary.                
def display_listing_by_location(Location):
    print(f"review_scores_cleanliness:{Location[0]}\nreview_scores_communication:{Location[1]}\nreview_scores_checkin:{Location[2]}\nreview_scores_rating:{Location[3]}") 
                    