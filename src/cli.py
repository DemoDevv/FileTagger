"""CLI parsing module"""

import argparse


def parse_arguments():
    """
    Parse the command line arguments
    :return: the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="FileTagger permet de tagger des fichiers suivant des mots-clés."
    )
    parser.add_argument(
        "-p", "--path", help="Chemin du dossier à analyser", required=True
    )
    parser.add_argument(
        "-t",
        "--tags",
        help="Liste des tags à rechercher",
        nargs="+",
        required=True,
    )
    parser.add_argument("-v", "--verbose", help="Affiche les logs", action="store_true")

    return parser.parse_args()
