from pathlib import Path

from src.analyzer.local_document_analyzer import LocalDocumentAnalyzer


def test_analyze_document_with_incompatible_extension():
    local_document_analyzer = LocalDocumentAnalyzer(["tag_test"])
    file_path = Path("tests/ressources/data.zip")

    assert (
        local_document_analyzer._extract_text(
            file_path, file_path.suffix.lower()
        )
        is None
    )


def test_analyze_document_with_compatible_extension():
    local_document_analyzer = LocalDocumentAnalyzer(["tag_test"])
    file_path = Path("tests/ressources/data.txt")

    assert (
        local_document_analyzer._extract_text(
            file_path, file_path.suffix.lower()
        )
        == ""
    )
