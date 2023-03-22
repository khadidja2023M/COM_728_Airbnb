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
    
def main_menu():
    
    print(f"""select which menu whoud you like:
    
    {"[first]":<6}:Retrieve data.\n 
    
    {"[second]":<6}:Analyse data.\n
    
    {"[third]":<6}:visualise data.\n
    
    {"[exit]":<6}:Exit the programme.
    """)
          
      
    selection=input('your selection: ')
    return selection.strip().lower() 
                  

#error function
def error():  
        print("Invalid Selection!")

#this function display the results of the function listing by id in the process module as a dictionnary.       
def display_listing_by_id(ID):
    print(f"host name:{ID['host_name']}\ndescription:{ID['description']}\nhost location:{ID['location']}\nhost   since:{ID['host_since']}")
    
#this function display the results of the function listing for specified location in the process module as a dictionnary.       
def display_listing_for_specified_location(location):
    print(f"host name:{location[0]}\nproperty type:{location[1]}\nprice:{location[2]}\nminimum nights:{location[3]}\nmaximum nights:{location[4]}") 
    
#this function display the results of the function listing by property type in the process module as a dictionnary.   
def display_listing_by_property_type(property_type):
    print(f"room type:{property_type['room_type']}\naccomodates:{property_type['accomodates']}\nbathrooms:{property_type['bathrooms']}\nbedroom:{property_type['bedroom']}\nbeds:{property_type['beds']}")                             
#this function display the results of the function listing by location in the process module as a dictionnary.                
def display_listing_by_location(Location):
    print(f"review scores cleanliness:{Location[0]}\nreview scores communication:{Location[1]}\nreview scores checkin:{Location[2]}\nreview scores rating:{Location[3]}") 
                    

