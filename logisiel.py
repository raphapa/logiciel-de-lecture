import tkinter as tk
from tkinter import filedialog, Text
import pyttsx3

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.pdf *.docx *.txt")])
    if filepath:
        # Ici, vous ajouteriez le code pour lire le fichier sélectionné et stocker le texte dans une variable.
        print(filepath)  # Placeholder pour la logique de traitement de fichier.

def speak_text():
    engine = pyttsx3.init()
    # Ici, vous utiliseriez la variable contenant le texte du fichier chargé.
    engine.say("Hello, this is a test")
    engine.runAndWait()

app = tk.Tk()
app.title("Lecteur de courrier")

load_button = tk.Button(app, text="Charger un fichier", padx=10, pady=5, fg="white", bg="#263D42", command=load_file)
load_button.pack()

speak_button = tk.Button(app, text="Lire le texte", padx=10, pady=5, fg="white", bg="#263D42", command=speak_text)
speak_button.pack()

app.mainloop()
