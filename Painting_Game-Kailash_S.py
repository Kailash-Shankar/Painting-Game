import pygame
import sys
import time

from pygame.examples.midi import Keyboard

from sudoku_generator import SudokuGenerator

#Title Screen
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("lightcoral")
W = pygame.font.Font(None, 100)
V = pygame.font.Font(None, 40)
Name = V.render("By Kailash S. | 11/13/2024", 0, "black")
Gametext = W.render("Painting Game", 0, "midnightblue")
Starttext = W.render("Start", 0, "white", "black")
Starttext2 = W.render("Start", 0, "yellow", "darkslategrey")

GT_rect = Gametext.get_rect(center=(300, 200))
ST_rect = Starttext.get_rect(center=((300, 400)))
N_rect = Name.get_rect(center=(300, 50))
ST_rect2 = Starttext2.get_rect(center=((300, 400)))
screen.blit(Gametext, GT_rect)
screen.blit(Starttext, ST_rect)
screen.blit(Name, N_rect)
pygame.display.update()
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



time.sleep(0.15)

#Main Interface
screen_color_list = ["tan", "pink", "powderblue", "lightgoldenrodyellow", "palegreen", "mediumslateblue", "darkslategrey", "linen"]
screen_color = screen_color_list[0]
SCL_index = 0

def draw_screen():
    screen.fill(screen_color)
draw_screen()
SWATCHES = ["black", "red", "yellow", "blue", "seagreen", "darkorange", "orchid", "cyan", "gold", "maroon"]
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

E_rect = Eraser.get_rect(center=(550, 50))
C_rect = Clear_Screen.get_rect(center=(550, 100))
B_rect = BG_Change.get_rect(center=(500, 550))
def draw_block_commands():
    screen.blit(Eraser, E_rect)
    screen.blit(Clear_Screen, C_rect)
    screen.blit(BG_Change, B_rect)


draw_block_commands()



def draw_highlight():
    pygame.draw.circle(screen, "white", (25, 50), 20, 5)
draw_highlight()
pygame.display.update()
COLOR = SWATCHES[0]

def setup():
    draw_screen()
    draw_block_commands()
    draw_swatches()
    draw_highlight()
    pygame.display.update()
    global COLOR
    COLOR = "black"


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
                    #Checks for mouse over color swatches
                    for i in val:
                        if i - 20 <= x <= i + 20:
                            COLOR = SWATCHES[val.index(i)]
                            draw_swatches()
                            pygame.draw.circle(screen, "white", (i, 50), 20, 5)
                            pygame.display.update()
                    #Checks for 'Erase' button press
                    if 500<x<600:
                        draw_swatches()
                        pygame.display.update()
                        COLOR = screen_color
                #Checks for 'Change Screen Color' button press
                elif 415<x<585 and 530<y<570:
                    SCL_index += 1
                    if SCL_index >= len(screen_color_list):
                        SCL_index = 0
                    screen_color = screen_color_list[SCL_index]
                    setup()


                #Checks for 'Clear' button press
                elif 80<y<120 and 500<x<600:
                    setup()


                #Turns pen on
                else:
                    down = True


            #Uses pen
            if down:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, COLOR, (x, y), 10)
                pygame.display.update()

            #Turns pen off
            if event.type == pygame.MOUSEBUTTONUP:
                down = False


except KeyboardInterrupt:
    pass