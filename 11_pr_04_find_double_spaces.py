string = "The day is very beautiful"

_find_ds = string.find("  ")
print(_find_ds)

#if result is any number that means double spaces are there
#if result is -1 then there is no double space in the statement

#_______________________________________________________________

#replace double space with single space

string = "The day is  very  beautiful  !!"

string  = string.replace("  ", " ")
print(string)
