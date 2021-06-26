import oekolopoly.envs.get_boxes as gb
import gym
from gym import spaces
import numpy as np

class OekoEnv(gym.Env):
    
    SANIERUNG       = 0
    PRODUKTION      = 1
    AUFKLAERUNG     = 2
    LEBENSQUALITAET = 3
    VERMEHRUNGSRATE = 4
    UMWELTBELASTUNG = 5
    BEVOELKERUNG    = 6
    POLITIK         = 7
    VALID_TURN      = 8
    ROUND           = 9
    POINTS          = 10

    OBS_NAMES = [
        'Sanierung',
        'Produktion',
        'Aufklaerung',
        'Lebensqualitaet',
        'Vermehrungsrate',
        'Umweltbelastung',
        'Bevoelkerung',
        'Politik',
    ]

    def __init__(self):
        #                      0   1   2   3   4   5   6    7   8   9  10
        #                      S   Pr  A   L   V   U   B    P  VT   R  AP
        self.Vmin = np.array([ 1,  1,  1,  1,  1,  1,  1, -10,  0,  0,  0])
        self.Vmax = np.array([29, 29, 29, 29, 29, 29, 48,  37,  1, 30, 36])

        self.Amin = np.array([ 0,-28,  0,  0,  0, -5])
        self.Amax = np.array([28, 28, 28, 28, 28,  5])

        self.action_space = spaces.MultiDiscrete([
            29,   # 0 Sanierung
            57,   # 1 Produktion
            29,   # 2 Aufklärung
            29,   # 3 Lebensqualität
            29,   # 4 Vermehrungsrate
            11,   # 5 box9 Aufklärung > Vermehrung
        ])
        
        self.observation_space = spaces.MultiDiscrete([
            29,    # 0 Sanierung 
            29,    # 1 Produktion
            29,    # 2 Aufklärung
            29,    # 3 Lebensqualität
            29,    # 4 Vermehrungsrate
            29,    # 5 Umweltbelastung
            48,    # 6 Bevölkerung
            48,    # 7 Politik
            31,    # 8 Runde
            37,    # 9 Aktionspunkte für nächste Runde
        ])

        self.rew_points=0
    
    
    def update_values (self, V, action):
    
        done = False
        done_info = None
        extra_points = action[5]
            
        # Update V and boxes
        box1 = gb.get_box1   (self.V[self.SANIERUNG])
        if not done:
            self.V[self.UMWELTBELASTUNG] += box1
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30):
                done = True
                done_info = "Umweltbelastung ist außerhalb des zulässigen Ranges"
        
        if not done:
            box2 = gb.get_box2   (self.V[self.SANIERUNG])
            self.V[self.SANIERUNG] += box2
            if self.V[self.SANIERUNG] not in range (1, 30):
                done = True
                done_info = "Sanierung ist außerhalb des zulässigen Ranges"
        
        if not done:
            box3 = gb.get_box3   (self.V[self.PRODUKTION])
            self.V[ self.PRODUKTION] += box3
            if self.V[ self.PRODUKTION] not in range (1, 30):
                done = True
                done_info = "Produktion ist außerhalb des zulässigen Ranges"
            
            
        if not done:
            box4 = gb.get_box4   (self.V[self.PRODUKTION])
            self.V[self.UMWELTBELASTUNG] += box4
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30):
                done = True
                done_info = "Umweltbelastung ist außerhalb des zulässigen Ranges"
        

        if not done:
            box5 = gb.get_box5   (self.V[self.UMWELTBELASTUNG])
            self.V[self.UMWELTBELASTUNG] += box5
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30):
                done = True
                done_info = "Umweltbelastung ist außerhalb des zulässigen Ranges"

        if not done:
            box6 = gb.get_box6   (self.V[self.UMWELTBELASTUNG])
            self.V[self.LEBENSQUALITAET]  += box6
            if self.V[self.LEBENSQUALITAET] not in range (1, 30):
                done = True
                done_info = "Lebensqualitaet ist außerhalb des zulässigen Ranges"

        if not done:
            box7 = gb.get_box7   (self.V[self.AUFKLAERUNG])
            self.V[self.AUFKLAERUNG] += box7
            if self.V[self.AUFKLAERUNG] not in range (1, 30):
                done = True
                done_info = "Aufklaerung ist außerhalb des zulässigen Ranges"
            
            
        if not done:
            box8 = gb.get_box8   (self.V[self.AUFKLAERUNG])
            self.V[self.LEBENSQUALITAET]  += box8
            if self.V[self.LEBENSQUALITAET] not in range (1, 30):
                done = True
                done_info = "Lebensqualitaet ist außerhalb des zulässigen Ranges"
        

        if not done:
            if self.V[self.AUFKLAERUNG] in range (21, 24): extra_points = max (-3, min (3, extra_points))
            if self.V[self.AUFKLAERUNG] in range (24, 28): extra_points = max (-4, min (4, extra_points))
            if self.V[self.AUFKLAERUNG] in range (28, 30): extra_points = max (-5, min (5, extra_points))
            if self.V[self.AUFKLAERUNG] < 21: extra_points = 0
            box9 = gb.get_box9   (self.V[self.AUFKLAERUNG], extra_points)
            self.V[self.VERMEHRUNGSRATE] += box9
            if self.V[self.VERMEHRUNGSRATE] not in range (1, 30):
                done = True
                done_info = "Vermehrungsrate ist außerhalb des zulässigen Ranges"


        if not done:
            box10 = gb.get_box10 (self.V[self.LEBENSQUALITAET])
            self.V[ self.LEBENSQUALITAET]  += box10
            if self.V[self.LEBENSQUALITAET] not in range (1, 30):
                done = True
                done_info = "Lebensqualitaet ist außerhalb des zulässigen Ranges"
            

        if not done:
            box11 = gb.get_box11 (self.V[self.LEBENSQUALITAET])
            self.V[ self.VERMEHRUNGSRATE] += box11
            if self.V[self.VERMEHRUNGSRATE] not in range (1, 30):
                done = True
                done_info = "Vermehrungsrate ist außerhalb des zulässigen Ranges"
        

        if not done:
            box12 = gb.get_box12 (self.V[self.LEBENSQUALITAET])
            self.V[self.POLITIK] += box12
            if self.V[self.POLITIK] not in range (-10, 38):
                done = True
                done_info = "Politik ist außerhalb des zulässigen Ranges"

        if not done:
            box13 = gb.get_box13 (self.V[self.VERMEHRUNGSRATE])
            boxW  = gb.get_boxW  (self.V[ self.BEVOELKERUNG])
            self.V[self.BEVOELKERUNG] += box13 * boxW
            if self.V[self.BEVOELKERUNG] not in range (1, 49):
                done = True
                done_info = "Bevoelkerung ist außerhalb des zulässigen Ranges"
        

        if not done:
            box14 = gb.get_box14 (self.V[self.BEVOELKERUNG])
            self.V[ self.LEBENSQUALITAET] += box14
            if self.V[self.LEBENSQUALITAET] not in range (1, 30):
                done = True
                done_info = "Lebensqualitaet ist außerhalb des zulässigen Ranges"
        
        return  self.V, done, done_info
    
    
    def step(self, action):
        assert (self.action_space.contains (action)), "AssertionError: action not in action_space"

        # Transform action space
        action = list(action)
        action[self.PRODUKTION] += self.Amin[self.PRODUKTION]
        action[5] += self.Amin[5]
        #extra_points = action[5]
        
        # Init
        done = False
        self.V[self.VALID_TURN] = 1
        self.reward = 0
        self.balance = 0
        used_points = 0
        
        # Sum points from action
        used_points += action[self.SANIERUNG]
        used_points += abs (action[self.PRODUKTION])
        used_points += action[self.AUFKLAERUNG]
        used_points += action[self.LEBENSQUALITAET]
        used_points += action[self.VERMEHRUNGSRATE]


        if used_points < 0 or used_points > self.V[self.POINTS]:
            self.V[self.VALID_TURN] = 0

        if self.V[self.VALID_TURN]:
            for i in range(5):
                if (self.V[i] + action[i]) not in range (self.Vmin[i], self.Vmax[i] + 1):
                    self.V[self.VALID_TURN] = 0
                    break

        if self.V[self.VALID_TURN]:
            for i in range(5): self.V[i] += action[i]

            # Update boxes and V accordingly
            self.V, done, done_info = self.update_values(self.V, action)
             
            # Update points and round 
            self.V[self.POINTS] -= used_points            
            self.V[self.ROUND] += 1
            
            # Clip values if not in range
            for i in range(8):
                if  self.V[i] not in range (self.Vmin[i],  self.Vmax[i] + 1):
                    self.V[i] = max( self.Vmin[i], min( self.Vmax[i],  self.V[i]))
                    done = True
            
            if  self.V[self.POINTS] <  0:
                self.V[self.POINTS] = 0
                done = True
                done_info = 'Minimale Anzahl von Aktionspunkten erreicht'
            
            if  self.V[self.ROUND] == 30:
                done = True
                done_info = 'Maximale Anzahl von Runden erreicht'
            
            # Points for next round
            if done:
                self.V[self.POINTS] = 0
            else:
                boxA  = gb.get_boxA  (self.V[self.BEVOELKERUNG])
                boxB  = gb.get_boxB  (self.V[self.POLITIK])
                boxC  = gb.get_boxC  (self.V[self.PRODUKTION])
                boxV  = gb.get_boxV  (self.V[self.PRODUKTION])
                boxD  = gb.get_boxD  (self.V[self.LEBENSQUALITAET])
            
                self.V[self.POINTS] += boxA * boxV
                self.V[self.POINTS] += boxB
                self.V[self.POINTS] += boxC
                self.V[self.POINTS] += boxD
                
            if  self.V[self.POINTS] > 36:
                self.V[self.POINTS] = 36
                done = True
                done_info = 'Maximale Anzahl von Aktionspunkten erreicht'


            boxD  = gb.get_boxD  (self.V[self.LEBENSQUALITAET])                
            a = float( (boxD*3 + self.V[self.POLITIK]) * 10)
            self.rew_points = int(a)
            
            if done:
                b = float(self.V[self.ROUND] + 3)
                #print(a,b,a/b)
                self.balance = round(float(a/b), 2)
                
                if self.V[self.ROUND] in range(10, 31):
                    self.reward = self.balance
                else:
                    self.reward = 0
                
        else:
            self.V[self.VALID_TURN] = 0
            done_info = 'Ungültiger Zug'

        if not self.V[self.VALID_TURN]:
            raise ValueError ("ValueError: Ungültiger Zug")

        # Transform V in obs
        self.obs = list(self.V - self.Vmin)
        assert (self.observation_space.contains(self.obs)), "AssertionError: obs not in observation_space"

        # if done_info == None:
        #    done_info = "Das Spiel setzt fort."

        return self.obs, self.reward, done, {'balance': self.balance, 'done_reason': done_info, 'rew_points': self.rew_points}


    def reset(self):
        self.V = np.array([
            1,  #0 Sanierung
            12, #1 Produktion
            4,  #2 Aufklärung
            10, #3 Lebensqualität
            20, #4 Vermehrungsrate
            13, #5 Umweltbelastung 
            21, #6 Bevölkerung
            0,  #7 Politik
            1,  #8  Valid turn
            0,  #9  Round
            8,  #10 Points
        ])
        
        self.obs = self.V - self.Vmin
        assert (self.observation_space.contains(self.obs)), "AssertionError: obs not in observation_space"
        
        return self.obs
