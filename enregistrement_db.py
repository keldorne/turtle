from datetime import datetime
nom_maison_retraite = "Monculx"
la_date_jour_save = datetime.today().strftime('%d-%m-%Y')
anamnese_db1=["",1]
anamnese_db2=["dejaapp","jamaisapp"]
anamnese_db3=[0,1]
anamnese_db4=[0,1]
anamnese_db5=["amdoullah","cava"]
anamnese_db6=["OK","Contre"]
anamnese_db7=[0,1]
anamnese_db8=[0,1]
anamnese_db9=[0,1]
anamnese_db10=[0,1]
nom_patients=["adboul","amar"]
prenom_patients=["jean","voine"]
nom_accompagnants=["ulf","gard"]
prenom_accompagnants=["titi","toto"]
telephone_accompagnants=["060545","047854"]
mail_accompagnants=["@oil","gmail@"]
numero_patient=len(anamnese_db1)


print(type(anamnese_db1))
import time

start = time.time()

print("The time used to execute this is given below")




import sqlite3
# Ouverture de la base de donnée et initialisation de la table info maison retraite et création référent VIDE
connection = sqlite3.connect("../googlecontactAPI/test3.db")
cursor_maison_retraite = connection.cursor()
cursor_referent = connection.cursor()

try:
    db_maison_retraite = (cursor_maison_retraite.lastrowid, nom_maison_retraite, "")
    cursor_maison_retraite.execute('INSERT INTO INFO_MAISON_RETRAITE VALUES(?,?,?)', db_maison_retraite)
    id_maison_retraite = cursor_maison_retraite.lastrowid
    print(id_maison_retraite)
except Exception as e:
    print("1erreur", e)
    connection.rollback()
    connection.close()

    # Référent vide pour l'instant en attendant l'interfaçage avec API GOOGLE

try:
    db_referent = (cursor_referent.lastrowid, id_maison_retraite, 2, "", "", "", "", "")
    cursor_referent.execute('INSERT INTO INFO_HUMAIN VALUES(?,?,?,?,?,?,?,?)', db_referent)
    id_referent = cursor_referent.lastrowid
except Exception as e:
    print("2erreur", e)
    connection.rollback()
    connection.close()

try:
    connection.commit()
    connection.close()
except:
    connection.close()

# Enregistrement de l'anamnèse, des patients, des accompagnants, des fiches patients dans la base de donnée
# anamnesedball = [cursor2.lastrowid, anamnese_db1, anamnese_db2, anamnese_db3, anamnese_db4, anamnese_db5, anamnese_db6, anamnese_db7, anamnese_db8, anamnese_db9, anamnese_db10]
# cursor2.executemany('INSERT INTO INFO_ANAMNESE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', anamnesedball)

for i in range(numero_patient):
    connection = sqlite3.connect("../googlecontactAPI/test3.db")
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()
    try:
        db_info_anamnese = (
        cursor2.lastrowid, anamnese_db1[i], anamnese_db2[i], anamnese_db3[i], anamnese_db4[i], anamnese_db5[i], anamnese_db6[i],
        anamnese_db7[i], anamnese_db8[i], anamnese_db9[i], anamnese_db10[i], "", "")
        cursor2.execute('INSERT INTO INFO_ANAMNESE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', db_info_anamnese)

        id_anamnese = cursor2.lastrowid
    except Exception as e:
        print("erreur", e)
        connection.rollback()
        connection.close()

    # Patient
    try:
        db_patient = (cursor3.lastrowid, id_maison_retraite, 0, nom_patients[i], prenom_patients[i], "", "", "")
        cursor3.execute('INSERT INTO INFO_HUMAIN VALUES(?,?,?,?,?,?,?,?)', db_patient)
        id_patient = cursor3.lastrowid
    except Exception as e:
        print("erreur", e)
        connection.rollback()


    # Accompagnant
    try:
        db_accompagnant = (cursor4.lastrowid, id_maison_retraite, 1, nom_accompagnants[i], prenom_accompagnants[i], "", telephone_accompagnants[i], mail_accompagnants[i])
        cursor4.execute('INSERT INTO INFO_HUMAIN VALUES(?,?,?,?,?,?,?,?)', db_accompagnant)
        id_accompagnant = cursor4.lastrowid
    except Exception as e:
        print("erreur", e)
        connection.rollback()


    # Fiche patient
    try:
        db_fiche_patient = (cursor5.lastrowid, id_patient, id_accompagnant, id_referent, id_anamnese, la_date_jour_save, "", "", "")
        cursor5.execute('INSERT INTO FICHE_PATIENT VALUES(?,?,?,?,?,?,?,?,?)', db_fiche_patient)
        id_fiche_patient = cursor5.lastrowid
    except Exception as e:
        print("erreur", e)
        connection.rollback()

    try:
        connection.commit()
        connection.close()
    except:
        connection.close()


connection.close()

end = time.time()

print(end - start)