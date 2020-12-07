import pygame
import time
import pickle

pygame.init()
win = pygame.display.set_mode(flags = pygame.FULLSCREEN)
run = True
clock = pygame.time.Clock()
cells=0
U=30

array= pickle.load(open("MYNAME.p","rb"))
size  = (1920,1080)
x=0
y=0
coords_x=[]
coords_y=[]
for row in range(size[1]//U):
    i=[]
    for col in range(size[0] // U):
        i.append(0)
    array.append(i)
# array[0][1]=1
for i in range(size[0]//U):
    x+=U
    coords_x.append([(x,0),(x,size[1])])
for i in range(size[1]//U):
    y+=U
    coords_y.append([(0,y),(size[0],y)])
font = pygame.font.SysFont("comicsans",30,True)



def redraw():
    for r in range(len(array)):
        for c in range(len(array[0])):
            x=c*U
            y=r*U
            if array[r][c]==1:
                pygame.draw.rect(win,(0,0,0),(x,y,U,U))
            else:
                pygame.draw.rect(win,(255,255,255),(x,y,U,U))

                # print(x)
                # print(y)

    for a in coords_x:
        pygame.draw.line(win, (25, 25, 25), a[0], a[1])
    for a in coords_y:

        pygame.draw.line(win, (25, 25, 25), a[0], a[1])

    text = font.render("CELLS : " + str(cells), 2, (0, 0, 0))
    win.blit(text, (size[0] // 9, size[1] // 9))
    pygame.display.update()




run = True

g=0
while run:
    clock.tick(27)
    if g <100:
        g+=1
        redraw()

        continue
    nb=[]
    for r in range(len(array)):
        i=[]
        for c in range(len(array[0])):
            n=0
            lr = r - 1
            ur = r + 2
            lc = c - 1
            uc = c + 2
            if r==0:
                lr = 0
            if c==0:
                lc = 0
            if r==len(array)-1:
                ur = len(array)-1
            if c==len(array[0])-1:
                uc = len(array[0])-1



            for a in range(lr,ur) :
                for b in range(lc,uc):

                    if (r==a) and (c==b):
                        continue

                    if array[a][b] ==1:

                        x = a * U
                        # print(x)
                        y = b * U
                        # print(y)
                        n += 1


            i.append(n)
        nb.append(i)
                        # time.sleep(1)
    for r in range(len(array)):
        i = []
        for c in range(len(array[0])):
            cell = array[r][c]
            n=nb[r][c]
            if cell ==0:
                if n==3:
                    array[r][c]=1
                    cells+=1
            if array[r][c]==1:

                if (n<2) or (n>3):
                    array[r][c]=0
                    cells-=1











    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run=False

for a in array:
    print(a)