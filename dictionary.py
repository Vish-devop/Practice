#Trying out key-value pairs: 
programming_dict={
    "Bug": "An error in a program that prevents from running as expected",
    "Function": "A peice of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

#Retrievning items from dict.
# print(programming_dict["Function"])

#Adding new items to dict.
programming_dict["positive"]="Code is working great."
# print(programming_dict)

#creating an emptu dict.
empty_dict={}
print(empty_dict)

#Editing an item inside dict.
programming_dict["positive"]="You should be positive every time"
# print(programming_dict)

#Looping through the dictionary
for key in programming_dict:
    print(key)  #By defaulyt loops inside dict. would return KEYS().
    print(programming_dict[key])
    print(f"{key}:{programming_dict[key]}")