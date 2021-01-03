import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, 'white', (self.left + self.cell_size * j,
                                                   self.top + self.cell_size * i,
                                                   self.cell_size,
                                                   self.cell_size), width=1)

    def get_cell(self, mouse_pos):
        if self.check_mouse_coords(mouse_pos):
            for i in range(self.height):
                for j in range(self.width):
                    x1 = self.left + self.cell_size * j
                    x2 = x1 + self.cell_size
                    y1 = self.top + self.cell_size * i
                    y2 = y1 + self.cell_size
                    if mouse_pos[0] in range(x1, x2 + 1) and mouse_pos[1] in range(y1, y2 + 1):
                        return j, i
        return None

    def check_mouse_coords(self, mouse_pos):
        if self.left > mouse_pos[0] or mouse_pos[0] > self.left + self.cell_size * self.width:
            return False
        if self.top > mouse_pos[1] or mouse_pos[1] > self.top + self.cell_size * self.height:
            return False
        return True

    def on_click(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = 1
        pygame.draw.rect(screen, 'green', (self.left + self.cell_size * cell_coords[0],
                                           self.top + self.cell_size * cell_coords[1],
                                           self.cell_size,
                                           self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def next_move(self):
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
                if event.button == 1:
                    board.get_click(pygame.mouse.get_pos())
                if event.button == 2:
                    pass
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

        board.render(screen)
        pygame.display.flip()

