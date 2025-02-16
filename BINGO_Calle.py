# "Färdigt BINGO"

import random

#gör en lista som senare kan fyllas på
random_nummer = []

#Tar fram en spelar bricka för datorn som är helt slumpad
for _ in range (25):
    while True:
        random_tal = random.randint(0,75)
        if random_tal not in random_nummer:
            random_nummer.append(random_tal)
            break
        else:
            continue

#ändrar listan till en 5x5 bricka
dator_bricka = [random_nummer[i:i+5] for i in range (0,25,5)]

#välkommst text och möjligheten att trycka ENTER för att börja
print("Välkommen till mitt bingo!")
print("Vill du fortsätta med spelet")
input("tryck ENTER för att börja!")


#en lista som användaren ska fylla i själv
spelar_nummer = []

#en loop som låter användaren fylla i 25 nummer
i = 0
while i < 25:
    print (f"skriv in 25 nummer mellan 0 till 75! {i}/25")
    try:
        #vill ha svar av användaren på frågan som printades över
        vald_spelar_nummer = int(input ())

        if 1<= vald_spelar_nummer <= 75:

            #om det valda nummret finns i listan så kommer inte det nummret läggas till
            if vald_spelar_nummer in spelar_nummer:
                print ("Välj ett annat nummer än ett som redan finns!")
                continue
            else:
                #om nummret inte finns läggs det till
                print (f"nummer {vald_spelar_nummer} tillagt!")

                #Här läggs nummret till
                spelar_nummer.append(vald_spelar_nummer)

                #lägger till 1 på while loopen som gör att den går 25 gånger på loopen om man väljer tillåtna nummer
                i += 1              
        else:
            #om talet är mindre än 0 eller större än 75 så triggas denna som låter användaren välja ett till nummer
            print("Välj ett tal mellan 0 till 75")
            continue

   #ifall man inte väljer ett nummer eller skriver in en bokstavs triggas denna, så att programmet inte ska crasha
    except ValueError:
        print("otillåtet format!")



#ändrar listan till en 5x5 bricka
spelar_bricka = [spelar_nummer[i:i+5] for i in range(0, 25, 5)]
print("Här kommer din bingo bricka!")
for row in spelar_bricka:
    print (row)


#funktion för att visa brickan med slumpade nummer
def visa_dator_bricka (dator_bricka, revealed_numbers):
    for row in dator_bricka:
        print(" ".join(str(num) if num in revealed_numbers else " " for num in row))


#en tom "lista" som visar ett nummer i taget i loopen under
revealed_numbers = set()



#Detta kollar ifall numret finns i spelaren nummer och lägger till X i rättningsmatrisen
for i  in  range(0,25):
    input (f"tryck för att byta nummer: {i+1} av 25!")

    #lägger till random_nummer som slumpats fram i reveald_numbers 
    revealed_numbers.add(random_nummer[i])

    print("------------------")
    print("datorns bricka:")

    #visar spelaren dom redan framslumpade nummerna
    visa_dator_bricka(dator_bricka, revealed_numbers)
    print("------------------")


    #om det slumpade numret finns i spelar nummer listan, ersätter den numret med ett "x"
    if random_nummer[i] in spelar_nummer:
        print ("Match")
        for row in spelar_bricka:
            for j in range(len(row)):
                if row[j] == random_nummer[i]:
                    row[j] = "x"
        random_nummer[i] = "x"
        print("------------------")
        print("Din ny rättade bricka!")
        for row in spelar_bricka:
            print(row)
        print("------------------")
    else:
        continue
        
        



#gör bingo till en bool som är False
bingo = False
for row in spelar_bricka:
    #om en hel rad lista i spelar brickan blir bingo = True 
    if all(element == "x" for element in row):
        bingo = True
        break

def check_toptobottom(bricka):
    #kollar uppifrån och ner i listorna för att se om alla är "x" 
    for col in range(5):
        if all(bricka[row][col] == "x" for row in range(5)):
            #om det stämmer så blir bingo True
            return True
    #om det in stämmer så Blir bingo False
    return False

#kollar diagonalerna på listorna i spelar_bricka
def check_diagonal(bricka):
    if all(bricka[i][i] == "x" for i in range(5)):
        return True
    if all(bricka[i][4-i] == "x" for i in range(5)):
        return True
    return False

#om den hittar bingo i diagonalen eller i upp och ner triggas denna och gör bingo = True
if check_diagonal(spelar_bricka) or check_toptobottom(spelar_bricka):
    bingo = True


#visar båda brickorna i slutet så det blir lättare att jämföra
print("------------------")
print("spelar_bricka")
for row in spelar_bricka:
    print (*row)
print("------------------")

print("------------------")
print ("dator_bricka")
for row in dator_bricka:
    print (*row)
print("------------------")


#om det är bingo visar den bingo meddelande
if bingo == True:
    print("------------------")
    print ("bingo")
    print("------------------")
    input("Tryck ENTER för att stänga av!")

#annars kommer ett meddelande med att användaren inte fick bingo
else:
    print("Tyvärr inte bingo!")
    input("Tryck ENTER för att stänga av!")







