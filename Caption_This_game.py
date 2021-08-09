from guizero import App, TextBox, Drawing

def caption():
    meme.clear()
    meme.image(0, 0, "doraemon.png")
    meme.text(
        20, 5, top_text.value, 
        color="orange",
        size=40, 
        font="courier")
    meme.text(
        250, 175, bottom_text.value,
        color="blue",
        size=28,
        font="times new roman",
        )

app = App("meme")

top_text = TextBox(app, "top text", command=caption)
bottom_text = TextBox(app, "bottom text", command=caption)

meme = Drawing(app, width="fill", height="fill")

caption()

app.display()
