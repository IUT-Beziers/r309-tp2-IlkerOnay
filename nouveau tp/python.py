#ONAY Ilker
#16/12 last edit


from tkinter import *
from PIL import Image,ImageTk

x_coord=0                       #flag creation variable
y_coord=0
flag_cursor=0
flag_switch=0
flag_routeur=0
flag_pc=0
flag_ligne=0
flag_drag_and_drop=0


def menu_cursor():  # permet de mettre tout les flag a zéro permet de cliquer avec le curseur sans rien modifier ou ajouter (activer avec le button cursor)
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=0
    flag_routeur=0
    flag_pc=0
    flag_ligne=0
    flag_drag_and_drop=0
    
def menu_switch(): # command du button switch permet de placer un switch grace a la fonction pose
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=1
    flag_routeur=0
    flag_pc=0
    flag_ligne=0
    flag_drag_and_drop=0

def menu_routeur(): # command du boutton routeur permet de placer un routeur quand on clique grace a la fonction pose
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=0
    flag_routeur=1
    flag_pc=0
    flag_ligne=0
    flag_drag_and_drop=0

def menu_pc(): # command du bouttoun pc permet de placer un pc quand on clique grace a la fonction pose
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=0
    flag_routeur=0
    flag_pc=1
    flag_ligne=0
    flag_drag_and_drop=0
    print("pc")

def menu_ligne(): # command du boutton ligne permet de crée une ligne verticale ou horizontale selon l'état du flag (changeable avec la touche "Ctrl") grace a la fonction pose et pose2
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=0
    flag_routeur=0
    flag_pc=0
    flag_ligne=1
    flag_drag_and_drop=0

def menu_drag_and_drop(): #focntion pour mettre le flag drag and drop ( NE MARCHE PAS)
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc
    flag_cursor=0
    flag_switch=0
    flag_routeur=0
    flag_pc=0
    flag_ligne=0
    flag_drag_and_drop=1

#Création des canvas et des bouttons du menu
root= Tk()
root.geometry("720x520")
menucan=Canvas(root,width=720,height=25)
menucan.pack(side=TOP)
MenuButton1=Button(menucan,text="Cursor",command=menu_cursor)
MenuButton1.grid(row=0,column=0)
MenuButton2=Button(menucan,text="Switch",command=menu_switch)
MenuButton2.grid(row=0,column=1)
MenuButton2=Button(menucan,text="Pc",command=menu_pc)
MenuButton2.grid(row=0,column=2)
MenuButton2=Button(menucan,text="Routeur",command=menu_routeur)
MenuButton2.grid(row=0,column=3)
MenuButton2=Button(menucan,text="Ligne",command=menu_ligne)
MenuButton2.grid(row=0,column=4)

can=Canvas(root,bg="grey",width=720,height=520)
can.pack(side=BOTTOM)

#les images 
img1=(Image.open("../NOUVEAU TP/switch1.png"))
resized_switch= img1.resize((50,50))
switch_img= ImageTk.PhotoImage(resized_switch)


img2=(Image.open("../NOUVEAU TP/router-1.png"))
resized_routeur= img2.resize((50,50))
routeur_img= ImageTk.PhotoImage(resized_routeur)

img3=(Image.open("../NOUVEAU TP/pc.png"))
resized_pc= img3.resize((50,50))
pc_img= ImageTk.PhotoImage(resized_pc)




#touche echappe pour fermer le "logiciel"
def destroy(event):
    root.destroy()

#touche s pour poser un switch 
def switch(event):
    x_coord,y_coord= event.x, event.y
    can.create_image(x_coord,y_coord,image=switch_img)

#touche c pour poser un pc
def pc(event):
    x_coord,y_coord= event.x, event.y
    can.create_image(x_coord,y_coord,image=pc_img)

#touche r pour poser un routeur
def routeur(event):
    x_coord,y_coord= event.x, event.y
    can.create_image(x_coord,y_coord,image=routeur_img)




#Fonction qui check les flags et qui pose l'image selon la selection
def pose(event):
    global flag_switch,flag_routeur,flag_cursor,flag_drag_and_drop,flag_ligne,flag_pc,x_coord,y_coord
    x_coord,y_coord= event.x, event.y
    if y_coord > 25 :
        if flag_switch == 1 :
            can_switch=can.create_image(x_coord,y_coord,image=switch_img)
        if flag_routeur == 1 :
            can_routeur=can.create_image(x_coord,y_coord,image=routeur_img)
        if flag_pc == 1 :
            can_pc=can.create_image(x_coord,y_coord,image=pc_img)
        if flag_ligne == 1 :
            print(x_coord,y_coord)
            return x_coord,y_coord             
    else:
        return

#fonction pour tracer les lignes grâce à la fonction pose qui renvoie les coordonnées lors du clique et cette fonction récupére les coordonnées lors du relachement du clique
def pose2(event):
    global flag_ligne,x_coord,y_coord
    if flag_ligne == 1:     
        can_ligne=can.create_line(x_coord,y_coord,event.x,y_coord,fill="black",width=3) # Vertical
    if flag_ligne == 2 :
        can_ligne=can.create_line(x_coord,y_coord,x_coord,event.y,fill="black",width=3) # Vertical


#fonction pour mettre à jour le flag (pour dessiner en vertical ou horizontale), change l'orientation quand on appuie sur la touche "ctrl"
def ligne(event):
    global flag_ligne
    if flag_ligne == 0 :
        flag_ligne = 1
    elif flag_ligne == 1 :
        flag_ligne += 1
    elif flag_ligne == 2 :
        flag_ligne =1


#Ne marche pas pour l'instant
def change(event):
    id=can.find_closest(event.x,event.y)



#bind
root.bind("<c>", pc)
root.bind("<s>", switch)
root.bind("<r>", routeur)
root.bind("<Escape>", destroy)
root.bind("<Button-1>", pose)
root.bind("<Button-3>",change)
root.bind("<ButtonRelease-1>",pose2)
root.bind("<Control-KeyRelease>",ligne)
#root.bind("<B3-Motion>", drag)


#lancement de la fenetre
root.title("Packet Tracer Free.Exe ")
root.mainloop()