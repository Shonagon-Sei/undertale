from tkinter import *
import random
import time
import sys
import keyboard
hp = 20
def hpp():
    global hp
    hp = hp -1

class Player:
    def __init__(self,canvas, up ,down, left, right):
        self.canvas = canvas
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.id = self.canvas.create_rectangle(0,0,20,20, fill='red', outline='')
        self.canvas.move(self.id, 490,310)
    def move(self):
        pos = self.canvas.coords(self.id)
        posup = self.canvas.coords(self.up)[3]
        posdown = self.canvas.coords(self.down)[1]
        posright = self.canvas.coords(self.right)[0]
        posleft = self.canvas.coords(self.left)[2]
        if keyboard.is_pressed('up'):
            self.canvas.move(self.id, 0, -5)
            if pos[1] <= posup:
                self.canvas.move(self.id, 0, 5)
        if keyboard.is_pressed('down'):
            self.canvas.move(self.id, 0, 5)
            if pos [3] >= posdown:
                  self.canvas.move(self.id, 0, -5)

        if keyboard.is_pressed('left'):
            self.canvas.move(self.id, -5, 0)
            if pos[0] <= posleft:
                 self.canvas.move(self.id, 5, 0)
        if keyboard.is_pressed('right'):
            self.canvas.move(self.id,5, 0)
            if pos[2] >= posright:
                 self.canvas.move(self.id, -5, 0)

class Attack:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player
        
        something = random.randrange(300, 680)
        self.id = self.canvas.create_rectangle(something,0,something + 20, 20, fill='white', outline='')
        
    def move(self):
        self.canvas.move(self.id, 0 , 6)
        
        pos = self.canvas.coords(self.id)
        if pos == []:
            pos = [1,1,1,1]
            pass
        posp = self.canvas.coords(self.player.id)
        if pos[3] >= 720:
            canvas.delete(self.id)
        if pos[0] <= posp[2] and pos[2] >= posp[0] and pos[1] <= posp[3] and pos[3] >= posp[1]:
            canvas.delete(self.id)
            hpp()
            print(hp)
            pass
            
            
            



tk = Tk()
tk.title("Undertale")

canvas = Canvas(tk, width=1000, height=700, bd=0, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(0, 0, 1100, 1080, fill='black')
up = canvas.create_line(320,150, 680, 150,  fill='white')
down = canvas.create_line(320,500, 680, 500,  fill='white')
left = canvas.create_line(320,150, 320, 500,  fill='white')
right = canvas.create_line(680,500, 680, 150,  fill='white')

player = Player(canvas, up, down, left, right)
tk.update_idletasks()
tk.update()
b = 0
newlist = []
while True:
    player.move()
    a = random.randrange(1,15)
    if a == 1 and b <= 0:
        newlist.append(Attack(canvas, player))
        b = 10
    else:
        b = b - 1
    for block in newlist: block.move() 
    tk.update_idletasks()
    tk.update()
    
    time.sleep(0.025)