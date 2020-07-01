users = [
    (0,"Bob","password"),
    (1,"Ed","123"),
    (2,"Eddie","md5"),
]

#list of the name keys
username_mapping = {user[1]: user for user in users}

print(username_mapping["Bob"])

