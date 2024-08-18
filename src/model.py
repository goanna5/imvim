from constants import *

class ImvimModel():
    def __init__(self) -> None:
        self.cursor_coords = (0,0)
        self.level = 0
        self.player_text = START_ZERO
        self.goal_text = GOAL_ZERO
        self.historical_keypress = [" "] * 10
        self.max_line_width = 60
        self.numbers_entered = 0 #track how many binary digits have been entered
        self.need_to_redraw = False
        # self.last_correct_char = (0,0)
        self.pop_up = False
        #self.capsLock = False

    # def get_caps(self):
    #     return self.capsLock
    
    # def set_caps(self, caps: bool):
    #     self.capsLock = caps

    def get_cursor_coords(self):
        # (col_num, row_num)
        # i.e. (x, y) with (0,0) being the top left corner
        return self.cursor_coords

    def get_player_text(self):
        # Returns a list of strings where each string is a line of text
        return self.player_text

    def reset_player_text(self):
        self.player_text = []
        self.cursor_coords = (0,0)
        self.numbers_entered = 0
    
    def get_goal_text(self):
        return self.goal_text
    
    def get_level(self):
        # each level adds a new layer of complexity
        return self.level

    def get_pop_up(self):
        return self.pop_up
    
    def set_pop_up(self, to_set):
        self.pop_up = to_set
        
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
                # col, row = self.cursor_coords
                #if cursor now on row that doesn't exist, add new row
                if row >= len(self.player_text):
                    self.player_text.append("")
            if len(self.player_text[row] + char) > self.max_line_width:
                self.cascade_row(row)
            #this is to make the overflow go to the next row, but it would need a for loop
            
            self.player_text[row] = self.player_text[row][:col] + char + self.player_text[row][col:self.max_line_width - 1]
            self.move_cursor(0, len(char))
    
    # cascade the first row
    def cascade_row(self, row):
        if row >= len(self.player_text) - 1:
            self.player_text.append("")

        self.player_text[row + 1] = self.player_text[row][(self.max_line_width - 1):] + self.player_text[row + 1]
        if len(self.player_text[row + 1]) > self.max_line_width:
            self.cascade_rows(row + 1)
            self.player_text[row + 1] = self.player_text[row + 1][:self.max_line_width]
        self.need_to_redraw = True
    
    #cascade subsequent rows
    def cascade_rows(self, row):
        if row >= len(self.player_text) - 1:
            self.player_text.append("")

        self.player_text[row + 1] = self.player_text[row][(self.max_line_width):] + self.player_text[row + 1]
        if len(self.player_text[row + 1]) > self.max_line_width:
            self.cascade_rows(row + 1)
            self.player_text[row + 1] = self.player_text[row + 1][:self.max_line_width]

    def enter_at_cursor(self) -> None:
        current_line = self.get_current_line()
        x, y = self.cursor_coords
        self.player_text[y] = current_line[:x]
        self.player_text.insert(y+1, current_line[x:])
        self.cursor_coords = (0, y+1)
        print(f"cursor coords: {self.cursor_coords}")
        self.need_to_redraw = True


    def move_cursor(self, row_delta: int, col_delta: int) -> None:
        c, r = self.cursor_coords
        max_r = len(self.player_text) - 1
        new_r = min(max(r + row_delta, 0), max_r)
        max_c = len(self.player_text[new_r])
        new_c = min(max(c + col_delta, 0), max_c)
        self.cursor_coords = (new_c, new_r)
    
    # deletes contents of the current row (row array is still in the overall array)
    def delete_current_row(self):
        # true if we need to redraw the whole thing
        if self.player_text and self.player_text != [""]:
            """row = self.player_text[self.cursor_coords[1]]
            for i in range(len(row)):
                row.pop()"""
            if self.player_text[self.cursor_coords[1]]:
                self.player_text[self.cursor_coords[1]] = ""
            else:
                self.player_text.pop(self.cursor_coords[1])
                if self.cursor_coords[1]:
                    self.move_cursor(-1, self.max_line_width)
                else:
                    self.move_cursor(0, 0)
                self.need_to_redraw = True
                return
        # self.move_cursor(0, len(row))
        self.move_cursor(0, 0)

    def is_level_beaten(self):
        # return not self.level
        return self.player_text == self.goal_text
    
    """def get_last_correct_char(self):
        return self.last_correct_char
    
    def update_last_correct_char(self):
        for i, row in enumerate(self.goal_text):
            if i >= len(self.player_text):  # goal text has more rows than player text
                self.last_correct_char = (0, i)
                if i > self.cursor_coords[1]:
                    self.need_to_redraw = True
                return
            if row == self.player_text[i]:  # this row matches
                continue
            else:
                # last correct char is on this row
                for j, char in enumerate(row):
                    if j >= len(self.player_text[i]) or char != self.player_text[i][j]:
                        self.last_correct_char = (j, i)
                        if i > self.cursor_coords[1]:
                            self.need_to_redraw = True
                        return
        x = len(self.goal_text[-1])
        y = len(self.goal_text) - 1
        self.last_correct_char = (x, y)
        if y > self.cursor_coords[1]:
            self.need_to_redraw = True"""
    
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
        self.update_last_correct_char()

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
        num = int(num)
        col, row = self.cursor_coords
        if col == 0 or (col > 0 and self.player_text[row][col-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            print("string")
            self.numbers_entered = 0
        self.numbers_entered = (1 + self.numbers_entered)
        print(self.numbers_entered)
        if self.numbers_entered == 1:
            self.insert_char_at_cursor(str(num))
        else:
            col, row = self.cursor_coords
            current_num = int(self.player_text[row][col - 1])
            current_num = (current_num + (num * (2**(self.numbers_entered-1)))) % 10
            self.player_text[row] = self.player_text[row][:col - 1] + str(current_num) + self.player_text[row][col:self.max_line_width - 1]
        self.numbers_entered %= 4

