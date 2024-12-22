import pygame
import random
import copy


#yellow -1
#red 1



class Bitboard:
    """
    Represents a Connect Four game state using bitboards for efficient computation.

    Attributes:
    -----------
    player_bitboards : list
        Stores the bitboards for both players. Index 1 is for red, -1 is for yellow.
    height : list
        Tracks the height of the discs in each column.
    colors : list
        Colors for each player and empty slots.
    turn : int
        Indicates the current player's turn (1 for red, -1 for yellow).
    winner : int or None
        Indicates the winner of the game. None if no winner yet, 0 for draw, 1 or -1 for players.
    """
    def __init__(self):
        self.player_bitboards = [None, 0, 0]  
        self.height = [0] * 7
        self.colors = ["#ffffff", "#db737a","#ccdb74"]
        self.turn = 1  
        self.winner = None

    def get_moves(self):
        """
        Retrieves a list of valid column indices for the next move.

        Returns:
        --------
        list
            List of valid column indices where discs can be dropped.
        """
        moves = []
        for index in range(7):
            if self.height[index] < 6:
                moves.append(index)
        return moves

    def play(self, index):
        """
        Plays a disc in the specified column for the current player.

        Parameters:
        -----------
        index : int
            The column index where the disc should be dropped.
        """
        moves = self.get_moves()

        if index not in moves:
            index = random.choice(moves)

        bit_position = index * 7 + self.height[index]
        self.player_bitboards[self.turn] |= 1 << bit_position
        self.height[index] += 1
        
        self.winner = self.get_winner()

        self.turn = -self.turn


    def get_winner(self):
        """
        Checks if there is a winner or a draw in the game.

        Returns:
        --------
        int or None
            The winner of the game (1 or -1), 0 for draw, or None if the game is ongoing.
        """
        winner = None

        if self.height == [6,6,6,6,6,6,6]:
            winner = 0
        
        bitboard = self.player_bitboards[self.turn]
        directions = [1, 6, 7, 8]
        for direction in directions:
            shifted = bitboard & (bitboard >> direction)
            if shifted & (shifted >> (2 * direction)):
                winner = self.turn
        return winner

    def set_state(self,state):
        """
        Sets the current game state to a given state.

        Parameters:
        -----------
        state : tuple
            A tuple containing player bitboards, column heights, and current turn.
        """
        temp_state = copy.deepcopy(state)
        self.player_bitboards = temp_state[0]
        self.height = temp_state[1]
        self.turn = temp_state[2]

    def get_state(self):
        """
        Retrieves the current game state.

        Returns:
        --------
        tuple
            A tuple containing player bitboards, column heights, and current turn.
        """
        state = copy.deepcopy([self.player_bitboards,self.height,self.turn])
        return state

    def reset(self):
        """
        Resets the game state to its initial configuration.
        """
        self.player_bitboards = [None, 0, 0]  
        self.height = [0] * 7
        self.turn = 1  
        self.winner = None

    def show(self, surface, width, height):
        """
        Displays the current game state on a Pygame surface.

        Parameters:
        -----------
        surface : pygame.Surface
            The surface to draw the game board on.
        width : int
            The width of the game board.
        height : int
            The height of the game board.
        """
        pygame.draw.rect(surface, "#189AB4", pygame.Rect(0, 0, width, height))
        for i in range(6):
            for j in range(7):
                
                position = (5-i + j*7)
                player = int(((self.player_bitboards[1] >> position) & 1) - ((self.player_bitboards[-1] >> position) & 1))
                color = self.colors[player]
                pygame.draw.circle(surface, color, ((j+0.5)*width/7,(i+0.5)*height/6), 30)
    
                
    def user_move(self, surface, width, height):
        """
        Handles the user's move by waiting for mouse input and updating the game state.

        Parameters:
        -----------
        surface : pygame.Surface
            The surface to draw the game board on.
        width : int
            The width of the game board.
        height : int
            The height of the game board.
        """
        finished = False
        step = (width//7)
        moves = self.get_moves()

        while not finished:
            events = pygame.event.get()
            pos = pygame.mouse.get_pos()
            i = pos[0]//step
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and (i in moves):
                    self.play(i)
                    return

            self.show(surface, width, height)
            if i in moves:
                pygame.draw.circle(surface, "#808080", ((i+0.5)*width/7,(0.5)*height/6), 30)

            pygame.display.flip()

def display_bits_in_grid(num):
    """
    Display a binary representation of a number as a 7x7 grid.

    Parameters:
    -----------
    num : int
        The number to be displayed as a binary grid.
    """
    binary = bin(num)[2:].zfill(49)
    binary = binary[-49:]
    grid = [[0 for _ in range(7)] for _ in range(7)]

    for bit_position in range(49):
        row = bit_position % 7 
        col = 6 - bit_position // 7 
        grid[row][col] = int(binary[bit_position])  

    for row in grid:
        print(" ".join(map(str, row)))
