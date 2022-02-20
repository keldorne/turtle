from Google import create_service
from pathlib import Path

# Paramètre pour tester l'application

nom_maison_retraite = "MR " + "MONCULX"
numero_telephone = "0601915531"
nom_cadre_sante = "CDS : " + "MME AYUNE"
adresse_postale = "14 rue parmentiers saint fons"
adresse_email = "septentriodnak@gmail.com"

# Standard contact en majuscule
nom_maison_retraite = nom_maison_retraite.upper()
nom_cadre_sante = nom_cadre_sante.upper()

# Paramètres d'authentification
CLIENT_SECRET_FILE = Path("tolkienetjason", "client_creercontact.json")
API_NAME = 'people'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/contacts']

# Appel de la fonction d'authentification
service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


service.people().createContact(body={
        "organizations": [
            {
                "name": nom_maison_retraite
            }
        ],
        "phoneNumbers": [
            {
                'value': numero_telephone,
                "type": nom_cadre_sante
            }
        ],
        "emailAddresses": [
            {
                'value': adresse_email
            }
        ],
        "addresses": [
            {
                "formattedValue": "14 rue parmentier saint fons"
            }
        ],
        "memberships": [
            {
                "contactGroupMembership": {
                    "contactGroupResourceName": "contactGroups/1c576d7f8bd43294"
                }
            }
        ]

    }).execute()
