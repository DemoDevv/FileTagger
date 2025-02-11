import logging
from pathlib import Path
from typing import List, Set, Union

import docx
import pandas as pd
import PyPDF2


class DocumentAnalyzer:
    def __init__(self, tags_list: List[str]):
        """
        Initialise l'analyseur avec une liste de tags
        """
        self.tags = set(tag.lower() for tag in tags_list)
        self.supported_extensions = {
            ".pdf",
            ".doc",
            ".docx",
            ".xlsx",
            ".xls",
            ".txt",
        }

        # Configuration du logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def analyze_document(self, file_path: Path) -> Union[dict, None]:
        """
        Analyse un document et retourne les tags trouvés
        """
        try:
            extension = file_path.suffix.lower()
            if extension not in self.supported_extensions:
                return None

            text_content = self._extract_text(file_path, extension)
            found_tags = self._find_tags(text_content)

            if found_tags:
                return {
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "tags": list(found_tags),
                }

        except Exception as e:
            logging.error(f"Erreur lors de l'analyse de {file_path}: {str(e)}")

    def _extract_text(self, file_path: Path, extension: str) -> str:
        """
        Extrait le texte d'un document selon son type
        """
        try:
            if extension == ".pdf":
                with open(file_path, "rb") as file:
                    reader = PyPDF2.PdfReader(file)
                    return " ".join(
                        page.extract_text() for page in reader.pages
                    )

            elif extension in [".docx", ".doc"]:
                doc = docx.Document(file_path.__str__())
                return " ".join(paragraph.text for paragraph in doc.paragraphs)

            elif extension in [".xlsx", ".xls"]:
                df = pd.read_excel(file_path)
                return " ".join(df.astype(str).values.flatten())

            elif extension == ".txt":
                with open(
                    file_path, "r", encoding="utf-8", errors="ignore"
                ) as file:
                    return file.read()

        except Exception as e:
            logging.error(f"Erreur d'extraction pour {file_path}: {str(e)}")
            return ""

        return ""

    def _find_tags(self, text: str) -> Set[str]:
        """
        Trouve les tags dans le texte
        """
        words = set(text.lower().split())
        return self.tags.intersection(words)
