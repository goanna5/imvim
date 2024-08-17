from constants import *

def handle_back_and_del(key_pressed, model) -> bool:
    """
    If input is backspace or delete,
    remove entire row
    """
    if key_pressed in ["BackSpace", "Delete"]:
        model.delete_current_row()
        return True
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
    if key_pressed in [UP, DOWN, LEFT, RIGHT]:
        model.move_cursor(MOVE_DELTAS[key_pressed][0], MOVE_DELTAS[key_pressed][1])
        return True
    return False

def handle_spacebar(key_pressed, model):
    """
    Write "space" if the input is a spacebar
    """
    if key_pressed == "space":
        model.insert_char_at_cursor("space")
        return True
    return False

def regular_char_to_char(key_pressed, model):
    if key_pressed in REGULAR_CHAR_TO_CHAR:
        model.insert_char_at_cursor(REGULAR_CHAR_TO_CHAR[key_pressed])
        return True
    return False

def caeser_cipher(input, model, other):
    """
    caesar cipher shift input if it is a letter
    ignore other characters.
    """
    pass

def convert_space(input, model, other):
    """
    HARD
    If we have just created the word "space" *ALL LOWERCASE*
    then replace "space" with " "
    Important: should do nothing if the word "space" was made
    due to a spacebar press
    (when the user presses the spacebar it prints "space" but
    this shouldnt immediately turn back into a " ")
    """
    pass