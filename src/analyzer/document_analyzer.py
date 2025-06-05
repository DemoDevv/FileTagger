from __future__ import print_function
from pathlib import Path
from typing import List, Optional, Set
import logging

from src.analyzer.readers import (
    doc_reader,
    docx_reader,
    pdf_reader,
    pptx_reader,
    txt_reader,
    xlsx_reader,
)


class DocumentAnalyzer:
    def __init__(
        self,
        tags_list: List[str],
        logging_level: bool = True,
    ):
        """
        Initialise l'analyseur avec une liste de tags
        """
        self.tags = set(tag.lower() for tag in tags_list)
        self.supported_extensions = {
            ".pdf": pdf_reader,
            ".doc": doc_reader,
            ".docx": docx_reader,
            ".xlsx": xlsx_reader,
            ".xls": xlsx_reader,
            ".txt": txt_reader,
            ".pptx": pptx_reader,
        }

        if logging_level:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
            )

    def analyze_document(self, file_path: Path) -> Optional[dict]:
        """
        Analyse un document et retourne les tags trouvés
        """
        try:
            extension = file_path.suffix.lower()

            if extension not in self.supported_extensions:
                return None

            text_content = self._extract_text(file_path, extension)

            if text_content is None:
                return None

            found_tags_title = self._find_tags(file_path.stem.lower())
            found_tags = self._find_tags(text_content.lower())
            found_tags.update(found_tags_title)

            if found_tags_title or found_tags:
                return {
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "tags": ",".join(sorted(found_tags)),
                }

        except Exception as e:
            logging.error(f"Erreur lors de l'analyse de {file_path}: {str(e)}")

    def _extract_text(self, file_path: Path, extension: str) -> Optional[str]:
        """
        Extrait le texte d'un document selon son type
        """
        try:
            return self.supported_extensions[extension](file_path)

        except Exception as e:
            logging.error(f"Erreur d'extraction pour {file_path}: {str(e)}")
            return None

    def _find_tags(self, text: str) -> Set[str]:
        """
        Trouve les tags dans le texte
        """
        return {tag for tag in self.tags if tag.lower() in text}
