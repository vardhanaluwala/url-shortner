import tkinter

import pyshorteners

def shorten():
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(longurl_E.get())
    print(shorturl_E.insert(0,short_url))
    #shorturl_E.insert(0,short_url)


root=tkinter.Tk()
root.title("URL Shortener")
root.geometry("400x200")
    

longurl_L=tkinter.Label(root,text="Enter Long URL")
longurl_E=tkinter.Entry(root)
shorturl_L=tkinter.Label(root,text="Output shortened URL")
shorturl_E=tkinter.Entry(root)
shorturl_B=tkinter.Button(root,text="Shorten URL",command=shorten)


longurl_L.pack()
longurl_E.pack()
shorturl_L.pack()
shorturl_E.pack()
shorturl_B.pack()

root.mainloop()