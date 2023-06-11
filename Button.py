import pygame
pygame.init()



class Button:
    def __init__(self, x,  y, image) -> None:
        self.x = x
        self.y = y

        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = pygame.Rect(x, y, self.width, self.height)

    def get_cords(self):
        return (self.x, self.y)
    
    def get_image(self):
        return self.image
    
    def get_rect(self):
        return self.rect

    def set_cords(self, new_x, new_y) -> None:
        self.x = new_x
        self.y = new_y

        self.rect.update(self.x, self.y, self.width, self.height)

    def set_image(self, new_image) -> None:
        self.image = new_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.update(self.x, self.y, self.width, self.height)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        
        return False

     