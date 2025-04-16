import requests
import pandas as pd

# URL de l'API
base_url = "https://examen-api.s3.eu-west-1.amazonaws.com/Student/"

# ID de l'étudiant
student_id = "70"  # Remplace par l'ID de l'étudiant souhaité

# Construire l'URL complète
url = f"{base_url}{student_id}"

# Faire une requête GET
response = requests.get(url)

# Vérifier le statut de la réponse
if response.status_code == 200:
    # Afficher le contenu brut de la réponse
    raw_data = response.json()
    print("Contenu brut de la réponse :")
    print(raw_data)

    # transoform the json into a dataframe
    #df = pd.DataFrame(raw_data)
    #print(df)

else:
    print("Erreur :", response.status_code)


