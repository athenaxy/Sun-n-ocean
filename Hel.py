uvod = "Hello, how're you doing?"
ODDEL = len(str(uvod)) * "-"
ODDELIT = 70 * "="

print(ODDEL)
print(uvod)
print(ODDEL)

registered = {"bob": "123",
              "ann": "pass123",
              "mike": "password123",
              "liz": "pass123"}

login = input("Please enter your login: ")
pw = input("Please enter your password: ")

print("Login: ", login)
print("Password: ", pw)

print(ODDEL)

if login in registered:
    print(f"Welcome back, {login}")
else:
    print("We didn't find you. Have you completed the registration already?")

if pw == registered.get(login):
    print("Your password is correct.")
else:
    print("You have entered an incorrect password.")
    exit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print(ODDELIT)
text_choice = int(input("Select which part of the text do you wish to analyze: part 1, 2 or 3? "))

selected_text = text_choice -1
final_text = TEXTS[selected_text]
print(final_text)

print(ODDELIT)

ocistena_slova = final_text.strip(".,:!?;-_")
words_in_text = ocistena_slova.split()


words_in_text_title = []
words_in_text_lower = []
words_in_text_upper = []
words_in_text_number =[]


for i in words_in_text:

    if i.isupper():
        words_in_text_upper.append(i)


    elif i.isdigit():
        i = int(i)
        words_in_text_number.append(i)

    elif i.istitle():
        words_in_text_title.append(i)

    elif i.islower():
        words_in_text_lower.append(i)


print(f"There are {len(words_in_text)} words in the chosen text.")
print(f"There are {len(words_in_text_title)} titlecase words in the chosen text.")
print(f"There are {len(words_in_text_upper)} uppercase words in the chosen text.")
print(f"There are {len(words_in_text_lower)} lowercase words in the chosen text.")
print(f"There are {len(words_in_text_number)} numbers in the chosen text.")

print(ODDELIT)

delky_slov = {}
while words_in_text:
    slovo = words_in_text.pop()
    delky_slov[len(slovo)] = delky_slov.get(len(slovo), 0) +1


for klic, hodnota in delky_slov.items():
    print(klic, "*" * hodnota, hodnota)


print(ODDELIT)

print(f"If we summed all the numbers in this text we would get: {sum(words_in_text_number)}")
