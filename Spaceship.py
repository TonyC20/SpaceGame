# Space game yay! - This is a space PvP game with a duel to space death! Controls are on the left
# By Tony Cai
import simplegui, math, random

# CONSTANTS===========================================================================================================================================
START_SCREEN = 0
MENU_SCREEN = 1
GAME_SCREEN = 2
END_SCREEN = 3

# Abilities
TELEPORT = 0
DASH = 1

# Canvas values
CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 800

# Map descriptions
DESCRIPTION_BOX_COL = 'rgba(83, 142, 237, 0.8)'
DESCRIPTION_SIZE = 50
DESCRIPTION_COL = '#b9d9eb'
DESCRIPTION_FONT = 'sans-serif'


# Background grid values
GRID1_COLOR = '#262626'
GRID1_THICKNESS = 3
GRID2_COLOR = '#1f1d1d'
GRID2_THICKNESS = 1
GRID_LINE_SPACING = 100

# Explosions
EXPLOSION_COL1 = '#ed2000'
EXPLOSION_COL2 = '#de6316'

# Ship
VELOCITY_DECAY = 0.97
SHIELD_DOWN_TIME = 180
SHIELD_COLOR = 'rgba(125, 142, 240, 0.6)'
SHIELD_REGEN_RATE = 0.1
HP_COLOR = 'rgba(7, 250, 2, 0.7)'
MISSLE_ANIMATION_SPEED = 0.2
RELOAD_DRAW_COL = 'rgba(241, 245, 47, 0.4)'
ABILITY_DRAW_COL = 'rgba(255, 160, 43, 0.4)'
HITBOX_COL = 'gray'

# Objects
BARRIER_COLOR = 'white'
STAR_SIZE = (12, 12)
STAR_FLASH_SPEED = 80

# Images
START_BACKGROUND = simplegui.load_image('https://i.pinimg.com/originals/ce/97/c4/ce97c43571aabc1ba2160dba91b2df13.jpg')
BACKGROUND = simplegui.load_image('https://wallpapercave.com/wp/wp4816757.jpg')
MISSLE = simplegui.load_image('https://cdn.discordapp.com/attachments/423673672663040001/797646011660763156/f37_missileSpriteSheet.png')
STAR1 = simplegui.load_image('https://cdn.discordapp.com/attachments/721912640288456715/800132615515406346/pixil-frame-0_3.png')
STAR2 = simplegui.load_image('https://cdn.discordapp.com/attachments/721912640288456715/800132600655249408/pixil-frame-0_2.png')
VICTORY_BACKGROUND = simplegui.load_image('https://www.nasa.gov/sites/default/files/thumbnails/image/archives_helix.jpg')
# Ship Images
MEGASHIP = simplegui.load_image('https://3.bp.blogspot.com/-cg1jtrxaZ8Y/Ufl5SmFUVaI/AAAAAAAAAzY/KBxNVcMmOB0/s1600/F5S4.png')
ATTACKER = simplegui.load_image('http://1.bp.blogspot.com/-SqwrVIJoXXY/U9vXJm7TiiI/AAAAAAAABwU/DyQAiOXcIgU/s1600/blueships1.png')
CAT_FACE = simplegui.load_image('https://static.vecteezy.com/system/resources/previews/001/199/181/original/emoji-cat-face-neutral-png.png')
MISSLE_SHIP = simplegui.load_image('http://2.bp.blogspot.com/-GEypUXgs8Rs/UyNGWzdtfVI/AAAAAAAABfQ/FACR_10KeRE/s1600/bluecargoship.png')
SIDE = simplegui.load_image('http://1.bp.blogspot.com/-R2zq5QEh9ks/UdHA9IXwCrI/AAAAAAAAAsY/cl3R-FIlpl0/s302/orangeship2.png')
TELEPORTER = simplegui.load_image('http://1.bp.blogspot.com/-PspnH522ZGE/U-PBCmXn3nI/AAAAAAAABws/J1S9AYNLzSE/s1600/redshipr.png')

# Sounds
LASER_FIRE = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804151356130197544/Laser_shoot_39.wav')
MISSLE_FIRE = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804152708554424360/Explosion_9_3.wav')
HIT = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804153453294911505/Hit_hurt_9.wav')
BUTTON_CLICK = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804154947175972864/Pickup_coin_15.wav')
WIN = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804161458518097920/win_loud.mp3')

# In game music
START_MUSIC = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804162595585130516/DeepSpaceA.mp3')
MENU_MUSIC = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804164156747939870/DubStepDropBoom.mp3')

SONG1 = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804158280430780426/DynamicFight_1.mp3')
SONG2 = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804158295413096454/DynamicFight_2.mp3')
SONG3 = simplegui.load_sound('https://cdn.discordapp.com/attachments/721912640288456715/804158308239409232/DynamicFight_3.mp3')

SONGS = [SONG1, SONG2, SONG3]

# Map values
SMALL_SHIP = 0
MISSLE_FUN = 1
BROADSIDE = 2
TELEPORT = 3
MEGASHIPS = 4

# Other
TRANSITION_SPEED = 0.01

# GLOBAL VARIABLES===========================================================================================================================================
game_transition = False
transition_state = 1
current_map = 0
time = 0
winning_team = 1
song_timer = 0

# Lists
buttons = []
projectiles = []
explosions = []
barriers = []
stars = []

# Players
# Player movement
p1_left = False
p1_right = False
p1_up = False
p1_down = False
p2_left = False
p2_right = False
p2_up = False
p2_down = False
# Player firing
p1_weapon1 = False
p1_weapon2 = False
p2_weapon1 = False
p2_weapon2 = False

# DICTIONARIES===========================================================================================================================================
# Team colors
TEAM_COLORS = {1:'red',
               2:'blue'}

# Image dictionaries
IMAGE_SIZES = {# Ships
              MEGASHIP:   [173, 291],
              ATTACKER:   [1021, 748],
              CAT_FACE:   [2812, 2259],
              MISSLE_SHIP:[470, 230],
              SIDE:       [172, 302],
              TELEPORTER: [960, 464],
    
              # Other
              MISSLE:            [1400/4, 160/2],
              STAR1:             [16, 16],
              STAR2:             [16, 16],
              BACKGROUND:        [3840, 2160],
              START_BACKGROUND:  [1920, 1141],
              VICTORY_BACKGROUND:[2000, 1361]}

# Map values
# Format -                 P1 position, P1 direction, P1 ship
#                          P2 position, P2 direction, P2 ship
MAP_VALUES = {SMALL_SHIP:[[100, 400],   0,            'speedy',
                          [1300, 400],  math.pi,      'speedy'],
              
              MISSLE_FUN:[[100, 100],   math.pi/2,    'missle',
                          [1300, 700],  -math.pi/2,   'missle'],
              
              BROADSIDE: [[100, 100],   0,            'broadsider',
                          [1300, 100],  math.pi,      'broadsider'],
              
              TELEPORT:  [[200, 200],   0,            'teleporter',
                          [1200, 600],  0,            'teleporter'],
              
              MEGASHIPS: [[700, 100],   math.pi/2,    'megaship', 
                          [700, 700],   -math.pi/2,   'megaship']}

# Format -                    position,   width, height
MAP_BARRIERS = {SMALL_SHIP:[[(300, 400),  60,    300],
                           [ (1100, 400), 60,    300]],
                
                MISSLE_FUN:[[(350, 400),  50,    500],
                           [ (1050, 400), 50,    500],
                           [ (700, 800),  50,    500],
                           [ (700, 0),    50,    500]],
                
                BROADSIDE: [[(700, 400),  300,   300]],
                
                TELEPORT:  [[(700, 400),  50,    2000],
                           [ (700, 400),  2500,  50]],
                
                MEGASHIPS: [[(700, 400),  500,   50]]}

# Map descriptions
MAP_DESCRIPTIONS = {SMALL_SHIP: 'Small ships are very fun',
                    MISSLE_FUN: 'Barriers and missles, a stratigic map',
                    BROADSIDE:  'Broadsiding ships aim well',
                    TELEPORT:   'Teleporting, missles, and surprise attacks',
                    MEGASHIPS:  'Big ships. They\'re big'}

# Cannon value dictionary
# Format -                           Dmg,  spd, dur, color,    size, bullet size
CANNON_VALUES = {'laser':           [10,   18,  50,  'white',  3,    2],
                 'burst_laser':     [12,   15,  60,  'black',  4,    3],
                 'eye_laser':       [10,   14,  50,  'red',    5,    3],
                 'big_cannon':      [70,   16,  80,  'orange', 5,    20],
                 'broadside_cannon':[14,   25,  60,  'yellow', 3,    5],
                 'megacannon':      [2000, 15,  100, 'white',  20,   60]}

# Missle value dictionary
# Format -                  Dmg, spd, turn spd, dur, color,    size, bullet size
MISSLE_VALUES = {'medium': [16,  10,  0.03,     160, 'black',  5,    4],
                 'swarm':  [9,   10,  0.05,     140, 'yellow', 3,    2],
                 'cruise': [50,  20,  0.07,     100, 'black',  3,    10],
                 'slow':   [80,  5,   0.016,    300, 'green',  5,    14]}


# Ship dictionaries
# List of cannons for each ship value
# Format -               is_missle, type, shoot dir, position, shoot offset
SHIP_CANNONS = {'speedy':[[[False, 'laser',       0, (10, 0), 0]],
                          [[False, 'burst_laser', 0, (32, 7), 0],
                           [False, 'burst_laser', 0, (32, 7), 10],
                           [False, 'burst_laser', 0, (32, 7), 20],
                           [False, 'burst_laser', 0, (32, 7), 30],
                           [False, 'burst_laser', 0, (32, 7), 40],
                           [False, 'burst_laser', 0, (32, -7), 0],
                           [False, 'burst_laser', 0, (32, -7), 10],
                           [False, 'burst_laser', 0, (32, -7), 20],
                           [False, 'burst_laser', 0, (32, -7), 30],
                           [False, 'burst_laser', 0, (32, -7), 40]]],
                
                'missle':[[[True, 'medium', 0,              (-20, 0),   0],
                           [True, 'medium', 0.4,            (-10, 10),  20],
                           [True, 'medium', -0.4,           (-10, -10), 20]],
                          [[True, 'swarm',  math.pi/2-0.6,  (0, 30),    0],
                           [True, 'swarm',  math.pi/2-0.4,  (3, 30),    0],
                           [True, 'swarm',  math.pi/2-0.2,  (6, 30),    0],
                           [True, 'swarm',  math.pi/2,      (9, 30),    0],
                           [True, 'swarm',  math.pi/2+0.2,  (12, 30),   0],
                           [True, 'swarm',  math.pi/2+0.4,  (15, 30),   0],
                           [True, 'swarm',  math.pi/2+0.6,  (18, 30),   0],
                           [True, 'swarm',  -math.pi/2-0.6, (0, -30),   0],
                           [True, 'swarm',  -math.pi/2-0.4, (3, -30),   0],
                           [True, 'swarm',  -math.pi/2-0.2, (6, -30),   0],
                           [True, 'swarm',  -math.pi/2,     (9, -30),   0],
                           [True, 'swarm',  -math.pi/2+0.2, (12, -30),  0],
                           [True, 'swarm',  -math.pi/2+0.4, (15, -30),  0],
                           [True, 'swarm',  -math.pi/2+0.6, (18, -30),  0]]],
                
                'broadsider':[[[False, 'broadside_cannon', math.pi/2,  (35, 25),   0],
                               [False, 'broadside_cannon', math.pi/2,  (23, 25),   5],
                               [False, 'broadside_cannon', math.pi/2,  (11, 25),   10],
                               [False, 'broadside_cannon', math.pi/2,  (-1, 25),   15],
                               [False, 'broadside_cannon', math.pi/2,  (-15, 20),  20],
                               [False, 'broadside_cannon', math.pi/2,  (-22, 20),  25],
                               [False, 'broadside_cannon', math.pi/2,  (-46, 20),  30],
                               [False, 'broadside_cannon', math.pi/2,  (-53, 20),  35],
                               [False, 'broadside_cannon', -math.pi/2, (35, -25),  0],
                               [False, 'broadside_cannon', -math.pi/2, (23, -25),  5],
                               [False, 'broadside_cannon', -math.pi/2, (11, -25),  10],
                               [False, 'broadside_cannon', -math.pi/2, (-1, -25),  15],
                               [False, 'broadside_cannon', -math.pi/2, (-15, -20), 20],
                               [False, 'broadside_cannon', -math.pi/2, (-22, -20), 25],
                               [False, 'broadside_cannon', -math.pi/2, (-46, -20), 30],
                               [False, 'broadside_cannon', -math.pi/2, (-53, -20), 35]],
                              [[True,  'cruise',           0,          (0, 0),     0]]],
                
               'teleporter':[[[True, 'cruise', 0,            (0, 0),     0]],
                             [[True, 'slow',   0,            (10, 0),    0],
                              [True, 'slow',   math.pi,      (-10, 0),   0],
                              [True, 'slow',   math.pi/2,    (0, 10),    0],
                              [True, 'slow',   -math.pi/2,   (0, -10),   0],
                              [True, 'slow',   -math.pi/4,   (10, -10),  0],
                              [True, 'slow',   math.pi/4,    (10, 10),   0],
                              [True, 'slow',   3*math.pi/4,  (-10, 10),  0],
                              [True, 'slow',   -3*math.pi/4, (-10, -10), 0]]],
                
               'megaship':[[[True, 'cruise',       0,          (20, 0),   20],
                            [True, 'swarm',        math.pi/2,  (0, 0),    20],
                            [True, 'swarm',        -math.pi/2, (0, 0),    20],
                            [True, 'medium',       math.pi/2,  (50, 30),  23],
                            [True, 'medium',       math.pi/2,  (35, 30),  23],
                            [True, 'medium',       -math.pi/2, (50, -30), 23],
                            [True, 'medium',       -math.pi/2, (35, -30), 23],
                            [True, 'slow',         0,          (-80, 0),  6],
                            [False, 'burst_laser', 0.1,        (5, 10),   10],
                            [False, 'burst_laser', -0.1,       (5, -10),  10],
                            [False, 'big_cannon',  0,          (-90, -20),0],
                            [False, 'big_cannon',  0,          (-90, 20), 0]],
                           [[False, 'megacannon',  0,          (-50, 0),  0]]]}

# Format -                  Spd,   Turn spd,dmg res, shield res, hitbox, prim rel, sec rel, ability,  ability cooldown
SHIP_VALUES = {'speedy':    [0.15, 0.0035,  0.7,     0.4,        45,     10,       300,     TELEPORT, 100],
               'missle':    [0.12, 0.0025,  0.6,     0.8,        40,     40,       350,     DASH,     100],
               'broadsider':[0.14, 0.003,   0.6,     1,          50,     60,       400,     DASH,     200],
               'teleporter':[0.2,  0.002,   0.25,    0.5,        60,     40,       400,     TELEPORT, 60],
               'megaship':  [0.1,  0.001,   0.03,    0.05,       100,    50,       1000,    DASH,     300]}

# Format - Image, (draw width, draw height), image rotation
SHIP_IMAGES = {'speedy':    [ATTACKER,   (90, 60),   0],
               'missle':    [MISSLE_SHIP,(130, 70),  math.pi],
               'broadsider':[SIDE,       (100, 150), math.pi/2],
               'teleporter':[TELEPORTER, (170, 110), 0],
               'megaship':  [MEGASHIP,   (170, 260), math.pi/2]}


# FUNCTIONS===========================================================================================================================================
def create_start_screen():
    global game_state, start_message, song_timer
    game_state = START_SCREEN
    song_timer = 0
    start_message = Text_box((CANVAS_WIDTH/2, CANVAS_HEIGHT-120),
                             500,
                             70,
                             '#0000003f',
                             'Click anywhere to start',
                             40,
                             'white',
                             'serif')
    # Sound
    START_MUSIC.rewind()
    START_MUSIC.play()
    
def create_menu():
    global game_state, next_button, back_button, return_button, select_button, map_info, map_name, current_map, song_timer
    set_map_values(current_map)
    # Music
    START_MUSIC.pause()
    MENU_MUSIC.rewind()
    MENU_MUSIC.play()
    song_timer = 0
    
    game_state = MENU_SCREEN
    # Map navigation buttons
    next_button = Text_box((CANVAS_WIDTH-400, CANVAS_HEIGHT-75),
                           170,
                           80,
                           'rgba(55, 140, 237, 0.6)',
                           'Next map',
                           27,
                           'rgb(197, 221, 232)',
                           'sans-serif')
    back_button = Text_box((400, CANVAS_HEIGHT-75),
                           170,
                           80,
                           'rgba(55, 140, 237, 0.6)',
                           'Previous map',
                           27,
                           'rgb(197, 221, 232)',
                           'sans-serif')
    # Return to start screen button
    return_button = Text_box((75, 50),
                           100,
                           50,
                           'rgba(97, 95, 96, 0.6)',
                           'Return',
                           30,
                           'white',
                           'serif')
    # Select map and start game button
    select_button = Text_box((CANVAS_WIDTH/2, CANVAS_HEIGHT-75),
                           400,
                           90,
                           'rgba(58, 55, 237, 0.8)',
                           'Start Game!',
                           60,
                           'rgb(197, 221, 232)',
                           'sans-serif')
    
def new_game():
    global player1, player2, game_state, song_timer
    game_state = GAME_SCREEN
    # Creates players
    player1 = Ship(player1_ship, [player1_starting_pos[0], player1_starting_pos[1]], player1_starting_dir, 1)
    player1.create_cannons()
    
    player2 = Ship(player2_ship, [player2_starting_pos[0], player2_starting_pos[1]], player2_starting_dir, 2)
    player2.create_cannons()
    
    # Generates and plays current song
    song_timer = 0
    MENU_MUSIC.pause()
    
    choose_new_song()
    current_song.rewind()
    current_song.play()
    
def create_end_screen():
    global game_state, victory_text, return_button
    game_state = END_SCREEN
    # Song
    current_song.pause()
    WIN.rewind()
    WIN.play()
    
    # Victory text box
    victory_text = Text_box((CANVAS_WIDTH/2, CANVAS_HEIGHT/2),
                            800,
                            150,
                            'rgba(41, 19, 156, 0.5)',
                            'Player ' + str(winning_team) + ' Victory!',
                            80,
                            'white',
                            'monospace')
    # Return to menu button
    return_button = Text_box((CANVAS_WIDTH/2, CANVAS_HEIGHT-100),
                             230,
                             70,
                             'rgba(79, 79, 82, 0.6)',
                             'Return to menu',
                             30,
                             'white',
                             'sans-serif')
    
def set_map_values(map_key):
    global player1_starting_pos, player1_starting_dir, player1_ship, player2_starting_pos, player2_starting_dir, player2_ship, map_description, projectiles, explosions
    # Clears all projectiles and explosions from previous game
    projectiles = []
    explosions = []
    
    # Set player ships, positions, and directions
    values = MAP_VALUES[map_key]
    player1_starting_pos = values[0]
    player1_starting_dir = values[1]
    player1_ship = values[2]
    player2_starting_pos = values[3]
    player2_starting_dir = values[4]
    player2_ship = values[5]
    
    # Map description
    description = MAP_DESCRIPTIONS[map_key]
    map_description = Text_box((CANVAS_WIDTH/2, 50),
                               1100,
                               60,
                               DESCRIPTION_BOX_COL,
                               description,
                               DESCRIPTION_SIZE,
                               DESCRIPTION_COL,
                               DESCRIPTION_FONT)
    
    # Sets barriers to current map
    global barriers
    barriers = []
    values = MAP_BARRIERS[map_key]
    for barrier_value in values:
        new_barrier = Barrier(barrier_value[0], barrier_value[1], barrier_value[2])
        barriers.append(new_barrier)
        
    # Randomly generates a new list of stars
    global stars
    stars = []
    for i in range(40):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        star_time = random.randint(0, STAR_FLASH_SPEED*2)
        new_star = Star((x, y), star_time)
        stars.append(new_star)

def set_sound_volumes():
    # Sets volume for sounds from 0.0 to 1.0
    LASER_FIRE.set_volume(0.3)
    MISSLE_FIRE.set_volume(0.9)
    HIT.set_volume(0.8)
    BUTTON_CLICK.set_volume(0.3)

def choose_new_song():
    global current_song
    current_song = random.choice(SONGS)

def draw_grid_lines(canvas):
    # Draws the background grid when game_state == GAME_SCREEN
    # Secondary Grid:
    # Secondary vertical lines
    for i in range(CANVAS_WIDTH//GRID_LINE_SPACING):
        canvas.draw_line((GRID_LINE_SPACING*i + GRID_LINE_SPACING/2, 0),
                         (GRID_LINE_SPACING*i + GRID_LINE_SPACING/2, CANVAS_HEIGHT),
                         GRID2_THICKNESS,
                         GRID2_COLOR)
    # Secondary horizontal lines
    for i in range(CANVAS_HEIGHT//GRID_LINE_SPACING):
        canvas.draw_line((0, GRID_LINE_SPACING*i + GRID_LINE_SPACING/2),
                         (CANVAS_WIDTH, GRID_LINE_SPACING*i + GRID_LINE_SPACING/2),
                         GRID2_THICKNESS,
                         GRID2_COLOR)
    # Primary Grid:
    # Primary vertical lines
    for i in range(CANVAS_WIDTH//GRID_LINE_SPACING - 1):
        canvas.draw_line((GRID_LINE_SPACING*i + GRID_LINE_SPACING, 0),
                         (GRID_LINE_SPACING*i + GRID_LINE_SPACING, CANVAS_HEIGHT),
                         GRID1_THICKNESS,
                         GRID1_COLOR)
    # Primary horizontal lines
    for i in range(CANVAS_WIDTH//GRID_LINE_SPACING - 1):
        canvas.draw_line((0, GRID_LINE_SPACING*i + GRID_LINE_SPACING),
                         (CANVAS_WIDTH, GRID_LINE_SPACING*i + GRID_LINE_SPACING),
                         GRID1_THICKNESS,
                         GRID1_COLOR)

def within_distance(pos1, distance, pos2):
    # Returns if points pos1 and pos2 are less than the variable distance apart
    x1, y1 = pos1
    x2, y2 = pos2
    return (x2-x1)**2 + (y2-y1)**2 < distance**2

def find_angle(position, target):
    # Finds angle from position to target
    x = target[0] - position[0]
    y = target[1] - position[1]
    angle = math.atan2(y, x)
    return angle

# CLASSES===========================================================================================================================================
class Text_box:
    def __init__(self, position, width, height, color, text, text_size, text_color, text_font):
        self.pos = position
        self.left = position[0] - width/2
        self.right = position[0] + width/2
        self.up = position[1] - height/2
        self.down = position[1] + height/2
        # List of the corner points
        self.points = [(self.left, self.up),   # Top left
                      (self.right, self.up),   # Top right
                      (self.right, self.down), # Bottom right
                      (self.left, self.down)]  # Bottom left
        # Text options
        self.col = color
        self.text = text
        self.text_size = text_size
        self.text_col = text_color
        self.text_font = text_font
    def draw(self, canvas):
        # Box
        canvas.draw_polygon(self.points, 3, self.col, self.col)
        # Draw text in center of box
        text_width = frame.get_canvas_textwidth(self.text, self.text_size, self.text_font)
        canvas.draw_text(self.text,
                         (self.pos[0]-text_width/2, self.pos[1]+self.text_size/3),
                         self.text_size,
                         self.text_col,
                         self.text_font)
    def is_clicked(self, mouse_position):
        # Returns if mouse_position is within the text box
        hor = self.left < mouse_position[0] < self.right
        ver = self.up < mouse_position[1] < self.down
        return hor and ver

class Star:
    def __init__(self, position, time):
        # Flashing star for the background
        self.pos = position
        self.time = time
    def update(self):
        # Update for flashing
        self.time += 1
        self.time %= STAR_FLASH_SPEED*2
    def draw(self, canvas):
        # Draws on canvas
        if self.time < STAR_FLASH_SPEED:
            width, height = IMAGE_SIZES[STAR1]
            canvas.draw_image(STAR1,
                              (width/2, height/2),
                              (width, height),
                              self.pos,
                              STAR_SIZE)
        else:
            width, height = IMAGE_SIZES[STAR2]
            canvas.draw_image(STAR2,
                              (width/2, height/2),
                              (width, height),
                              self.pos,
                              STAR_SIZE)

# Game Classes
class Ship:
    def __init__(self, ship_key, starting_pos, starting_dir, team):
        # Imput values
        self.dir = starting_dir # In radians
        self.pos = starting_pos
        self.team = team
        # Gets ship values from dictionary
        values = SHIP_VALUES[ship_key]
        self.spd = values[0]
        self.turn_spd = values[1]
        self.dmg_res = values[2]
        self.shield_res = values[3]
        self.hit_rad = values[4]
        self.rel1 = values[5]
        self.rel2 = values[6]
        self.ability = values[7]
        self.default_ability_cooldown = values[8]
        # Gets image values from dictionary
        values = SHIP_IMAGES[ship_key]
        self.img = values[0]
        self.draw_size = values[1]
        self.img_rot = values[2]
        # List of what cannons are going to be on the ship
        self.CANNON_VALUES = SHIP_CANNONS[ship_key]
        # Preset values
        self.hp = 100      # 100 is a percent
        self.shield = 100
        self.shield_down_time = 0
        self.vel = [0, 0]
        self.weapons1 = []
        self.weapons2 = []
        self.active_rel1 = 0
        self.active_rel2 = 0
        self.ability_cooldown = 0
        
    def update(self):
        # Movement
        self.movement_update()
        # Cannons
        for weapon in self.weapons1:
            weapon.update()
        for weapon in self.weapons2:
            weapon.update()
        # Ability
        if self.ability_cooldown > 0:
            self.ability_cooldown -= 1
        # Reload
        if self.active_rel1 > 0:
            self.active_rel1 -= 1
        if self.active_rel2 > 0:
            self.active_rel2 -= 1
        # Shield regeneration
        self.reg_shield()
        # Barriers
        self.move_out_of_barriers()
        # Collisions
        self.collision_detect()
        
    def draw(self, canvas):
        # Hitbox
        canvas.draw_circle(self.pos,
                           self.hit_rad,
                           self.hit_rad/10,
                           HITBOX_COL)
        # HP
        end_angle = self.hp/100 * 2*math.pi
        canvas.draw_arc(self.pos,
                        self.hit_rad,
                        -math.pi/2,
                        end_angle - math.pi/2,
                        self.hit_rad/7,
                        HP_COLOR)
        # Shield
        end_angle = self.shield/100 * 2*math.pi
        canvas.draw_arc(self.pos,
                        self.hit_rad*1.17,
                        -math.pi/2,
                        end_angle - math.pi/2,
                        self.hit_rad/5,
                        SHIELD_COLOR)
        # Ship image
        img_width, img_height = IMAGE_SIZES[self.img]
        canvas.draw_image(self.img,
                          (img_width/2, img_height/2),
                          (img_width, img_height),
                          self.pos,
                          self.draw_size,
                          self.dir + self.img_rot)
        # Cannons
        for cannon in self.weapons1:
            cannon.draw(canvas)
        for cannon in self.weapons2:
            cannon.draw(canvas)
                
        # Secondary reload cooldown
        offset_pos = (self.pos[0]+self.hit_rad*1.3, self.pos[1]+self.hit_rad)
        cooldown_percent = self.active_rel2/self.rel2
        canvas.draw_line(offset_pos,
                        (offset_pos[0], offset_pos[1] - cooldown_percent*2*self.hit_rad),
                         20,
                         RELOAD_DRAW_COL)
        # Ability cooldown
        offset_pos = (self.pos[0]-self.hit_rad*1.3, self.pos[1]+self.hit_rad)
        cooldown_percent = self.ability_cooldown/self.default_ability_cooldown
        canvas.draw_line(offset_pos,
                        (offset_pos[0], offset_pos[1] - cooldown_percent*2*self.hit_rad),
                         20,
                         ABILITY_DRAW_COL)
    
    def create_cannons(self):
        self.weapons1 = []
        self.weapons2 = []
        # Adds primary cannons
        for value in self.CANNON_VALUES[0]:
            new_weapon = Cannon(self, value[0], value[1], value[2], value[3], value[4])
            self.weapons1.append(new_weapon)
        # Adds secondary cannons
        for value in self.CANNON_VALUES[1]:
            new_weapon = Cannon(self, value[0], value[1], value[2], value[3], value[4])
            self.weapons2.append(new_weapon)
    
    def shoot(self, weapon_group):
        if weapon_group == 1:
            for weapon in self.weapons1:
                weapon.shooting = True
        else:
            for weapon in self.weapons2:
                weapon.shooting = True
    
    def collision_detect(self):
        for projectile in projectiles:
            if projectile.team != self.team and within_distance(self.pos, self.hit_rad, projectile.pos):
                new_explosion = Explosion(projectile.pos, round(5*math.sqrt(projectile.dmg)))
                explosions.append(new_explosion)
                projectiles.remove(projectile)
                self.hit(projectile.dmg)
    
    def use_ability(self):
        if self.ability_cooldown == 0:
            if self.ability == DASH:
                self.vel[1] = 100 * self.spd
            elif self.ability == TELEPORT:
                self.pos[0] += 300 * math.cos(self.dir)
                self.pos[1] += 300 * math.sin(self.dir)
            self.ability_cooldown = self.default_ability_cooldown
    
    def hit(self, damage):
        # Sound
        HIT.rewind()
        HIT.play()
        # Removes damage amount of shield or health, reduced by ship damage resistance
        global winning_team
        # If ships still has shield
        if self.shield > 0:
            self.shield -= damage * self.shield_res
            if self.shield < 0:
                self.shield = 0
        else: # Else will take damage from ship hp
            self.hp -= damage * self.dmg_res
            if self.hp < 0:
                # Ship will be destroyed
                if self.team == 1:
                    winning_team = 2
                else:
                    winning_team = 1
                create_end_screen()
        self.shield_down_time = SHIELD_DOWN_TIME
    def move_out_of_barriers(self):
        # Barriers
        for barrier in barriers:
            # Checks if ship distance is within corners
            for point in barrier.points:
                if within_distance(self.pos, self.hit_rad, point):
                    angle = find_angle(point, self.pos)
                    self.pos[0] = point[0] + math.cos(angle)*self.hit_rad
                    self.pos[1] = point[1] + math.sin(angle)*self.hit_rad
            # Top and bottom of barrier
            if barrier.left < self.pos[0] < barrier.right:
                if barrier.up - self.hit_rad < self.pos[1] < barrier.pos[1]:
                    self.pos[1] = barrier.up - self.hit_rad
                elif barrier.pos[1] < self.pos[1] < barrier.down + self.hit_rad:
                    self.pos[1] = barrier.down + self.hit_rad
            # Left and right of barrier
            elif barrier.up < self.pos[1] < barrier.down:
                if barrier.left - self.hit_rad < self.pos[0] < barrier.pos[0]:
                    self.pos[0] = barrier.left - self.hit_rad
                elif barrier.pos[0] < self.pos[0] < barrier.right + self.hit_rad:
                    self.pos[0] = barrier.right + self.hit_rad
                    
    def movement_update(self):
        # Update position
        self.pos[0] += self.vel[1] * math.cos(self.dir)
        self.pos[1] += self.vel[1] * math.sin(self.dir)
        self.dir += self.vel[0]
        
        # Velocity decrease
        self.vel[0] *= VELOCITY_DECAY**2
        self.vel[1] *= VELOCITY_DECAY
        
        # Check if offscreen
        if self.pos[0] < 0:
            self.pos[0] = 0
        if CANVAS_WIDTH < self.pos[0]:
            self.pos[0] = CANVAS_WIDTH
        if self.pos[1] < 0:
            self.pos[1] = 0
        if CANVAS_HEIGHT < self.pos[1]:
            self.pos[1] = CANVAS_HEIGHT
            
        # Player velocity update
        if self.team == 1:
            if p1_left:
                self.vel[0] += -self.turn_spd
            if p1_right:
                self.vel[0] += self.turn_spd
            if p1_up:
                self.vel[1] += self.spd
            if p1_down:
                self.vel[1] += -self.spd/2
            if p1_weapon1:
                if self.active_rel1 == 0:
                    self.shoot(1)
                    self.active_rel1 = self.rel1
            if p1_weapon2:
                if self.active_rel2 == 0:
                    self.shoot(2)
                    self.active_rel2 = self.rel2
        else:
            if p2_left:
                self.vel[0] += -self.turn_spd
            if p2_right:
                self.vel[0] += self.turn_spd
            if p2_up:
                self.vel[1] += self.spd
            if p2_down:
                self.vel[1] += -self.spd/2
            if p2_weapon1:
                if self.active_rel1 == 0:
                    self.shoot(1)
                    self.active_rel1 = self.rel1
            if p2_weapon2:
                if self.active_rel2 == 0:
                    self.shoot(2)
                    self.active_rel2 = self.rel2
    def reg_shield(self):
        if not self.shield == 100:
            if self.shield_down_time == 0:
                self.shield += SHIELD_REGEN_RATE
                if self.shield > 100:
                    self.shield = 100
            else:
                self.shield_down_time -= 1

class Cannon:
    # Cannon_offset is a tuple that tells what the cannon position is relative to the host
    def __init__(self, host, is_missle, cannon_type, direction, cannon_position_offset, cannon_shoot_offset):
        # Input values
        self.host = host
        self.dir = direction # The direction that the cannon will be shooting
        self.shoot_time = cannon_shoot_offset
        self.is_missle = is_missle
        # Converts cannon_offset to an angle and distance from host
        x, y = cannon_position_offset
        self.host_dist = math.sqrt(x**2 + y**2)
        self.host_angle = math.atan2(y, x)
        # Gets cannon or missle values from the dictionaries
        if is_missle:
            values = MISSLE_VALUES[cannon_type]
            self.dmg = values[0]
            self.spd = values[1]
            self.turn_spd = values[2]
            self.dur = values[3]
            self.col = values[4]
            self.size = values[5]   # Turret size
            self.b_size = values[6] # Bullet size
        else:
            values = CANNON_VALUES[cannon_type]
            self.dmg = values[0]
            self.spd = values[1]
            self.dur = values[2]
            self.col = values[3]
            self.size = values[4]   # Turret size
            self.b_size = values[5] # Bullet size
        self.pos = self.host.pos
        self.shooting = False
        self.current_time = 0
    
    def update(self):
        host_dir = self.host.dir
        # Finds x and y position relative to host
        x = math.cos(host_dir + self.host_angle) * self.host_dist
        y = math.sin(host_dir + self.host_angle) * self.host_dist
        # Finds x and y position on canvas
        x += self.host.pos[0]
        y += self.host.pos[1]
        # Updates position
        self.pos = (x, y)
        # Shoot check
        self.shoot_check()
    def draw(self, canvas):
        team_color = TEAM_COLORS[self.host.team]
        canvas.draw_circle(self.pos, self.size, 2, team_color, self.col)
    def shoot_check(self):
        if self.shooting:
            if self.current_time == self.shoot_time:
                # New projectile direction
                if self.is_missle:
                    MISSLE_FIRE.rewind()
                    MISSLE_FIRE.play()
                    new_projectile = Missle(self.dir + self.host.dir,
                                            self.pos,
                                            self.spd,
                                            self.turn_spd,
                                            self.b_size,
                                            self.dur,
                                            self.dmg,
                                            self.host.team)
                                            
                else:
                    LASER_FIRE.rewind()
                    LASER_FIRE.play()
                    projectile_dir = (math.cos(self.host.dir + self.dir), math.sin(self.host.dir + self.dir))
                    new_projectile = Projectile(projectile_dir,
                                                self.pos,
                                                self.spd,
                                                self.b_size,
                                                self.dur,
                                                self.col,
                                                self.dmg,
                                                self.host.team)
                projectiles.append(new_projectile)
                self.current_time = 0
                self.shooting = False
            else:
                self.current_time += 1

class Projectile:
    def __init__(self, direction, position, speed, size, duration, color, damage, team):
        self.pos = [position[0], position[1]]
        self.size = size
        self.dmg = damage
        self.spd = speed
        self.dur = duration
        self.dir = direction
        self.col = color
        self.team = team
    
    def draw(self, canvas):
        team_color = TEAM_COLORS[self.team]
        canvas.draw_circle(self.pos, self.size, 2, team_color, self.col)
    
    def update(self):
        # Movement update
        self.pos[0] += self.dir[0] * self.spd
        self.pos[1] += self.dir[1] * self.spd
        # Duration
        self.dur -= 1
        if self.dur == 0:
            projectiles.remove(self)
        # Barriers
        elif self.is_in_barrier():
            projectiles.remove(self)
    
    def is_in_barrier(self):
        in_barrier = False
        for barrier in barriers:
            hor = barrier.left < self.pos[0] < barrier.right
            ver = barrier.up < self.pos[1] < barrier.down
            if hor and ver:
                in_barrier = True
        return in_barrier

class Missle:
    def __init__(self, direction, position, speed, turn_speed, size, duration, damage, team):
        self.pos = [position[0], position[1]]
        self.dir = direction
        self.spd = speed
        self.tspd = turn_speed
        self.size = size
        self.dur = duration
        self.dmg = damage
        self.team = team
        self.time = 0
    def draw(self, canvas):
        # Team color circle
        team_color = TEAM_COLORS[self.team]
        canvas.draw_circle(self.pos, self.size, 1, team_color, team_color)
        width, height = IMAGE_SIZES[MISSLE]
        col = int(self.time)%4
        canvas.draw_image(MISSLE, (width/2 + col * width, 1.5 * height), (width, height), self.pos, (7*self.size, 2*self.size), self.dir)
        # Missle sprite
    def update(self):
        # Animation
        self.time += MISSLE_ANIMATION_SPEED
        self.time %= 4
        # Duration
        self.dur -= 1
        if self.dur == 0:
            projectiles.remove(self)
        # Barriers
        elif self.is_in_barrier():
            projectiles.remove(self)
        # Position update
        self.pos[0] += math.cos(self.dir) * self.spd
        self.pos[1] += math.sin(self.dir) * self.spd
        # Target
        if self.team == 1:
            target = player2.pos
        elif self.team == 2:
            target = player1.pos

        # Turn towards player
        a = self.dir                           # Current facing
        at = find_angle(self.pos, target)      # Angle to target
        # Makes the angles from 0 to 2pi radians
        a %= 2*math.pi
        at %= 2*math.pi
        ar = a - math.pi                       # Reference angle
        if ar > 0:
            # ar will be lower than a
            if ar < at < a:
                self.dir -= self.tspd #cw
            else:
                self.dir += self.tspd #ccw
        else: #ar will be less than 0
            ar += 2*math.pi 
            # ar will now be between pi and 2pi so ar will be higher than a
            if a < at < ar:
                self.dir += self.tspd #cw
            else:
                self.dir -= self.tspd #ccw
    def is_in_barrier(self):
        # Barrier hit detection
        in_barrier = False
        for barrier in barriers:
            hor = barrier.left < self.pos[0] < barrier.right
            ver = barrier.up < self.pos[1] < barrier.down
            if hor and ver:
                in_barrier = True
        return in_barrier

class Explosion:
    # Explosion if projectile hits ship
    def __init__(self, position, time):
        self.time = time
        self.pos = position
    
    def draw(self, canvas):
        # The size of the exposions depends on the duration of the explosion
        canvas.draw_circle(self.pos,
                           self.time,
                           0.3*self.time,
                           EXPLOSION_COL1,
                           EXPLOSION_COL2)
    
    def update(self):
        self.time -= 1
        if self.time == 1:
            explosions.remove(self)

class Barrier:
    def __init__(self, position, width, height):
        self.pos = position
        self.width = width
        self.height = height
        self.left = position[0] - width/2
        self.right = position[0] + width/2
        self.up = position[1] - height/2
        self.down = position[1] + height/2
        # Corner points of barrier
        self.points = [(self.left, self.up),   # Top left
                      (self.right, self.up),   # Top right
                      (self.right, self.down), # Bottom right
                      (self.left, self.down)]  # Bottom left
    def draw(self, canvas):
        # Draws barrier
        canvas.draw_polygon(self.points, 1, BARRIER_COLOR, BARRIER_COLOR)

# HANDLERS===========================================================================================================================================
# Draw handler
def draw_handler(canvas):
    global time, transition_state, game_transition, song_timer
    
    if game_state == START_SCREEN:
        # Background
        width, height = IMAGE_SIZES[START_BACKGROUND]
        canvas.draw_image(START_BACKGROUND,
                          (width/2, height/2),
                          (width, height),
                         (CANVAS_WIDTH/2, CANVAS_HEIGHT/2),
                          (CANVAS_WIDTH, CANVAS_HEIGHT))
        # Start message
        time += 1
        time %= 120
        if time < 60:
            start_message.draw(canvas)
        # Song
        song_timer += 1
        if song_timer == 3600:
            START_MUSIC.rewind()
            START_MUSIC.play()
            song_timer = 0
    
    elif game_state == MENU_SCREEN:
        # Stars
        for star in stars:
            star.update()
            star.draw(canvas)
        # Draw map
        for barrier in barriers:
            barrier.draw(canvas)
        # Draw buttons
        map_description.draw(canvas)
        next_button.draw(canvas)
        back_button.draw(canvas)
        return_button.draw(canvas)
        select_button.draw(canvas)
        # Start game with fade in
        if game_transition:
            canvas.draw_polygon([(0, 0),
                                (0, CANVAS_HEIGHT),
                                (CANVAS_WIDTH, CANVAS_HEIGHT),
                                (CANVAS_WIDTH, 0)],
                                1,
                                'black',
                                'rgba(255, 255, 255, '+str(transition_state)+')')
            transition_state += TRANSITION_SPEED
            # If fade in effect ends, start a new game
            if transition_state >= 1:
                transition_state = 1
                new_game()
    
    elif game_state == GAME_SCREEN:
        # Song
        song_timer += 1
        if song_timer == 7200:
            current_song.rewind()
            current_song.play()
            song_timer = 0
        # Background
        width, height = IMAGE_SIZES[BACKGROUND]
        canvas.draw_image(BACKGROUND,
                          (width/2, height/2),
                          (width, height),
                          (CANVAS_WIDTH/2, CANVAS_HEIGHT/2),
                          (CANVAS_WIDTH, CANVAS_HEIGHT))
        # Grid lines
        draw_grid_lines(canvas)
        # Stars
        for star in stars:
            star.update()
            star.draw(canvas)
        # Player update
        player1.update()
        player2.update()
        # Player draw
        player1.draw(canvas)
        player2.draw(canvas)
        # Projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw(canvas)
        # Explosions
        for explosion in explosions:
            explosion.update()
            explosion.draw(canvas)
        # Barriers
        for barrier in barriers:
            barrier.draw(canvas)
        # Fade into the game
        if game_transition:
            canvas.draw_polygon([(0, 0),
                                (0, CANVAS_HEIGHT),
                                (CANVAS_WIDTH, CANVAS_HEIGHT),
                                (CANVAS_WIDTH, 0)],
                                1,
                                'black',
                                'rgba(255, 255, 255, '+str(transition_state)+')')
            transition_state -= TRANSITION_SPEED
            # Check if the transition has ended
            if transition_state <= 0:
                game_transition = False
    elif game_state == END_SCREEN:
        # Victory screen - a player has won the game
        # Background
        width, height = IMAGE_SIZES[VICTORY_BACKGROUND]
        canvas.draw_image(VICTORY_BACKGROUND,
                          (width/2, height/2),
                          (width, height),
                          (CANVAS_WIDTH/2, CANVAS_HEIGHT/2),
                          (CANVAS_WIDTH, CANVAS_HEIGHT))
        # Text
        victory_text.draw(canvas)
        return_button.draw(canvas)

# Key handlers for player ship controls
def key_down(key):
    global p1_up, p1_down, p1_left, p1_right, p1_weapon1, p1_weapon2
    global p2_up, p2_down, p2_left, p2_right, p2_weapon1, p2_weapon2
    # Player1 Controls
    # Basic movement wasd
    if key == simplegui.KEY_MAP['a']:
        p1_left = True
    if key == simplegui.KEY_MAP['d']:
        p1_right = True
    if key == simplegui.KEY_MAP['w']:
        p1_up = True
    if key == simplegui.KEY_MAP['s']:
        p1_down = True
    # Firing controls
    if key == simplegui.KEY_MAP['f']:
        p1_weapon1 = True
    if key == simplegui.KEY_MAP['g']:
        p1_weapon2 = True
    # Ability
    if key == simplegui.KEY_MAP['h']:
        player1.use_ability()

    # Player2 Controls
    # Basic movement wasd
    if key == simplegui.KEY_MAP['j']:
        global p2_left
        p2_left = True
    if key == simplegui.KEY_MAP['l']:
        global p2_right
        p2_right = True
    if key == simplegui.KEY_MAP['i']:
        global p2_up
        p2_up = True
    if key == simplegui.KEY_MAP['k']:
        global p2_down
        p2_down = True
    # Firing controls
    if key == simplegui.KEY_MAP['left']:
        p2_weapon1 = True
    if key == simplegui.KEY_MAP['down']:
        p2_weapon2 = True
    # Ability
    if key == simplegui.KEY_MAP['right']:
        player2.use_ability()
    # Back to menu
    if game_state == GAME_SCREEN:
        if key == simplegui.KEY_MAP['m']:
            current_song.pause()
            create_menu()
def key_up(key):
    global p1_up, p1_down, p1_left, p1_right, p1_weapon1, p1_weapon2
    global p2_up, p2_down, p2_left, p2_right, p2_weapon1, p2_weapon2
    # Player 1
    # Basic movement wasd
    if key == simplegui.KEY_MAP['a']:
        p1_left = False
    if key == simplegui.KEY_MAP['d']:
        p1_right = False
    if key == simplegui.KEY_MAP['w']:
        p1_up = False
    if key == simplegui.KEY_MAP['s']:
        p1_down = False
    # Firing controls
    if key == simplegui.KEY_MAP['f']:
        p1_weapon1 = False
    if key == simplegui.KEY_MAP['g']:
        p1_weapon2 = False
    # Player 2
    # Basic movement wasd
    if key == simplegui.KEY_MAP['j']:
        global p2_left
        p2_left = False
    if key == simplegui.KEY_MAP['l']:
        global p2_right
        p2_right = False
    if key == simplegui.KEY_MAP['i']:
        global p2_up
        p2_up = False
    if key == simplegui.KEY_MAP['k']:
        global p2_down
        p2_down = False
    # Firing controls
    if key == simplegui.KEY_MAP['left']:
        p2_weapon1 = False
    if key == simplegui.KEY_MAP['down']:
        p2_weapon2 = False

# Mouse position used for menu navigation
def mouse_click(mouse_position):
    global game_state, current_map, game_transition, transition_state
    if game_state == START_SCREEN:
        # If in start screen, clicking anywhere will start the game
        BUTTON_CLICK.rewind()
        BUTTON_CLICK.play()
        create_menu()
        
    elif game_state == MENU_SCREEN:
        # Map Navigation:
        # Back to start screen
        if return_button.is_clicked(mouse_position):
            MENU_MUSIC.pause()
            BUTTON_CLICK.rewind()
            BUTTON_CLICK.play()
            
            create_start_screen()
        # Back and forward button for maps
        if back_button.is_clicked(mouse_position):
            # Sound
            BUTTON_CLICK.rewind()
            BUTTON_CLICK.play()
            
            current_map -= 1
            # First map will loop back to last
            current_map %= len(MAP_VALUES)
            set_map_values(current_map)
        if next_button.is_clicked(mouse_position):
            # Sound
            BUTTON_CLICK.rewind()
            BUTTON_CLICK.play()
            
            current_map += 1
            # Last map will loop back to first
            current_map %= len(MAP_VALUES)
            set_map_values(current_map)
        # Start game button
        if select_button.is_clicked(mouse_position):
            BUTTON_CLICK.rewind()
            BUTTON_CLICK.play()
            game_transition = True
            transition_state = 0
            
    elif game_state == END_SCREEN:
        if return_button.is_clicked(mouse_position):
            BUTTON_CLICK.rewind()
            BUTTON_CLICK.play()
            create_menu()

# FRAME===========================================================================================================================================
frame = simplegui.create_frame('Game', CANVAS_WIDTH, CANVAS_HEIGHT, 200)

# Assign handlers
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(mouse_click)

# Instructions for controls
frame.add_label('-----Player 1 Controls-----'
                'W: Accelerate--------------'
                'S: Decelerate--------------'
                'A: Turn Left---------------'
                'D: Turn Right--------------'
                'F: PrimaryWeapon-----------'
                'G: SecondaryWeapon---------'
                'H: UseAbility--------------'
                '===========================')
frame.add_label('-----Player 2 Controls-----'
                'I: Accelerate--------------'
                'K: Decelerate--------------'
                'J: Turn Left---------------'
                'L: Turn Right--------------'
                'LeftArrow: PrimaryWeapon---'
                'DownArrow: SecondaryWeapon-'
                'RightArrow: UseAbility-----'
                '===========================')
frame.add_label('M: ReturnToMenu------------'
                '===========================')
frame.add_label('P1: RedBulletOutline-------'
                'P2: BlueBulletOutline------')

# Start frame
set_sound_volumes()
create_start_screen()
frame.start()