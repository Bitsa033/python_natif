from tkinter import *
from tkinter import filedialog

def oen_explorer():
    link=filedialog.askdirectory(initialdir='/',title='Nom du dossier')

#interface graaphique
fen=Tk()
#boite dans l'interface
frame=Frame(fen,width=480,height=480,background='green')
# titre de l'interface
label_title=Label(frame,text='Internet downloader',
     background='white',padx=200,pady=5
)
# message utilisateur
link_title=Label(frame,text='Entrer le lien de la vidéo:',
    padx=5,pady=5,background='green'
)
# lien du fichier vidéo saisie par l'utilisateur
link_input=Entry(frame,width=50,textvariable='entry',borderwidth=2)
# nom du repertoire de sauvegarde
dir_title=Label(frame,text='Enregistrer sous:',
    padx=5,pady=5,background='green'
)
# lien du repertoire de sauvegarde
dir_input=Entry(frame,width=35,textvariable='entry',borderwidth=2)
#bouton pour ouvrir l'explorateur de fichier
explorer_bouton=Button(frame,text="Ouvrir",
    borderwidth='3',width=11,command=oen_explorer
)
#barre de progression
# bar_progress=me(frame)

# bar_progress.place(x=1,y=120)
explorer_bouton.place(x=357,y=80)
dir_input.place(x=140,y=80)
dir_title.place(x=1,y=80)
link_input.place(x=140,y=50)
link_title.place(x=1,y=50)
label_title.place(x=0,y=0)
frame.pack()


fen.mainloop()