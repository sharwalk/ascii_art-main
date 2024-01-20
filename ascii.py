import pygame as pg
import cv2
import os
class ArtConverter:
    def __init__(self, path='img/car.jpg', font_size=12):
        pg.init()
        self.path = path
        self.image = self.get_image()
        self.RES = self.HEIGHT, self.WIDTH = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.ASCII_CHARS = " .,:;irs?@$%&#=+-1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ASCII_COEFFICIENT = 255 // (len(self.ASCII_CHARS) - 1)
        self.font = pg.font.SysFont('Courier', font_size, bold=True)
        self.CHAR_STEP = int(font_size * 0.6)
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]

    def draw_converted_image(self):
        char_indices = self.image // self.ASCII_COEFFICIENT
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indices[y, x]
                if char_index < len(self.RENDERED_ASCII_CHARS):
                    char = self.RENDERED_ASCII_CHARS[char_index]
                    self.surface.blit(char, (y, x))

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def draw_cv2_image(self):
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
        self.draw_cv2_image()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        self.save_image()
                        print('Image saved')
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()

    def save_image(self):
        pygame_image = pg.surfarray.array3d(self.surface)
        numpy_image = cv2.cvtColor(pygame_image, cv2.COLOR_RGB2BGR)
        transposed_image = cv2.transpose(numpy_image)

        output_dir = 'output/img'
        os.makedirs(output_dir, exist_ok=True)  # Создание папки, если она не существует

        cv2.imwrite(os.path.join(output_dir, 'ascii_image.jpg'), transposed_image)

if __name__ == "__main__":
    app = ArtConverter()
    app.run()