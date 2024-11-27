#Write a program to display a user entered name followed by Good AfterNoon using input() function

'''
_a=input("enter your name :")
print("GoodMorning",_a)
'''

#write a program to fill in letter template given below with name and date

"""
_a=input("enter your name :")
_b=input("enter your date :")
letter='''Dear <|Name|>,
          You are selected!
          Date: <|Date|>'''
_c=letter.replace("<|Name|>",_a).replace("<|Date|>",_b)
print(_c)
"""

#write a program to detect double space in a string

'''
a="Kaverappa is  a good boy"
_b=a.find("  ")
print(_b)
'''

#replace the double space from problem 3 with single spaces

'''
a="Kaverappa is  a good boy"
_c=a.replace("  "," ")       #fid and replace
print(_c)
'''

#write a program to format the following letter using escape sequence characters

'''_letter="Dear Harry, this python course is nice. Thanks!"
_formatted_letter="Dear Harry,\n this python course is nice.\n\t Thanks!"

print(_formatted_letter)
'''