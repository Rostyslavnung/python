from tkinter import *
import tkinter.filedialog

def LoadFile():
    fn = tkinter.filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    with open(fn, 'r', encoding='utf-8') as f:
        textbox.insert('1.0', f.read())

def SaveFile():
    fn = tkinter.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
    )
    if fn == '':
        return
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(textbox.get('1.0', 'end-1c'))

root = Tk()
root.title("Text Editor")

panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Open', command=LoadFile)
loadBtn.place(x=10, y=1, width=40, height=20)

saveBtn = Button(panelFrame, text='Save', command=SaveFile)
saveBtn.place(x=60, y=1, width=40, height=20)

root.mainloop()
