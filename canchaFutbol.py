from tkinter import*
tk=Tk()

x=0
y=0
canvas=Canvas(tk,width=390,height=241)
canvas.pack()
my_image=PhotoImage(file="cancha.gif")
my_image1=PhotoImage(file="gol.gif")

canvas.create_image(0,0,anchor=NW, image=my_image)
canvas.create_image(80,160,anchor=NW, image=my_image1)

def mover(event):
    global y,x
    if event.keysym=="arriba":
        
        canvas.move(2,0,-6)
        y=y-6
    elif event.keysym=="abajo":
        
        
        canvas.move(2,0,6)
        y=y+6
    elif event.keysym=="Izquierda":
        
        canvas.move(2,-6,0)
        x=x-6
    else:        
        canvas.move(2,6,0)

        x=x+6
    if x==324 or x==-54:
        print("GOOOOOOOOOOOLLLLLLLLL!!!!!!!!!!!=)")

    print(str(x),''+str(y))
    
canvas.bind_all('<KeyPress-Up>',mover)
canvas.bind_all('<KeyPress-Down>',mover)
canvas.bind_all('<KeyPress-Left>',mover)
canvas.bind_all('<KeyPress-Right>',mover)



tk.mainloop()
