from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import time

def close():
    fen.destroy()

def download():
    step=20
    x=0
    while(x<step):
        time.sleep(1)
        progress_bar['value']+=5
        x+=1
        fen.update_idletasks()
        if x==step:
            messagebox.showinfo('Message','Téléchargement terminé!')
            fen.destroy()
    

def open_dir():
    link=filedialog.askdirectory()
    save_as.insert(0,link)


# on genere la fenetre principale
fen=Tk()
fen.geometry("500x200")
# frame du formulaire
frame_form=Frame(fen,background="#288345",width=800,height=500)
link_file=Entry(frame_form,font=('helvetica',10),width=67)
save_as=Entry(frame_form,font=('helvetica',10),width=53)
open_dir_button=Button(frame_form,width=15,font=('helvetica',7),background="blueviolet",text="Enregistrer sous",command=open_dir)
progress_bar=ttk.Progressbar(frame_form,length=470)
validation_button=Button(frame_form,width=20,background="blueviolet",text="Telécharger",command=download)
reset_button=Button(frame_form,width=20,background="blueviolet",text="Pause")
stop_button=Button(frame_form,width=20,background="blueviolet",text="Fermer",command=close)
# affichages
link_file.place(x=5,y=30)
# link_file.bind("<1>", file())
save_as.place(x=5,y=70)
open_dir_button.place(x=380,y=70)
progress_bar.place(x=5,y=120)
validation_button.place(x=10,y=160)
reset_button.place(x=160,y=160)
stop_button.place(x=310,y=160)
frame_form.place(x=0,y=0)
# on affiche la fenetre principale
        
fen.mainloop()