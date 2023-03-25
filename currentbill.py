from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
color_blue = '#FFE6E6'
word_color = "green"
window = Tk()
window.title('CURRENT BILL CALCULATOR !!!')
window.minsize(width=500, height=400)
window.config(padx=50, pady=20, bg=color_blue)


def fun1(x):
    if 0 < x < 75:
        return 'A'
    elif 75 < x <= 225:
        return 'B'
    else:
        return 'C'


def money_calculations():

    try:
        x = int(entry.get())
        bill = 0.0
        if fun1(x) == 'A':
            if 0 < x <= 50:
                bill = x*1.65+x/16.66667+25
            elif 50 < x <= 75:
                bill = 50*1.65+(x-50)*2.80+x/16.66667+30
        if fun1(x) == 'B':
            if 0 < x <= 100:
                bill = x*2.80+x/16.66667+40
            elif 100 < x <= 200:
                bill = 100*2.80+(x-100)*3.80+x/16.6666667+45
            else:
                bill = 100*(2.80+3.80)+(x-200)*7.14+x/16.6666667+50
        if fun1(x) == 'C':
            if 0 < x <= 50:
                bill = x*2.85+x/16.6667+35
            elif 50 < x <= 100:
                bill = 50*2.85+x/16.6667+(x-5)*3.60+40
            elif 100 < x <= 200:
                bill = 50*(2.85+3.60)+(x-100)*5.60+45+x/16.66667
            elif 200 < x <= 300:
                bill = 50*(2.85+3.60)+100*5.60+(x-200)*7.30+50+x/16.66667+50
            elif 300 < x <= 400:
                bill = 50*(2.85+3.60)+100*(5.60+7.30)+(x-300)*8.20+55+x/16.66667
            elif 400 < x <= 500:
                bill = 50*(2.85+3.65)+100*(5.60+7.30+8.20)+(x-400)*9.15+55
            else:
                bill = 50*(2.85+3.65)+100*(5.60+7.30+8.20+9.15)+(x-500)*10.20
    except ValueError:
        messagebox.showerror(title='Warning!!!', message=' Enter the number of units consumed in the entry box.\n'
                                                         'It should be a number!!!')
    else:
        canvas.itemconfig(bill_, text=f"Bill to be paid in RS {str(round(bill))}/-", font=('Ariel', 20, 'bold'),
                          fill=word_color)
# bill_result_label.config(text=str(round(bill, 2)))


canvas = Canvas(width=800, height=526, bg=color_blue, highlightthickness=0)
front_img = ImageTk.PhotoImage(Image.open('bill_project.png'))
canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
cal_button = ImageTk.PhotoImage(Image.open('calculatebutton.jpg'))
button = Button(text='Calculate', image=cal_button, command=money_calculations, highlightthickness=0)
button.grid(column=1, row=2, columnspan=2)
canvas.create_text(400, 50, text='CURRENT BILL CALCULATOR', font=('Ariel', 34, 'bold'), fill='purple')
bill_ = canvas.create_text(500, 270, text='Bill to be paid in RS 0/-', font=('Ariel', 20, 'bold'), fill=word_color)
canvas.create_text(200, 200, text="Units consumed", font=('Ariel', 20, 'bold'), fill=word_color)

# entry
entry = Entry(width=20, font=30)
entry.insert(0, string='Enter units')
entry.grid(column=0, row=0)

mainloop()
