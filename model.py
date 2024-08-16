class ImvimModel():
    def __init__(self) -> None:
        self.player_text = []
        self.cursor_coords = (0,0)
        self.level = 0
        self.goal_text = []
    
    def get_cursor_coords(self):
        return self.cursor_coords

    def get_player_text(self):
        ''' Returns a list of strings where each string is a line of text
        '''
        return self.player_text
    
    def get_level(self):
        # each level adds a new layer of complexity
        return self.level

    def update_row(self, row_num: int, new_text: str):
        # (0 indexed) 0 is top row
        if row_num < len(self.player_text):
            self.player_text[row_num] = new_text
    
    def insert_char_at_cursor(self, char: str) -> None:
        row, col = self.cursor_coords
        self.player_text[row] = self.player_text[row][:col] + char + self.player_text[row][col:]

    def move_cursor(self, row_delta: int, col_delta: int) -> None:
        r, c = self.cursor_coords
        max_r = len(self.player_text) - 1
        max_c = len(self.player_text[r])
        new_r = min(max(r + row_delta, 0), max_r)
        new_c = min(max(c + col_delta, 0), max_c)
        self.cursor_coords = (new_r, new_c)
    
    def delete_current_row(self):
        self.player_text.remove(self.cursor_coords[0])

    def is_level_beaten(self):
        return self.player_text == self.goal_text