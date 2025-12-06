import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title('5秒以内にできるだけクリック！')

count = 0
time = 5
running = False
finish = False


label1 = tk.Label(root, text=str(count))
label1.pack()

label2 = tk.Label(root, text=str(time))
label2.pack(side="bottom", anchor="n")

def countdown():
    global time,running,finish
    if running and time > 0:
        root.after(1000, countdown)
        time -=1
        label2.config(text=str(time))
    elif time == 0:
        label2.config(text='終了!')
        finish = True


def clicked():
    global finish
    if finish:
        return
    global count
    count += 1
    label1.config(text=str(count))
    global running
    if running:
        return
    if not running:
        running = True
    countdown()

button = tk.Button(root, text='start', command=clicked, width=10, height=3)
button.pack()

root.mainloop()