
# Les bibliothèques importées
from fenetre_maisonretraite import FenetreDossierMaisonRetraite
from fenetre_donnee import FenetreDonnee
from fenetre_anamnese import FenetreAnamnese
import keyboard
from pynput.keyboard import *
import time
import pyautogui
import os
import pygame
import openpyxl
from datetime import datetime
import shutil

# Variable globale pour gérer les étapes dans l'ordre
global step_one, step_two, step_three, numero_patient, nom_maison_retraite, nom_patient, prenom_patient, nom_accompagnant, prenom_accompagnant, telephone_accompagnant, mail_accompagnant, app3
global chemin_calisto, chemin_calisto_barre, dossier_sauvegarde, la_date_jour_save
#

####
# Path à modifier en fonction de votre configuration
chemin_calisto = r"C:\\Users\\Audio69\\Documents\\DocumentCalisto"
chemin_liste_referent = r"C:\\Users\\Audio69\\Documents\\DocOdipro\\DocMaster\\Liste Referents.xlsx"
dossier_sauvegarde = rf"C:\\Users\\Audio69\\Documents\\DocOdipro\\SynologyDrive\\Depistages"
# os.makedirs(chemin_calisto)
# os.makedirs(chemin_liste_referent)
# os.makedirs(dossier_sauvegarde)
####


# Paramètre fonctionnement
chemin_calisto_barre = chemin_calisto + "\\"
duree = 0.1

step_one = 0
step_two = 0
step_three = 0
numero_patient = 1

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
ws.cell(row=2, column=4).value = app1.nom_maison_retraite
ws.cell(row=2, column=7).value = la_date_jour_save




# Fonction principale qui détecte les touches du clavier
def press_on(key):
    global step_one, step_two, step_three, numero_patient, nom_maison_retraite, nom_patient, prenom_patient, nom_accompagnant, prenom_accompagnant, telephone_accompagnant, mail_accompagnant, app3
    if key == Key.f9:
        if step_one == 0 and step_two == 0 and step_three == 0:
            # On ouvre la fenetre permettant d'entrer les données patient et accompagnant
            app2 = FenetreDonnee()
            app2.mainloop()
            nom_patient = app2.nom_patient
            prenom_patient = app2.prenom_patient
            nom_accompagnant = app2.nom_accompagnant
            prenom_accompagnant = app2.prenom_accompagnant
            telephone_accompagnant = app2.telephone_accompagnant
            mail_accompagnant = app2.mail_accompagnant
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
            keyboard.write(nom_patient)
            time.sleep(duree)
            # CLic Prénom patient + remplissage
            pyautogui.click(1149, 232)
            time.sleep(duree)
            keyboard.write(prenom_patient)
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
            prenom_nom_patient = [prenom_patient +"  " +nom_patient]
            keyboard.write(prenom_nom_patient)
            time.sleep(0.6)
            # Selection fiche
            pyautogui.click(52, 340)
            time.sleep(0.6)
            pyautogui.click(118, 337)
            time.sleep(0.6)
            # On ouvre le programme Calisto
            pyautogui.click(103, 74)
            # On valide la première étape
            step_one = 1

    if key == Key.f10:
        if step_one == 1 and step_two == 0 and step_three == 0:
            # Ouverture de la fenetre graphique
            app3 = FenetreAnamnese()
            app3.mainloop()

            # Ouverture note
            pyautogui.click(157, 587)
            # Placement correct de la fenêtre
            pyautogui.moveTo(941, 208, 0.1)
            pyautogui.dragTo(317, 411, 0.2, button='left')
            pyautogui.click(8, 463)

            # On transforme les résultats obtenus avec le GUI en texte à copier dans le calisto pour le rapport
            # On integre le nom de la maison de retraite au debut du texte
            text_a_copier = "Etablissement : " + app1.nom_maison_retraite + "\n" + "\n"

            # Ligne cognition
            text_a_copier = text_a_copier + "   " + app3.les_texts[0 ] +"  " +app3.text_reponse[0 ] +"\n"

            # Ligne déjà appareillé
            if app3.text_reponse[1] == "":
                pass
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[1] + " " + app3.text_reponse[1] + "\n"

            # Ligne otoscopie
            if app3.text_reponse[2] == "" and app3.text_reponse[3] == "":
                pass
            elif app3.text_reponse[2] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[2] + " " + app3.text_reponse[3] + "\n"
            elif app3.text_reponse[3] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[2] + " " + app3.text_reponse[2] + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[2] + " " + app3.text_reponse[2] + ",  " + \
                                app3.text_reponse[3] + "\n"

            # Ligne prise d'empreinte
            if app3.text_reponse[4] == "" and app3.text_reponse[5] == "":
                pass
            elif app3.text_reponse[4] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[3] + " " + app3.text_reponse[5] + "\n"
            elif app3.text_reponse[5] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[3] + " " + app3.text_reponse[4] + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[3] + " " + app3.text_reponse[4] + ",  " + \
                                app3.text_reponse[5] + "\n"

            # Ligne remarque
            if app3.text_reponse[6] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[4] + " Aucune" + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[4] + " " + app3.text_reponse[6] + "\n"

            # Ligne avis
            if app3.text_reponse[7] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[5] + " Impossible de receuillir une réponse" + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[5] + " " + app3.text_reponse[7] + "\n"

            # Ligne conseil d'appareillage
            if app3.text_reponse[8] == "" and app3.text_reponse[9] == "":
                pass
            elif app3.text_reponse[8] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[6] + " " + app3.text_reponse[9] + "\n"
            elif app3.text_reponse[9] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[6] + " " + app3.text_reponse[8] + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[6] + " " + app3.text_reponse[8] + ",  " + \
                                    app3.text_reponse[9] + "\n"

            # Ligne choix dome embout
            if app3.text_reponse[10] == "" and app3.text_reponse[11] == "":
                pass
            elif app3.text_reponse[10] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[7] + " " + app3.text_reponse[11] + "\n"
            elif app3.text_reponse[11] == "":
                text_a_copier = text_a_copier + "   " + app3.les_texts[7] + " " + app3.text_reponse[10] + "\n"
            else:
                text_a_copier = text_a_copier + "   " + app3.les_texts[7] + " " + app3.text_reponse[10] + ",  " + \
                                    app3.text_reponse[11] + "\n"

            print (text_a_copier)
            pyautogui.click(5, 461)
            # pyautogui.dragTo(650, 1110, 0.2, button='left')
            keyboard.write(text_a_copier)
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
            if os.path.exists(chemin_calisto_barre + "Report.pdf"):
                # on modifie le nom du pdf generé avec le nom du patient
                file_oldname = chemin_calisto_barre + "Report.pdf"
                file_newname_newfile = rf"{chemin_calisto}\\{nom_maison_retraite}\\{nom_patient} {prenom_patient} {nom_maison_retraite}.pdf"
                os.rename(file_oldname, file_newname_newfile)
                # on ferme la session
                pyautogui.click(1897, 12)
                # on met à jour le fichier excel avec identité patient et accompagnant
                ws.cell(row=numero_patient + 3, column=2).value = nom_patient
                ws.cell(row=numero_patient + 3, column=3).value = prenom_patient
                ws.cell(row=numero_patient + 3, column=5).value = nom_accompagnant
                ws.cell(row=numero_patient + 3, column=6).value = prenom_accompagnant
                ws.cell(row=numero_patient + 3, column=7).value = telephone_accompagnant
                ws.cell(row=numero_patient + 3, column=8).value = mail_accompagnant
                # on indique si il y a des empreintes
                if app3.text_reponse[4] == "" and app3.text_reponse[5] == "":
                    ws.cell(row=numero_patient + 3, column=9).value = "Aucune"
                elif app3.text_reponse[4] == "":
                    ws.cell(row=numero_patient + 3, column=9).value = "OD"
                elif app3.text_reponse[5] == "":
                    ws.cell(row=numero_patient + 3, column=9).value = "OG"
                else:
                    ws.cell(row=numero_patient + 3, column=9).value = "ODG"
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
        print("On reinitialise les etapes")
        pygame.mixer.init()
        pygame.mixer.music.load('son_fin.mp3')
        pygame.mixer.music.play()
        step_one = 0
        step_two = 0


# Fermeture avec la touche esc
def press_off(key):
    global chemin_calisto, chemin_calisto_barre, nom_maison_retraite, dossier_sauvegarde, la_date_jour_save
    if key == Key.esc:
        if len(os.listdir(chemin_calisto_barre + nom_maison_retraite)) == 0:
            print("Le répertoire est vide")
            exit()
        else:
            print("fermeture du programme")
            pygame.mixer.init()
            pygame.mixer.music.load('son_fin.mp3')
            pygame.mixer.music.play()
            time.sleep(0.0125)
            pygame.mixer.music.play()
            pygame.mixer.quit()
            # On enregistre le fichier excel dans le dossier de la maison de retraite
            liste_enregistre = chemin_calisto_barre + nom_maison_retraite + r"\\ListeRef-" + la_date_jour_save + "-" + nom_maison_retraite + "-RhoneAlpesAuvergne-KPERREAUT.xlsx"
            wb.save(liste_enregistre)
            # On renomme le dossier de la maison de retraite avec date jour zone
            nom_dossier_sauvegarde = nom_maison_retraite + "-" + datetime.today().strftime('%d-%m-%Y')
            dossier_maison_retraite = chemin_calisto_barre + nom_maison_retraite
            dossier_maison_retraite_date = chemin_calisto_barre + nom_dossier_sauvegarde
            shutil.move(dossier_maison_retraite, dossier_maison_retraite_date)
            # On genere un fichier zip contenant les CR + l'excel
            shutil.make_archive(dossier_maison_retraite_date, 'zip', chemin_calisto, nom_dossier_sauvegarde)
            # On déplace l'archive dans le dossier
            shutil.move(dossier_maison_retraite_date + ".zip", dossier_maison_retraite_date)
            # On déplace le dossier avec les comptes rendus + fichier excel + version ziper recapitulatif dans le dossier de sauvegarde
            shutil.move(dossier_maison_retraite_date, dossier_sauvegarde)
            exit()
            return 0


# On reste en veille des touches du clavier
with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
