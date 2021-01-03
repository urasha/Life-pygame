import pygame
from board import Board


class Life(Board):
    pass


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((460, 460))
    pygame.display.set_caption('Игра «Жизнь»')

    board = Board(30, 30)
    board.set_view(5, 5, 15)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(pygame.mouse.get_pos())

        board.render(screen)
        pygame.display.flip()
