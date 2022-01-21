

# Les bibliothèques importées
from fenetre_maisonretraite import FenetreDossierMaisonRetraite
from fenetre_donnee import FenetreDonnee
from fenetre_anamnese import FenetreAnamnese

import keyboard
from pynput.keyboard import *
import time
import pyautogui
import pyperclip
import os
import winsound
import openpyxl
from datetime import datetime
import shutil

# Variable globale pour gérer les étapes dans l'ordre
step_one = 0
step_two = 0
step_three = 0
numero_patient = 1

# Variable globale pour la récupération des données et l'allumage de Callisto
nom = "nom_generique"
prenom = "prenom_generique"
duree = 0.1
chemin_calisto = r"C:\\Users\\Audio69\\Documents\\DocumentCalisto"
# Ce dossier contient le modèle du fichier excel à remplir
chemin_liste_referent = r"C:\\Users\\Audio69\\Documents\\DocOdipro\\DocMaster\\Liste Referents.xlsx"

# Extraction du nom de dossier de la MR GUI pour vérifier l'état du dossier de l'audiomètre il doit contenir 
# uniquement le dossier vide avec nom de la maison de retraite 
app1 = FenetreDossierMaisonRetraite(chemin_calisto)
app1.mainloop()

# Tests d'erreur pour vérifier les pré-requis
files = os.listdir(chemin_calisto)
nb_de_fichier = len(files)
files_str = str(files)
if nb_de_fichier > 1:
    print("Le dossier n'est pas conforme, trop de fichier(s)/dossier(s)")
    nom_maison_retraite = ""
    exit()

elif nb_de_fichier == 0:
    print("Il n'y a pas de dossier avec le nom de la maison de retraite")
    nom_maison_retraite = ""
    exit()

elif ".pdf" in files_str or ".txt" in files_str:
    nom_maison_retraite = ""
    print("Il n'y a pas le dossier de la maison de retraite")
    exit()

else:
    for files in files:
        nom_maison_retraite = app1.nom_maison_retraite

# Fin de l'extraction du nom de dossier

# On rempli la maison de retraite et la date du jour dans l'excel des référents
la_date_jour_save = datetime.today().strftime('%d-%m-%Y')
wb = openpyxl.load_workbook(chemin_liste_referent)
ws = wb['Feuil1']
sheet = wb.active
ws.cell(row=2, column=4).value = nom_maison_retraite
ws.cell(row=2, column=7).value = la_date_jour_save




# Fonction principale qui détecte les touches du clavier
def press_on(key):
    global step_one, step_two, step_three,\
        nom, nom_maison_retraite, numero_patient, chemin_calisto,\
        duree, prenom

    if key == Key.f9:
        if step_one == 0 and step_two == 0 and step_three == 0:
            # On ouvre la fenetre permettant d'entrer les données patient et accompagnant
            app2 = FenetreDonnee()
            app2.mainloop()
            # Première étape on récupère nom prénom et on allume Calisto
            # Clic fichier
            pyautogui.click(42, 34)
            time.sleep(duree)
            # Clic Ajouter nouveau patient
            pyautogui.click(118, 99)
            time.sleep(duree)
            # Clic Nom patient + remplissage
            pyautogui.click(750, 232)
            time.sleep(duree)
            keyboard.write(app2.nom_patient)
            time.sleep(duree)
            # CLic Prénom patient + remplissage
            pyautogui.click(1149, 232)
            time.sleep(duree)
            keyboard.write(app2.prenom_patient)
            time.sleep(duree)
            # Selection sexe patient
            if app2.sexe_patient == "Homme":
                pyautogui.click(1153, 267)
            else:
                pyautogui.click(1239, 268)
            time.sleep(duree)
            # On enregistre la fiche patient
            pyautogui.click(1111, 874)
            time.sleep(duree)
            # On clique sur la barre de recherche
            pyautogui.click(22, 171)
            time.sleep(duree)
            # On colle le prénom et le nom du patient
            prenom_nom_patient = [app2.prenom_patient+" "+app2.nom_patient]
            keyboard.write(prenom_nom_patient)
            # Selection fiche
            pyautogui.click(52, 340)
            # On ouvre le programme Calisto
            pyautogui.click(103, 74)
            # On valide la première étape
            step_one = 1

    if key == Key.f10:
        if step_one == 1 and step_two == 0 and step_three == 0:
            # Ouverture de la fenetre graphique
            app = FenetreAnamnese()
            app.mainloop()

            # Ouverture note
            pyautogui.click(157, 587)
            # Placement correct de la fenêtre
            pyautogui.moveTo(941, 208, 0.1)
            pyautogui.dragTo(317, 411, 0.2, button='left')
            pyautogui.click(8, 463)
            # On modifie l'établissement
            pyautogui.click(112, 461)
            pyautogui.dragTo(388, 462, 0.2, button='left')
            keyboard.write(nom_maison_retraite)
            step_two = 1
        else:
            print("Il faut compléter la premiere étape où finir la troisième étape")

    if key == Key.f11:
        if step_one == 1 and step_two == 1 and step_three == 0:
            # on ferme la fiche note
            pyautogui.click(709, 411)
            time.sleep(0.1)
            # On valide la confirmation d'enregistrement dans le cas où on revient sur la fiche
            pyautogui.click(928, 566)
            time.sleep(0.1)
            # on enregistre le rapport en pdf
            pyautogui.click(122, 45)
            time.sleep(0.1)
            # on enregistre la session
            pyautogui.click(148, 45)
            time.sleep(2)
            # On verifie que le rapport est a bien été enregistré
            path = fr"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\Report.pdf"
            if os.path.exists(path):
                # on modifie le nom du pdf generé avec le nom du patient
                file_oldname = rf"{chemin_calisto}\\Report.pdf"
                file_newname_newfile = rf"{chemin_calisto}\\{nom_maison_retraite}\\{nom} {prenom} {nom_maison_retraite}.pdf"
                os.rename(file_oldname, file_newname_newfile)
                # on ferme la session
                pyautogui.click(1897, 12)
                # on met à jour le fichier excel avec le nom des patients
                ws.cell(row=numero_patient + 3, column=2).value = nom
                ws.cell(row=numero_patient + 3, column=3).value = prenom
                # On incrémente les variables
                step_one = 0
                step_two = 0
                numero_patient = numero_patient + 1
            else:
                print("Le fichier à mal été enregistré")
        else:
            print("il faut compléter les étapes précédentes")

    if key == Key.f7:
        print(pyautogui.position())

    if key == Key.f5:
        print("fermeture du programme")
        winsound.PlaySound('son_fin.wav', winsound.SND_FILENAME)
        time.sleep(0.0125)
        winsound.PlaySound('son_fin.wav', winsound.SND_FILENAME)
        step_one = 0
        step_two = 0


# Fermeture avec la touche esc
def press_off(key):
    # print('Press OFF:  {}'.format(key))
    if key == Key.esc:
        if len(os.listdir(rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_maison_retraite}")) == 0:
            print("Le répertoire est vide")
            exit()
        else:
            print("fermeture du programme")
            winsound.PlaySound('son_fin.wav', winsound.SND_FILENAME)
            # On enregistre et on ferme le fichier excel
            liste_enr = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_maison_retraite}\\ListeRef-{la_date_jour_save}-{nom_maison_retraite}-RhoneAlpesAuvergne-KPERREAUT.xlsx "
            wb.save(liste_enr)
            # On déplace le dossier avec les CR + fichier excel dans le dossier de sauvegarde
            src = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_maison_retraite}"
            src_mod = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_maison_retraite}-{datetime.today().strftime('%d-%m-%Y')}"
            dest = rf"C:\\Users\\Audio69\\Documents\\DocOdipro\\SynologyDrive\\Depistages"
            # On renomme le dossier avec date jour zone
            shutil.move(src, src_mod)
            # On genere un fichier zip contenant les CR + l'excel
            shutil.make_archive(src_mod, 'zip',chemin_calisto)
            # On déplace l'archive dans le dossier
            shutil.move(rf"{src_mod}.zip", src_mod)
            # On deplace l'archive dans le dossier de stockage
            shutil.move(src_mod, dest)
            exit()
            return 0


# On reste en veille des touches du clavier
with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
