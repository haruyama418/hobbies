from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title('Vocarash_beta')
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text='Enter English word')
#frame2 = ttk.Frame(root)
label2 = ttk.Label(frame1, text="What does it mean?")
label3 = ttk.Label(frame1, text="\ncontinue with \n↓")
def word(event=None):
    print('Hello, %s!' % entry1.get())
    with open('tkinter.txt', 'a') as f:
        print(entry1.get() + "   :   "+entry2.get(), file=f)
        print("--------------------------------------------", file=f)

    messagebox._show("Confirmation", "Succeeded!\nPush enter and keep going!")
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


entry1 = ttk.Entry(frame1)
entry2 = ttk.Entry(frame1)


#button1 = ttk.Button(frame1, text='OK', command=word)
#shift+return でボタンを押す
root.bind('<Shift-Key-Return>', word)
button2 = ttk.Button(frame1, text='OK  [Shift]+[Return]', command=word,)



#design
#Labelの順番は以下の順番になる？！
frame1.pack(side=TOP)
label1.pack(side=TOP)
entry1.pack(side=TOP)
#button1.pack(side=TOP)

label2.pack(side=TOP)
entry2.pack(side=TOP)
label3.pack(side=TOP)
button2.pack(side=TOP)





root.mainloop()

if __name__  == '__main__':
    run()
