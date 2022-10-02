import sys

import pygame as pg
import random


class MatrixLetters:
    """Класс для отрисовки матрицы"""

    def __init__(self, app):
        """Инициализация класса"""
        self.app = app  # Атрибут приложения
        self.letters = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'  # Создание символов
        self.font_size = 8  # Размер шрифта
        self.font = pg.font.SysFont('arial', self.font_size, bold=True)  # Создание визуальных параметров шрифта
        self.column = self.app.width // self.font_size  # Кол-во столбцов
        self.drops = [1 for i in range(0, self.column)]  # Положение букв в колонках [1, 1, 1, 1, 1, 1]

    def _draw_symbols(self):
        """Отрисовка символов на экране"""
        for i in range(0, len(self.drops)):  # Отрисовка каждого символа на экране
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0, 255, 0))  # Отображение символа на экране
            position = i * self.font_size, (self.drops[i] - 1) * self.font_size  # Подсчет позиции символа
            self.app.surface.blit(char_render, position)  # Обращение к приложжению
            if self.drops[i] * self.font_size > self.app.height and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1
            
    def run(self):
        self._draw_symbols()


class MatrixApp:
    """Класс приложеня"""
    def __init__(self):
        """Инициализация приложения"""
        self.RES = self.width, self.height = 1000, 700  # Ширина и высота экрана
        pg.init()  # Инициализируем pygame
        self.screen = pg.display.set_mode(self.RES)  # Отображаемый экран
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)  # Поверхность отрисовки
        self.clock = pg.time.Clock()  # Отслеживаем время с помощью модуля pygame
        self.matrixLetters = MatrixLetters(self)  # Экземпляр класса букв

    def _draw_screen(self):
        """Отрисовка экрана"""
        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))  # Нанесение пов-ти на главный экран

    def run(self):
        while True:
            self._draw_screen()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
            self.clock.tick(40)


if __name__ == "__main__":
    app = MatrixApp()
    app.run()



