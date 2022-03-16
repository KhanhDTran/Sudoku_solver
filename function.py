from cells import Cell
import pygame
import random

Red = (250, 42, 56)

def text_to_screen(screen, text, x, y, size, color):
    text = str(text)
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def input_number(screen, number, cells, chosen_cell, Blue, Black):
    if check_available_input(screen, cells, chosen_cell, number, Black):
        for cell in cells:
            if cell.ordinal == chosen_cell.ordinal:
                cell.number = number
                pygame.draw.rect(screen, Blue, (chosen_cell.left + 3, chosen_cell.top + 3, 75, 75))
                if number != 0:
                    text_to_screen(screen, str(number), chosen_cell.x + 25, chosen_cell.y + 18, 50, Black)
                if number == 0:
                    pygame.draw.rect(screen, Blue, (chosen_cell.x + 3, chosen_cell.y + 3, 75, 75))
                    cell.clue = False
                if number != 0:
                    cell.clue = True
                    


def check_available_input(screen, cells, cell, number, Black):
    for cellx in cells:
        if cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block:
            if cellx.number != 0 and cellx.number == number:
                pygame.draw.rect(screen, Red, (cellx.x + 3, cellx.y + 3, 75, 75))
                text_to_screen(screen, str(cellx.number), cellx.x + 25, cellx.y + 18, 50, Black)
                return False
    
    return True

def potentialList(Cell, cells):
    for cell in cells:
        if cell.row == Cell.row and cell.column != Cell.column:
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)
        if cell.column == Cell.column and cell.row != Cell.row:
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)
        if cell.block == Cell.block and (cell.column != Cell.column or cell.row != Cell.row):
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)

    for eli in Cell.eliminate:
        for num in Cell.potential:
            if eli == num:
                Cell.potential.remove(num)

    return Cell.potential



def check_not_finish(cells):
    for cell in cells:
        if cell.number == 0:
            return True
    else:
        return False

def solve_board(cells):
    while check_not_finish(cells):
        for cell in cells:
            if cell.number == 0 and not cell.clue:
                cell.potential = potentialList(cell, cells)
                if len(cell.potential) == 0:
                    x = cell.ordinal
                    cells[x].potential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    cells[x].eleminate = []
                    while True:
                        x -= 1
                        if not cells[x].clue:
                            if cells[x].number in cells[x].potential:
                                cells[x].potential.remove(cells[x].number)
                                cells[x].number = 0
                                break
                    break
                
                if cell.number == 0:
                    cell.number = cell.potential[0]

                







