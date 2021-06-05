from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")
root.iconbitmap("vimeo_icon_146250.ico")
root.configure(bg="#6272a4")

"""
to dispaly an image, define the image and its location and then pass it to a label and pack
"""
my_img1 = ImageTk.PhotoImage(Image.open(
    r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-155.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-47.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-170.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-182.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-193.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-203.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open(r"images/HQ-Wallpapers-for-a-desktop-(Part 341)-206.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def forward(image_number):
    global my_label, forward_btn, back_btn

    my_label.grid_forget()  # Clear grid
    my_label = Label(image=image_list[image_number - 1])  # insert picture as label
    forward_btn = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_btn = Button(root, text='<<', command=lambda: forward(image_number - 1))

    if image_number == len(image_list):
        forward_btn = Button(root, text=">>", state=DISABLED)
    if image_number == 1:
        back_btn = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    forward_btn.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

"""
def back(image_number):
    global my_label, forward_btn, back_btn

    my_label.grid_forget()  # Clear grid
    my_label = Label(image=image_list[image_number - 1])
    forward_btn = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_btn = Button(root, text='<<', command=lambda: forward(image_number - 1))

    if image_number == 1:
        back_btn = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    forward_btn.grid(row=1, column=2)
"""

back_btn = Button(root, text='<<', state=DISABLED)
exit_btn = Button(root, text='EXIT', padx=50, command=root.quit)
forward_btn = Button(root, text='>>', command=lambda: forward(2))

back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2, pady=10)

root.mainloop()
