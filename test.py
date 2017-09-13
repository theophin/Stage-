# coding: utf8

import os.path, time
import csv
import string
from codecs import open

class color:

    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def CalculeFreq(param1,param2) :
    return (1/(param2-param1))

def GetTemps(a,b):

    c=float(row[1])
    d=float(row[1])
    return c,d


nom ="ex1"#input("Nom du fichier : ")

fichier =nom+'.csv'
data = nom+'.dat'
config= nom+'.cfg'

#Debut de la boucle
try :

    with open (fichier, 'r',  encoding='utf8',errors= 'replace') as csvfile :
    #ouverture du fichier .csv

        reader = csv.reader(csvfile)
        #creation du lecteur pour le fichier .csv

        with open(data, 'w', encoding='utf8') as dfile :
        #ouverture/creation du .dat

            with open(config, 'w',encoding='utf8') as cfile:
            #ouverture/creation du .cfg

                wc = csv.writer(cfile, quoting=csv.QUOTE_NONE,escapechar=' ') #creation de loutil decriture pour le .cfg
                wd = csv.writer(dfile, quoting=csv.QUOTE_NONE,escapechar=' ') #creation de loutil decriture pour le .dat

                user = "popo"#input("identifiant : ")
                log = "popo"#input("logiciel utilisé : ")
                index ="oui" #input("présence d'un index ? ")
                titre="non"#input("présence d'une première ligne avec les titres ? " )
                SignauxA="3"#input("nombre de signaux analogiques : ")
                SignauxD="0" #input("nombre de signaux digitaux : ")
                unite="A"#input("unité des valeurs :")
                freq="50" #input("fréquence du réseau : ")
                freqE=0 # fréquence d'échantillonage
                NbrSignaux= int(SignauxA) + int(SignauxD)   #Calcule le nombre total de signaux
                NbrP=0 #Nombre de points

                if("oui" in titre) : #Permet de trouve le noms des signaux

                    header=next(reader) #Permet de stocker la premiere ligne du .csv

                else:

                    header = list(string.ascii_uppercase) #Sil ny pas de premiere ligne, se sert de lalphabet

    #ecriture du .dat
                if("oui" in index ): #Permet de recuperer uniquement les colonnes concernant le nombres de signaux indiques

                    i=2+NbrSignaux
                    a=0
                    b=0
                    for row in reader:
                        wd.writerow(row[0:i])
                        NbrP+=1
                        if(a==1):
                            c=GetTemps(a,b)[0]
                        if(b==2):
                            d=GetTemps(a,b)[1]
                        a+=1
                        b+=1


                else : #Si le fichier ne contient pas dindex lajoute et recupere les colonnes concernant le nombre de signaux demande

                    a=1
                    i=1+NbrSignaux
                    for row in reader :

                        wd.writerow([a]+row[0:i]) #Ecrit les colonnes demandes en ajoutant un index
                        NbrP+=1
                        a+=1

    #ecriture du .cfg
                freqE=CalculeFreq(c,d)
                wc.writerow([user]+[log]) #Ecrit la premiere ligne du .cfg avec lindentifiant et le logiciel utilise

                wc.writerow([NbrSignaux]+[SignauxA+'A']+[SignauxD+'D']) #Ecrit la deuxieme ligne avec le nombre total de signaux, le nombres de signaux analogiques et le nombre de signaux digitaux

                for i in range (1,NbrSignaux+1):
                #Ecrit les lignes contenant lindex, le nom des signaux, lunite,...etc
                    wc.writerow([i]+[header[i+1]]+['']+['']+[unite]+[1]+[0]+[0.0]+[-32767]+[32767])

                wc.writerow([freq]) #Ecrit la frequence du reseau
                wc.writerow('1')#Nombre de frequence de la simulation
                wc.writerow([freqE]+[NbrP]) #Ecrit la frequence dechantillonage et le nombre de point de la simulation
                wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))]) #Ecrit la date de creation du fichier .csv
                wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))])
                wc.writerow(['ASCII']) #Ecrit lencodage par defaut du fichier .cfg



    print(color.OKGREEN+"Fichier convertie"+color.ENDC)
    #Signale la fin de la convertion. OKGREEN et ENDC sont là pour ajouter de la couleur à laffichage

except FileNotFoundError :
# Recupere lerreur si le nom du fichier nest pas le bon

    print(color.WARNING+"Pas de fichier trouvé à ce nom "+color.ENDC )

