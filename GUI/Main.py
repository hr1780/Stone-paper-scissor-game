from random import randint
import tkinter as tk
root = tk.Tk()
root.geometry('200x200+10+20')
root.title('GAME')
l = tk.Label(root,text ="Click on any Image:")
l.place(x=0.5,y=0.5,width=200,height=20)
photo=tk.PhotoImage(file="rock.png")
R = tk.Button(root, text ="Rock",fg='RED',image=photo,padx=30,pady=40,command= lambda: action('Rock'))
R.place(x=20,y=25,width=70,height=50)
p1=tk.PhotoImage(file="sc.png")
S = tk.Button(root, text ="Scissor",fg='RED',image=p1,padx=30,pady=40,command= lambda: action('Scissor'))
S.place(x=110,y=25,width=70,height=50)
p2=tk.PhotoImage(file="paper.png")
P = tk.Button(root,image=p2,padx=30,pady=40,text ="Paper",fg='RED',command= lambda: action('Paper'))
P.place(x=65,y=90,width=70,height=50)


def action(player):
    chosen = randint(1,3)

    if chosen == 1:
        computer = 'Rock'
    elif chosen==2:
        computer = 'Paper'
    elif chosen==3:
        computer = 'Scissor'
    l1 = tk.Label(root,text="Computer: "+computer+" V/S "+" Payer: "+player,fg='blue')
    l1.place(x=0.5,y=140,width=200,height=20)
    if (player == computer):
        res="Draw"
    elif(player == 'Rock' and computer == 'Scissor'):
        res="Player Wins"
    elif(player == 'Rock' and computer == 'Paper'):
        res="Computer Wins"
    elif( player == 'Paper' and computer == 'Rock'):
        res="Computer Wins"
    elif(player == 'Paper' and computer == 'Scissor'):
        res="Computer Wins"
    elif(player == 'Scissor' and computer == 'Paper'):
        res="Player Wins"
    elif(player == 'Scissor' and computer == 'Rock'):
        res="Computer Wins"
    l2 = tk.Label(root,text="Result is : "+res,fg='blue')
    l2.place(x=10,y=170,width=200,height=20)


        

