import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys


def get_file_paths_gui_tkinter():
    # Root-Fenster erzeugen und verstecken
    root = tk.Tk()
    root.withdraw()

    # Dialog zum Auswählen mehrerer PDF-Dateien öffnen
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files", filetypes=[("PDF files", "*.pdf")]
    )

    # Ergebnis ausgeben
    if file_paths:
        print("Choosen files:")
        for i, path in enumerate(file_paths):
            print(f"{i}.", path)
    else:
        print("No files selected!")

    return file_paths


def get_file_paths_gui_qt5():

    app = QApplication(sys.argv)

    # Datei-Dialog öffnen
    files, _ = QFileDialog.getOpenFileNames(
        None, "Select PDF files", "", "PDF files (*.pdf)"
    )
    # Ergebnis ausgeben
    if files:
        print("Choosen files:")
        for i, path in enumerate(files):
            print(f"{i}.", path)
    else:
        print("No files selected!")

    return files
