# -*- coding: utf-8 -*-

import os
from pathlib import Path

from PyPDF2 import PdfFileMerger

import glob
import win32com.client


# pass the path of the parent_folder
def pdf_merge(parent_folder: str, output_folder: str):
    #Lecture du dossier
    patern = parent_folder + "/*.pdf"
    target_files = glob.glob(patern)
    print(target_files)
    #Fusion des .pdf
    merger = PdfFileMerger()

    for pdf in target_files:
        merger.append(pdf)

    merger.write(output_folder)
    merger.close()
    return 0


# get a list of all the paths of the pdf
#parent_folder_path = r'C:\Users\Audio69\Downloads\102350-1724043-fusionner-ou-concatener-des-fichiers-pdf\PDFmerger\fusion_pdf'
#output_pdf_path = r"C:\Users\Audio69\Desktop\final.pdf"
#pdf_merge(parent_folder_path, output_pdf_path)


import cv2
import pytesseract
import re
import pyscreenshot
import math
import numpy as np
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Audio69\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# img = cv2.imread('imageaudiovoid.png')

# Cette fonction prend une capture d'écran d'une audiométrie sur Calisto et extraie la perte d'audition en dB
def loss_noah_extractor():
    # Capture de l'image
    image = np.array(pyscreenshot.grab().convert('RGB'))
    try:
        print(image.shape)
    except:
        pass

    # image = cv2.imread('imageaudiovoid.png')
    print("OK")
    # Traitement de l'image
    # Recadrage, binarisation de l'oreille droite
    imageOD = image[260:285, 225:425]
    imageOD = cv2.cvtColor(imageOD, cv2.COLOR_BGR2GRAY)
    imageOD = cv2.threshold(imageOD, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Recadrage, binarisation de l'oreille gauche
    imageOG = image[260:285, 1750:1925]
    imageOG = cv2.cvtColor(imageOG, cv2.COLOR_BGR2GRAY)
    imageOG = cv2.threshold(imageOG, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Extraction des textes
    textOD = pytesseract.image_to_string(imageOD)
    textOG = pytesseract.image_to_string(imageOG)

    # Extraction des valeurs des pertes
    perteod = re.findall("[0-9,-]+", textOD)
    perteog = re.findall("[0-9,-]+", textOG)

    # Mise en forme des valeurs
    if not perteod:
        pod = 0
        perteod = 1000
    elif perteod[0] == '-':
        pod = 0
        perteod = 1000
    else:
        pod = 1
        perteod = math.ceil(float(perteod[0].replace(",", ".")))

    if not perteog:
        pog = 0
        perteog = 2000
    elif perteog[0] == '-':
        pog = 0
        perteog = 2000
    else:
        pog = 1
        perteog = math.ceil(float(perteog[0].replace(",", ".")))

    # Logique d'analyse de la perte et retour du texte rapport
    if perteod == perteog:
        moyenne_perte = (perteod + perteog) / 2
    elif perteod > perteog:
        moyenne_perte = math.ceil((3 * perteod + 7 * perteog) / 10)
    elif perteod < perteog:
        moyenne_perte = math.ceil((7 * perteod + 3 * perteog) / 10)

    if 200 < abs(perteod - perteog):
        analyse_symetrie = ""
        crit_sym = 4
    if 19 < abs(perteod - perteog) < 120:
        analyse_symetrie = "asymétrique"
        crit_sym = 3
    elif abs(perteod - perteog) < 6:
        analyse_symetrie = "symétrique"
        crit_sym = 1
    elif 5 < abs(perteod - perteog) < 20:
        analyse_symetrie = "bilatérale"
        crit_sym = 2
    oreilles = [perteod, perteog, moyenne_perte]
    oreilles_reponse = ["", "", ""]
    degre_reponse = ["", "", ""]
    for count, oreille in enumerate(oreilles):
        if count == 0:
            text_choix_oreille = 'OD'
        elif count == 1:
            text_choix_oreille = 'OG'
        elif count == 2:
            text_choix_oreille = 'ODG'

        if oreille == 1000 or oreille == 2000:
            oreilles_reponse[count] = f"{text_choix_oreille} courbe non caractérisable"
            degre_reponse[count] = 8
        elif oreille < 20:
            oreilles_reponse[count] = f"{text_choix_oreille} audition normale"
            degre_reponse[count] = 0
        elif 20 < oreille < 31:
            oreilles_reponse[count] = f"{text_choix_oreille} perte légère de {oreilles[count]} dB"
            degre_reponse[count] = 1
        elif 30 < oreille < 41:
            oreilles_reponse[count] = f"{text_choix_oreille} perte légère-moyenne de {oreilles[count]} dB"
            degre_reponse[count] = 2
        elif 40 < oreille < 56:
            oreilles_reponse[count] = f"{text_choix_oreille} perte moyenne de {oreilles[count]} dB"
            degre_reponse[count] = 3
        elif 55 < oreille < 71:
            oreilles_reponse[count] = f"{text_choix_oreille} perte moyenne-sévère de {oreilles[count]} dB"
            degre_reponse[count] = 4
        elif 70 < oreille < 81:
            oreilles_reponse[count] = f"{text_choix_oreille} perte sévère de {oreilles[count]} dB"
            degre_reponse[count] = 5
        elif 80 < oreille < 91:
            oreilles_reponse[count] = f"{text_choix_oreille} perte sévère-profonde de {oreilles[count]} dB"
            degre_reponse[count] = 6
        elif 90 < oreille < 119:
            oreilles_reponse[count] = f"{text_choix_oreille} perte profonde de {oreilles[count]} dB"
            degre_reponse[count] = 7

    if perteod > 20 and perteog > 20 and crit_sym == 4:
        analyse = oreilles_reponse[0] + " / " + oreilles_reponse[1]

    elif perteod < 21 and perteog < 21:
        analyse = oreilles_reponse[2]

    elif (perteod < 21 and 20 < perteog) or (20 < perteod and perteog < 21) and (crit_sym == 2 or crit_sym == 3):
        analyse = "Surdité unilérale " + oreilles_reponse[0] + " / " + oreilles_reponse[1]

    elif perteod > 20 and perteog > 20 and crit_sym == 1:
        analyse = f"Surdité {analyse_symetrie} " + oreilles_reponse[2]

    elif perteod > 20 and perteog > 20 and crit_sym == 2 and degre_reponse[0] != degre_reponse[1]:
        analyse = f"Surdité {analyse_symetrie} " + oreilles_reponse[0] + " / " + oreilles_reponse[1]

    elif perteod > 20 and perteog > 20 and crit_sym == 2 and degre_reponse[0] == degre_reponse[1]:
        analyse = f"Surdité {analyse_symetrie} " + oreilles_reponse[2]

    elif perteod > 20 and perteog > 20 and crit_sym == 3:
        analyse = f"Surdité {analyse_symetrie} " + oreilles_reponse[0] + " / " + oreilles_reponse[1]

    if 30 < perteod < 120 or 30 < perteog < 120:
        besoin = "Oui"
    elif 20 < perteod < 31 and 20 < perteog < 31:
        besoin = "Si besoin ressenti"
    elif -15 < perteod < 21 and -15 < perteog < 21:
        besoin = "Non"
    else:
        besoin = "Indeterminé"



    analyse_od = oreilles_reponse[0]
    analyse_og = oreilles_reponse[1]
    print(analyse_od)
    print(analyse_og)
    return analyse_od, analyse_og, analyse, besoin


def excel_triage(liste, synthese):
    # Traitement de la liste
    excel_liste = win32com.client.Dispatch("Excel.Application")
    liste_abs = os.path.abspath(liste)
    wb = excel_liste.Workbooks.Open(liste_abs)
    ws = wb.Worksheets('Feuil1')
    ws.Range('B4:I28').Sort(Key1=ws.Range('B3'), Order1=1, Orientation=1)
    wb.Save()
    excel_liste.Application.Quit()
    # Traitement de la synthèse
    excel_synthese = win32com.client.Dispatch("Excel.Application")
    synthese_abs = os.path.abspath(synthese)
    wb = excel_synthese.Workbooks.Open(synthese_abs)
    ws = wb.Worksheets('Feuil1')
    ws.Range('B6:E28').Sort(Key1=ws.Range('B5'), Order1=1, Orientation=1)
    wb.Save()
    excel_synthese.Application.Quit()
