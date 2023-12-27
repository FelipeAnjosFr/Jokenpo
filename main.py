from tkinter import *
from random import randint

root = Tk()
root.title("JOKENPÔ")
root.geometry("800x600")
root.minsize(800, 600)
root.maxsize(800, 600)
root.config(bg="#383838")


margin = Canvas(root, bg="#383838", width=800, height=60, bd=0, highlightthickness=0, relief="ridge")
margin.grid(row=0, column=0, columnspan=3)

img = PhotoImage(file="images/header.png")
header = Label(root, image=img, bd=0, highlightthickness=0, relief="ridge")
header.grid(row=1, column=0, columnspan=3)


def game_menu():
    global stone_img
    global paper_img
    global scissor_img

    global stone
    global paper
    global scissor

    margin2 = Canvas(root, bg="#383838", width=600, height=80, bd=0, highlightthickness=0, relief="ridge")
    margin2.grid(row=2, column=0, columnspan=3)

    stone_img = PhotoImage(file="images/stone_resized.png")
    stone = Button(root, image=stone_img, command=lambda: [stone_choice(), start_game()], bg="#383838", activebackground="#383838",bd=0, highlightthickness=0, relief="ridge")
    stone.grid(row=3, column=0)

    paper_img = PhotoImage(file="images/paper_resized.png")
    paper = Button(root, image=paper_img, command=lambda: [paper_choice(), start_game()], bg="#383838", activebackground="#383838" ,bd=0, highlightthickness=0, relief="ridge")
    paper.grid(row=3, column=1)

    scissor_img = PhotoImage(file="images/scissor_resized.png")
    scissor = Button(root, image=scissor_img, command=lambda: [scissor_choice(), start_game()], bg="#383838", activebackground="#383838", bd=0, highlightthickness=0, relief="ridge")
    scissor.grid(row=3, column=2)


game_menu()


def winner():
    if choice == 1 and pc_choice == 2:
        winner = 0
    elif choice == 1 and pc_choice == 3:
        winner = 1
    elif choice == 2 and pc_choice == 1:
        winner = 1
    elif choice == 2 and pc_choice == 3:
        winner = 0
    elif choice == 3 and pc_choice == 1:
        winner = 0
    elif choice == 3 and pc_choice == 2:
        winner = 1
    else:
        winner = 2

    return winner


def stone_choice():
    global result
    global choice
    global pc_choice
    choice = 1
    pc_choice = randint(1,3)

    result = winner()


def paper_choice():
    global result
    global choice
    global pc_choice
    choice = 2
    pc_choice = randint(1,3)

    result = winner()


def scissor_choice():
    global result
    global choice
    global pc_choice
    choice = 3
    pc_choice = randint(1,3)

    result = winner()


def start_game():
    global stone_game_img
    global paper_game_img
    global scissor_game_img

    global stone_game_img_pc
    global paper_game_img_pc
    global scissor_game_img_pc

    global vs_image

    global stone_game
    global paper_game
    global scissor_game

    global stone_game_pc
    global paper_game_pc
    global scissor_game_pc

    global vs

    global text_result
    global again

    stone.destroy()
    paper.destroy()
    scissor.destroy()

    if choice == 1:
        stone_game_img = PhotoImage(file="images/stone_game.png")
        stone_game = Label(root, image=stone_game_img, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        stone_game.grid(row=3, column=0)

    elif choice == 2:
        paper_game_img = PhotoImage(file="images/paper_game.png")
        paper_game = Label(root, image=paper_game_img, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        paper_game.grid(row=3, column=0)
    
    else:
        scissor_game_img = PhotoImage(file="images/scissor_game.png")
        scissor_game = Label(root, image=scissor_game_img, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        scissor_game.grid(row=3, column=0)


    if pc_choice == 1:
        stone_game_img_pc = PhotoImage(file="images/stone_game_pc.png")
        stone_game_pc = Label(root, image=stone_game_img_pc, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        stone_game_pc.grid(row=3, column=2)

    elif pc_choice == 2:
        paper_game_img_pc = PhotoImage(file="images/paper_game_pc.png")
        paper_game_pc = Label(root, image=paper_game_img_pc, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        paper_game_pc.grid(row=3, column=2)
    
    else:
        scissor_game_img_pc = PhotoImage(file="images/scissor_game_pc.png")
        scissor_game_pc = Label(root, image=scissor_game_img_pc, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
        scissor_game_pc.grid(row=3, column=2)


    vs_image = PhotoImage(file="images/Vs.png")
    vs = Label(root, image=vs_image, bg="#383838", bd=0, highlightthickness=0, relief="ridge")
    vs.grid(row=3, column=1)

    margin3 = Canvas(root, bg="#383838", width=800, height=70, bd=0, highlightthickness=0, relief="ridge")
    margin3.grid(row=4, column=0, columnspan=3)

    if result == 0:
        text_result = Label(root, text="VOCÊ PERDEU!", bg="#383838", bd=0, highlightthickness=0, fg="#FFFFFF", relief="ridge", font=("arial", 26))
        text_result.grid(row=5, column=1)
    elif result == 1:
        text_result = Label(root, text="VOCÊ GANHOU!", bg="#383838", bd=0, highlightthickness=0, fg="#FFFFFF", relief="ridge", font=("arial", 26))
        text_result.grid(row=5, column=1)
    else:
        text_result = Label(root, text="EMPATE!", bg="#383838", bd=0, highlightthickness=0, fg="#FFFFFF", relief="ridge", font=("arial", 26))
        text_result.grid(row=5, column=1)
    

    margin4 = Canvas(root, bg="#383838", width=800, height=70, bd=0, highlightthickness=0, relief="ridge")
    margin4.grid(row=6, column=0, columnspan=3)

    again = Button(root, text="RECOMEÇAR", command=restart_game, bg="#383838", activebackground="#383838", bd=0, highlightthickness=0, fg="#00ffff", relief="ridge", font=("arial", 20))
    again.grid(row=7, column=1)


def restart_game():
    if choice == 1:
        stone_game.destroy()
    elif choice == 2:
        paper_game.destroy()
    else:
        scissor_game.destroy()

    if pc_choice == 1:
        stone_game_pc.destroy()
    elif pc_choice == 2:
        paper_game_pc.destroy()
    else:
        scissor_game_pc.destroy()

    vs.destroy()
    text_result.destroy()
    again.destroy()

    game_menu()

root.mainloop()
