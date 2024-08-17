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

def char_to_arrow(key_pressed, model):
    """
    If input is "udlr" convert this to a direction
    """
    MIN_LEVEL = 1

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in MOVE_DELTAS:
            model.move_cursor(MOVE_DELTAS[key_pressed][0], MOVE_DELTAS[key_pressed][1])
            return True
    return False

def handle_spacebar(key_pressed, model):
    """
    Write "space" if the input is a spacebar
    """
    MIN_LEVEL = 1

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
    MIN_LEVEL = 1

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
    Write "space" if the input is a spacebar
    """
    MIN_LEVEL = 1

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in SYM_TABS:
            model.insert_char_at_cursor(TAB_SYM)
            return True
    return False

def handle_enter(key_pressed, model):
    """
    If input is enter/return/grave, create a new row
    """
    MIN_LEVEL = 1

    if model.get_level() >= MIN_LEVEL:
        if key_pressed in SYM_ENTERS:
        #will not be inserting a new char, will insert a new row/line!!!
        # model.insert_char_at_cursor(ENTER)
            return True
    elif key_pressed == ENTER:
        return True
    return False

def handle_special(key_pressed, model):
    """
    If input is . T Y U O then call the respective special handlers
    """
    pass

def handle_numbers(key_pressed, model):
    """
    If input is 0 or 1, update the number
    """
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
    MIN_LEVEL = 1
    
    if model.get_level() >= MIN_LEVEL:
        if key_pressed in REGULAR_CHAR_TO_CHAR and REGULAR_CHAR_TO_CHAR[key_pressed] == 'e':
            if model.check_space():
                model.delete_space()
                model.insert_char_at_cursor(" ")
                return True
    return False