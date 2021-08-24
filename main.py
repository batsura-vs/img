from PIL import Image

colors = {
    (70, 110, 140): 'blue',
    (251, 207, 49): 'yellow',
    (245, 245, 245): 'white',
    (203, 56, 45): 'red',
    (15, 15, 15): 'black',
    (146, 61, 161): 'purple',
    (106, 162, 67): 'green',
    (153, 91, 69): 'brown',
    (160, 200, 200): 'liteBlue1',
    (251, 217, 179): 'skin1',
    (219, 181, 142): 'skin2',
    (180, 136, 103): 'skin3',
    (160, 103, 66): 'skin4',
    (107, 78, 70): 'skin5',
    (255, 164, 174): 'pink',
    (138, 189, 84): 'liteGreen',
    (67, 189, 245): 'liteBlue2',
    (243, 124, 31): 'orange',
    (53, 100, 190): 'darkBlue',
    (63, 149, 68): 'green1',
    (5, 127, 114): 'green2',
    (76, 94, 68): 'green',
    (252, 201, 48): 'orange1',
    (255, 164, 4): 'orange2',
    (246, 128, 4): 'orange3',
    (228, 79, 30): 'orange4',
    (130, 130, 130): 'gray',
    (190, 190, 190): 'gray',
    (20, 70, 170): 'darkestBlue',
    (19, 21, 33): 'black',
    (125, 134, 132): 'gray',
    (26, 26, 36): 'black',
    (62, 69, 85): 'blueGray',
    (92, 80, 74): 'skin3',
    (1, 41, 59): 'blueGray'
}

smiles = {
    'liteBlue2': '🟦',
    'yellow': '🟨',
    'orange': '🟧',
    'white': '⬜',
    'red': '🟥',
    'black': '⬛',
    'purple': '🟪',
    'green': '🟩',
    'liteGreen': '♍',
    'brown': '🟫',
    'blue': '🚹',
    'skin1': '🏻',
    'skin2': '🏼',
    'skin3': '🏽',
    'skin4': '🏾',
    'skin5': '🏿',
    'pink': '♓',
    'liteBlue1': '🈁',
    'darkBlue': '♐',
    'green1': '♎',
    'green2': '♏',
    'orange1': '♌',
    'orange2': '♋',
    'orange3': '♊',
    'orange4': '♉',
    'gray': '📓',
    'darkestBlue': '📘',
    'blueGray': '🌚',

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
    return colors[score[min(score.keys())]]


inp = Image.open('а.jpg')
inp_pix = inp.load()
inp_width, inp_height = inp.size
ans = '<div style="font-size: 1px">'
for h in range(inp_height):
    for w in range(inp_width):
        ans += smiles[x(*inp_pix[w, h])]
    ans += '<br>'
ans += '</div>'
with open('ans.html', 'w') as f:
    f.write(ans)
