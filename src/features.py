from constants import *

def handle_back_and_del(key_pressed, model) -> bool:
    """
    If input is backspace or delete,
    remove entire row
    """
    MIN_LEVEL = 0

    if key_pressed in ["BackSpace", "Delete"]:
        if model.get_level() >= MIN_LEVEL:
            model.delete_current_row()
            return True
        else:
            print("something's wrong - delete row should always be active")
    return False

def arrow_to_char(key_pressed, model):
    """
    If input is an arrow key, write corresponding letter
    """
    if key_pressed in ARROW_TO_CHAR:
        model.insert_char_at_cursor(ARROW_TO_CHAR[key_pressed])
        return True
    return False


def char_to_arrow(key_pressed, model):
    """
    If input is "udlr" convert this to a direction
    """
    # before min_level, arrow keys move normal distances
    MIN_LEVEL = 1  # at min_level, arrow keys move cursed distances
    MIN_LEVEL_TWO = 1  # min_level 2: 'udlr' move cursed distances

    if model.get_level() < MIN_LEVEL_TWO:
        if model.get_level() < MIN_LEVEL:
            if key_pressed in NORMAL_MOVE_DELTAS:
                model.move_cursor(NORMAL_MOVE_DELTAS[key_pressed][0], NORMAL_MOVE_DELTAS[key_pressed][1])
                return True
        else:
            if key_pressed in CURSED_MOVE_DELTAS:
                model.move_cursor(CURSED_MOVE_DELTAS[key_pressed][0], CURSED_MOVE_DELTAS[key_pressed][1])
                return True
    else:
        if key_pressed in MOVE_DELTAS:
            model.move_cursor(MOVE_DELTAS[key_pressed][0], MOVE_DELTAS[key_pressed][1])
            return True
    return False

def handle_spacebar(key_pressed, model):
    """
    Write "space" if the input is a spacebar
    """
    MIN_LEVEL = 3

    if key_pressed == "space":
        if model.get_level() >= MIN_LEVEL:
            model.insert_char_at_cursor("s")
            model.insert_char_at_cursor("p")
            model.insert_char_at_cursor("a")
            model.insert_char_at_cursor("c")
            model.insert_char_at_cursor("e")
        else:
            model.insert_char_at_cursor(" ")
        return True
    return False

def regular_char_to_char(key_pressed, model):
    MIN_LEVEL = 3

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in REGULAR_CHAR_TO_CHAR:
            if key_pressed in SYMBOLS_MORE_THAN_ONE_CHAR:
                #this doesn't work -> will manually write
                to_add = str(SYMBOLS_MORE_THAN_ONE_CHAR[key_pressed])
                for i in str(to_add):
                    model.insert_char_at_cursor(i)
            else:
                model.insert_char_at_cursor(REGULAR_CHAR_TO_CHAR[key_pressed])
            return True
    return False

def handle_tab(key_pressed, model):
    """
    Handles tabs
    """
    MIN_LEVEL = 3

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in SYM_TABS:
            model.insert_char_at_cursor(TAB_SYM)
            return True
    return False

def handle_enter(key_pressed, model):
    """
    If input is enter/return/grave, create a new row
    """
    MIN_LEVEL = 3

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in SYM_ENTERS:
        #will not be inserting a new char, will insert a new row/line!!!
        # model.insert_char_at_cursor(ENTER)
            model.enter_at_cursor()
            return True
    elif key_pressed == ENTER:
        model.enter_at_cursor()
        return True
    return False

def handle_special(key_pressed, model):
    """
    If input is . T Y U O then call the respective special handlers
    """
    pass

def handle_force_quit(key_pressed, window):
    """
    If input is O then force quit.
    """
    if key_pressed == "O":
        window.destroy()
        exit()

# def handle_caps_lock(key_pressed):
#     """
#     If input is . then toggle caps lock
#     """
#     return key_pressed == FULL_STOP
        
def handle_clear_file(key_pressed, model, view):
    """
    If input is U, clear file
    """
    if key_pressed == "U":
        num_lines_to_clear = len(model.get_player_text())
        model.reset_player_text()
        view.redraw_section(num_lines_to_clear, "")
        return True
    return False


def handle_numbers(key_pressed, model):
    """
    If input is 0 or 1, update the number
    """
    MIN_LEVEL = 2
    if model.get_level() >= MIN_LEVEL:
        if key_pressed in SYMBOLS_TO_NUMBERS:
            model.add_number(SYMBOLS_TO_NUMBERS[key_pressed])
            return True
    return False


def convert_space(key_pressed, model):
    """
    HARD
    If we have just created the word "space" *ALL LOWERCASE*
    then replace "space" with " "
    Important: should do nothing if the word "space" was made
    due to a spacebar press
    (when the user presses the spacebar it prints "space" but
    this shouldnt immediately turn back into a " ")
    """
    MIN_LEVEL = 3
    
    if model.get_level() >= MIN_LEVEL:
        if key_pressed in REGULAR_CHAR_TO_CHAR and REGULAR_CHAR_TO_CHAR[key_pressed] == 'e':
            if model.check_space():
                model.delete_space()
                model.insert_char_at_cursor(" ")
                return True
    return False