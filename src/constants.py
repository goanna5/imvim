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

# Costants related to tab caps enter
CAPS = "Caps_Lock"
TAB = "Tab"
ENTER = "Return"

# Constants related to symbols
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

POWER = "**"
EQUAL_TO = "=="
LOGICAL_AND = "&&"
LOGICAL_OR = "||"

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