from constants import *

class ImvimModel():
    def __init__(self) -> None:
        self.player_text = []
        self.cursor_coords = (0,0)
        self.level = 0
        self.goal_text = GOAL_ZERO
        self.historical_keypress = [" "] * 10
        self.max_line_width = 20
        self.numbers_entered = 0 #track how many binary digits have been entered

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
        if self.is_printable(char):
            col, row = self.cursor_coords
            if len(self.player_text) <= row:
                self.player_text.append("")
            elif col >= self.max_line_width:
                row = row + 1
                self.cursor_coords = (0, row)
                col, row = self.cursor_coords
                #if cursor now on row that doesn't exist, add new row
                if row > len(self.player_text):
                    self.player_text.append("")
            
            #this is to make the overflow go to the next row, but it would need a for loop
            # if len(self.player_text[row] + char) > self.max_line_width:
            #     if row >= len(self.player_text):
            #         self.player_text.append("")
            #     self.player_text[row + 1] = [self.max_line_width - 1:] + self.player_text[row + 1]
            self.player_text[row] = self.player_text[row][:col] + char + self.player_text[row][col:self.max_line_width - 1]
            self.move_cursor(0, len(char))
            
    def enter_at_cursor(self) -> None:
        current_line = self.get_current_line()
        x, y = self.cursor_coords
        self.player_text[y] = current_line[:x]
        self.player_text.insert(y+1, current_line[x:])
        self.cursor_coords = (0, y+1)
        print(f"cursor coords: {self.cursor_coords}")


    def move_cursor(self, row_delta: int, col_delta: int) -> None:
        c, r = self.cursor_coords
        max_r = len(self.player_text) - 1
        new_r = min(max(r + row_delta, 0), max_r)
        max_c = len(self.player_text[new_r])
        new_c = min(max(c + col_delta, 0), max_c)
        self.cursor_coords = (new_c, new_r)
    
    # deletes contents of the current row (row array is still in the overall array)
    def delete_current_row(self):
        if self.player_text != []:
            """row = self.player_text[self.cursor_coords[1]]
            for i in range(len(row)):
                row.pop()"""
            self.player_text[self.cursor_coords[1]] = ""
        # self.move_cursor(0, len(row))
        self.move_cursor(0, 0)

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
        self.cursor_coords = (0,0)
        self.level += 1
        self.player_text = START_TEXTS[self.level]
        self.goal_text = GOAL_TEXTS[self.level]

    def set_historical_keypress(self, keypressed):
        if len(self.historical_keypress) >= 10:
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
    
    # Returns true if the char is printable, false if not
    def is_printable(self, char: str) -> bool:
        return (char in PRINTABLE)
    
    #checks if the previous historical keypresses are 'c', 'a', 'p', 's'
    def check_space(self) -> bool:
        if len(self.historical_keypress) >= 5:
            if (REGULAR_CHAR_TO_CHAR[self.historical_keypress[-1]] == 'c' 
                and REGULAR_CHAR_TO_CHAR[self.historical_keypress[-2]] == 'a' 
                and REGULAR_CHAR_TO_CHAR[self.historical_keypress[-3]] == 'p' 
                and REGULAR_CHAR_TO_CHAR[self.historical_keypress[-4]] == 's'):
                return True 
        return False
    
    #remove the spac from the terminal
    def delete_space(self) -> None:
        # currently broken
        # NEED TO CHANGE - CURRENTLY FOR THE ONE-CHARACTER-PER-ENTRY THINGO
        col, row = self.cursor_coords
        for i in range(4):
            print("cords", col, row)
            #this is in case the space is across two lines
            if len(self.player_text[row]) < 1 or col < 1:
                self.cursor_coords = (self.end_of_previous_row(self.cursor_coords[1]),self.cursor_coords[1] - 1)
                col, row = self.cursor_coords
            print("row?",(self.player_text[row][(col):self.max_line_width - 1]))
            self.player_text[row] = self.player_text[row][:(col - 1)] + self.player_text[row][(col):self.max_line_width - 1]
            self.cursor_coords = (self.cursor_coords[0] - 1,self.cursor_coords[1])
            col, row = self.cursor_coords
        #self.move_cursor(0, 4)
    
    #returns the position of the last character of the previous row
    def end_of_previous_row(self, current_row: int) -> int:
        if current_row > 0:
            return len(self.player_text[current_row - 1]) - 1
        
    def add_number(self, num: int) -> None:
        pass
