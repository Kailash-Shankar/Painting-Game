import pygame
import sys
import time



#Title Screen
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("lightcoral")
W = pygame.font.Font(None, 100)
V = pygame.font.Font(None, 40)
Name = V.render("By Kailash S. | 11/15/2024", 0, "black")
Gametext = W.render("Painting Game", 0, "midnightblue")
Starttext = W.render("Start", 0, "white", "black")
Starttext2 = W.render("Start", 0, "yellow", "darkslategrey")


#Sounds
pygame.mixer.init()
try:
    pop = pygame.mixer.Sound("pop.wav")
    long_pop = pygame.mixer.Sound("longpop.wav")
    C_Chord = pygame.mixer.Sound("c-chord-83638.mp3")
    audio = True
except:
    audio = False

flag = 0

GT_rect = Gametext.get_rect(center=(300, 200))
ST_rect = Starttext.get_rect(center=((300, 400)))
N_rect = Name.get_rect(center=(300, 50))
ST_rect2 = Starttext2.get_rect(center=((300, 400)))
screen.blit(Gametext, GT_rect)
screen.blit(Starttext, ST_rect)
screen.blit(Name, N_rect)
pygame.display.update()
if audio:
    pygame.mixer.Sound.play(C_Chord)
Title = True
while Title:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if 220<x<380 and 350<y<450:

                screen.blit(Starttext2, ST_rect2)
                pygame.display.update()
                Title = False

if audio:
    pygame.mixer.Sound.play(long_pop)
time.sleep(0.15)

#Main Interface
screen_color_list = ["tan", "pink", "powderblue", "lightgoldenrodyellow", "palegreen", "mediumslateblue", "darkslategrey", "linen"]
screen_color = screen_color_list[0]
SCL_index = 0

def draw_screen():
    screen.fill(screen_color)
draw_screen()
SWATCHES = ["black", "red", "yellow", "blue", "seagreen", "darkorange", "orchid", "cyan", "gold", "maroon"]
sizes = [5, 10, 15, 20]
SIZE = sizes[1]
depth = [470, 495, 530, 575]
DEPTH = depth[1]

val = []
for i in range(len(SWATCHES)):
    val.append(25+i*50)

def draw_swatches():
    for i in range(len(SWATCHES)):
        pygame.draw.circle(screen, SWATCHES[i], (val[i], 50), 20)
draw_swatches()
pygame.display.update()

pygame.display.set_caption("Painting Game")
X = pygame.font.Font(None, 50)
Y = pygame.font.Font(None, 25)
Eraser = X.render("Erase", 0, "black", "silver")
Clear_Screen = X.render("Clear", 0, "black", "white")
BG_Change = Y.render("Change Screen Color", 0, "black", "white")
Brush_Size = Y.render("Brush Size", 0, "black")

E_rect = Eraser.get_rect(center=(550, 50))
C_rect = Clear_Screen.get_rect(center=(550, 100))
B_rect = BG_Change.get_rect(center=(500, 550))
BS_rect = Brush_Size.get_rect(center=(50, 445))
def draw_block_commands():
    screen.blit(Eraser, E_rect)
    screen.blit(Clear_Screen, C_rect)
    screen.blit(BG_Change, B_rect)
    screen.blit(Brush_Size, BS_rect)





draw_block_commands()



def draw_highlight():
    pygame.draw.circle(screen, "white", (25, 50), 20, 5)

def draw_highlight_sizes():
    pygame.draw.circle(screen, "white", (40, DEPTH), SIZE, 4)
draw_highlight()

pygame.display.update()
COLOR = SWATCHES[0]
BrushSize = [[depth[0], sizes[0]], [depth[1], sizes[1]],[depth[2], sizes[2]], [depth[3], sizes[3]]]

def draw_brush_sizes():
    if COLOR != screen_color:
        for i in range(len(BrushSize)):
            pygame.draw.circle(screen, COLOR, (40, BrushSize[i][0]), BrushSize[i][1])
    else:
        for i in range(len(BrushSize)):
            pygame.draw.circle(screen, "grey", (40, BrushSize[i][0]), BrushSize[i][1])

draw_brush_sizes()
draw_highlight_sizes()
pygame.display.update()

def setup():
    draw_screen()
    global SIZE, DEPTH
    SIZE, DEPTH = sizes[1], depth[1]
    global COLOR
    COLOR = SWATCHES[0]
    draw_block_commands()
    draw_swatches()
    draw_highlight()
    draw_brush_sizes()
    draw_highlight_sizes()
    pygame.display.update()



clock = pygame.time.Clock()
down = False
running = True
try:
    #Event Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos


                if 30<y<70:
                    #Checks for color swatches mouse presses
                    for i in val:
                        if i - 20 <= x <= i + 20:
                            COLOR = SWATCHES[val.index(i)]
                            draw_swatches()
                            draw_brush_sizes()
                            pygame.draw.circle(screen, "white", (i, 50), 20, 5)
                            draw_highlight_sizes()
                            pygame.display.update()
                            if audio:
                                pygame.mixer.Sound.play(pop)
                    #Checks for 'Erase' button press
                    if 500<x<600:
                        COLOR = screen_color
                        draw_swatches()
                        draw_brush_sizes()
                        draw_highlight_sizes()
                        pygame.display.update()
                        COLOR = screen_color
                        if audio:
                            pygame.mixer.Sound.play(pop)

                #Checks for 'Change Screen Color' button press
                elif 415<x<585 and 530<y<570:
                    SCL_index += 1
                    if SCL_index >= len(screen_color_list):
                        SCL_index = 0
                    placeholder = COLOR if COLOR == screen_color else 0
                    P2 = COLOR if placeholder == 0 else 7
                    screen_color = screen_color_list[SCL_index]
                    if placeholder != 0 or flag == 1:
                        COLOR = screen_color
                        flag = 1
                    else:
                        flag = 0
                        COLOR = P2 if P2 != 7 else screen_color
                    setup()
                    if audio:
                        pygame.mixer.Sound.play(long_pop)


                #Checks for 'Clear' button press
                elif 80<y<120 and 500<x<600:
                    setup()
                    if audio:
                        pygame.mixer.Sound.play(long_pop)

                #Checks for brush size mouse presses
                elif 20<x<60:
                    for i in range(len(depth)):
                        if depth[i]-20<y<depth[i]+20:
                            DEPTH = depth[i]
                            SIZE = sizes[i]

                            draw_brush_sizes()
                            draw_highlight_sizes()
                            pygame.display.update()
                            if audio:
                                pygame.mixer.Sound.play(pop)


                #Turns pen on
                else:
                    down = True


            #Uses pen
            if down:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, COLOR, (x, y), SIZE)
                pygame.display.update()

            #Turns pen off
            if event.type == pygame.MOUSEBUTTONUP:
                down = False


except KeyboardInterrupt:
    pass