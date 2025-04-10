import argparse
import Config
import os


def parse_args_and_set():
    parser = argparse.ArgumentParser(
        description="You are using MyBrain!\nImport PDF files, extract and clean their content, and store semantically indexed passages in FAISS and SQLite databases for powerful contextual search."
    )

    parser.add_argument(
        "-e",
        "--edit",
        action="store_false",
        help="Enable manual post-editing of imported texts (default: off)",
    )

    parser.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="Overwrite existing databases if they exist",
    )

    project = parser.add_argument_group("Project-based database configuration")
    project.add_argument(
        "-p",
        "--project-name",
        type=str,
        help="Name of the project (default: Definition in .config)",
    )

    project.add_argument(
        "-d",
        "--shared-db-dir",
        type=str,
        help="Single directory path to use for both FAISS and SQLite databases",
    )

    file = parser.add_argument_group("File-based database configuration")
    file.add_argument(
        "-f",
        "--faiss-path",
        type=str,
        help="Path to the FAISS database (requires --sqlite-path)",
    )
    file.add_argument(
        "-s",
        "--sqlite-path",
        type=str,
        help="Path to the SQLite database (requires --faiss-path)",
    )

    parser.add_argument("inputs", nargs="*", help="Optional input files of type pdf")

    args = parser.parse_args()

    Config.overwrite = args.overwrite
    Config.edit = args.edit

    project_mode = args.project_name or args.shared_db_dir
    file_mode = args.faiss_path or args.sqlite_path

    if project_mode and file_mode:
        parser.error(
            "Choose either project-based or file-based configuration — not both."
        )

    if file_mode:
        if not args.faiss_path or not args.sqlite_path:
            parser.error(
                "Both --faiss-path and --sqlite-path are required for file-based configuration."
            )
        else:
            Config.set_faiss_path(args.faiss_path)
            Config.set_sqlite_path(args.sqlite_path)
    if project_mode:
        if args.project_name and args.shared_db_dir:
            Config.set_faiss_dir_name(args.shared_db_dir, args.project_name)
            Config.set_sqlite_dir_name(args.shared_db_dir, args.project_name)
        elif args.project_name:
            Config.set_faiss_name(args.project_name)
            Config.set_sqlite_name(args.project_name)
        else:
            Config.set_faiss_dir(args.shared_db_dir)
            Config.set_sqlite_dir(args.shared_db_dir)

    for input_path in args.inputs:
        if not os.path.isfile(input_path) or not input_path.lower().endswith(".pdf"):
            parser.error(f"Warning: Input path is not a valid pdf file: {input_path}")

    # Example debug output:
    print(f"Edit: {args.edit}")
    print(f"Overwrite: {args.overwrite}")
    print(f"FAISS path: {args.faiss_path}")
    print(f"SQLite path: {args.sqlite_path}")
    print(f"Shared DB path: {args.shared_db_dir}")
    print(f"Project name: {args.project_name}")
    print(f"Inputs: {args.inputs}")

    return args.inputs
