import logging
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import List, Union

import pandas as pd

from src.analyzer.document_analyzer import DocumentAnalyzer


class LocalDocumentAnalyzer(DocumentAnalyzer):
    def __init__(self, tags_list: List[str], logging_level: bool):
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

        # Analyse les fichiers en parallèle
        results = []
        with ProcessPoolExecutor() as executor:
            future_to_file = {
                executor.submit(self.analyze_document, file_path): file_path
                for file_path in all_files
            }

            for future in future_to_file:
                file_path = future_to_file[future]

                logging.info(f"Analyse de {file_path}")

                result = future.result()
                if result:
                    results.append(result)

        # Exporte les résultats
        if results:
            df = pd.DataFrame(results)
            df.to_excel(output_file, index=False)
            logging.info(f"Résultats exportés dans {output_file}")
            logging.info(f"Trouvé {len(results)} fichiers contenant des tags")
        else:
            logging.warning("Aucun tag trouvé dans les documents")

        return results
