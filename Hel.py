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
text_choice = int(input("Which part of the text do you wish to analyze? Choose Part 1, 2 or 3: "))

selected_text = text_choice -1
final_text = TEXTS[selected_text]
print(final_text)

# if text_choice == "1":
#     text = TEXTS[0]
#     print(" ")
# elif text_choice == "2":
#     text = TEXTS[1]
#     print(" ")
# elif text_choice == "3":
#     text = TEXTS[2]
#     print(" ")


print(ODDELIT)

word_list = final_text.split()


word_list_title = []
word_list_lower = []
word_list_upper = []
word_list_number =[]


for i in word_list:

    if i.isupper():
        word_list_upper.append(i)
        UPPER = len(word_list_upper)

    elif i.isdigit():
        word_list_number.append(i)
        NUMBER = len(word_list_number)

    elif i.istitle():
        word_list_title.append(i)
        TITLE = len(word_list_title)

    elif i.islower():
        word_list_lower.append(i)
        LOWER = len(word_list_lower)


  # for a in word_list:
#     if a.isupper():
#         word_list_upper.append(a)
#     elif not a.isdigit():
#         UPPER = len(word_list_upper)

# for b in word_list:
#     if b.isdigit():
#         word_list_number.append(b)
#         NUMBER = len(word_list_number)


print(f"There are {len(word_list)} words in the chosen text.")
print(f"There are {TITLE} titlecase words in the chosen text.")
print(f"There are {UPPER} uppercase words in the chosen text.")
print(f"There are {LOWER} lowercase words in the chosen text.")
print(f"There are {NUMBER} numbers in the chosen text.")

print(ODDELIT)

delky_slov = {}
while word_list:
    slovo = word_list.pop()
    delky_slov[len(slovo)] = delky_slov.get(len(slovo), 0) +1


for klic, hodnota in delky_slov.items():
    print(hodnota, "*" * klic, klic)



for lll in range(0, len(word_list_number)):
    word_list_number[lll] = int(word_list_number[lll])
print(ODDELIT)

print(f"If we summed all the numbers in this text we would get: {sum(word_list_number)}")
