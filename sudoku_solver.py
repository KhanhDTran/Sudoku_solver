import pygame
from pygame.constants import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_BACKSPACE, K_DELETE, QUIT
from cells import Cell
import function as func
from buttons import Button

pygame.init()

screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Sudoku Solver")

White = (255, 255, 255)
Black = (0, 0, 0)
Blue = (189, 240, 255)

screen.fill(White)

running = True
cells = []
ordinal = 0

submit_button = Button(850, 200, 150, 50, "Submit")


for row in range(1, 10):
    for column in range(1, 10):
        x = 80 * column
        y = 80 * row
        cell = Cell(ordinal, row, column, x, y) 
        rect = pygame.Rect(x, y, 80, 80)
        cell.width = rect.width
        cell.height = rect.height
        cell.top = rect.top
        cell.bottom = rect.bottom
        cell.left = rect.left
        cell.right = rect.right

        if row <= 3 and column <= 3:
            cell.block = 1
        if row <= 3 and column > 3 and column <= 6:
            cell.block = 2
        if row <= 3 and column > 6:
            cell.block = 3
        if row > 3 and row <= 6 and column <= 3:
            cell.block = 4
        if row > 3 and row <= 6 and column > 3 and column <= 6:
            cell.block = 5
        if row > 3 and row <= 6 and column > 6:
            cell.block = 6
        if row > 6 and column <= 3:
            cell.block = 7
        if row > 6 and column > 3 and column <= 6:
            cell.block = 8
        if row > 6 and column > 6:
            cell.block = 9

        cells.append(cell)
        ordinal += 1

for cell in cells:
    pygame.draw.rect(screen, Black, (cell.x, cell.y, cell.width, cell.height), 1)
    for col in range(0, 11):
        if col % 3 == 1:
            pygame.draw.line(screen, (60, 64, 59),
                             (col * 80, 80), (col * 80, 800), 6)

    for row in range(0, 11):
        if row % 3 == 1:
            pygame.draw.line(screen, Black, (80, row * 80), (800, row * 80), 6)

left_board = cells[0].left
top_board = cells[0].top
right_board = cells[80].right
bottom_board = cells[80].bottom

chosen_cell = Cell(100, 10, 10, 100, 100)

func.text_to_screen(screen, "At least 17 clues to solve", 200, 830, 50, Black)
check_not_finish = True

while running:

    

    if submit_button.drawButton(screen):
        clues = 0
        for cell in cells:
            if cell.number != 0:
                clues += 1
        pygame.draw.rect(screen, White, (200, 10, 500, 50))
        func.text_to_screen(screen, "clues: " + str(clues), 200, 10, 50, Black)

        if clues >= 17:
            func.solve_board(cells)
            for cell in cells:
                if not cell.clue:
                    func.text_to_screen(screen, str(cell.number), cell.x + 25, cell.y + 18, 50, (3, 81, 130))
        check_not_finish = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and check_not_finish:
            x, y = pygame.mouse.get_pos()

            if left_board <= x and x <= right_board and top_board <= y and y <= bottom_board:
                for cell in cells:
                    if cell.left <= x and x <= cell.right and y >= cell.top and y <= cell.bottom:
                        cell.chosen = True
                        chosen_cell = cell
                        pygame.draw.rect(screen, Blue, (cell.left + 3, cell.top + 3, 75, 75))
                        if cell.number != 0:
                            func.text_to_screen(screen, str(cell.number), cell.x + 25, cell.y + 18, 50, Black)
                    else:
                        cell.chosen = False
                        pygame.draw.rect(screen, White, (cell.left + 3, cell.top + 3, 75, 75))
                        if cell.number != 0:
                            func.text_to_screen(screen, str(cell.number), cell.x + 25, cell.y + 18, 50, Black)
            else:
                for cell in cells:
                    if cell.chosen:
                        cell.chosen = False
                        pygame.draw.rect(screen, White, (cell.left + 3, cell.top + 3, 75, 75))
                        if cell.number != 0:
                            func.text_to_screen(screen, str(cell.number), cell.x + 25, cell.y + 18, 50, Black)

                chosen_cell = Cell(100, 10, 10, 100, 100)

        if event.type == pygame.KEYDOWN and check_not_finish:
            if event.key == K_1 and chosen_cell.ordinal != 100:
                func.input_number(screen, 1, cells, chosen_cell, Blue, Black)
            if event.key == K_2 and chosen_cell.ordinal != 100:
                func.input_number(screen, 2, cells, chosen_cell, Blue, Black)
            if event.key == K_3 and chosen_cell.ordinal != 100:
                func.input_number(screen, 3, cells, chosen_cell, Blue, Black)              
            if event.key == K_4 and chosen_cell.ordinal != 100:
                func.input_number(screen, 4, cells, chosen_cell, Blue, Black)
            if event.key == K_5 and chosen_cell.ordinal != 100:
                func.input_number(screen, 5, cells, chosen_cell, Blue, Black)
            if event.key == K_6 and chosen_cell.ordinal != 100:
                func.input_number(screen, 6, cells, chosen_cell, Blue, Black)
            if event.key == K_7 and chosen_cell.ordinal != 100:
                func.input_number(screen, 7, cells, chosen_cell, Blue, Black)
            if event.key == K_8 and chosen_cell.ordinal != 100:
                func.input_number(screen, 8, cells, chosen_cell, Blue, Black)
            if event.key == K_9 and chosen_cell.ordinal != 100:
                func.input_number(screen, 9, cells, chosen_cell, Blue, Black)
            if event.key == K_BACKSPACE or event.key == K_DELETE and chosen_cell.ordinal != 100:
                func.input_number(screen, 0, cells, chosen_cell, Blue, Black)
                
    pygame.display.flip()

pygame.quit()


