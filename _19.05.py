import customtkinter as ctk
from tkinter import simpledialog,Canvas
from PIL import Image, ImageTk
import pygame

pildid={}
olemas={}
objektid={}


nagu=["pea1.png", "pea2.png", "pea3.png", "pea4.png", "pea5.png"]
nagu_index=-1

silmad=["silmad1.png"]
silmad_index=-1

juuksed=["juuksed1.png"]
juuksed_index=-1

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi]=False
    else:
        pil_img=Image.open(fail).convert("RGBA").resize((400,400))
        tk_img=ImageTk.PhotoImage(pil_img)
        pildid[nimi]=tk_img
        objektid[nimi]=canvas.create_image(x,y,image=tk_img)
        olemas[nimi]=True

def toggle_nagu():
    global nagu_index
    nagu_index = (nagu_index + 1) % len(nagu)
    fail = nagu[nagu_index].strip()
    olemas["nagu"] = False
    toggle_osa("nagu", fail, 200, 200)

def toggle_juuksed():
    global juuksed_index
    juuksed_index = (juuksed_index + 1) % len(juuksed)
    fail = juuksed[juuksed_index].strip()
    olemas["juuksed"] = False
    toggle_osa("juuksed", fail, 200, 200)


def toggle_silmad():
    global silmad_index
    silmad_index = (silmad_index + 1) % len(silmad)
    fail = silmad[silmad_index].strip()
    olemas["silmad"] = False
    toggle_osa("silmad", fail, 200, 200)



def salvesta_nägu():
    failnimi=simpledialog.askstring("Salvestapilt", "Sisesta failinimi (ilma laiendita):")
    if not failnimi:
                return
    lõpp_pilt= Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    for nimi in ["nägu", "juuksed", "kulmud", "silmad", "nina", "suu"]:
        if olemas.get(nimi):
            failitee={
                "nägu":"pea1.png",
                "juuksed": "juuksed1.png",
                "silmad":"silmad1.png",
                "nina":"nina1.png",
                "suu":"suu1.png"}.get(nimi)
            if failitee:
                osa=Image.open(failitee).convert("RGBA").resize((400,400))
                lõpp_pilt.alpha_composite(osa)

    lõpp_pilt.save(failnimi+".png")

# def mangi_muusika():
#     pygame.mixer_music.play(loops=-1) 
# def peata_muusika():
#     pygame.mixer.music.stop()

# # pygame.mixer.init()
# # pygame.mixer.music.load(файл с музыкой)
                                                                                                         
app=ctk.CTk()
app.geometry("800x800")
app.title("Näo koostaja nuppudega")
frame=ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)
seaded={
    "width": 150, "height": 40,
    "font":("Segoe UI Emoji", 32),
    "fg_color":"#4CAF50",
    "text_color":"white",
    "corner_radius":20
    }

canvas= Canvas(app, width=400, height=400,bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nägu", "alus.png", 200,200) #face first
olemas["nägu"]=True

ctk.CTkLabel(frame, text="Vali näoosad:", **seaded).pack(pady=10)
ctk.CTkButton(frame, text="Nägu", command=lambda: toggle_nagu(), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Juuksed", command=lambda: toggle_juuksed(), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_silmad(), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "alus.png", 150,150), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "alus.png", 150,150), **seaded).pack(pady=5)

nupp=ctk.CTkButton(frame, text="Salvesta", command=salvesta_nägu, **seaded).pack(side="bottom", pady=5)

frame_mus=ctk.CTkFrame(frame)
frame_mus.pack( padx=10, pady=10)
# ctk.CTkButton(frame_mus, text="Nängi muusikat", command=mangi_muusika, **seaded).pack(side="left", pady=5)
# ctk.CTkButton(frame_mus, text="Peata muusika", command=peata_muusika, **seaded).pack(side="left", pady=5)

app.mainloop()
