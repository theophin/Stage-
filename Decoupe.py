#coding utf8

import os.path, time
import csv, string
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



nom="ex2"# input("Nom du fichier : ")

fichier =nom+'.csv'



try:
    user = "popo"#input("identifiant : ")
    log = "popo"#input("logiciel utilisé : ")
    index ="oui" #input("présence d'un index ? ")
    titre="oui"#input("présence d'une première ligne avec les titres ? " )

    freq="50" #input("fréquence du réseau : ")
    NbrSim ="2"# input("Nombre de simulation dans ce fichier : ")
    unite = "A" #input("Unité des valeurs ?")
    freqE=0 # fréquence d'échantillonage
    SignauxA="3"#input("Nombre de signaux analogiques : ")
    SignauxD="0" #input("Nombre de signaux digitaux : ")
    NbrSignaux= int(SignauxA) + int(SignauxD)

    n=0
    a=2

    while n<int(NbrSim) :
        with open (fichier, 'r',  encoding='utf8',errors= 'replace') as csvfile :
            data = nom+str(n)+'.dat'
            config= nom+str(n)+'.cfg'
            reader = csv.reader(csvfile)

            if("oui"in titre) :
                header = next(reader)
            else:
                header = list(string.ascii_uppercase)

            with open(data, 'w', encoding='utf8') as dfile :

                with open(config, 'w',encoding='utf8') as cfile:

                    wc = csv.writer(cfile, quoting=csv.QUOTE_NONE,escapechar=' ')
                    wd = csv.writer(dfile, quoting=csv.QUOTE_NONE,escapechar=' ')
                    NbrP=0 #Nombre de points

                #ecriture du .dat
                    if("oui" in index ):

                        k=0
                        b=0
                        for row in reader :
                            wd.writerow(row[0:2]+row[a:a+NbrSignaux])
                            NbrP+=1
                            if(k==1):
                                c=GetTemps(k,b)[0]
                            if(b==2):
                                d=GetTemps(k,b)[1]
                            k+=1
                            b+=1

                    else :
                        k=1
                        b=0
                        f=0
                        for row in reader :
                            wd.writerow([k]+[row[0]]+row[a-1:a+NbrSignaux-1])
                            k+=1
                            NbrP+=1
                            if(b==1):
                                c=GetTemps(b,f)[0]
                            if(f==2):
                                d=GetTemps(b,f)[1]
                            f+=1
                            b+=1


                #ecriture du .cfg
                    freqE=CalculeFreq(c,d)
                    wc.writerow([user]+[log]) #Ecrit la premiere ligne du .cfg avec lindentifiant et le logiciel utilise
                    wc.writerow([NbrSignaux]+[SignauxA+'A']+[SignauxD+'D']) #Ecrit la deuxieme ligne avec le nombre total de signaux, le nombres de signaux analogiques et le nombre de signaux digitaux

                    for i in range (1,NbrSignaux+1) :
                        wc.writerow([i]+[header[i+a-1]]+['']+['']+[unite]+[1]+[0]+[0.0]+[-32767]+[32767])
                    wc.writerow([freq]) #Ecrit la frequence du reseau
                    wc.writerow('1')#Nombre de frequence de la simulation
                    wc.writerow([freqE]+[NbrP]) #Ecrit la frequence dechantillonage et le nombre de point de la simulation
                    wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))]) #Ecrit la date de creation du fichier .csv
                    wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))])
                    wc.writerow(['ASCII']) #Ecrit lencodage par defaut du fichier .cfg


        a+=NbrSignaux
        n+=1



    print(color.OKGREEN+"Fichier convertie"+color.ENDC)
    #Signale la fin de la convertion. OKGREEN et ENDC sont là pour ajouter de la couleur à laffichage


except FileNotFoundError :

    print(color.WARNING+"Pas de fichier trouvé à ce nom "+color.ENDC )
