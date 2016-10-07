import PIL.Image
import PIL.ImageTk
AlphaImagePath = "H:\PROJECT\AlphabetImages\\"
Photo=[]
AlphaStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for alpha in AlphaStr:
    pathalpha = AlphaImagePath + alpha + '.png'
    Photo.append(PIL.ImageTk.PhotoImage(PIL.Image.open(pathalpha)))
