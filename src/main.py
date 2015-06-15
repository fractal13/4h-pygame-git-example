from pygame_game import PygameGame
import pygame, pygame.locals

class Demo(PygameGame):

    def __init__(self, width_px, height_px, frames_per_second):
        # PygameGame sets self.width and self.height        
        PygameGame.__init__(self, "Git Demo", width_px, height_px, frames_per_second)
        pygame.font.init()
        self.x = 300
        self.y = 500
        self.font = pygame.font.SysFont("OCR A Extended",14)
        self.font2 = pygame.font.SysFont("Times New Roman",14)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        
        # Add (don't replace) an awesome literary quote, for a different key press

        if pygame.K_a in newkeys:
            print "The one with ravishing hair."

        if pygame.K_b in newkeys:
            print "I am no man!"



        if pygame.K_m in newkeys:
            print "Does not Happen"


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

        if pygame.K_d in newkeys:
            print "Nitwit! Blubber! Oddment! Tweak!"
            
        if pygame.K_n in newkeys:
            print "For a moment, nothing happened. Then, after a second or so, nothing continued to happen."

        if pygame.K_m in newkeys:
            print "Does not happen"

        if pygame.K_g in newkeys:
            print "You shall not pass!"


        if pygame.K_j in newkeys:
            print "The apple had changed. Just for an instant. It had changed in mid-air."

        if pygame.K_m in newkeys:
            print "Does not Happen"
    
        if pygame.K_c in newkeys:
            print "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn"

        if pygame.K_z in newkeys:
            print "42 is the answer."


        if pygame.K_r in newkeys:
            print "Rubber Ducky is a good video."

        return

       

        return


    def paint(self, surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        
        # Add (don't replace) an awesome literary character
        #                                   color            x   y
        self.drawTextLeft(surface, "Jonas", (200, 0, 255), 300, 60, self.font)

        self.drawTextLeft(surface, "Bilbo", (255, 0, 255), 300, 30, self.font)


        self.drawTextLeft(surface, "Mau", (255, 0, 255), 300, 90, self.font)

        self.drawTextLeft(surface, "Cthulhu", (0, 255, 0), 295, 45, self.font)

        self.drawTextLeft(surface, "Ender", (0, 255, 0), 30, 300, self.font)

        self.drawTextLeft(surface, "JoeJoe the Capybara", (0, 255, 0), 72, 391, self.font)       

        self.drawTextLeft(surface, "Marvin", (64, 0, 230), 10, 10, self.font)       

        self.drawTextLeft(surface, "Mau", (255, 0, 255), 300, 90, self.font)

        self.drawTextLeft(surface, "Gandalf", (255, 140, 0), 300, 120, self.font)

        self.drawTextLeft(surface, "Ender", (0, 255, 0), 30, 300, self.font)
        
        self.drawTextLeft(surface, "Ender's Shadow (bean)", (0, 255, 0), 30, 400, self.font)
        
        self.drawTextLeft(surface, "Spider-man", (255, 255, 0), self.x, self.y, self.font)

        self.drawTextLeft(surface, "Cthulhu", (0, 255, 0), 295, 45, self.font2)

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
