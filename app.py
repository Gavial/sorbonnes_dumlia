import streamlit as st
import requests

# Définir l'URL du point de terminaison FastAPI
API_URL = 'https://api-913491001221.europe-west1.run.app/predict'

# CSS pour améliorer le designe
st.markdown("""
    <style>
    /* Style général */
    body {
        background-color: #f9f9f9;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #4A90E2;
        font-size: 2.5em;
    }
    h2, h3 {
        color: #333333;
    }
    .stRadio > div {
        display: flex;
        justify-content: center;
        color: #4A90E2;
    }
    .css-17eq0hr {
        background-color: #ffffff !important;
    }
    /* Style des boutons */
    button {
        background-color: #4A90E2 !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.75em 1.25em;
        display: inline-block;
        margin: 0 10px; /* Ajoute un espacement horizontal entre les boutons */
    }
    /* Style des champs de saisie */
    .stTextInput, .stNumberInput, .stCheckbox, .stSelectbox {
        padding: 0.5em;
        background: #F8F8FF;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    /* Style des "+" et "-" des champs de saisie */     
    .number-input-button { 
        display: inline-block;
        margin: 0 10px; 
    }            
    </style>
""", unsafe_allow_html=True)

# Streamlit app
def main():
    st.markdown("<h1 style='text-align: center;'>Analyse des données de santé cardiaque</h1>", unsafe_allow_html=True)
    
    # Liste des pages
    pages = ["Descriptif", "Dictionnaire", "Prédiction"]

    # Sélection de la page
    selected_page = st.sidebar.radio("Volet de navigation :", pages)

    # Page "Descriptif"
    if selected_page == "Descriptif":
        st.header("Description du projet")
        st.subheader("Prédiction et Visualisation des Maladies Cardiaques")
        st.write("""Développer un tableau de bord interactif pour prédire les risques de maladies cardiaques en fonction des données de santé des patients.""")
        st.markdown("""1. **Données Kaggle** :  
        - <u>*Heart Disease UCI*</u> ; [https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)""",
        unsafe_allow_html=True)
        st.markdown("""2. **Technologies** :  
        - <u>*Python*</u> ; Jupyter Notebook  
        - <u>*Streamlit*</u> ; pour le tableau de bord interactif  
        - <u>*Scikit-Learn*</u> ; pour les modèles de machine learning  
        - <u>*Matplotlib/Seaborn*</u> ; pour les visualisations
        """, 
        unsafe_allow_html=True)
        st.markdown("""3. **Fonctionnalités** :  
        - <u>*Visualisation des données*</u> ; Distribution des caractéristiques des patients (âge, sexe, pression artérielle, etc.).  
        - <u>*Modèles de prédiction*</u> ; Utilisation de modèles de machine learning (par exemple, logistic regression, decision tree, random forest) pour prédire les risques de maladies cardiaques.  
        - <u>*Interface utilisateur*</u> ; Permettre aux utilisateurs de saisir leurs données de santé et d'obtenir une prédiction du risque.  
        - <u>*Analyse des caractéristiques*</u> ; Afficher les caractéristiques les plus influentes pour les prédictions.""", 
        unsafe_allow_html=True)
        st.markdown("""4. **Avantages** :  
        - <u>*Pertinence*</u> ; Correspond à notre apprentissage en machine learning, deep learning, et traitement de données.  
        - <u>*Impact*</u> ; Utilité pratique et impact potentiel sur la santé publique.  
        - <u>*Accessibilité*</u> ; Données disponibles gratuitement sur Kaggle, outils utilisés gratuits.""", 
        unsafe_allow_html=True)


    # Page "Dictionnaire"
    if selected_page == "Dictionnaire":
        st.header("Dictionnaire de données")

        st.write("""
        Description des colonnes présentes dans le dataset **heart_disease_uci.csv** :
        """)

        st.write("1. **id** : Identifiant unique pour chaque patient. Cette colonne est utilisée pour l'identification et n'a pas de valeur dans les analyses statistiques.")

        st.write("2. **age** : Âge du patient en années. Cette caractéristique est importante car l'âge est un facteur de risque significatif pour les maladies cardiaques.")

        st.write("3. **sex** : Sexe du patient. C’est un facteur de risque pour les maladies cardiaques, avec des différences dans la prévalence et la gravité entre les sexes.")

        st.write("4. **dataset** : Lieu d'études.")

        st.markdown("""5. **cp** : Type de douleur thoracique. Il s'agit d'une variable catégorielle avec plusieurs niveaux ;  
        - Douleur angineuse typique  
        - Douleur angineuse atypique  
        - Douleur non angineuse  
        - Pas de douleur
        """)

        st.write("6. **trestbps** : Pression artérielle au repos en mm Hg.")

        st.write("7. **chol** : Taux de cholestérol sérique en mg/dl. Un taux élevé de cholestérol est associé à un risque accru de maladies cardiaques.")

        st.markdown("""8. **fbs** : Glycémie à jeun (fbs > 120 mg/dl) ;  
        - <u>*True*</u> : Glycémie élevée  
        - <u>*False*</u> : Glycémie normale
        """, unsafe_allow_html=True)

        st.markdown("""9. **restecg** : Résultats de l'électrocardiogramme au repos ;  
        - Normal  
        - Présence de signes d'une anomalie st  
        - Présence de signes d'une anomalie hypertrophie ventriculaire gauche
        """)

        st.write("10. **thalch** : Fréquence cardiaque maximale atteinte pendant l'exercice.")

        st.markdown("""11. **exang** : Indication d'angine induite par l'exercice ;  
        - <u>*True*</u> : Oui  
        - <u>*False*</u> : Non
        """, unsafe_allow_html=True)

        st.write("12. **oldpeak** : Dépression du segment ST induite par l'exercice par rapport au repos. Cela peut indiquer une maladie cardiaque si la dépression est significative.")

        st.markdown("""13. **slope** : Pente du segment ST au pic de l'exercice ;  
        - Pente ascendante  
        - Pente plate  
        - Pente descendante
        """)

        st.write("14. **ca** : Nombre de vaisseaux principaux (0-3) colorés par fluoroscopie. Plus le nombre est élevé, plus il y a de vaisseaux obstructifs.")

        st.markdown("""15. **thal** : Thalassémie (anomalie génétique) ;  
        - Normal  
        - Fixation défectueuse  
        - Fixation réduite
        """)

        st.markdown("""16. **num** : Niveau de la présence de la maladie cardiaque ;  
        - <u>*0*</u> : Absence de maladie cardiaque  
        - <u>*1*</u> : Présence de maladie cardiaque faible  
        - <u>*2*</u> : Présence de maladie cardiaque moyenne  
        - <u>*3*</u> : Présence de maladie cardiaque grave  
        - <u>*4*</u> : Présence de maladie cardiaque sévère
        """, unsafe_allow_html=True)

    # Page "Prédiction"
    elif selected_page == "Prédiction":
        st.header("Entrez vos données de santé ci-dessous pour obtenir une prédiction :")
        
        # Champs de saisie pour la prédiction
        age = st.number_input("Age", min_value=0, max_value=130, value=50)
        sex = st.selectbox("Genre (0 = femme, 1 = homme)", [0, 1], index=1)
        dataset = st.text_input("Lieu d'études", value="Cleveland")
        cp = st.selectbox("Type de douleur thoracique (de faible à intense)", [1, 2, 3, 4], index=0)
        trestbps = st.number_input("Pression artérielle au repos en mm Hg", min_value=0.0, max_value=300.0, value=120.0)
        chol = st.number_input("Taux de cholestérol sérique en mg/dl", min_value=0.0, max_value=700.0, value=200.0)
        fbs = st.checkbox("Glycémie à jeun (à cocher si vrai)", value=False)
        restecg = st.selectbox("Electrocardiogramme au repos", ["normal", "lv hypertrophy", "st-t abnormality"], index=0)
        thalch = st.number_input("Fréquence cardiaque maximale atteinte pendant l'exercice", min_value=0.0, max_value=300.0, value=140.0)
        exang = st.checkbox("Angine induite par l'exercice (à cocher si vrai)", value=False)
        oldpeak = st.number_input("Dépression du segment ST", min_value=0.0, max_value=7.0, value=0.0)
        slope = st.selectbox("Pente du segment ST au pic de l'exercice", ["flat", "upsloping", "downsloping"], index=0)
        #ca = st.number_input("Nombre de vaisseaux principaux colorés", min_value=0.0, max_value=4.0, value=0.0)
        ca = st.selectbox("Nombre de vaisseaux principaux colorés", ["0.0", "1.0", "2.0","3.0","nan"], index=0)
        thal = st.selectbox("Thalassémie", ["normal", "reversable defect", "fixed defect"], index=0)

        # Soumission du formulaire
        if st.button("Envoyer"):
            payload = {
                'age': age,
                'sex': sex,
                'dataset': dataset,
                'cp': cp,
                'trestbps': trestbps,
                'chol': chol,
                'fbs': fbs,
                'restecg': restecg,
                'thalch': thalch,
                'exang': exang,
                'oldpeak': oldpeak,
                'slope': slope,
                'ca': ca,
                'thal': thal,
            }
            response = requests.get(API_URL, params=payload)
            if response.status_code == 200:
                prediction = response.json().get('prediction')

                # Traduire la prédiction numérique en message
                if prediction == 0:
                    message = "Patient en bonne santé"
                    color = "green"  # Couleur pour la bonne santé
                elif prediction == 1:
                    message = "Patient atteint de maladie"
                    color = "darkred"  # Couleur rose foncé (ou utiliser un code hexadécimal)
                else:
                    message = "Prédiction non valide"  # Au cas où la prédiction ne serait pas 0 ou 1
                    color = "black"  # Couleur par défaut

                # Afficher le message avec la couleur appropriée
                st.markdown(f"<h1 style='color: {color};'>{message}</h1>", unsafe_allow_html=True)
            else:
                st.write("Erreur :", response.status_code, response.text)

if __name__ == "__main__":
    main()
