MAX_LEVEL = 4


GOAL_ZERO = ["Hello, World!"]

GOAL_ONE = ["Level 1", 
            "is really intuitive", 
            "to navigate lol"]

GOAL_TWO = ["*Different challenge:",
            "Fix the text to look like the right, keep everything else:",
            "",
            "Bit of text up here",
            "bit down here",
            "3 lines?",
            "or 4..."]

GOAL_THREE = ["I built a lot of blocks up from earth",
              "to the maximum build height: 320",
              "(minecraft core!!)"]

GOAL_FOUR = ["Soooo super odd keyboard layouts huh",
             "&& this is meant to be (very) intuitive,",
             "*of course* duh, easy as 123."]

GOAL_TEXTS = [GOAL_ZERO, GOAL_ONE, GOAL_TWO, GOAL_THREE, GOAL_FOUR]

START_ZERO = ["================== Welcome to imvim! ==================",
"",
"Each level will introduce new uhh... intuitive... ",
"keybinds: your goal is to type the text on the right ",
"correctly on the left (MAKE SURE YOU DELETE ALL HINTS). ",
"",
"Hints are your friend, **READ THEM** ",
"",
"To get started, delete all this text and then ",
"type the text on the right"]

START_ONE = ["(delete these lines) Hint: We made moving around *much* ",
             "more intuitive. Why does one press l to go right in vim..."]

START_TWO = ["*Different challenge:",
            "Fix the text to look like the right, keep everything else:",
            "",
            "Bit of text p here",
            "bit down her",
            "3 lines?",
            "or ..."]

START_THREE = ["Hint: for maximum efficiency you can move super quick :D"]

START_FOUR = ["Hint: think about what kinda keyboard layouts there are ",
               "- qwerty SUCKS. Directions are always constant dw ",
               "We maximised the efficiency of this keyboard for ",
               "programmers: () {} are *central* yknow"]

START_TEXTS = [START_ZERO, START_ONE, START_TWO, START_THREE, START_FOUR]

KEY_PRESS_FRAME_HEIGHT = 150
TEXT_OFFSET = 4

# Constants related to moving the player
UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'


ARROW_UP = 'Up'
ARROW_DOWN = 'Down'
ARROW_LEFT = 'Left'
ARROW_RIGHT = 'Right'

# Costants related to caps enter tab
CAPS = "Caps_Lock"
ENTER = "Return"
TAB = "Tab"

# Constants related to symbols (symbol representation)
GRAVE_SYM = "`"
NOT_SYM = "~"
EXCLAMATION_SYM = "!"
AT_SYM = "@"
HASH_SYM = "#"
DOLLAR_SYM = "$"
PERCENT_SYM = "%"
CARET_SYM = "^"
AMPERSAND_SYM = "&"
ASTERISK_SYM = "*"
OPEN_PARENTHESIS_SYM = "("
CLOSE_PARENTHESIS_SYM = ")"
MINUS_SYM = "-"
UNDERSCORE_SYM = "_"
PLUS_SYM = "+"
EQUALS_SYM = "="
OPEN_BRACKET_SYM = "["
OPEN_BRACE_SYM = "{"
CLOSE_BRACKET_SYM = "]"
CLOSE_BRACE_SYM = "}"
BAR_SYM = "|"
BACKSLASH_SYM = "\\"
COLON_SYM = ":"
SEMICOLON_SYM = ";"
DOUBLE_QUOTES_SYM = "\""
SINGLE_QUOTE_SYM = "\'"
COMMA_SYM = ","
LESS_THAN_SYM = "<"
FULL_STOP_SYM = "."
GREATER_THAN_SYM = ">"
SLASH_SYM = "/"
QUESTION_MARK_SYM = "?"
POWER_SYM = "**"
EQUAL_TO_SYM = "=="
LOGICAL_AND_SYM = "&&"
LOGICAL_OR_SYM = "||"
TAB_SYM = "\t"
SPACE_SYM = " "

# Constants related to symbols (text representation)
GRAVE = "grave"
NOT = "asciitilde"
EXCLAMATION = "exclam"
AT = "at"
HASH = "numbersign"
DOLLAR = "dollar"
PERCENT = "percent"
CARET = "asciicircum"
AMPERSAND = "ampersand"
ASTERISK = "asterisk"
OPEN_PARENTHESIS = "parenleft"
CLOSE_PARENTHESIS = "parenright"
MINUS = "minus"
UNDERSCORE = "underscore"
PLUS = "plus"
EQUALS = "equal"
OPEN_BRACKET = "bracketleft"
OPEN_BRACE = "braceleft"
CLOSE_BRACKET = "bracketright"
CLOSE_BRACE = "braceright"
BAR = "bar"
BACKSLASH = "backaslash"
COLON = "colon"
SEMICOLON = "semicolon"
DOUBLE_QUOTES = "quotedbl"
SINGLE_QUOTE = "apostrophe"
COMMA = "comma"
LESS_THAN = "less"
FULL_STOP = "period"
GREATER_THAN = "greater"
SLASH = "slash"
QUESTION_MARK = "question"

# Constants relating to special functionality
RIGHT_TO_LEFT_OVERRIDE = "U+202E" #this is the unicode character
CHANGE_TAB_WIDTH = "tab width"
CLEAR_FILE = "clear"
FORCE_QUIT = "exit"

PRINTABLE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "\\n",
GRAVE_SYM, NOT_SYM, EXCLAMATION_SYM, AT_SYM, HASH_SYM, DOLLAR_SYM, PERCENT_SYM, CARET_SYM, AMPERSAND_SYM, ASTERISK_SYM, OPEN_PARENTHESIS_SYM, CLOSE_PARENTHESIS_SYM, MINUS_SYM, UNDERSCORE_SYM, PLUS_SYM, EQUALS_SYM, OPEN_BRACKET_SYM, OPEN_BRACE_SYM, CLOSE_BRACKET_SYM, CLOSE_BRACE_SYM, BAR_SYM, BACKSLASH_SYM, COLON_SYM, SEMICOLON_SYM, DOUBLE_QUOTES_SYM, SINGLE_QUOTE_SYM, COMMA_SYM, LESS_THAN_SYM,
FULL_STOP_SYM, GREATER_THAN_SYM, SLASH_SYM, QUESTION_MARK_SYM, POWER_SYM, EQUAL_TO_SYM, LOGICAL_AND_SYM, LOGICAL_OR_SYM, TAB_SYM, SPACE_SYM]

# Mapping of directions to coordinates
FULL_CURSED_MOVE_DELTAS = {
    UP: (-2, 0),
    DOWN: (3, 0),
    RIGHT: (0, 7),
    LEFT: (0, -5),
}

ARROW_MOVE_DELTAS = {
    ARROW_UP: (-1, 0),
    ARROW_DOWN: (1, 0),
    ARROW_RIGHT: (0, 1),
    ARROW_LEFT: (0, -1),
}

SORTA_CURSED_MOVE_DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    RIGHT: (0, 1),
    LEFT: (0, -1),
}

ARROW_TO_CHAR = {
    ARROW_UP : UP,
    ARROW_DOWN: DOWN,
    ARROW_LEFT: LEFT,
    ARROW_RIGHT: RIGHT,
}

REGULAR_CHAR_TO_CHAR = {
    # Numbers to symbols
    "0": AMPERSAND_SYM,
    "1": PLUS_SYM,
    "2": MINUS_SYM,
    "3": ASTERISK_SYM,
    "4": SLASH_SYM,
    "5": EQUALS_SYM,
    "6": PERCENT_SYM,
    "7": POWER_SYM,
    "8": LESS_THAN_SYM,
    "9": GREATER_THAN_SYM,

    # symbols to letters
    EXCLAMATION: "j",
    AT: "J",
    PERCENT: "h",
    CARET: "H",
    AMPERSAND: "f",
    ASTERISK: "F",
    OPEN_PARENTHESIS: "g",
    CLOSE_PARENTHESIS: "G",
    LESS_THAN: "L",

    # symbols to symbols
    NOT: GRAVE_SYM,
    MINUS: BAR_SYM,
    UNDERSCORE: CARET_SYM,
    PLUS: NOT_SYM,
    EQUALS: EXCLAMATION_SYM,
    OPEN_BRACE: COMMA_SYM,
    OPEN_BRACKET: COLON_SYM,
    CLOSE_BRACE: UNDERSCORE_SYM,
    CLOSE_BRACKET: HASH_SYM,
    BACKSLASH: DOLLAR_SYM,
    BAR: AT_SYM,
    COLON: OPEN_BRACE_SYM,
    SEMICOLON: CLOSE_BRACE_SYM,
    SINGLE_QUOTE: QUESTION_MARK_SYM,
    DOUBLE_QUOTES: BACKSLASH_SYM,
    GREATER_THAN: "\\n",
    EQUALS: EQUAL_TO_SYM,
    FULL_STOP: LOGICAL_AND_SYM,
    SLASH: LOGICAL_OR_SYM,

    # letters to letters
    "q": "q",
    "Q": "A",
    "w": "w",
    "W": "B",
    "e": "t",
    "E": "C",
    "R": "E",
    "t": "p",
    "y": "n",
    "i": "i",
    "I": "I",
    "o": "y",
    "p": "o",
    "P": "K",
    "a": "a",
    "A": "M",
    "s": "s",
    "S": "N",
    "D": "O",
    "k": "e",
    "K": "P",
    "L": "Q",
    "z": "z",
    "Z": "S",
    "x": "x",
    "X": "T",
    "c": "c",
    "C": "V",
    "v": "v",
    "V": "W",
    "b": "b",
    "B": "X",
    "n": "k",
    "N": "Y",
    "m": "m",
    "M": "Z",

    # letters to symbols
    "f": OPEN_PARENTHESIS_SYM,
    "F": OPEN_BRACKET_SYM,
    "g": DOUBLE_QUOTES_SYM,
    "G": SINGLE_QUOTE_SYM,
    "h": FULL_STOP_SYM,
    "H": SEMICOLON_SYM,
    "j": CLOSE_PARENTHESIS_SYM,
    "J": CLOSE_BRACKET_SYM,

    # arrows to chars
    "Up": UP,
    "Down": DOWN,
    "Left": LEFT,
    "Right": RIGHT
}

SYMBOLS_MORE_THAN_ONE_CHAR = {
    GREATER_THAN: "\\n",
    COMMA: EQUAL_TO_SYM,
    FULL_STOP: LOGICAL_AND_SYM,
    SLASH: LOGICAL_OR_SYM,
}

SPECIAL_FUNCTIONALITY = {
    FULL_STOP: CAPS,
    "T": RIGHT_TO_LEFT_OVERRIDE,
    "Y": CHANGE_TAB_WIDTH,
    "U": CLEAR_FILE,
    "O": FORCE_QUIT
}

SYMBOLS_TO_NUMBERS = {
    # symbols to numbers
    HASH: "0",
    DOLLAR: "1",
}

SYM_ENTERS = [GRAVE, ENTER] #write to enter

SYM_TABS = [QUESTION_MARK, TAB] #write to tab