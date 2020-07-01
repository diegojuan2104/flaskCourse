#Dictionarie

friend_ages = {"Rolf":22,"Adam":32,"Anne":27}

#Get dictionarie value

print(friend_ages["Rolf"])

#list of dictionaries 

friends = [
    {"name":"Rolf","age":32},
    {"name":"Pipa","age":31},
    {"name":"Adam","age":33},
    ]

#Particular value inside of list dictionarie
print(friends[1]["age"])

# all the values
for friend in friends:
    print(f"{friend}")

#better way to get values in a dictionarie it's a kind of destructuration

student_attendance = {"Rolf":83,"Bob":43,"Carl":23}

for name, attendance in student_attendance.items():
    print(f"{name}: {attendance}")