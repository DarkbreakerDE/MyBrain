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
        title="PDF-Dateien auswählen", filetypes=[("PDF Dateien", "*.pdf")]
    )

    # Ergebnis ausgeben
    print("Ausgewählte Dateien:")
    for path in file_paths:
        print(path)

    return file_paths


def get_file_paths_gui_qt5():

    app = QApplication(sys.argv)

    # Datei-Dialog öffnen
    files, _ = QFileDialog.getOpenFileNames(
        None, "PDF-Dateien auswählen", "", "PDF Dateien (*.pdf)"
    )
    # Ergebnis ausgeben
    print("Ausgewählte Dateien:")
    for path in files:
        print(path)

    return files
