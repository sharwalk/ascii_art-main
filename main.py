import pygame as pg
import cv2

class ArtConverter:
    def __init__(self, path='img/car.jpg'):
        pg.init()
        self.path = path
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
    def get_image (self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        rgb_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        return rgb_image
    def draw_cv2_image (self):
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360) , interpolation=cv2.INTER_AREA)
        cv2.imshow('img', resized_cv2_image)

    def draw (self):
        pg.surfarray.blit_array(self.surface, self.image)
        self.draw_cv2_image()
    def run (self):
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()


if __name__ == "__main__":
    app = ArtConverter()
    app.run()