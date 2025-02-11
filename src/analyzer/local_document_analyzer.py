import logging
from pathlib import Path
from typing import List, Union

from src.analyzer.document_analyzer import DocumentAnalyzer


class LocalDocumentAnalyzer(DocumentAnalyzer):
    def __init__(self, tags_list: List[str]):
        super().__init__(tags_list)

    def process_directory(
        self,
        directory_path: Union[Path, str],
        output_file: str = "tagged_documents.xlsx",
    ):
        """
        Analyse tous les documents d'un répertoire et ses sous-répertoires
        """
        directory_path = Path(directory_path)
        all_files = []

        for file_path in directory_path.rglob("*"):
            if (
                file_path.is_file()
                and file_path.suffix.lower() in self.supported_extensions
            ):
                all_files.append(file_path)

        logging.info(f"Trouvé {len(all_files)} fichiers à analyser")
