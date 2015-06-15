from pygame_game import PygameGame
import pygame, pygame.locals

class Demo(PygameGame):

    def __init__(self, width_px, height_px, frames_per_second):
        # PygameGame sets self.width and self.height        
        PygameGame.__init__(self, "Git Demo", width_px, height_px, frames_per_second)
        pygame.font.init()
        self.font = pygame.font.SysFont("Times New Roman",14)
        self.x = 282
        self.y = 30
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        
        # Add (don't replace) an awesome literary quote, for a different key press
        if pygame.K_b in newkeys:
            print "I am no man!"

        if pygame.K_s in newkeys:
            print "noooooooooooooooo"

        if pygame.K_RIGHT in keys:
            self.x += 2

        if pygame.K_UP in keys:
            self.y -= 2

        if pygame.K_LEFT in keys:
            self.x -= 2

        if pygame.K_DOWN in keys:
            self.y += 2
        if pygame.K_c in newkeys:
            print "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn"

        if pygame.K_z in newkeys:
            print "42 is the answer."
        return

    def paint(self, surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )

        self.drawTextLeft(surface, "Bilbo", (255, 0, 255), 300, 30, self.font)

        self.drawTextLeft(surface, "Cthulhu", (0, 255, 0), 295, 45, self.font)

        self.drawTextLeft(surface, "Ender", (0, 255, 0), 30, 300, self.font)
        
        self.drawTextLeft(surface, "Spider-man", (255, 255, 0), self.x, self.y, self.font)

        return

    def drawTextLeft(self, surface, text, color, x, y, font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

def demo_main():
    game = Demo(600, 600, 30)
    game.main_loop()
    return

if __name__ == "__main__":
    demo_main()
