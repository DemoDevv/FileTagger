from pathlib import Path

from src.analyzer.local_document_analyzer import LocalDocumentAnalyzer


def test_analyze_document_with_incompatible_extension():
    local_document_analyzer = LocalDocumentAnalyzer(["tag_test"])
    file_path = Path("tests/resources/data.zip")

    assert local_document_analyzer.analyze_document(file_path) is None
