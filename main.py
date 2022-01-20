# Pré-requis pour que le script marche
# Preparation en amont, dans le logiciel Callisto il faut rebinder les raccourucis F5 à F12.
# Dans le logiciel callisto il faut paramètrer le bon template pour la prise de note
# Dans les options de calisto il faut importer le bon template d'impression, qu'il faut définir par défaut
# dans menu/règlage/Configuration AC440/Configuration impression de la catégorie audiométrie tonale (
# partie audiomètre
# Il faut configurer dans calisto l'impression pdf par défaut menu/règlage/paramètre généraux/impression pdf
# Il faut un dossier DocumentsCalisto à l'endroit du calisto_report_path où modifier le path en conséquence
# Le dossier DocumentCalisto doit contenir un dossier au nom de l'EHPAD

# Les bibliothèques importées
import keyboard
from anamnese_fen import FenetreAnamnese
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
CALISTO_REPORT_PATH = r"C:\\Users\\Audio69\\Documents\\DocumentCalisto"

# Extraction du nom de dossier de la MR
files = os.listdir(CALISTO_REPORT_PATH)
nb_de_fichier = len(files)
files_str = str(files)

if nb_de_fichier > 1:
    print("Le dossier n'est pas conforme, trop de fichier(s)/dossier(s)")
    nom_MR = ""
    exit()

elif nb_de_fichier == 0:
    print("Il n'y a pas de dossier avec le nom de la maison de retraite")
    nom_MR = ""
    exit()

elif ".pdf" in files_str or ".txt" in files_str:
    nom_MR = ""
    print("Il n'y a pas le dossier de la maison de retraite")
    exit()

else:
    for files in files:
        nom_MR = files

# Fin de l'extraction du nom de dossier

# On rempli la maison de retraite et la date du jour dans l'excel des référents
la_date_jour_save = datetime.today().strftime('%d-%m-%Y')
list_ref = r"C:\\Users\\Audio69\\Documents\\DocOdipro\\DocMaster\\Liste Referents.xlsx"
wb = openpyxl.load_workbook(list_ref)
ws = wb['Feuil1']
sheet = wb.active
ws.cell(row=2, column=4).value = nom_MR
ws.cell(row=2, column=7).value = la_date_jour_save


# Fonction principale qui détecte les touches du clavier
def press_on(key):
    global step_one
    global step_two
    global step_three
    global nom
    global prenom
    global duree
    global CALISTO_REPORT_PATH
    global numero_patient
    global nom_MR

    if key == Key.f9:
        if step_one == 0 and step_two == 0 and step_three == 0:
            # Première étape on récupère nom prénom et on allume Calisto
            pyautogui.click(107, 31)
            time.sleep(duree)
            keyboard.press_and_release('down')
            time.sleep(duree)
            keyboard.press_and_release('enter')
            time.sleep(duree)
            pyperclip.copy('')
            pyautogui.click(750, 230, button='right')
            time.sleep(duree)
            pyautogui.click(824, 265)
            time.sleep(duree)
            nom = pyperclip.paste()
            print(nom)
            time.sleep(duree)
            pyperclip.copy('')
            pyautogui.click(1150, 230, button='right')
            time.sleep(duree)
            pyautogui.click(1213, 265)
            time.sleep(duree)
            prenom = pyperclip.paste()
            print(prenom)
            keyboard.press_and_release('enter')
            if nom == "":
                print("la première étape n'a pas marché")
            else:
                # On ouvre callisto
                step_one = 1
                pyautogui.click(103, 74)
        else:
            print("Finissez le complèter les étapes avant de recommencer")

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
            keyboard.write(nom_MR)
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
                file_oldname = rf"{CALISTO_REPORT_PATH}\\Report.pdf"
                file_newname_newfile = rf"{CALISTO_REPORT_PATH}\\{nom_MR}\\{nom} {prenom} {nom_MR}.pdf"
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
        if len(os.listdir(rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_MR}")) == 0:
            print("Le répertoire est vide")
            exit()
        else:
            print("fermeture du programme")
            winsound.PlaySound('son_fin.wav', winsound.SND_FILENAME)
            # On enregistre et on ferme le fichier excel
            liste_enr = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_MR}\\ListeRef-{la_date_jour_save}-{nom_MR}-RhoneAlpesAuvergne-KPERREAUT.xlsx "
            wb.save(liste_enr)
            # On déplace le dossier avec les CR + fichier excel dans le dossier de sauvegarde
            src = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_MR}"
            src_mod = rf"C:\\Users\\Audio69\\Documents\\DocumentCalisto\\{nom_MR}-{datetime.today().strftime('%d-%m-%Y')}"
            dest = rf"C:\\Users\\Audio69\\Documents\\DocOdipro\\SynologyDrive\\Depistages"
            # On renomme le dossier avec date jour zone
            shutil.move(src, src_mod)
            # On genere un fichier zip contenant les CR + l'excel
            shutil.make_archive(src_mod, 'zip',CALISTO_REPORT_PATH)
            # On déplace l'archive dans le dossier
            shutil.move(rf"{src_mod}.zip", src_mod)
            # On deplace l'archive dans le dossier de stockage
            shutil.move(src_mod, dest)
            exit()
            return 0


# On reste en veille des touches du clavier
with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
