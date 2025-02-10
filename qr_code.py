import tkinter as tk
from tkinter import filedialog
import pyqrcode
import tkinter.font as tkFont


def qr():
    url=new_url.get()

    if url:
        qr_url=pyqrcode.create(url)
        file_path=filedialog.asksaveasfilename(defaultextension=".svg", filetypes=(("SVG files", "*.svg"),))

        if file_path:
            qr_url.svg(file_path , scale=8)
            status_tag.config(text="✅ QR Code saved to " + file_path,fg="green")

        else:
            status_tag.config(text="QR Code not saved",fg="red")

    else:
        status_tag.config(text="Please enter a URL !",bg="red",fg="white")

app_window=tk.Tk()
app_window.title("QR Code Generator")
app_window.geometry("300x300")
font = tkFont.Font(family="Arial", size=10, slant="italic")

tag=tk.Label(app_window,text="🔗 Enter URL:",font=font,fg="green")
new_url=tk.Entry(app_window)
qr_code_button=tk.Button(app_window,text="Generate QR Code 🎉",command=qr,activebackground="blue", activeforeground="white",font=font,bg='green',fg="white")
status_tag=tk.Label(app_window,text="",font=font,fg='green')
app_window.configure(bg='#90ee90')


tag.grid(row=0,column=0,padx=10,pady=10)
new_url.grid(row=0,column=1,padx=10,pady=10)
qr_code_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
status_tag.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

app_window.mainloop()