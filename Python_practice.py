print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
counties[-1]
print(counties[-1])
print(len(counties))
print(counties[0:2])
counties.append("ElPaso")
print(counties)
counties.insert(2,"ElPaso")
print(counties)

print(counties)
counties.remove("ElPaso")
print(counties)
print(counties)
counties.pop(3)
print(counties)
counties[2]="El Paso"
print(counties)
my_tuple = tuple()
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)

print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict['Arapahoe'])
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
print(voting_data)
voting_data.insert(1,({"county": "El Paso","registered_voters":461149}))
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
print(voting_data)
voting_data.remove({"county":"Denver","registered_voters":463353})
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print(voting_data)
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
# total votes in the election
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received
percentage_votes = int((my_votes / total_votes) * 100)
print("I received " + str(percentage_votes) + "% of the total votes.")
counties = ["Arapahoe", "Denver" , "Jefferson"]
if counties [1] == "Denver":
    print(counties[1])

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score=int(input("What is your test score?"))
#Determine the grade. 
if score >= 90:
    print("Your grade is an A.")
else:
    if score >=80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is an F.")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):

    print(counties[i])

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters) 


for county, voters in counties_dict.items():

    print(str(county) + " county has " + str(voters) + " registered voters.")

for county_dict in voting_data:  

     print(county_dict.values())

for county_dict in voting_data:    

   for value in county_dict:      

       print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():

    print(f"{county} county has {voters:,} registered voters.")




for county_dict in voting_data:
        print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

