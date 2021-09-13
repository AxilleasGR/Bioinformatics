import random
from Bio import SeqIO
#Φορτώνουμε τις 2 αλληλουχιες 
for sequence1 in SeqIO.parse("liver.fasta", "fasta"): 
	xromo_liver = sequence1.seq	
for sequence2 in SeqIO.parse("brain.fasta", "fasta"):
	xromo_brain = sequence2.seq
xromo_liver = len(sequence1) #Βρίσκουμε το μέγεθος της πρώτης αλληλουχιάς
xromo_brain = len(sequence2) #Βρίσκουμε το μέγεθος της δεύτερης αλληλουχιάς
player = 1
#Εδώ ελέγχουμε αν κέρδισε καποιος παίχτης
def check(player):
    if(xromo_brain==0 or xromo_liver==0):
        print("Νικητής ειναι ο παίχτης ",player)
while(True): #Το παιχνίδι παίζει μέχρι να νικήσει ένας από τους δύο παίχτες
    if(xromo_brain!=0 and xromo_liver!=0): #Αν δεν εχει μηδενισει καμια αλληλουχια μπαινει στην if
        print("Παίζει ο παίχτης νούμερο ",player ," \n  Θέλεις να σβήσεις απο την πρώτη(liver) ή την" +
        "δεύτερη(brain) ή και απο τις δυο αλληλουχίες επέλεξε την επιλογή 1 ή 2 ή 3 αντίστοιχα")
        if(xromo_brain<xromo_liver): #αν η αλληλουχια 1 ειναι μικροτερη απο την 2 τοτε ο τυχαιος αριθμος θα ειναι απο το 1 μεχρι το μεγεθος της αλληλουχιας 1
            smaller=xromo_brain
        else:
            smaller=xromo_liver     #αν η αλληλουχια 2 ειναι μικροτερη απο την 1 τοτε ο τυχαιος αριθμος θα ειναι απο το 1 μεχρι το μεγεθος της αλληλουχιας 2
        randomremove = random.randint(1,smaller)    #τυχαιος αρθμος απο το 1 μεχρι τον αριθμο που ορισαμε απο πανω
        epilogh = random.randint(1,3) #auto play
        print(epilogh) #auto play
        #epilogh= int(input()) #Ο χρηστης δινει στο προγραμμα το τι θελει να κανει
        while(True):    #Τρέχει μεχρι να δεχτει σωστο τυπο input απο τον χρηστη
            if(epilogh==1 or epilogh==2 or epilogh==3): #Αν η επιλογη ειναι 1 η 2 η 3 βγαινει απο την while και συνεχιζει
                break
            else:
                print("Διαθέσιμες επιλογές 1 ή 2 ή 3")  #Αν η επιλογη δεν ειναι 1 η 2 η 3 εκτυπωνονται οι διαθεσιμες επιλογες 
                epilogh = int(input()) #Ο χρηστης δινει στο προγραμμα το τι θελει να κανει
        if(epilogh==1): #Αν επιλεξει την επιλογη 1
            xromo_liver-=randomremove #Αφαιρουμε απο την αλληλουχια 1 τον τυχαιο αριθμο randremove
            check(player) #Ελεγχουμε μηπως τελειωσε το παιχνιδι
        elif(epilogh==2):#Αν επιλεξει την επιλογη 2
            xromo_brain-=randomremove #Αφαιρουμε απο την αλληλουχια 2 τον τυχαιο αριθμο randremove
            check(player) #Ελεγχουμε μηπως τελειωσε το παιχνιδι
        elif(epilogh==3):#Αν επιλεξει την επιλογη 3
            xromo_brain-=randomremove #Αφαιρουμε απο την αλληλουχια 1 τον τυχαιο αριθμο randremove και
            xromo_liver-=randomremove #Αφαιρουμε απο την αλληλουχια 2 τον τυχαιο αριθμο randremove
            check(player)

        if(player==1): #Αλλαγη παιχτων
            player=2 #Αν επαιζε ο παιχτης 1 τωρα εχει σειρα ο παιχτης 2
        elif(player==2): #Αλλαγη παιχτων
            player=1 #Αν επαιζε ο παιχτης 2 τωρα εχει σειρα ο παιχτης 1
    else: #Αν δεν μπει στην if 
        break; #Βγαινει απο την while