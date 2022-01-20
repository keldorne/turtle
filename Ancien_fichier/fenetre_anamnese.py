import tkinter as tk
from tkinter import END

# Paramètre de la fenetre

def fenetre_anamnese():
    formulaire_patient_accompagnant = tk.Tk()
    # formulaire_patient_accompagnant.geometry("500x500")
    formulaire_patient_accompagnant.resizable(False, False)
    formulaire_patient_accompagnant.title('Anamnèse')

    # On cré les variables
    global text_reponse
    text_reponse = [0]*15

    # Fonction pour chercher les valeurs entrées
    def recuperation_data(*args):
    la_ligne = les_items[0].curselection()[0]
    value = les_items[0].get(la_ligne)
    print(value)

    # Fonction pour remettre à 0 tout le formulaire sauf les remarques
    def fenetre_clear(*args):
    print("On efface les listes")
    for i in range(len(les_items)):
        try:
            les_items[i].selection_clear(0, END)
        except:
            print("")

    def resultat_recolteur():
    for i in range(len(les_items)):
        if les_items[i] == entry_remarque:
            text_reponse[i] = entry_remarque.get()
            if text_reponse[i] == "":
                print(f"remarque item {i} pas rempli")
            else:
                print(text_reponse[i])
        else:
            try:
                text_reponse[i] = les_items[i].get(les_items[i].curselection()[0])
                print(text_reponse[i])
            except:
                print(f"La liste {i} pas rempli")


    # Création des objets de la fenetre
    label_cognition = tk.Label(formulaire_patient_accompagnant, text="Cognition :")
    label_dejaappareille = tk.Label(formulaire_patient_accompagnant, text="Patient déjà appareillé :")
    label_otoscopie = tk.Label(formulaire_patient_accompagnant, text="Otoscopie :")
    label_prisedempreinte = tk.Label(formulaire_patient_accompagnant, text="Prise d'empreinte :")
    label_remarque = tk.Label(formulaire_patient_accompagnant, text="Remarques :")
    label_avisduresident = tk.Label(formulaire_patient_accompagnant, text="Avis du résident (Si possible) :")
    label_conseildappareillage = tk.Label(formulaire_patient_accompagnant, text="Conseils d'appareillage :")
    label_dome_embout = tk.Label(formulaire_patient_accompagnant, text="Choix dome/embout")
    bouton_fin = tk.Button(formulaire_patient_accompagnant, text="Enregistrer", command=resultat_recolteur)
    bouton_clear = tk.Button(formulaire_patient_accompagnant, text="Annuler", command=fenetre_clear)

    list_cognition = tk.Listbox(formulaire_patient_accompagnant, height=4, width=25, exportselection=0)
    list_cognition.insert(1, "Bonne")
    list_cognition.insert(2, "Moyenne")
    list_cognition.insert(3, "Mauvaise")
    list_cognition.insert(4, "Non Appareillable")

    list_dejaappareille = tk.Listbox(formulaire_patient_accompagnant, height=3, width=25, exportselection=0)
    list_dejaappareille.insert(1, "NON")
    list_dejaappareille.insert(2, "OUI avec dome")
    list_dejaappareille.insert(3, "OUI avec embout")

    list_otoscopieOG = tk.Listbox(formulaire_patient_accompagnant, height=3, activestyle='underline', width=25, exportselection=0)
    list_otoscopieOG.insert(1, "Ok OG")
    list_otoscopieOG.insert(2, "Cerumen gênant OG")
    list_otoscopieOG.insert(3, "Bouchon OG")

    list_otoscopieOD = tk.Listbox(formulaire_patient_accompagnant, height=3, width=25, exportselection=0)
    list_otoscopieOD.insert(1, "Ok OD")
    list_otoscopieOD.insert(2, "Cerumen gênant OD")
    list_otoscopieOD.insert(3, "Bouchon OD")

    list_prisedempreinteOG = tk.Listbox(formulaire_patient_accompagnant, height=2, width=25, exportselection=0)
    list_prisedempreinteOG.insert(1, "OUI OG")
    list_prisedempreinteOG.insert(2, "NON OG")

    list_prisedempreinteOD = tk.Listbox(formulaire_patient_accompagnant, height=2, width=25, exportselection=0)
    list_prisedempreinteOD.insert(1, "OUI OD")
    list_prisedempreinteOD.insert(2, "NON OD")

    entry_remarque = tk.Entry(formulaire_patient_accompagnant, width=50)

    list_avisduresident = tk.Listbox(formulaire_patient_accompagnant, height=3, width=25, exportselection=0)
    list_avisduresident.insert(1, "OK")
    list_avisduresident.insert(1, "Contre")

    list_conseildappareillageOG = tk.Listbox(formulaire_patient_accompagnant, width=25, exportselection=0)
    list_conseildappareillageOG.insert(1, "BTE 312 M OG")
    list_conseildappareillageOG.insert(1, "BTE 13 P OG")
    list_conseildappareillageOG.insert(1, "BTE 675 OG")

    list_conseildappareillageOD = tk.Listbox(formulaire_patient_accompagnant, width=25, exportselection=0)
    list_conseildappareillageOD.insert(1, "BTE 312 M OD")
    list_conseildappareillageOD.insert(1, "BTE 13 P OD")
    list_conseildappareillageOD.insert(1, "BTE 675 OD")

    list_dome_emboutOG = tk.Listbox(formulaire_patient_accompagnant, width=25, exportselection=0)
    list_dome_emboutOG.insert(1, "Tube fin Dome open OG")
    list_dome_emboutOG.insert(2, "Tube fin Dome ferme OG")
    list_dome_emboutOG.insert(3, "Tube fin Dome double OG")
    list_dome_emboutOG.insert(4, "Gabarit court OG")
    list_dome_emboutOG.insert(5, "Gabarit moyen OG")
    list_dome_emboutOG.insert(6, "Gabarit long OG")
    list_dome_emboutOG.insert(7, "Tube fin Embout OG")
    list_dome_emboutOG.insert(8, "Tube gros Embout OG")

    list_dome_emboutOD = tk.Listbox(formulaire_patient_accompagnant, width=25, exportselection=0)
    list_dome_emboutOD.insert(1, "Tube fin Dome ouvert OD")
    list_dome_emboutOD.insert(2, "Tube fin Dome ferme OD")
    list_dome_emboutOD.insert(3, "Tube fin Dome double OD")
    list_dome_emboutOD.insert(4, "Gabarit court OD")
    list_dome_emboutOD.insert(5, "Gabarit moyen OD")
    list_dome_emboutOD.insert(6, "Gabarit long OD")
    list_dome_emboutOD.insert(7, "Tube fin Embout OD")
    list_dome_emboutOD.insert(8, "Tube gros Embout OD")

    # Affichage du formulaire
    label_cognition.grid(row=0, column=0)
    label_dejaappareille.grid(row=1, column=0)
    label_otoscopie.grid(row=2, column=0)
    label_prisedempreinte.grid(row=3, column=0)
    label_remarque.grid(row=4, column=0)
    label_avisduresident.grid(row=5, column=0)
    label_conseildappareillage.grid(row=6, column=0)
    label_dome_embout.grid(row=7, column=0)

    list_cognition.grid(row=0, column=1)
    list_dejaappareille.grid(row=1, column=1)
    list_otoscopieOG.grid(row=2, column=1)
    list_otoscopieOD.grid(row=2, column=2)
    list_prisedempreinteOG.grid(row=3, column=1)
    list_prisedempreinteOD.grid(row=3, column=2)
    entry_remarque.grid(row=4, column=1, columnspan=2)
    list_avisduresident.grid(row=5, column=1)
    list_conseildappareillageOG.grid(row=6, column=1)
    list_conseildappareillageOD.grid(row=6, column=2)
    list_dome_emboutOG.grid(row=7, column=1)
    list_dome_emboutOD.grid(row=7, column=2)
    bouton_fin.grid(row=8, column=0)
    bouton_clear.grid(row=8, column=2)

    # Création de la liste contenant les réponses choisie
    les_item1 = [list_cognition, list_dejaappareille, list_otoscopieOG, list_otoscopieOD, list_prisedempreinteOG, list_prisedempreinteOD]
    les_item2 = [entry_remarque, list_avisduresident, list_conseildappareillageOG, list_conseildappareillageOD, list_dome_emboutOG]
    les_item3 = [list_dome_emboutOD]
    les_items = les_item1 + les_item2 + les_item3

    formulaire_patient_accompagnant.mainloop()


