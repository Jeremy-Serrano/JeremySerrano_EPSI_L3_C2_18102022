#commentaire ligne

#x = 5 #AUtomatiquement le type int
#y = "Salut" #Automatiquement le type str

#print(x)
#print(y)

#x=str(5)
#y=int(5)
#z=float(5)

#print(type(x))
#print(type(y))
#print(type(z))

#a="Vincent"
#b='Artz'

#print(a)
#print(b)

#x,y,z = "Fruits", "legumes", "lait"
#print(x)
#print(y)
#print(z)

#x=y=z="Fruits"
#print(x)
#print(y)
#print(z)

#fruits = ["Pomme","banane","cerise"]
#x,y,z = fruits
#print(x)
#print(y)
#print(z)

#x = "Python"
#y = "Est"
#z = "Top"
#print (x,y,z) #ou print(x+y+z)

#x = 2
#y = 5
#print(x+y)

#x = "Test"
#y = 5
#print(x,y)

#x = "cool"
#def mafonction():
#	print("Python est "+x)
#mafonction()


#x = "cool"
#def mafonction():
#	x = "Superbe"
#	print("Python est "+x)
#mafonction()
#print("Python est " + x)


#def mafonction():
#	global x
#	x = "genial"
#mafonction()
#print("Python est " + x)



#x=1
#y=4.5
#z=1j
#print(type(z))


#x=35e3
#y=12E4
#z=-87e100
#print(type(z))

# x=1
# y=3.5
# z=1j
#
# a=float(x)
# b=int(y)
# c=complex(x)
#
# print (a)
# print(b)
# print(c)

#import random
#print(random.randrange(1,10))

#from math import factorial
#print(factorial(5))

# a= "Hello, ca va"
# print(a[1])
#
# a= "Hello, ca va"
# print(len(a))
#
# for x in "Vincent":
# 	print(x)
#
# a= "Hello, ca va? Mais ca va bien ou pas ?"
# if "va" in a:
#     print("trouvé")
#
# a= "Hello, ca va? Mais ca va bien ou pas ?"
# if "uwu" not in a:
#     print("pas trouvé")

# x = "Salut les amis"
# print(x[2:5])

#depuis le debut
# x = "Salut les amis"
# print(x[-5:-2])

def exo1():
    prenom ="Pierre"
    age="20"
    majeur= True
    compte_en_banque = 20135,384
    amis=["Marie","Julien","Adrien"]
    parents = ("Marc", "Caroline")
    print(prenom, age, majeur, compte_en_banque, amis, parents)
#exo1()

def exo2():
    nombre = 15
    print("Le nombre est " + str(nombre))
#exo2()

def exo3():
    a=2
    b=6
    c=3
    print(a,"+",b, "+", c)
    print(a,b,c, sep = " + ")
#exo3()

def exo4():
    test = range(3)
    list2 = range(5)
    print(list(list2))
#exo4()

def exo5():
    prenom = "Pierre"
    res = isinstance(prenom, str)
    if (res == True):
        print ("la variable est une chaine de carac")

    age = 20
    test = isinstance(age, int)
    if(test == True):
        print("la variable est un int")
#exo5()

# a = "hello"
# print(a.upper())
#
# b = "HELLO"
# print(b.lower())

# c = " Bonjour ca va ?"
# print(c.strip())
#
# d = " Bonjour ca va  ? "
# print (d)
#
# e = " Bonjour ca va ? "
# print(e.replace("j", "o"))

# f =" Bonjour ca va ? "
# print(f.split(","))

# age = 20
# age2 = 40
# age3 = 60
# txt = "Voici mon age {} dans 20ans je vais avoir {} et beaucoup plus tard {}"
# print(txt.format(age,age2,age3))
#
# age = 20
# age2 = 40
# age3 = 60
# txt = "Voici mon age {1} dans 20ans je vais avoir {0} et beaucoup plus tard {2}"
# print(txt.format(age,age2,age3))

# x=5
# print(not(x>3 and x<10))
#
# x = ["fruits", "legumes"]
# y = ["fruits", "legumes"]
#
# z=x
# print(x is z)
#
# print(x is z)
# print(x is y)
# print(x == y)

def exo6():
    phrase = "Bonjour tout le monde. Je repète Bonsoir"
    print(phrase.replace("Bonjour", "Bonsoir", 1))
#exo6()

def exo_7():
    names = "Pierre, Julien, Anne, Marie, Julien";
    namesArray = names.split(', ');
    namesArray.sort();
    print(", ".join(map(str, namesArray)))
#exo_7()

# maliste = ["Pierre", "Julien", "Anne", "Marie", "Julien"]
# print(maliste)

#maliste = ["Pierre", "Julien", "Anne", "Marie", "Julien"]
# print(len(maliste))
#
# maliste[1]= "Vincent"
# print(maliste)
#maliste[1:3] = ["Vincent", "Sophie"]

#maliste.insert(2,"Vincent")
#print(maliste)

# maliste1 = ["Anne", "Marie", "Lucien"]
# malistetuple = ("Pierre", "Lucien")
#
# maliste1.extend(malistetuple)
# print(maliste1)

# maliste1 = ["Anne", "Marie", "Lucien"]
# maliste1.remove(1)
# print(maliste1)

# maliste1 = ["Anne", "Marie", "Lucien"]
# maliste1.pop()
# print(maliste1)
#
# maliste1 = ["Anne", "Marie", "Lucien"]
# x = 0
# while x < len(maliste1):
#     print(maliste1[x])
#     x+=1
# for x in range(len(maliste1)):
#     print(maliste1[x])

#maliste1 = ["Anne", "Marie", "Lucien"]
# [print(x) for x in maliste1]

# fruits = ["Banane", "Pomme", "kiwi", "mangue"]
# nouvelleliste = []
#
# for x in fruits:
#     if"a" in x :
#         nouvelleliste.append(x)
#
# print(nouvelleliste)

# fruits = ["Banane", "Pomme", "kiwi", "mangue"]
# nouvelleliste = [x for x in fruits if "a" in x]
# print(nouvelleliste)

# fruits = ["Banane", "Pomme", "kiwi", "mangue"]
# nouvelleliste = [x for x in fruits if x != "Banane"]
# print(nouvelleliste)
#
# nouvelleliste = [x for x in range(5)]
# print(nouvelleliste)

def exo10():
    from cmath import pi

    ray = int(input("ENTREZ LE RAYON DE LA SPHERE: "))

    vol = (4 * pi) / 3 * ray ** 3

    print("LE VOLUME DE LA SPHERE EST DE ", vol)
#exo10()

def exo11(a):
    if a>10:
        return "Le nombre saisi est plus grand que 10"
    elif a == 10:
        return "Le nombre saisi est égal à 10"
    else:
        return "Le nombre saisi est inférieur à 10"
#a = input()
#print(exo9(int(a)))

def exo12():
    numberChoice = int(input("Choisis un nombre :"))

    lst = []

    def createList(n):

        if numberChoice > 15:

            print('Nombre trop grand')

        else:

            for i in range(5, n + 1):
                lst.append(i)

                return (lst)

    print(createList(numberChoice))
#exo12()

def Fonction(n):
    return abs(n-50)

fruits = [100,52,47,34]
fruits.sort(key = Fonction)
print(fruits)
