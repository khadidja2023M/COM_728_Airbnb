#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tui module

#Create a starting function that will indicate the start of the programme.
def started(msg=""):  
    dashes=('#')*75
    print(dashes)
    print(f"Operation started: {msg}...\n")
    
#Create a completed function that will indicate the end of the programme.    
def completed():
    print("Operation completed.")
    dashes=('#')*75
    print(dashes)
#Create a main menu to give the user a chance to choose what he wants to do.    
def main_menu():
    print(f"""select which menu would you like:
    {"[first]":<6}:Retrieve data.\n   
    {"[second]":<6}:Analyse data.\n
    {"[third]":<6}:visualise data.\n
    {"[exit]":<6}:Exit the programme.""")
    #Input for the user to enter his selection.
    selection=input('your selection: ')
    # strip and lower if the user unter capital letter and strip to remove the spaces. 
    return selection.strip().lower() 
                  

#error function to handle the errors.
def error():  
        print("Invalid Selection!")

#this function display the results of the function listing by id in the retrieve module as a dictionnary.       
def display_listing_by_id(ID):
    print(f"host name:{ID[0]}\ndescription:{ID[1]}\nhost location:{ID[2]}\nhost since:{ID[3]}")
    
#this function display the results of the function listing for specified location in the retrieve module as a dictionnary.       
def display_listing_for_specified_location(location):
    print(f"host name:{location[0]}\nproperty type:{location[1]}\nprice:{location[2]}\nminimum nights:{location[3]}\nmaximum nights:{location[4]}") 
    
#this function display the results of the function listing by property type in the retrieve module as a dictionnary.   
def display_listing_by_property_type(property_type):
    print(f"room type:{property_type[0]}\naccommodates:{property_type[1]}\nbathrooms:{property_type[2]}\nbedroom:{property_type[3]}\nbeds:{property_type[4]}")




#this function display the results of the function listing by location in the retrieve module as a dictionnary.            
def display_listing_by_location(Location):
    print(f"review scores cleanliness:{Location[0]}\nreview scores communication:{Location[1]}\nreview scores checkin:{Location[2]}\nreview scores rating:{Location[3]}") 
                    

