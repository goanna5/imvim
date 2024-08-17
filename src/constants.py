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