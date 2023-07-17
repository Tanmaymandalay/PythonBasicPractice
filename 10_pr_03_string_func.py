letter = ''' Dear <|Name|>,
Congratulations!! You are selected. Your joining date is <|Date|>'''

name = input("Enter you Name: ")
date = input("Enter date: ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)