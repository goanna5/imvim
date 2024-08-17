MAX_LEVEL = 0

GOAL_ZERO = ["Hello, World!"]

GOAL_TEXTS = [GOAL_ZERO]

START_ZERO = ["Here is some text.",
              "This is a sentence.",
              "Sample text."]

START_TEXTS = [START_ZERO]

KEY_PRESS_FRAME_HEIGHT = 150
TEXT_OFFSET = 4

# Constants related to moving the player
UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'

MOVE_DELTAS = {
    UP: (-2, 0),
    DOWN: (3, 0),
    RIGHT: (0, 7),
    LEFT: (0, -5),
}

ARROW_TO_CHAR = {
    "Up": UP,
    "Down": DOWN,
    "Left": LEFT,
    "Right": RIGHT,
}


# Costants related to tab caps enter
CAPS = "Caps_Lock"
TAB = "Tab"
ENTER = "Return"

# Constants related to symbols
'''
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
'''

GRAVE = "`",
NOT = "~",
EXCLAMATION = "!",
AT = "@",
HASH = "#",
DOLLAR = "$",
PERCENT = "%",
CARET = "^",
AMPERSAND = "&",
ASTERISK = "*",
OPEN_PARENTHESIS = "(",
CLOSE_PARENTHESIS = ")",
MINUS = "-",
UNDERSCORE = "_",
PLUS = "+",
EQUALS = "=",
OPEN_BRACKET = "[",
OPEN_BRACE = "{",
CLOSE_BRACKET = "]",
CLOSE_BRACE = "}",
BAR = "|",
BACKSLASH = "\\",
COLON = ":",
SEMICOLON = ";",
DOUBLE_QUOTES = "\"",
SINGLE_QUOTE = "\'",
COMMA = ",",
LESS_THAN = "<",
FULL_STOP = ".",
GREATER_THAN = ">",
SLASH = "/",
QUESTION_MARK = "?",
POWER = "**",
EQUAL_TO = "==",
LOGICAL_AND = "&&",
LOGICAL_OR = "||"

'''
POWER = "**"
EQUAL_TO = "=="
LOGICAL_AND = "&&"
LOGICAL_OR = "||"
'''
# Constants relating to special functionality
RIGHT_TO_LEFT_OVERRIDE = "U+202E" #this is the unicode character
CHANGE_TAB_WIDTH = "tab width"
CLEAR_FILE = "clear"
FORCE_QUIT = "exit"



# Mapping of the numbers to the operators
NUMBERS_TO_SYM = {
    "0": AMPERSAND,
    "1": PLUS,
    "2": MINUS,
    "3": ASTERISK,
    "4": SLASH,
    "5": EQUALS,
    "6": PERCENT,
    "7": POWER,
    "8": LESS_THAN,
    "9": GREATER_THAN
}

# Mapping of the symbols to letters
SYMBOLS_TO_CHAR = {
    EXCLAMATION: "j",
    AT: "J",
    PERCENT: "h",
    CARET: "H",
    AMPERSAND: "f",
    ASTERISK: "F",
    OPEN_PARENTHESIS: "g",
    CLOSE_PARENTHESIS: "G"
}

# Mapping of the symbols to numbers
SYMBOLS_TO_NUM = {
    HASH: "0",
    DOLLAR: "1"
}

# Mapping of the symbols to other symbols
SYMBOLS_TO_SYM = {
    GRAVE: ENTER,
    NOT: GRAVE,
    MINUS: BAR,
    UNDERSCORE: CARET,
    PLUS: NOT,
    EQUALS: EXCLAMATION,
    OPEN_BRACE: COMMA,
    OPEN_BRACKET: COLON,
    CLOSE_BRACE: UNDERSCORE,
    CLOSE_BRACKET: HASH,
    BACKSLASH: DOLLAR,
    BAR: AT,
    COLON: OPEN_BRACE,
    SEMICOLON: CLOSE_BRACE,
    SINGLE_QUOTE: QUESTION_MARK,
    DOUBLE_QUOTES: BACKSLASH,
    COMMA: '\n',
    LESS_THAN: EQUAL_TO,
    FULL_STOP: CAPS,
    GREATER_THAN: LOGICAL_AND,
    SLASH: TAB,
    QUESTION_MARK: LOGICAL_OR
}

# Mapping of the characters
CHAR_TO = {
    "q": "q",
    "Q": "A",
    "w": "w",
    "W": "B",
    "e": "t",
    "E": "C",
    RIGHT: "Right",
    "R": "E",
    "t": "p",
    "T": RIGHT_TO_LEFT_OVERRIDE,
    "y": "n",
    "Y": CHANGE_TAB_WIDTH,
    UP: "Up",
    "U": CLEAR_FILE,
    "i": "i",
    "I": "I",
    "o": "y",
    "O": FORCE_QUIT,
    "p": "o",
    "P": "K",
    "a": "a",
    "A": "M",
    "s": "s",
    "S": "N",
    DOWN: "Down",
    "D": "O",
    "f": OPEN_PARENTHESIS,
    "F": OPEN_BRACKET,
    "g": DOUBLE_QUOTES,
    "G": SINGLE_QUOTE,
    "h": FULL_STOP,
    "H": SEMICOLON,
    "j": CLOSE_PARENTHESIS,
    "J": CLOSE_BRACKET,
    "k": "e",
    "K": "P",
    LEFT: "Left",
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
    "M": "Z"
}

# Regular mapping characters
REGULAR_CHAR_TO = {
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
    "M": "Z"
}
