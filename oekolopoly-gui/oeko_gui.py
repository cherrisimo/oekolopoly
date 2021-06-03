import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QSlider, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QGridLayout

import gym


def get_avaiable_points (env, sliders):
    if hasattr (env, 'V'):
        used_points = 0
        for i in range (len (sliders) - 1):
            used_points += abs (sliders[i].value)
        available_points = env.V[env.POINTS] - used_points
    else:
        available_points = 0

    return available_points


def update_points_label (points_label, env, sliders):
    available_points = get_avaiable_points (env, sliders)
    points_label.setText ("Aktionspunkte: {}".format (available_points))


class ActionSlider:
    def __init__(self, options, env, sliders, points_label):
        self.env = env
        self.sliders = sliders
        self.points_label = points_label

        self.name = options['name']
        self.min  = options['min']
        self.max  = options['max']
        if 'default' in options:
            self.default = options['default']
        else:
            self.default = self.min

        self.label = QLabel ("")

        self.icon = QLabel ()
        self.icon.setPixmap (QPixmap (options['icon']))

        self.slider = QSlider (Qt.Horizontal)
        self.slider.setMinimum(self.min)
        self.slider.setMaximum(self.max)

        self.slider.valueChanged.connect (self.onchange)

        self.layout = QGridLayout ()
        self.layout.setHorizontalSpacing (10)
        self.layout.setVerticalSpacing (0)
        self.layout.setContentsMargins (0, 0, 0, 0)
        self.layout.addWidget (self.icon,   0, 0, 0, 1)
        self.layout.addWidget (self.label,  0, 1)
        self.layout.addWidget (self.slider, 1, 1)
        self.widget = QWidget ()
        self.widget.setLayout (self.layout)
        
        self.reset ()

    def onchange (self, value):
        self.change (value)

    def reset (self):
        self.value = self.default
        self.slider.valueChanged.disconnect (self.onchange)
        self.slider.setValue (self.default)
        self.slider.valueChanged.connect (self.onchange)
        self.set_label ()

    def change (self, value):
        self.value = value
        available_points = get_avaiable_points (self.env, self.sliders)
        if available_points < 0:
            if self.value < 0:
                self.value -= available_points
            else:
                self.value += available_points

            self.slider.valueChanged.disconnect (self.onchange)
            self.slider.setValue (self.value)
            self.slider.valueChanged.connect (self.onchange)
        
        self.set_label ()
        update_points_label (self.points_label, self.env, self.sliders)

    def set_label (self):
        self.label.setText("{}: {}".format(self.name, self.value))


def update_obs_table (obs_table, obs):
    # Add column and set header
    curr_col = obs_table.columnCount ()
    obs_table.setColumnCount (curr_col + 1)

    col_header = QTableWidgetItem (str(curr_col))
    obs_table.setHorizontalHeaderItem (curr_col, col_header)

    # Add rows to the new column
    for i in range(len(obs)):
        cell = str(obs[i])
        item = QTableWidgetItem (cell)
        item.setFlags (Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        obs_table.setItem (i, curr_col, item)


def step (step_button, env, action_sliders, obs_table, obs_status, points_label):
    action = []
    for action_slider in action_sliders:
        action.append (action_slider.value)

    action[env.PRODUKTION] -= env.Amin[env.PRODUKTION]
    action[5] -= env.Amin[5]
    try:
        obs, reward, done, info = env.step (action)
        valid_move = True
    except ValueError as e:
        obs_status.setText (str(e))
        valid_move = False

    if valid_move:
        if done:
            step_button.setEnabled (False)
            obs_status.setText ("Done | Bilanz: {}".format(env.reward))
            for action_slider in action_sliders: action_slider.reset ()
        else:
            obs_status.setText ("Round {}".format(env.V[env.ROUND]))
            for action_slider in action_sliders: action_slider.reset ()

        if env.V[env.VALID_TURN]:
            update_obs_table (obs_table, list(env.V))

        update_points_label (points_label, env, action_sliders)


def reset (step_button, env, action_sliders, obs_table, obs_status, points_label):
    env.reset ()
    for action_slider in action_sliders: action_slider.reset ()
    step_button.setEnabled (True)
    obs_status.setText ("Round 0")

    obs_table.setColumnCount (0)
    update_obs_table (obs_table, list(env.V))

    update_points_label (points_label, env, action_sliders)


def main ():
    env = gym.make('oekolopoly:Oekolopoly-v0')

    qapp = QApplication (sys.argv)

    f = open('res/Combinear.qss')
    stylesheet = f.read()
    f.close ()

    window = QMainWindow ()
    window.setWindowTitle ("Ökolopoly")
    window.setWindowIcon (QIcon("res/imgs/icon2.png"))
    window.resize (800, 100)
    window.show()

    action_options = [
        {'name': "Sanierung",       "icon": "res/imgs/s.png",  "min": env.Amin[env.SANIERUNG],       "max": env.Amax[env.SANIERUNG],       "default": 0},
        {'name': "Produktion",      "icon": "res/imgs/pr.png", "min": env.Amin[env.PRODUKTION],      "max": env.Amax[env.PRODUKTION],      "default": 0},
        {'name': "Aufklärung",      "icon": "res/imgs/a.png", "min": env.Amin[env.AUFKLAERUNG],      "max": env.Amax[env.AUFKLAERUNG],     "default": 0},
        {'name': "Lebensqualität",  "icon": "res/imgs/l.png", "min": env.Amin[env.LEBENSQUALITAET],  "max": env.Amax[env.LEBENSQUALITAET], "default": 0},
        {'name': "Vermehrungsrate", "icon": "res/imgs/v.png",  "min": env.Amin[env.VERMEHRUNGSRATE], "max": env.Amax[env.VERMEHRUNGSRATE], "default": 0},
        {'name': "Bonuspunkte",     "icon": "res/imgs/b.png",  "min": env.Amin[5],                   "max": env.Amax[5], "default": 0},
    ]

    table_headers = [
        "Sanierung",
        "Produktion",
        "Aufklärung",
        "Lebensqualität",
        "Vermehrungsrate",
        "Umweltbelastung",
        "Bevölkerung",
        "Politik",
        "Valid turn",
        "Round",
        "Points"
    ]
    
    # Set sliders and buttons
    controls_layout = QVBoxLayout ()
    controls_layout.setSpacing (30)
    controls_widget = QWidget ()
    controls_widget.setFixedWidth (300)
    controls_widget.setLayout (controls_layout)
    controls_widget.setStyleSheet (stylesheet)
    
    # Set fonts
    title_font = QFont ()
    #title_font.setFamily ('Times New Roman')
    title_font.setWeight (63)
    title_font.setPointSize (11)
    
    text_font = QFont ()
    text_font.setWeight (63)
    text_font.setPointSize (9)
    
    column_font = QFont ()
    column_font.setItalic(True)
    
    controls_title = QLabel ("Aktionslider")
    controls_title.setFont (title_font)
    
    points_label = QLabel ()
    points_label.setAlignment(Qt.AlignRight)
    points_label.setStyleSheet("color: #F2C063")
    points_label.setFont(text_font)

    # Set sliders
    sliders_layout = QVBoxLayout ()
    sliders_layout.setSpacing (25)
    sliders_layout.setContentsMargins (0, 0, 0, 0)
    sliders_widget = QWidget ()
    sliders_widget.setLayout (sliders_layout)
    sliders_layout.addWidget (controls_title, 0, Qt.AlignCenter)
    sliders_layout.addWidget (points_label)
    controls_layout.addWidget (sliders_widget, 0, Qt.AlignTop)
    
    # Sliders init
    action_sliders = []
    for action_option in action_options:
        action_slider = ActionSlider (action_option, env, action_sliders, points_label)
        sliders_layout.addWidget (action_slider.widget)
        action_sliders.append (action_slider)
    
    # Set buttons
    step_button  = QPushButton ("Step")
    step_button.setStyleSheet(stylesheet)
    
    reset_button = QPushButton ("Reset")
    reset_button.setStyleSheet(stylesheet)
    
    buttons_layout = QHBoxLayout ()
    buttons_layout.setContentsMargins (0, 0, 0, 0)
    buttons_layout.addWidget (step_button)
    buttons_layout.addWidget (reset_button)
    buttons_widget = QWidget ()
    buttons_widget.setLayout (buttons_layout)
    controls_layout.addWidget (buttons_widget, 0, Qt.AlignTop)

    obs_title = QLabel ("Protokoll")
    obs_title.setFont (title_font)

    # Make table
    obs_table = QTableWidget (len (table_headers), 0)
  
    for i in range (len (table_headers)):
        row_header = QTableWidgetItem (table_headers[i])
        obs_table.setVerticalHeaderItem (i, row_header)
        if i == len (table_headers) - 1 or i == len (table_headers) - 2 or i == len (table_headers) - 3:
            row_header.setFont(column_font)
        
    

    # Set status
    obs_status = QLabel ()
    obs_layout = QVBoxLayout ()
    obs_layout.addWidget (obs_title, 0, Qt.AlignCenter)
    obs_layout.addWidget (obs_table)
    obs_layout.addWidget (obs_status, 0, Qt.AlignCenter)
    obs_widget = QWidget ()
    obs_widget.setLayout (obs_layout)
    obs_widget.setStyleSheet (stylesheet)
    
    obs_status.setStyleSheet ("color: #F2C063")
    obs_status.setFont(text_font)

    # Set window
    window_layout = QHBoxLayout ()
    window_layout.setSpacing (0)
    window_layout.setContentsMargins (0, 0, 0, 0)
    window_layout.addWidget (controls_widget)
    window_layout.addWidget (obs_widget)
    window_center = QWidget ()
    window_center.setLayout (window_layout);
    window.setCentralWidget (window_center);

    reset (                                            step_button, env, action_sliders, obs_table, obs_status, points_label)
    step_button.clicked.connect  (lambda value: step  (step_button, env, action_sliders, obs_table, obs_status, points_label))
    reset_button.clicked.connect (lambda value: reset (step_button, env, action_sliders, obs_table, obs_status, points_label))
    qapp.exec_ ()


if __name__ == '__main__':
    main ()
