from numpy import log as ln
two_states=('A','B') #Δυο καταστασεις (Α,Β)


a_pos = [['A','G','T','C'],[0.4,0.4,0.1,0.1]] #Η πιθανοτητα να εκπεμψει πουρινες και πυριμιδινες στην κατασταση A
b_pos=[['T','C','A','G'],[0.3,0.3,0.2,0.2]] #Η πιθανοτητα να εκπεμψει πουρινες και πυριμιδινες στην κατασταση Β

goal=('G','G','C','T')  #Η ζητουμενη αλληλουχια

from_a_to_a_and_b=[0.9,0.1] #Η πιθανοτητα να συνεχισει απο την Α κατασταση στην Α και στην Β
from_b_to_a_and_b=[0.1,0.9] #Η πιθανοτητα να συνεχισει απο την Β κατασταση στην Β και στην Α

start_posibility=[0.5,0.5]  ##Η αρχικη πιθανοτητα να ξεκινησει απο το Α και το Β


def algo(a_pos,from_a_to_a_and_b,goal,start_posibility,b_pos,from_b_to_b_and_a,two_states):
    temp_a=[]   #Αποθηκευονται οι τιμες της Α καταστασης απο τον viterbi αλγοριθμο
    temp_b=[]   #Αποθηκευονται οι τιμες της Β καταστασης απο τον viterbi αλγοριθμο
    temp=True
    temp1=False
    temp2=False
    start=False
    log_num=0
    i=0
    best_path=[]
    while(temp):    #Οσο το temp παραμενει true η while θα τρεχει 
        for j in range(0,len(goal)):    #Μπαινει σε μια for με μεγεθος οση ειναι η ζητουμενη αλληλουχια(goal)
            if(start==False):   #Εαν το start ειναι false σημαινει οτι βρισκομαστε στην πρωτη κατασταση με ζητουμενο το G
                if(a_pos[0][j]==goal[i]):       #Εαν το a_pos[0][j] ισουται με το ζητουμενο
                    temp_a.append(start_posibility[0]*a_pos[1][j]) #τοτε η temp_a παιρνει την αρχικη πιθανοτητα του A και την πολλαπλασιαζει με την πιθανοτητα του ζητουμενου νουκλεοτιδιου
                    temp1=True
                if(b_pos[0][j]==goal[i]):
                    temp_b.append(start_posibility[1]*b_pos[1][j]) ##τοτε η temp_b παιρνει την αρχικη πιθανοτητα του Β και την πολλαπλασιαζει με την πιθανοτητα του ζητουμενου νουκλεοτιδιου
                    temp2=True
                if(temp1 and temp2): #Εαν το temp1 και το temp2 ειναι true τοτε εχουμε βρει το πρωτο ζητουμενο(goal[0])
                    start=True #Το start γινεται True οποτε το προγραμμα δεν μπαινει ξανα στην αρχικη if
                    i+=1
                    if(temp_a[0]>temp_b[0]):    #Εαν το temp_a που βρηκαμε ειναι μεγαλυτερο απο το temp_b που βρηκαμε τοτε 
                        best_path.append(two_states[0]) #Το best_path παιρνει την πρωτη κατασταση
                        log_num+= ln(temp_a[0])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num
                    elif(temp_a[0]<temp_b[0]):  #Αλλιως το best_path παιρνει την δευτερη κατασταση
                        best_path.append(two_states[1])
                        log_num+= ln(temp_b[0])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num
                    break       #Αφου βρει ποιο ειναι μεγαλυτερο κανει break απο την for και ξεκιναει για τις υπολοιπες καταστασεις αφου το start γινεται True στην σειρα 36
            if(start and temp1 and temp2):  #Εαν και τα τρια temp ειναι true ψαχνουμε τις υπολοιπες καταστασεις
                temp1=False     #Κανουμε το temp1 και το temp2 False ωστε να τα χρησιμοποιησουμε ξανα στον υπολοιπο κωδικα
                temp2=False 
            if(start==True):    #Εαν το start ειναι True
                if(a_pos[0][j]==goal[i] and best_path[i-1]=='A'):   #Εαν το νουκλεοτιδιο της a_pos  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την πρωτη κατασταση(Α)
                    temp_a.append(round(from_a_to_a_and_b[0]*a_pos[1][j]*temp_a[i-1],10))   #Η temp_a παιρνει την πιθανοτητα να παει απο το Α στο Α πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_a της προηγουμενης καταστασης
                    temp1=True
                elif(a_pos[0][j]==goal[i] and best_path[i-1]=='B'):     #Αλλιως εαν το νουκλεοτιδιο της a_pos  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την δευτερη κατασταση(Β)
                    temp_a.append(round(from_b_to_a_and_b[0]*a_pos[1][j]*temp_b[i-1],10))   #Η temp_a παιρνει την πιθανοτητα να παει απο το Β στο Α πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_b της προηγουμενης καταστασης
                    temp1=True                      
                if(b_pos[0][j]==goal[i] and best_path[i-1]=='A'):   #Εαν το νουκλεοτιδιο της b_pos  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την πρωτη κατασταση(Α)
                    temp_b.append(round(from_a_to_a_and_b[1]*b_pos[1][j]*temp_a[i-1],10))   #Η temp_b παιρνει την πιθανοτητα να παει απο το Α στο Β πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_a της προηγουμενης καταστασης
                    temp2=True
                elif(b_pos[0][j]==goal[i] and best_path[i-1]=='B'): #Αλλιως εαν το νουκλεοτιδιο της b_pos  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την δευτερη κατασταση(Β)
                    temp_b.append(round(from_b_to_a_and_b[1]*b_pos[1][j]*temp_b[i-1],10))   #Η temp_b παιρνει την πιθανοτητα να παει απο το Β στο Β πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_b της προηγουμενης καταστασης
                    temp2=True
                if(temp1==True and temp2==True):    #Εαν το temp1 και το temp2 ειναι True
                    if(temp_a[i]>temp_b[i]):        #Εαν το temp_a ειναι μεγαλυτερο του temp_b 
                        best_path.append(two_states[0]) #Τοτε το best_path παιρνει την πρωτη κατασταση
                        log_num+= ln(temp_a[i])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num 
                    else:
                        best_path.append(two_states[1]) #Αλλιως το best_path παιρνει την δευτερη κατασταση
                        log_num+= ln(temp_b[i])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num 
                    i+=1
            if(i==4 and len(best_path)==4): #Εαν το i εχει γινει 4 και το best_path εχει 4 τιμες τοτε
                temp=False  #Το temp γινεται false και οταν τελειωσει η while βγαινει απο αυτην
                for i in range(0,len(best_path)):        #Με μια for εκτυπωνει τις τιμες της Α και της Β καταστασης καθως και το μονοπατι με την μεγαλυτερη πιθανοτητα
                    print('to A einai',temp_a[i],'kai to B einai',temp_b[i])
                print('to best path einai',best_path,'kai to logarithmiko athroisma tou best_path me stroggulopoihsh einai',round(log_num,4))  #Εκτυπωνει το καλυτερο μονοπατι και το αθροισμα των λογαριθμικο αθροισμα 
                break   #Αφου εχουν εκτπωθει ολα κανει break, βγαινει απο την for και αφου το temp εχει γινει False τελειωνει και η while
                        
algo(a_pos,from_a_to_a_and_b,goal,start_posibility,b_pos,from_b_to_a_and_b,two_states)  #Καλειται η algo
