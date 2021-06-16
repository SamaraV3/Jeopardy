from tkinter import *
from functools import partial

root = Tk()

# First I should make buttons
# Which means I should create categories first lol
root.title("Jeopardy!!")
root["bg"] = "#e8e8e8"
game = LabelFrame(root, padx=10, pady=10, bg="#5ec9ff")
game.grid(row=0, column=0, padx=5, pady=10)

label_food = Label(game, text="Foods", height=1, width=9, pady=30, borderwidth=5, font=("Comic Sans MS", 25, "normal", "italic"), bg="#5ec9ff")
label_pop_culture = Label(game, text="Pop Culture", height=1, width=9, pady=30, borderwidth=5, font=("Comic Sans MS", 25, "normal", "italic"), bg="#5ec9ff")
label_literature = Label(game, text="Literature", height=1, width=9, pady=30, borderwidth=5, font=("Comic Sans MS", 25, "normal", "italic"), bg="#5ec9ff")
label_capitals = Label(game, text="Capitals", height=1, width=9, pady=30, borderwidth=5, font=("Comic Sans MS", 25, "normal", "italic"), bg="#5ec9ff")
label_fun_facts = Label(game, text="Fun Facts", height=1, width=9, pady=30, borderwidth=5, font=("Comic Sans MS", 25, "normal", "italic"), bg="#5ec9ff")

label_food.grid(row=0, column=0)
label_pop_culture.grid(row=0, column=1)
label_literature.grid(row=0, column=2)
label_capitals.grid(row=0, column=3)
label_fun_facts.grid(row=0, column=4)

#All my methods. rip me
#Also all my python code. Why do I torture myself lol
#Foods
f_questions = ["Fill in the blank: An _____ a day keeps the doctor away", "Zuppa is Italian for this dish",
               "This nut, from the state tree of Texas is a southern pie staple",
               "Orange butter sauce doused in grand marnier and prepared in a chafing dish, it's flame on for this crepe dish!",
               "Which of the following fruits is not technically a berry"]
f_correct_answers = ["Apple", "Soup", "Pecan", "Crepe Suzette", "Strawberries"]
f_answers = [ ["Pomegranate", "Orange", "Apple", "Banana"],
              ["Soup", "Salsa", "Ambrosia", "Guacamole"],
              ["Walnut", "Pecan", "Almond", "Hickory nut"],
              ["Crepe Suzette", "Crepe Louis", "Crepe Marie", "Crepe Antoinette"],
              ["Bananas", "Strawberries", "Cranberries", "Avocados"] ]

#Pop Culture
pc_questions = ["Who originally sings the song \"Say So\"",
                "Which avenger other than Captain America was able to pick up Thor's Mjolnir in the marvel movies",
                "Who is the oldest Kardashian sister?",
                "Which Emmy Award-winning producer was behind Glee, Hollywood, The Politician and American Horror Story?",
                "Which famous american pop band was originally called \"Kara's Flowers'\""]
pc_correct_answers = ["Doja Cat", "Vision", "Kourtney", "Ryan Murphy", "Maroon 5"]
pc_answers = [ ["Saweetie", "Doja Cat", "Cardi B", "Megan Thee Stallion"],
                ["Vision", "Iron Man", "Scarlet Witch", "Black Widow"],
                ["Kim", "Khloe", "Kendall", "Kourtney"],
                ["David E. Kelly", "Ryan Murphy", "James L. Brooks", "Lorne Michaels"],
                ["Maroon 5", "Backstreet Boys", "NSYNC", "Boyz II Men"] ]

#Literature
l_questions = ["Who is the author of \"The Iliad\" and \"The Odyssey\"", "\"Don Quixote\" was written in what language?",
               "Who is the heroine of Nathaniel Hawthorne's \"The Scarlet Letter\"",
               "Put the three cantos of \"The Divine Comedy\" in the correct order.",
               "This poet, who is associated with Romanticism, wrote \"Songs of Innocence and Experience\""]
l_correct_answers = ["Homer", "Spanish", "Hester Prynne", "Inferno, Purgatorio, Paradiso", "William Blake"]
l_answers = [ ["Euripides", "Homer", "Beowulf", "Virgil"],
              ["Old English", "Italian", "Spanish", "Greek"],
              ["Anne Hutchinson", "Hester Prynne", "Scarlett O'Hara", "Elizabeth Bennet"],
              ["Paradiso, Purgatorio, Inferno", "Inferno, Limbo, Paradiso", "Purgatorio, Inferno, Limbo", "Inferno, Purgatorio, Paradiso"],
              ["William Blake", "John Keats", "Percy Bysshe Shelley", "Mary Shelley"] ]

#Capitals
c_questions = ["What is the capital of Mexico?", "What is the capital of the U.S?", "What is the capital of Canada",
               "What is the capital of Australia?", "What is the capital of Morocco?"]
c_correct_answers = ["Mexico City", "Washington DC", "Ottawa", "Canberra", "Rabat"]
c_answers = [ ["Cancun", "Mexico City", "Oaxaca", "Guadalajara"],
              ["Albany", "Washington DC", "Los Angeles", "Las Vegas"],
              ["Ottawa", "Toronto", "Quebec City", "Calgary"],
              ["Canberra", "Brisbane", "Perth", "Melbourne"],
              ["Casablanca", "Marrakesh", "Fes", "Rabat"] ]

#Fun Facts
ff_questions = ["How much is a \"Baker's Dozen\"?", "What is the fear of the number 13 called?",
                "What is the order of the 5 NYC boroughs by smallest to largest population number?",
               "In which state was the first Target opened?", "What is the name of the \"#\" symbol?"]
ff_correct_answers = ["13", "Triskaidekaphobia", "Staten Island, Bronx, Manhattan, Queens, Brooklyn", "Minnesota", "Octothorpe"]
ff_answers = [ ["13", "12", "14", "11"],
              ["Coulrophobia", "Triskaidekaphobia", "Gephyrophobia", "Paraskevidekatriaphobia"],
              ["Staten Island, Queens, Bronx, Manhattan, Brooklyn", "Bronx, Staten Island, Manhattan, Queens, Brooklyn",
               "Staten Island, Bronx, Manhattan, Brooklyn, Queens", "Staten Island, Bronx, Manhattan, Queens, Brooklyn"],
              ["California", "Minnesota", "Colorado", "Texas"],
              ["Lozenge", "Circumflex", "Ampersand", "Octothorpe"] ]


#index1 is the index of the question. index2 is the index of the answer
def setFoodAnswer(index1, index2, answer):
    global packRow
    if index2 == 0:
        a1["state"] = DISABLED
    elif index2 == 1:
        a2["state"] = DISABLED
    elif index2 == 2:
        a3["state"] = DISABLED
    elif index2 == 3:
        a4["state"] = DISABLED
    packRow = 10
    inc = Label(top, text="Incorrect!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    cor = Label(top, text="Correct!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    if answer != f_correct_answers[index1]:
        cor.grid_forget()
        inc.grid(row=packRow, column=0)
    else:
        inc.grid_forget()
        cor.grid(row=packRow + 1, column=0)


def foodQ (index):
    #Prints out question (and sets global variables)
    global top
    global a1
    global a2
    global a3
    global a4
    top = Toplevel(bg="#5ec9ff")
    question = Label(top, text=f_questions[index], wraplength=510, pady=80, font=("Comic Sans MS", 15, "normal", "italic"), bg="#5ec9ff")
    question.grid(row=0, column=0)
    #Then the answers
    a1 = Button(top, text=f_answers[index][0], height=4, width=70, command=partial(setFoodAnswer, index, 0, f_answers[index][0]), bg="#82d5ff")
    a2 = Button(top, text=f_answers[index][1], height=4, width=70, command=partial(setFoodAnswer, index, 1, f_answers[index][1]), bg="#82d5ff")
    a3 = Button(top, text=f_answers[index][2], height=4, width=70, command=partial(setFoodAnswer, index, 2, f_answers[index][2]), bg="#82d5ff")
    a4 = Button(top, text=f_answers[index][3], height=4, width=70, command=partial(setFoodAnswer, index, 3, f_answers[index][3]), bg="#82d5ff")
    a1.grid(row=1, column=0)
    a2.grid(row=2, column=0)
    a3.grid(row=3, column=0)
    a4.grid(row=4, column=0)
    #Disables pressed button
    if index == 0:
        f1["state"] = DISABLED
        f1["text"] = ""
        f1["relief"] = "groove"
    elif index == 1:
        f2["state"] = DISABLED
        f2["text"] = ""
        f2["relief"] = "groove"
    elif index == 2:
        f3["state"] = DISABLED
        f3["text"] = ""
        f3["relief"] = "groove"
    elif index == 3:
        f4["state"] = DISABLED
        f4["text"] = ""
        f4["relief"] = "groove"
    elif index == 4:
        f5["state"] = DISABLED
        f5["text"] = ""
        f5["relief"] = "groove"


def setPCAnswer(index1, index2, answer):
    global packRow
    if index2 == 0:
        a1["state"] = DISABLED
    elif index2 == 1:
        a2["state"] = DISABLED
    elif index2 == 2:
        a3["state"] = DISABLED
    elif index2 == 3:
        a4["state"] = DISABLED
    packRow = 10
    inc = Label(top, text="Incorrect!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    cor = Label(top, text="Correct!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    if answer != pc_correct_answers[index1]:
        cor.grid_forget()
        inc.grid(row=packRow, column=0)
    else:
        inc.grid_forget()
        cor.grid(row=packRow + 1, column=0)


def pcQ (index):
    #Prints out question (and sets global variables)
    global top
    global a1
    global a2
    global a3
    global a4
    top = Toplevel(bg="#5ec9ff")
    question = Label(top, text=pc_questions[index], wraplength=510, pady=80, font=("Comic Sans MS", 15, "normal", "italic"), bg="#5ec9ff")
    question.grid(row=0, column=0)
    #Then the answers
    a1 = Button(top, text=pc_answers[index][0], height=4, width=70, command=partial(setPCAnswer, index, 0, pc_answers[index][0]), bg="#82d5ff")
    a2 = Button(top, text=pc_answers[index][1], height=4, width=70, command=partial(setPCAnswer, index, 1, pc_answers[index][1]), bg="#82d5ff")
    a3 = Button(top, text=pc_answers[index][2], height=4, width=70, command=partial(setPCAnswer, index, 2, pc_answers[index][2]), bg="#82d5ff")
    a4 = Button(top, text=pc_answers[index][3], height=4, width=70, command=partial(setPCAnswer, index, 3, pc_answers[index][3]), bg="#82d5ff")
    a1.grid(row=1, column=0)
    a2.grid(row=2, column=0)
    a3.grid(row=3, column=0)
    a4.grid(row=4, column=0)
    #Disables pressed button
    if index == 0:
        pc1["state"] = DISABLED
        pc1["text"] = ""
        pc1["relief"] = "groove"
    elif index == 1:
        pc2["state"] = DISABLED
        pc2["text"] = ""
        pc2["relief"] = "groove"
    elif index == 2:
        pc3["state"] = DISABLED
        pc3["text"] = ""
        pc3["relief"] = "groove"
    elif index == 3:
        pc4["state"] = DISABLED
        pc4["text"] = ""
        pc4["relief"] = "groove"
    elif index == 4:
        pc5["state"] = DISABLED
        pc5["text"] = ""
        pc5["relief"] = "groove"


def setLitAnswer(index1, index2, answer):
    global packRow
    if index2 == 0:
        a1["state"] = DISABLED
    elif index2 == 1:
        a2["state"] = DISABLED
    elif index2 == 2:
        a3["state"] = DISABLED
    elif index2 == 3:
        a4["state"] = DISABLED
    packRow = 10
    inc = Label(top, text="Incorrect!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    cor = Label(top, text="Correct!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    if answer != l_correct_answers[index1]:
        cor.grid_forget()
        inc.grid(row=packRow, column=0)
    else:
        inc.grid_forget()
        cor.grid(row=packRow + 1, column=0)


def litQ (index):
    #Prints out question (and sets global variables)
    global top
    global a1
    global a2
    global a3
    global a4
    top = Toplevel(bg="#5ec9ff")
    question = Label(top, text=l_questions[index], wraplength=510, pady=80, font=("Comic Sans MS", 15, "normal", "italic"), bg="#5ec9ff")
    question.grid(row=0, column=0)
    #Then the answers
    a1 = Button(top, text=l_answers[index][0], height=4, width=70, command=partial(setLitAnswer, index, 0, l_answers[index][0]), bg="#82d5ff")
    a2 = Button(top, text=l_answers[index][1], height=4, width=70, command=partial(setLitAnswer, index, 1, l_answers[index][1]), bg="#82d5ff")
    a3 = Button(top, text=l_answers[index][2], height=4, width=70, command=partial(setLitAnswer, index, 2, l_answers[index][2]), bg="#82d5ff")
    a4 = Button(top, text=l_answers[index][3], height=4, width=70, command=partial(setLitAnswer, index, 3, l_answers[index][3]), bg="#82d5ff")
    a1.grid(row=1, column=0)
    a2.grid(row=2, column=0)
    a3.grid(row=3, column=0)
    a4.grid(row=4, column=0)
    #Disables pressed button
    if index == 0:
        l1["state"] = DISABLED
        l1["text"] = ""
        l1["relief"] = "groove"
    elif index == 1:
        l2["state"] = DISABLED
        l2["text"] = ""
        l2["relief"] = "groove"
    elif index == 2:
        l3["state"] = DISABLED
        l3["text"] = ""
        l3["relief"] = "groove"
    elif index == 3:
        l4["state"] = DISABLED
        l4["text"] = ""
        l4["relief"] = "groove"
    elif index == 4:
        l5["state"] = DISABLED
        l5["text"] = ""
        l5["relief"] = "groove"


def setCapAnswer(index1, index2, answer):
    global packRow
    if index2 == 0:
        a1["state"] = DISABLED
    elif index2 == 1:
        a2["state"] = DISABLED
    elif index2 == 2:
        a3["state"] = DISABLED
    elif index2 == 3:
        a4["state"] = DISABLED
    packRow = 10
    inc = Label(top, text="Incorrect!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    cor = Label(top, text="Correct!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    if answer != c_correct_answers[index1]:
        cor.grid_forget()
        inc.grid(row=packRow, column=0)
    else:
        inc.grid_forget()
        cor.grid(row=packRow + 1, column=0)


def capitalQ (index):
    #Prints out question (and sets global variables)
    global top
    global a1
    global a2
    global a3
    global a4
    top = Toplevel(bg="#5ec9ff")
    question = Label(top, text=c_questions[index], wraplength=510, pady=80, font=("Comic Sans MS", 15, "normal", "italic"), bg="#5ec9ff")
    question.grid(row=0, column=0)
    #Then the answers
    a1 = Button(top, text=c_answers[index][0], height=4, width=70, command=partial(setCapAnswer, index, 0, c_answers[index][0]), bg="#82d5ff")
    a2 = Button(top, text=c_answers[index][1], height=4, width=70, command=partial(setCapAnswer, index, 1, c_answers[index][1]), bg="#82d5ff")
    a3 = Button(top, text=c_answers[index][2], height=4, width=70, command=partial(setCapAnswer, index, 2, c_answers[index][2]), bg="#82d5ff")
    a4 = Button(top, text=c_answers[index][3], height=4, width=70, command=partial(setCapAnswer, index, 3, c_answers[index][3]), bg="#82d5ff")
    a1.grid(row=1, column=0)
    a2.grid(row=2, column=0)
    a3.grid(row=3, column=0)
    a4.grid(row=4, column=0)
    #Disables pressed button
    if index == 0:
        c1["state"] = DISABLED
        c1["text"] = ""
        c1["relief"] = "groove"
    elif index == 1:
        c2["state"] = DISABLED
        c2["text"] = ""
        c2["relief"] = "groove"
    elif index == 2:
        c3["state"] = DISABLED
        c3["text"] = ""
        c3["relief"] = "groove"
    elif index == 3:
        c4["state"] = DISABLED
        c4["text"] = ""
        c4["relief"] = "groove"
    elif index == 4:
        c5["state"] = DISABLED
        c5["text"] = ""
        c5["relief"] = "groove"


def setFFAnswer(index1, index2, answer):
    global packRow
    if index2 == 0:
        a1["state"] = DISABLED
    elif index2 == 1:
        a2["state"] = DISABLED
    elif index2 == 2:
        a3["state"] = DISABLED
    elif index2 == 3:
        a4["state"] = DISABLED
    packRow = 10
    inc = Label(top, text="Incorrect!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    cor = Label(top, text="Correct!", font=("Arial", 25, "normal", "italic"), bg="#5ec9ff")
    if answer != ff_correct_answers[index1]:
        cor.grid_forget()
        inc.grid(row=packRow, column=0)
    else:
        inc.grid_forget()
        cor.grid(row=packRow + 1, column=0)


def ffQ (index):
    #Prints out question (and sets global variables)
    global top
    global a1
    global a2
    global a3
    global a4
    top = Toplevel(bg="#5ec9ff")
    question = Label(top, text=ff_questions[index], wraplength=510, pady=80, font=("Comic Sans MS", 15, "normal", "italic"), bg="#5ec9ff")
    question.grid(row=0, column=0)
    #Then the answers
    a1 = Button(top, text=ff_answers[index][0], height=4, width=70, command=partial(setFFAnswer, index, 0, ff_answers[index][0]), bg="#82d5ff")
    a2 = Button(top, text=ff_answers[index][1], height=4, width=70, command=partial(setFFAnswer, index, 1, ff_answers[index][1]), bg="#82d5ff")
    a3 = Button(top, text=ff_answers[index][2], height=4, width=70, command=partial(setFFAnswer, index, 2, ff_answers[index][2]), bg="#82d5ff")
    a4 = Button(top, text=ff_answers[index][3], height=4, width=70, command=partial(setFFAnswer, index, 3, ff_answers[index][3]), bg="#82d5ff")
    a1.grid(row=1, column=0)
    a2.grid(row=2, column=0)
    a3.grid(row=3, column=0)
    a4.grid(row=4, column=0)
    #Disables pressed button
    if index == 0:
        ff1["state"] = DISABLED
        ff1["text"] = ""
        ff1["relief"] = "groove"
    elif index == 1:
        ff2["state"] = DISABLED
        ff2["text"] = ""
        ff2["relief"] = "groove"
    elif index == 2:
        ff3["state"] = DISABLED
        ff3["text"] = ""
        ff3["relief"] = "groove"
    elif index == 3:
        ff4["state"] = DISABLED
        ff4["text"] = ""
        ff4["relief"] = "groove"
    elif index == 4:
        ff5["state"] = DISABLED
        ff5["text"] = ""
        ff5["relief"] = "groove"

# My Buttons
# f = food, pc = pop culture, l = literature, c = capitals, ff = fun facts
# They are also numbered: 1 - 100 points, to 5 - 500 points


f1 = Button(game, text="100", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(foodQ, 0), bg="#82d5ff" )
f2 = Button(game, text="200", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(foodQ, 1), bg="#82d5ff" )
f3 = Button(game, text="300", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(foodQ, 2), bg="#82d5ff" )
f4 = Button(game, text="400", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(foodQ, 3), bg="#82d5ff" )
f5 = Button(game, text="500", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(foodQ, 4), bg="#82d5ff" )

pc1 = Button(game, text="100", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(pcQ, 0), bg="#82d5ff" )
pc2 = Button(game, text="200", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(pcQ, 1), bg="#82d5ff" )
pc3 = Button(game, text="300", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(pcQ, 2), bg="#82d5ff" )
pc4 = Button(game, text="400", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(pcQ, 3), bg="#82d5ff" )
pc5 = Button(game, text="500", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(pcQ, 4), bg="#82d5ff" )

l1 = Button(game, text="100", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(litQ, 0), bg="#82d5ff" )
l2 = Button(game, text="200", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(litQ, 1), bg="#82d5ff" )
l3 = Button(game, text="300", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(litQ, 2), bg="#82d5ff" )
l4 = Button(game, text="400", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(litQ, 3), bg="#82d5ff" )
l5 = Button(game, text="500", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(litQ, 4), bg="#82d5ff" )

c1 = Button(game, text="100", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(capitalQ, 0), bg="#82d5ff" )
c2 = Button(game, text="200", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(capitalQ, 1), bg="#82d5ff" )
c3 = Button(game, text="300", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(capitalQ, 2), bg="#82d5ff" )
c4 = Button(game, text="400", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(capitalQ, 3), bg="#82d5ff" )
c5 = Button(game, text="500", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(capitalQ, 4), bg="#82d5ff" )

ff1 = Button(game, text="100", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(ffQ, 0), bg="#82d5ff" )
ff2 = Button(game, text="200", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(ffQ, 1), bg="#82d5ff" )
ff3 = Button(game, text="300", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(ffQ, 2), bg="#82d5ff" )
ff4 = Button(game, text="400", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(ffQ, 3), bg="#82d5ff" )
ff5 = Button(game, text="500", height=7, width=30, borderwidth=5, relief="ridge", state=NORMAL, command=partial(ffQ, 4), bg="#82d5ff" )

f1.grid(row=1, column=0)
f2.grid(row=2, column=0)
f3.grid(row=3, column=0)
f4.grid(row=4, column=0)
f5.grid(row=5, column=0)

pc1.grid(row=1, column=1)
pc2.grid(row=2, column=1)
pc3.grid(row=3, column=1)
pc4.grid(row=4, column=1)
pc5.grid(row=5, column=1)

l1.grid(row=1, column=2)
l2.grid(row=2, column=2)
l3.grid(row=3, column=2)
l4.grid(row=4, column=2)
l5.grid(row=5, column=2)

c1.grid(row=1, column=3)
c2.grid(row=2, column=3)
c3.grid(row=3, column=3)
c4.grid(row=4, column=3)
c5.grid(row=5, column=3)

ff1.grid(row=1, column=4)
ff2.grid(row=2, column=4)
ff3.grid(row=3, column=4)
ff4.grid(row=4, column=4)
ff5.grid(row=5, column=4)

root.mainloop()
