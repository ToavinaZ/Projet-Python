import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


def calculer_moyenne(notes):
    return sum(notes) / len(notes)

def attribuer_rang(moyennes):
    rangs = sorted(range(len(moyennes)), key=lambda k: moyennes[k], reverse=True)
    return [r+1 for r in rangs]

def ajouter():
    nom_eleve = ajout_nom_eleve.get()
    notes_eleve = [float(ajout_notes_matieres[i].get()) for i in range(nombre_matieres)]

    noms_eleves.append(nom_eleve)
    notes_par_eleve.append(notes_eleve)

    ajout_nom_eleve.delete(0, tk.END)
    for entry in ajout_notes_matieres:
        entry.delete(0, tk.END)

def calculer_afficher():
    if not noms_eleves or not notes_par_eleve:
        messagebox.showerror("Erreur", "Veuillez ajouter au moins un élève avec ses notes.")
        return

    moyennes = [calculer_moyenne(notes) for notes in notes_par_eleve]

    
    rangs = attribuer_rang(moyennes)

    
    result_label.config(text="Résultats :")
    for i in range(len(noms_eleves)):
        result_label.config(text=result_label.cget("text") + f"\n{noms_eleves[i]} - Moyenne : {moyennes[i]} - Rang : {rangs[i]}")

# Interface graphique
root = tk.Tk()
root.title("Gestion des notes")

nombre_matieres = int(input("Entrez le nombre de matières : "))

noms_eleves = []
notes_par_eleve = []

Label(root, text="Nom de l'élève :").grid(row=0, column=0)
ajout_nom_eleve = Entry(root)
ajout_nom_eleve.grid(row=0, column=1)


ajout_notes_matieres = []
for i in range(nombre_matieres):
    Label(root, text=f"Note en matière {i+1} :").grid(row=i+1, column=0)
    ajout_notes_matiere = Entry(root)
    ajout_notes_matiere.grid(row=i+1, column=1)
    ajout_notes_matieres.append(ajout_notes_matiere)

Boutton = Button(root, text="Ajouter", command=ajouter)
Boutton.grid(row=nombre_matieres+1, column=0, columnspan=2)


calculer_afficher_boutton = Button(root, text="Calculer et Afficher", command=calculer_afficher)
calculer_afficher_boutton.grid(row=nombre_matieres+2, column=0, columnspan=2)


result_label = Label(root, text="")
result_label.grid(row=nombre_matieres+3, column=0, columnspan=2)


root.mainloop()
