# import numpy as np
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer


# def main():
#     """Main function."""
#     dataset = pd.read_excel("ressources/data.xlsx")

#     features = [
#         x.replace(" ", "__").split("/")
#         for x in dataset["Chemin d'accès"].unique().tolist()
#     ]

#     features = [" ".join(feature[3:]) for feature in features]

#     countVectorizer = CountVectorizer()
#     X = countVectorizer.fit_transform(features)

#     # Obtenir les mots et leur fréquence totale
#     somme_frequences = np.array(X.sum(axis=0)).flatten()  # Somme par colonne
#     vocabulaire = countVectorizer.get_feature_names_out()
#     vocabulaire = map(lambda x: x.replace("__", " "), vocabulaire)

#     # Combiner mots et fréquences, puis trier par fréquence croissante
#     mots_avec_frequences = sorted(
#         zip(vocabulaire, somme_frequences), key=lambda x: x[1]
#     )

#     # Affichage des mots triés par fréquence
#     for mot, freq in mots_avec_frequences:
#         print(f"{mot}: {freq}")
from src.analyzer.local_document_analyzer import LocalDocumentAnalyzer


def main():
    local_file_analyzer = LocalDocumentAnalyzer(["python", "java", "c++"])
    local_file_analyzer.process_directory("./ressources")
