from .analyzer.local_document_analyzer import LocalDocumentAnalyzer
from .cli import parse_arguments


def main():
    args = parse_arguments()

    local_file_analyzer = LocalDocumentAnalyzer(args.tags, args.verbose)
    local_file_analyzer.process_directory(args.path)
