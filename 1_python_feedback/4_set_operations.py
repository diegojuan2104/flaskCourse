friends = {"Bob","Rolf","Anne"}
abroad = {"Rolf","Anne"}

local_friends = friends.difference(abroad)
print("Difference: ",local_friends)

art = {"Mikkel","Addam","Jonas"}
science = {"Franchesca","Addam","Jonas"}

both_studies = art.intersection(science)

print("Intersection: ", both_studies)