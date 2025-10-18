from tkinter import *
from tkinter import colorchooser, simpledialog

shape_settings = {
    "triangle": {"fill": "yellow", "outline": "white", "scale": 1},
    "rectangle": {"fill": "blue", "outline": "white", "width": 240, "height": 150},
    "circle": {"fill": "lightblue", "outline": "blue", "radius": 100}
}

text_settings = {
    "font": ("Times", 14),
    "color": "black"
}

def triangle():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    s = shape_settings["triangle"]["scale"]
    canvas.itemconfig(t, fill=shape_settings["triangle"]["fill"],
                      outline=shape_settings["triangle"]["outline"])
    canvas.coords(t, (50, 200, 340 * s, 200, 110, 60 * s))
    update_text("Зображення трикутника")

def rectangle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    w = shape_settings["rectangle"]["width"]
    h = shape_settings["rectangle"]["height"]
    canvas.itemconfig(r, fill=shape_settings["rectangle"]["fill"],
                      outline=shape_settings["rectangle"]["outline"])
    canvas.coords(r, (80, 50, 80 + w, 50 + h))
    update_text("Зображення прямокутника")

def circle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    rds = shape_settings["circle"]["radius"]
    canvas.itemconfig(c, fill=shape_settings["circle"]["fill"],
                      outline=shape_settings["circle"]["outline"])
    canvas.coords(c, (150-rds, 150-rds, 150+rds, 150+rds))
    update_text("Зображення кола")

def clear_canvas():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    update_text("Полотно очищене", color="red")

def update_text(msg, color=None):
    text.delete(1.0, END)
    text.insert(1.0, msg)
    text.tag_add('title', '1.0', '1.end')
    font, size = text_settings["font"][0], text_settings["font"][1]
    clr = color if color else text_settings["color"]
    text.tag_config('title', font=(font, size), foreground=clr)

def settings_triangle():
    color = colorchooser.askcolor(title="Колір трикутника")[1]
    if color:
        shape_settings["triangle"]["fill"] = color
    scale = simpledialog.askfloat("Масштаб трикутника", "Введіть масштаб (0.5–3.0):", minvalue=0.5, maxvalue=3.0)
    if scale:
        shape_settings["triangle"]["scale"] = scale

def settings_rectangle():
    color = colorchooser.askcolor(title="Колір прямокутника")[1]
    if color:
        shape_settings["rectangle"]["fill"] = color
    w = simpledialog.askinteger("Ширина прямокутника", "Введіть ширину:", minvalue=50, maxvalue=400)
    h = simpledialog.askinteger("Висота прямокутника", "Введіть висоту:", minvalue=50, maxvalue=300)
    if w and h:
        shape_settings["rectangle"]["width"] = w
        shape_settings["rectangle"]["height"] = h

def settings_circle():
    color = colorchooser.askcolor(title="Колір кола")[1]
    if color:
        shape_settings["circle"]["fill"] = color
    rds = simpledialog.askinteger("Радіус кола", "Введіть радіус:", minvalue=20, maxvalue=150)
    if rds:
        shape_settings["circle"]["radius"] = rds

# ---- налаштування тексту ----
def settings_text():
    color = colorchooser.askcolor(title="Колір тексту")[1]
    if color:
        text_settings["color"] = color
    size = simpledialog.askinteger("Розмір шрифту", "Введіть розмір шрифту:", minvalue=8, maxvalue=48)
    if size:
        text_settings["font"] = (text_settings["font"][0], size)

win = Tk()
win.title("Фігури на Canvas")

menubar = Menu(win)
settings_menu = Menu(menubar, tearoff=0)
images_menu = Menu(settings_menu, tearoff=0)
images_menu.add_command(label="Трикутник", command=settings_triangle)
images_menu.add_command(label="Прямокутник", command=settings_rectangle)
images_menu.add_command(label="Коло", command=settings_circle)
settings_menu.add_cascade(label="Налаштування зображень", menu=images_menu)
settings_menu.add_command(label="Налаштування тексту", command=settings_text)

menubar.add_cascade(label="Налаштування", menu=settings_menu)
win.config(menu=menubar)

b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clear = Button(text="Очистити", width=15, command=clear_canvas)

canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)

t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)

b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clear.grid(row=3, column=0)

canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)

win.mainloop()
