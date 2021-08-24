from PIL import Image

colors = {
    (0, 0, 0): (255, 255, 255),
    (255, 255, 255): (0, 0, 0)
}


def x(r, g, b, *args):
    score = {

    }
    for i in colors:
        red = [r, i[0]]
        green = [g, i[1]]
        blue = [b, i[2]]
        r_score = max(red) - min(red)
        g_score = max(green) - min(green)
        b_score = max(blue) - min(blue)
        res = r_score + g_score + b_score
        score[res] = i
    return colors[score[min(score.keys())]], min(score.keys())


inp = Image.open('j.jpg')
inp_pix = inp.load()
inp_width, inp_height = inp.size
for h in range(inp_height):
    for w in range(inp_width):
        sm = sum(i for i in inp_pix[w, h])
        inp_pix[w, h] = (sm // 3, sm // 3, sm // 3)
inp.show()
