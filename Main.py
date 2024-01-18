"""
Exercise 1 - Python, I Choose You!
By Kalina (Alice Wilder)

"""

import pandas as pd; # Importing pandas
import time; # importing time to use sleep function

# Changing Excel files to Dataframe
pokemon_df = pd.read_csv("pokemon.csv"); 
locations_df = pd.read_csv("locations.csv");
encounters_df = pd.read_csv("encounters.csv");
regions_df = pd.read_csv("regions.csv");

# cities_towns function that selects a town/route/etc. and then shows what pokemon is in that area
def cities_towns(regionNum) :
    for ct in locations_df["identifier"] :
        area = locations_df.loc[locations_df["region_id"] == regionNum, "identifier"];
        
        # prints out all the areas in the selected region
        for ar in area :
            print(ar.title().replace("-", " "));
        break;    

    locInput = input("\n> ");    
    location = locInput.lower().replace(" ", "-");
    
    locID = locations_df.loc[locations_df["identifier"] == location, "id"].iloc[0];
    
    encounter_pk = encounters_df.loc[encounters_df["location_area_id"] == locID, "encounter_slot_id"];

    print("\nList of Pokemon in", location.title().replace("-", " "), ":\n");

    # prints out all pokemon in that selected area
    for en in encounter_pk :
    
        species_pk = pokemon_df.loc[pokemon_df["species_id"] == en, "identifier"];
        
        for sp in species_pk :
            print(sp.title().replace("-", " "));

# Main Function/Method
# Welcome Message
print("Welcome to the National Pokedex!");
print("Please choose an option:\n");

choice = input("Search By:\nName\nRegion\n");
revisedChoice = choice.lower();

# if statement to determine if user is asking for name or region
if revisedChoice == "name" :
    userInput = input("\nWhat pokemon would you like to search for?\n");
    revisedInput = userInput.lower();

    # for loop to get pokemon name and its index from the excel spreadsheet
    for i in pokemon_df["identifier"] :
    
        if i == revisedInput :
            print("\nPokemon Name:", i.title());
            species = pokemon_df.loc[pokemon_df["identifier"] == revisedInput, "species_id"].iloc[0];
            print("National Dex Number:", species);
  
    #for loop to get the location area id using the species number
    for j in encounters_df["encounter_slot_id"] :
            
        if j == species : 
            encounter = encounters_df.loc[encounters_df["encounter_slot_id"] == species, "location_area_id"];

    print("Locations:\n"); # printing out the title before printing out all the locations
    time.sleep(2.7); # delays for two seconds
    
    # for loop to get the name of the locations using its location id           
    for k in encounter :
    
        locations = locations_df.loc[locations_df["id"] == k, "identifier"];
        
        # prints out all of the pokemon's locations
        for m in locations :
            print(m.title().replace("-", " "));
   
    # for loop to get max and min level & locations            
    for a in encounter :
    
        # gets all the min levels
        pk_min = encounters_df.loc[encounters_df["location_area_id"] == a, "min_level"];
    
        # gets all the max levels
        pk_max = encounters_df.loc[encounters_df["location_area_id"] == a, "max_level"];
    
        # merges encounters & locations together
        merged = pd.merge(encounters_df, locations_df, how='left', left_on='location_area_id', right_on='id')
    
        # gets the name of the location for the lowest max and highest min of the pokemon
        minName = merged.loc[merged["min_level"] == min(pk_min), "identifier"];
        maxName = merged.loc[merged["max_level"] == max(pk_max), "identifier"];
    
        # for loop used to get the one name for the lowest min
        for b in minName :

            break;
        
        # for loop used to get the one name for the highest max
        for c in maxName :
        
            break;
        break;  

    # variables used to get the lowest min and highest max levels    
    lowMin = min(pk_min);
    highMax = max(pk_max);

    # prints out the lowest min and highest max levels along with the location
    print("\nMin:", b.title().replace("-", " "), "-> Level", lowMin);
    print("Max:", c.title().replace("-", " "), "-> Level", highMax);
    
else :
    print("Please select your region:\n"); # asks user for what region they want
    
    #for loop to get list of regions
    for r in regions_df["identifier"] :
        print(r.title());
    
    regionInput = input("\n> ");
    newRegionInput = regionInput.lower();

    print("\nPlease select the area to find out what pokemon are in it:\n")
    
    # if statement to determine which region to show areas/pokemon using cities_town function
    if newRegionInput == "kanto" :
        cities_towns(1);
    
    elif newRegionInput == "johto" :
        cities_towns(2);

    elif newRegionInput == "hoenn" :
        cities_towns(3);    
    
    elif newRegionInput == "sinnoh" :
        cities_towns(4); 
    
    elif newRegionInput == "unova" :
        cities_towns(5);  
    
    elif newRegionInput == "kalos" :
        cities_towns(6); 

    elif newRegionInput == "alola" :
        cities_towns(7); 

    elif newRegionInput == "galar" :
        cities_towns(8);     

"""Sources:"""
# https://stackoverflow.com/questions/36684013/extract-column-value-based-on-another-column-in-pandas
    # This link helped me with getting data from one column and using it in another
# https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string
    # This link helped me capitalize the first letter with title()
# https://datagy.io/python-remove-character-from-string/
    # This link helped me fix the data coming out to a more user-friendly way
    # Basically getting rid of the dashes in the names and replacing them with spaces
    