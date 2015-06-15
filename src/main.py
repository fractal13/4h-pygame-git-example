from pygame_game import PygameGame
import pygame, pygame.locals

class Demo(PygameGame):

    def __init__(self, width_px, height_px, frames_per_second):
        # PygameGame sets self.width and self.height        
        PygameGame.__init__(self, "Git Demo", width_px, height_px, frames_per_second)
        pygame.font.init()
        self.font = pygame.font.SysFont("Times New Roman",14)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        
        # Add (don't replace) an awesome literary quote, for a different key press
        if pygame.K_b in newkeys:
            print "I am no man!"

        if pygame.K_g in newkeys:
            print "You shall not pass!"

        return

    def paint(self, surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        
        # Add (don't replace) an awesome literary character
        #                                   color            x   y
        self.drawTextLeft(surface, "Bilbo", (255, 0, 255), 300, 30, self.font)

        self.drawTextLeft(surface, "Gandalf", (34, 139, 34), 300, 120, self.font)

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
