import os
from dotenv import load_dotenv
load_dotenv()

PREFIX = '&'

LOG_FILE = 'bot.log'
GENERIC_ERROR = ('Whoops! An error occured while executing this command. You '
                 'should probably tell the bot author about it or something'
                 '...')

# This is set to false to prevent cheating when secretly generating a Sha265
LOG_DEBUG_TO_FILE = os.getenv('DEBUG') == "TRUE"

# Phases
_phase_bartering = 'Bartering Phase'
_phase_auction = 'Auction Phase'

PHASES_BY_DAY = {
    'Monday': _phase_auction,
    'Tuesday': _phase_auction,
    'Wednesday': _phase_auction,
    'Thursday': _phase_bartering,
    'Friday': _phase_bartering,
    'Saturday': _phase_bartering,
    'Sunday': _phase_bartering
}

PHASE_CYCLE = {
    _phase_bartering: _phase_auction,
    _phase_auction: _phase_bartering
}

PHASE_START = {
    _phase_bartering: 'Thursday',
    _phase_auction: 'Monday'
}

# Cards
CARD_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'E', 'D', 'H', 'U', 'O', 'N', 'B', 'R', 'Q', 'K']
CARD_SUITS = ['L', '♦', 'U', '♣', 'A', 'R', 'B', 'D', 'S', '♥', 'C', '♠']

# Cards for determining suit/rank value for alternate formats
# Strings should be normalized uppercase before comparing to these
CARD_RANKS_FORMATS = [
    # Default card ranks
    CARD_RANKS,

    # Wiki {{Card}} format
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'U', 'O', 'N', 'B', 'R', 'Q', 'K'],

    # 10 is also sometimes T
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', '11', '12', '13', 'U', 'O', 'N', 'B', 'R', 'Q', 'K'],

    # Long formats
    ['ACE',
     'TWO',
     'THREE',
     'FOUR',
     'FIVE',
     'SIX',
     'SEVEN',
     'EIGHT',
     'NINE',
     'TEN',
     'ELEVEN',
     'TWELVE',
     'THIRTEEN',
     'UNTER KNAVE',
     'OBER KNAVE',
     'KNIGHT',
     'BISHOP',
     'ROOK',
     'QUEEN',
     'KING'],

    ['THE ACE',
     'THE TWO',
     'THE THREE',
     'THE FOUR',
     'THE FIVE',
     'THE SIX',
     'THE SEVEN',
     'THE EIGHT',
     'THE NINE',
     'THE TEN',
     'THE ELEVEN',
     'THE TWELVE',
     'THE THIRTEEN',
     'THE UNTER KNAVE',
     'THE OBER KNAVE',
     'THE KNIGHT',
     'THE BISHOP',
     'THE ROOK',
     'THE QUEEN',
     'THE KING'],

    ['A ACE',
     'A TWO',
     'A THREE',
     'A FOUR',
     'A FIVE',
     'A SIX',
     'A SEVEN',
     'A EIGHT',
     'A NINE',
     'A TEN',
     'A ELEVEN',
     'A TWELVE',
     'A THIRTEEN',
     'A UNTER KNAVE',
     'A OBER KNAVE',
     'A KNIGHT',
     'A BISHOP',
     'A ROOK',
     'A QUEEN',
     'A KING']
]

CARD_SUITS_FORMATS = [
    # Default card suits, normalized uppercase
    [suit.upper() for suit in CARD_SUITS],

    # Wiki format
    ['L', 'D', 'CP', 'C', 'A', 'R', 'B', 'SW', 'SH', 'H', 'CN', 'S'],

    # Emojis if you like
    ['🍃', '♦', '🥤', '♣', '🌰', '🌹', '🔔', '⚔', '🛡', '♥', '👛', '♠'],
    ['🍂', '💎', '🏆', '♣', '🌰', '🌹', '🛎', '🤺', '🛡', '♥', '💰', '♠'],

    # Long format
    ['LEAVES',
     'DIAMONDS',
     'CUPS',
     'CLUBS',
     'ACORNS',
     'ROSES',
     'BELLS',
     'SWORDS',
     'SHIELDS',
     'HEARTS',
     'COINS',
     'SPADES']
]

# Scoring Groups

SCORE_SENATORIAL = [16, 17, 18]
SCORE_REGIONALS = [
    [2, 4, 10, 12],     # French
    [3, 4, 8, 11],      # Spanish
    [1, 5, 7, 10],      # German
    [5, 6, 7, 9],       # Swiss
]
SCORE_COLORS = [
    [2, 6, 10],     # Red
    [4, 8, 12],     # Black
    [1, 5, 9],      # Green
    [3, 7, 11],     # Gold
]
