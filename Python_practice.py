
#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
 #   print('Your grade is an A.')
#else:
#    if score >= 80:
#        print('Your grade is a B.')
#    else:
 #       if score >= 70:
  #          print('Your grade is a C.')
   #     else:
    #        if score >= 60:
     #           print('Your grade is a D.')
      #      else:
       #         print('Your grade is an F.')


counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not the list of counties.")


for county in counties:
        print(county)


#The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. The letter i is often used for simplicity, but any variable can be used.
#Inside the range() function, we get the length of the list of counties, which is the integer 3.
#Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
#This process is continued until all three items, or counties, in the list are printed to the screen.

for i in range(len(counties)):
    print(counties[i])

#getting the keys and values from a dictionary using a for loop
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict:
    #print(county)

#When we use the items() method, we get the key and the value for each dictionary by referencing them as "key" and "value" as in the code above, or we can reference them by name, like "county" and "voters"
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(county, voters)

    print(county," county has", voters, "registered voters.")

#Iterate Through a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)