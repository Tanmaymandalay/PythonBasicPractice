my_dict = {
    "Fast": "In a quick manner",    
    "Tanmay": "A coder",
    "marks": [88, 92, 79],
    "another_dict": {"Sumit": "A true friend"},
    1: 99
}

# print(my_dict)

# #dictionary methods

# print(list(my_dict.keys())) #Prints the keys of the dictionary
# print(list(my_dict.values())) #Prints the values associated to keys
# print(list(my_dict.items())) #prints the keys along with its associated values

# #update the dictionary
# update_dict = {
#     "Tejas" : "Another true friend",
#     "Sumit" : "An Inspiration"
# }

# my_dict.update(update_dict) #update the keys and associated value from update_dict
# print(list(my_dict.items()))


print(my_dict.get("Tanmay")) #Prints the value associated to asked key
print(my_dict["Tanmay"]) #Prints the value associated to asked key

#diffrence between .get() and []syntax when key is not present in the dictionary
print(my_dict.get("Tanmay2")) #Prints "None" 
print(my_dict["Tanmay2"]) #Throws error
