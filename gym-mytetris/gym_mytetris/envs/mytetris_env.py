import pygame
import random
import gym

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

'''
MIT License

Copyright (c) 2019 Kavish Hukmani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.S = [['.....',
              '......',
              '..00..',
              '.00...',
              '.....'],
             ['.....',
              '..0..',
              '..00.',
              '...0.',
              '.....']]

        self.Z = [['.....',
              '.....',
              '.00..',
              '..00.',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '.0...',
              '.....']]

        self.I = [['..0..',
              '..0..',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '0000.',
              '.....',
              '.....',
              '.....']]

        self.O = [['.....',
              '.....',
              '.00..',
              '.00..',
              '.....']]

        self.J = [['.....',
              '.0...',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..00.',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '...0.',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '.00..',
              '.....']]

        self.L = [['.....',
              '...0.',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '..00.',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '.0...',
              '.....'],
             ['.....',
              '.00..',
              '..0..',
              '..0..',
              '.....']]

        self.T = [['.....',
              '..0..',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..00.',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '..0..',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '..0..',
              '.....']]

        self.shapes = [self.S, self.Z, self.I, self.O, self.J, self.L, self.T]
        shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
        self.color = shape_colors[self.shapes.index(shape)]
        self.rotation = 0


class MyTetrisEnv(gym.Env):

    
    def __init__(self):
            
        """
        10 x 20 square grid
        shapes: S, Z, I, O, J, L, T
        represented in order by 0 - 6
        """

        pygame.font.init()

        # GLOBALS VARS
        self.s_width = 800
        self.s_height = 700
        self.play_width = 300  # meaning 300 // 10 = 30 width per block
        self.play_height = 600  # meaning 600 // 20 = 20 height per block
        self.block_size = 30

        self.top_left_x = (self.s_width - self.play_width) // 2
        self.top_left_y = self.s_height - self.play_height

        # SHAPE FORMATS

        self.S = [['.....',
              '......',
              '..00..',
              '.00...',
              '.....'],
             ['.....',
              '..0..',
              '..00.',
              '...0.',
              '.....']]

        self.Z = [['.....',
              '.....',
              '.00..',
              '..00.',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '.0...',
              '.....']]

        self.I = [['..0..',
              '..0..',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '0000.',
              '.....',
              '.....',
              '.....']]

        self.O = [['.....',
              '.....',
              '.00..',
              '.00..',
              '.....']]

        self.J = [['.....',
              '.0...',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..00.',
              '..0..',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '...0.',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '.00..',
              '.....']]

        self.L = [['.....',
              '...0.',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..0..',
              '..00.',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '.0...',
              '.....'],
             ['.....',
              '.00..',
              '..0..',
              '..0..',
              '.....']]

        self.T = [['.....',
              '..0..',
              '.000.',
              '.....',
              '.....'],
             ['.....',
              '..0..',
              '..00.',
              '..0..',
              '.....'],
             ['.....',
              '.....',
              '.000.',
              '..0..',
              '.....'],
             ['.....',
              '..0..',
              '.00..',
              '..0..',
              '.....']]

        self.shapes = [self.S, self.Z, self.I, self.O, self.J, self.L, self.T]
        self.shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
        # index 0 - 6 represent shape
        self.bag = []
        self.locked_positions = {}
        
        self.change_piece = False
        self.run = True
        self.current_piece = self.get_shape()
        self.next_piece = self.get_shape()
        self.held_piece = None
        self.hold_used = False
        self.score = 0
        self.win = None
        self.first_time = True
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=1, shape=
                    (200))
    
    def reset(self):
        self.change_piece = False
        self.run = True
        self.locked_positions = {}
        self.grid = self.create_grid()
        self.current_piece = self.get_shape()
        self.next_piece = self.get_shape()
        self.held_piece = None
        self.hold_used = False
        self.score = 0
        
        if self.win != None:
            pygame.display.quit()
            self.win = None
        self.first_time = True
        l = [0]*200
        for y in range(20):
            for x in range(10):
                if self.grid[y][x] != (0,0,0):
                    l[y*10+x] = 1
        return l
        
    def step(self,action):
        self.grid = self.create_grid(self.locked_positions)
        
        
        self.first_time = False
        if action == 0:
            self.current_piece.x -= 1
            if not self.valid_space(self.current_piece, self.grid):
                self.current_piece.x += 1

        elif action == 1:
            self.current_piece.x += 1
            if not self.valid_space(self.current_piece, self.grid):
                self.current_piece.x -= 1

        elif action == 2:
            self.current_piece.y += 1
            if not self.valid_space(self.current_piece, self.grid):
                self.current_piece.y -= 1

        elif action == 3:
            self.current_piece.rotation += 1
            if not self.valid_space(self.current_piece, self.grid):
                self.current_piece.rotation -= 1
 
        if not self.first_time:
            self.current_piece.y += 1
            if not self.valid_space(self.current_piece, self.grid) and self.current_piece.y > 0:
                self.current_piece.y -= 1
                self.change_piece = True
        
        shape_pos = self.convert_shape_format(self.current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                self.grid[y][x] = self.current_piece.color
        
        actual_score = 0
        done = False
        
        if self.change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                self.locked_positions[p] = self.current_piece.color

            self.current_piece = self.next_piece
            self.next_piece = self.get_shape()
            self.change_piece = False
            self.hold_used = False
            actual_score = self.clear_rows(self.grid, self.locked_positions) * 10
            self.score += actual_score
        
        #if actual_score == 0:
        #    actual_score = 1
        if self.check_lost(self.locked_positions):
            done = True
            actual_score = -1
        l = [0]*200
        for y in range(20):
            for x in range(10):
                if self.grid[y][x] != (0,0,0):
                    l[y*10+x] = 1
        shape_pos = self.convert_shape_format(self.current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                l[y*10+x] = -1
        if actual_score == 0:
            actual_score = 0.1
        elif actual_score > 0:
            actual_score*=4
        return l, actual_score, done, {}
    
    def render_local(self):
        if self.win == None:
            self.win = pygame.display.set_mode((self.s_width, self.s_height))
            pygame.display.set_caption('Tetris')
            self.win.fill((0, 0, 0))
            pygame.display.update()
        else:
            self.draw_window(self.win, self.grid, self.score)
            self.draw_next_shape(self.next_piece, self.win)
            self.draw_held_shape(self.held_piece, self.win)
            pygame.display.update()

        if self.check_lost(self.locked_positions):
            self.draw_text_middle("You Lost! :(", 80, (255, 255, 255), self.win)
            pygame.display.update()
    
    def get_new_state(self,state):
        piece = [0]*4
        new_state = [0]*40
        
        shape_pos = self.convert_shape_format(self.current_piece)
        count = 0
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                piece[count] = float(((20-y)*10+x)/20)
                state[y*10+x] = 0
                count+=1
        for x in range(10):
            block = False
            for y in range(4):
                s = 0
                for z in range(5):
                    if state[(y*5+z)*10+x] == 1:
                        s+=2**z
                s/=32
                new_state[y*10+x] = s
        return [new_state,piece]
                        
                
        
        
    def create_grid(self,locked_positions={}):#ok
        grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_positions:
                    c = locked_positions[(j, i)]
                    grid[i][j] = c

        return grid


    def convert_shape_format(self,shape):#ok
        positions = []
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions


    def valid_space(self,shape, grid):#ok
        accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = self.convert_shape_format(shape)
        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True


    def check_lost(self,positions):#ok
        for pos in positions:
            x, y = pos
            if y < 1:
                return True

        return False


    def get_shape(self):#ok
        if len(self.bag) == 0:
            self.make_bag()
        piece = random.choice(self.bag)
        self.bag.remove(piece)
        return Piece(5, 0, piece)


    def make_bag(self):#ok
        self.bag = self.shapes.copy()


    def draw_text_middle(self,text, size, color, surface):#ok
        font = pygame.font.SysFont('freesansbol.tff', size, bold=True)
        label = font.render(text, 1, color)
        surface.blit(label, (self.top_left_x + self.play_width/2 - (label.get_width()/2), self.top_left_y + self.play_height/2 - (label.get_height()/2)))


    def draw_grid(self,surface, grid):#ok
        sx = self.top_left_x
        sy = self.top_left_y

        for i in range(len(grid)):
            pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * self.block_size), (sx + self.play_width, sy + i * self.block_size))
            for j in range(len(grid[1])):
                pygame.draw.line(surface, (128, 128, 128), (sx + j * self.block_size, sy),
                                 (sx + j * self.block_size, sy + self.play_height))


    def clear_rows(self,grid, locked):#ok
        inc = 0

        for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                ind = i

                for j in range(len(row)):
                    try:
                        del locked[(j, i)]
                    except:
                        continue

        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newkey = (x, y + inc)
                    locked[newkey] = locked.pop(key)

        return inc


    def draw_next_shape(self,shape, surface):#ok
        font = pygame.font.SysFont('freesansbol.tff', 30)
        label = font.render('Next Piece', 1, (255, 255, 255))

        sx = self.top_left_x + self.play_width + 50
        sy = self.top_left_y + self.play_height/2 - 100
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (sx + j*self.block_size, sy + i*self.block_size, self.block_size, self.block_size), 0)

        surface.blit(label, (sx + 10, sy - 30))  # TODO add borders to the pieces


    def draw_held_shape(self,shape, surface):#ok
        font = pygame.font.SysFont('freesansbol.tff', 30)
        label = font.render('Held Piece', 1, (255, 255, 255))

        sx = self.top_left_x - self.play_width + 50
        sy = self.top_left_y + self.play_height/2 - 100

        if shape is not None:
            format_shape = shape.shape[shape.rotation % len(shape.shape)]

            for i, line in enumerate(format_shape):
                row = list(line)
                for j, column in enumerate(row):
                    if column == '0':
                        pygame.draw.rect(surface, shape.color, (sx + j*self.block_size, sy + i*self.block_size, self.block_size, self.block_size), 0)

        surface.blit(label, (sx + 10, sy - 30))  # TODO add borders to the pieces


    def draw_window(self,surface, grid, score=0):#ok
        surface.fill((0, 0, 0))

        font = pygame.font.SysFont('freesansbold.ttf', 60)
        label = font.render('Tetris', 1, (255, 255, 255))

        surface.blit(label, (self.top_left_x + self.play_width / 2 - (label.get_width() / 2), 30))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (self.top_left_x + j*self.block_size, self.top_left_y +i*self.block_size, self.block_size, self.block_size), 0)
        pygame.draw.rect(surface, (255, 0, 0), (self.top_left_x, self.top_left_y, self.play_width, self.play_height), 5)

        font = pygame.font.SysFont('freesansbol.tff', 30)
        label = font.render('Score: ' + str(score), 1, (255, 255, 255))

        sx = self.top_left_x + self.play_width + 50
        sy = self.top_left_y + self.play_height / 2 - 100

        surface.blit(label, (sx + 20, sy + 160))
        self.draw_grid(surface, grid)


    def hold_piece(self,current_piece, held_piece, next_piece):#ok
        if held_piece is None:
            held_piece = current_piece
            current_piece = next_piece
            next_piece = self.get_shape()
        else:
            held_piece, current_piece = current_piece, held_piece
        return current_piece, held_piece, next_piece

    def close(self):
        self.reset()
