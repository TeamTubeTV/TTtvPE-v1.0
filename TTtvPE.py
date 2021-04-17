#TTtvPE (TeamTubeTV's Python engine)
import pygame
class Engine:
    def __init__(self,width,height,GN):
        pygame.init()
        self.win = pygame.display.set_mode((width,height))
        self.GameName = GN
        pygame.display.set_caption(GN)
        self.QUIT = pygame.QUIT
        self.KEYUP = pygame.KEYUP
        self.KEYDOWN = pygame.KEYDOWN
        self.Keys = {'a':pygame.K_a,'b':pygame.K_b,'c':pygame.K_c,'d':pygame.K_d,'e':pygame.K_e,'f':pygame.K_f,'g':pygame.K_g,'h':pygame.K_h,'i':pygame.K_i,'j':pygame.K_j,'k':pygame.K_k,'l':pygame.K_l,'m':pygame.K_m,'n':pygame.K_n,'o':pygame.K_o,'p':pygame.K_p,'q':pygame.K_q,'r':pygame.K_r,'s':pygame.K_s,'t':pygame.K_t,'u':pygame.K_u,'v':pygame.K_v,'w':pygame.K_w,'x':pygame.K_x,'y':pygame.K_y,'z':pygame.K_z,'0':pygame.K_0,'1':pygame.K_1,'2':pygame.K_2,'3':pygame.K_3,'4':pygame.K_4,'5':pygame.K_5,'6':pygame.K_6,'7':pygame.K_7,'8':pygame.K_8,'9':pygame.K_9,' ':pygame.K_SPACE,'backspace':pygame.K_BACKSPACE,'pause':pygame.K_PAUSE,'escape':pygame.K_ESCAPE,'tab':pygame.K_TAB,',':pygame.K_COMMA,'.':pygame.K_PERIOD,'rshift':pygame.K_RSHIFT,'lshift':pygame.K_LSHIFT,'insert':pygame.K_INSERT,'up':pygame.K_UP,'down':pygame.K_DOWN,'right':pygame.K_RIGHT,'left':pygame.K_LEFT,'f1':pygame.K_F1,'f2':pygame.K_F2,'f3':pygame.K_F3,'f4':pygame.K_F4,'f5':pygame.K_F5,'f6':pygame.K_F6,'f7':pygame.K_F7,'f8':pygame.K_F8,'f9':pygame.K_F9,'f10':pygame.K_F10,'f11':pygame.K_F11,'f12':pygame.K_F12}
        self.colliders = []
        self.fonts = {"pixel":pygame.font.Font("TTtvPE/pixel.ttf",32),"arial":pygame.font.Font("TTtvPE/arialBold.ttf",32),"8bit":pygame.font.Font("TTtvPE/8bit.ttf",32),"8bit 3d":pygame.font.Font("TTtvPE/8bit 3d.ttf",56),"DOS":pygame.font.Font("TTtvPE/DOS.ttf",32),"mario":pygame.font.Font("TTtvPE/Mario.ttf",32),"karate":pygame.font.Font("TTtvPE/Karate.ttf",32),"medieval":pygame.font.Font("TTtvPE/Medieval.ttf",44),"pixel 3d":pygame.font.Font("TTtvPE/3dPixel.ttf",32)}
    def GetWin(self):
        return self.win
    def ChangeTitle(self,title):
        pygame.display.set_caption(title)
    def ResizeWin(self,w,h):
        win = pygame.display.set_mode((w,h))
    def SetIcon(self,icon_image):
        pygame.display.set_icon(icon_image)
    def LoadImage(self,img):
        return pygame.image.load(img)
    def ResizeImage(self,img,w,h):
        pygame.transform.scale(img,(w,h))
    def WinBackground(self,c):
        self.win.fill(c)
    def DrawImage(self,img,x,y):
        self.win.blit(img,(x,y))
    def DrawRect(self,x,y,w,h,c):
        pygame.draw.rect(self.win,c,(x,y,w,h))
    def update(self):
        pygame.display.update()
    def GetEvents(self):
        return pygame.event.get()
    def DrawSprite(self,sprite,colors,x,y,w,h):
        pw = w/len(sprite[0])
        ph = h/(len(sprite))
        ix = 0
        iy = 0
        for py in sprite:
            for px in py:
                if sprite[iy][ix]:
                    self.DrawRect(x+ix*pw,y+iy*ph,pw,ph,colors[sprite[iy][ix]-1])
                ix += 1
            iy += 1
            ix = 0
    def Wait(self,sec):
        pygame.time.wait(sec)
    def DrawText(self,x,y,font,txt,color):
        ShowText = font.render(txt,True,color)
        self.DrawImage(ShowText,x,y)
    def LoadFont(self,font,size):
        return pygame.font.Font(font,size)
    def GetMousePress(self):
        if pygame.mouse.get_pressed()[0]:
            return pygame.mouse.get_pos()
        else:
            return False
    def GetCurrentMousePosition(self):
        return pygame.mouse.get_pos()