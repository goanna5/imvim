from constants import *

class ImvimModel():
    def __init__(self) -> None:
        self.player_text = []
        self.cursor_coords = (0,0)
        self.level = 0
        self.goal_text = GOAL_ZERO
        self.historical_keypress = []
        self.max_line_width = 60
    
    def get_cursor_coords(self):
        # (col_num, row_num)
        # i.e. (x, y) with (0,0) being the top left corner
        return self.cursor_coords

    def get_player_text(self):
        # Returns a list of strings where each string is a line of text
        return self.player_text
    
    def get_goal_text(self):
        return self.goal_text
    
    def get_level(self):
        # each level adds a new layer of complexity
        return self.level

    def update_row(self, row_num: int, new_text: str):
        # (0 indexed) 0 is top row
        if row_num < len(self.player_text):
            self.player_text[row_num] = new_text
    
    def insert_char_at_cursor(self, char: str) -> None:
        col, row = self.cursor_coords
        if len(self.player_text) <= row:
            self.player_text.append(char)
        elif col >= self.max_line_width:
            self.player_text.append(char)
            self.cursor_coords = (1, row+1)
            return
        else:
            self.player_text[row] = self.player_text[row][:col] + char + self.player_text[row][col:]
        self.move_cursor(0, len(char))


    def move_cursor(self, row_delta: int, col_delta: int) -> None:
        c, r = self.cursor_coords
        max_r = len(self.player_text) - 1
        max_c = len(self.player_text[r])
        new_r = min(max(r + row_delta, 0), max_r)
        new_c = min(max(c + col_delta, 0), max_c)
        self.cursor_coords = (new_c, new_r)
    
    def delete_current_row(self):
        self.player_text.pop(self.cursor_coords[1])

    def is_level_beaten(self):
        return self.player_text == self.goal_text
    
    def get_last_correct_char(self):
        for i, row in enumerate(self.goal_text):
            if i >= len(self.player_text):
                return (i, 0)
            if row == self.player_text[i]:
                continue
            else:
                # last correct char is on this row
                for j, char in enumerate(row):
                    if j >= len(self.player_text[i]) or char != self.player_text[i][j]:
                        return (i, j)
        return None
    
    def start_next_level(self) -> None:
        # when level complete, call this method
        if self.level == MAX_LEVEL:
            # if we are on the final level, do nothing
            return
        # reset all data stuff
        self.player_text = []
        self.cursor_coords = (0,0)
        self.level += 1
        self.goal_text = GOAL_TEXTS[self.level]

    def set_historical_keypress(self, keypressed):
        if len(self.historical_keypress) > 10:
            self.historical_keypress = self.historical_keypress[1:]
        self.historical_keypress.append(keypressed)
    
    def get_historical_keypress(self):
        return self.historical_keypress

    def get_line(self, line_num):
        # Return line specified by line num
        return self.player_text[line_num]

    def get_line_length(self, line_num):
        # Return length of the line specified by line num
        return len(self.get_line(line_num))

    def get_current_line(self):
        # Return current line
        return self.get_line(self.cursor_coords[1])

    def get_current_line_length(self):
        # Return length of current line
        return len(self.get_current_line())