
#SOURCE: https://stable-baselines.readthedocs.io/en/master/guide/custom_env.html

import gym
from gym import error, spaces, utils
from gym.utils import seeding

SANIERUNG       = 0
PRODUKTION      = 1
AUFKLÄRUNG      = 2
LEBENSQUALITÄT  = 3
VERMEHRUNGSRATE = 4
UMWELTBELASTUNG = 5
BEVÖLKERUNG     = 6
POLITIK         = 7


def get_box1_and_box2_from_region0 (region0):
    # if region0 not in (1,30): return 0,0
    #print (region0)

    #Box 1 Sanierung-Umweltbelastung 0-5
    if   region0  <  2: box1 =  0
    elif region0  <  8: box1 = -1
    elif region0  < 13: box1 = -2
    elif region0  < 18: box1 = -3
    elif region0  < 21: box1 = -4
    elif region0  < 24: box1 = -5
    elif region0  < 26: box1 = -6
    elif region0  < 28: box1 = -7
    elif region0 == 28: box1 = -8
    elif region0 == 29: box1 = -9
     
    #Box 2 Sanierung-Sanierung 0-0
    if   region0  < 22: box2 =  0
    elif region0  < 24: box2 = -1  # self.regions[5] -= 1
    elif region0  < 26: box2 = -2
    elif region0 == 26: box2 = -3
    elif region0 == 27: box2 = -4
    elif region0 == 28: box2 = -5
    elif region0 == 29: box2 = -6

    return box1, box2


def get_box3_box4_boxC_and_boxV_from_region1(region1):
    # if region1 not in (1,30): return 0,0,0,0
    # print (region1)
    
    #Box 3 Produktion-Produktion 4-4
    if   region1  <  7:                     box3 = 0
    elif region1  <  22 or region1  == 29 : box3 = 1
    elif region1  < 29:                     box3 = 2

    #Box 4 Produktion-Umweltbelastung 4-5
    if   region1  <  5: box4 = 0
    elif region1  <  9: box4 = 1
    elif region1  < 13: box4 = 2
    elif region1  < 15: box4 = 3
    elif region1  < 17: box4 = 4
    elif region1  < 19: box4 = 5
    elif region1  < 21: box4 = 6
    elif region1  < 23: box4 = 7
    elif region1 == 23: box4 = 8
    elif region1 == 24: box4 = 9
    elif region1 == 25: box4 = 10
    elif region1 == 26: box4 = 12
    elif region1 == 27: box4 = 14
    elif region1 == 28: box4 = 18
    elif region1 == 29: box4 = 22

    #Box C Produktion-Aktionspunkte 4-A
    if   region1  == 1: boxC = -4
    elif region1  == 2: boxC = -3
    elif region1  == 3: boxC = -2
    elif region1  == 4: boxC = -1
    elif region1  == 5: boxC = 0
    elif region1  < 8:  boxC = 2 
    elif region1  < 11: boxC = 3
    elif region1  < 14: boxC = 4
    elif region1  < 17: boxC = 5
    elif region1  < 20: boxC = 6
    elif region1  < 22: boxC = 7
    elif region1  < 24: boxC = 8
    elif region1  < 26: boxC = 9
    elif region1 == 26: boxC = 10
    elif region1 == 27: boxC = 11
    elif region1 == 28: boxC = 12
    elif region1 == 29: boxC = 0

    #Box V Multiplier Produktion-Aktionspunkte 4-A
    if   region1  == 1: boxV = -4
    elif region1  == 2: boxV = -3
    elif region1  < 5:  boxV = -2
    elif region1  < 7:  boxV = -1
    elif region1  < 9:  boxV = 0
    elif region1  < 30: boxV = 1
            
    return box3, box4, boxC, boxV


def get_box5_and_box6_from_region5 (region5):
    # if region5 not in (1,30): return 0,0
    # print (region5)
    
    #Box 5 Umweltbelastung-Umweltbelastung 5-5
    if   region5  <  4 or region5 == 28 or region5 == 29: box5 =  0
    elif region5  < 14 or region5 == 27:                  box5 = -1
    elif region5  < 20 or region5 == 26:                  box5 = -2
    elif region5 == 24:                                   box5 = -4
    elif region5  < 24 or region5 == 25:                  box5 = -3
    
            
    #Box 6 Umweltbelastung-Lebensqualität 5-2
    if   region5  <  8: box6 =  0
    elif region5  < 11: box6 = -1
    elif region5  < 15: box6 = -2
    elif region5  < 18: box6 = -3
    elif region5  < 20: box6 = -4
    elif region5  < 22: box6 = -5
    elif region5 == 22: box6 = -6
    elif region5 == 23: box6 = -7
    elif region5 == 24: box6 = -8
    elif region5 == 25: box6 = -10
    elif region5 == 26: box6 = -12
    elif region5 == 27: box6 = -14
    elif region5 == 28: box6 = -18
    elif region5 == 29: box6 = -25

    return box5, box6


def get_box7_box8_and_box9_from_region2(region2, extra_points):
    # if region2 not in (1,30): return 0,0,0
    # print (region2, extra_points)
    
    #Box 7 Aufklärung-Aufklärung 1-1
    if   region2  <  3 or region2 in range(6, 15) or region2 == 29: box7 = 0
    elif region2  <  6:                                             box7 = -1
    elif region2  < 21 or region2 in range(24, 29):                 box7 = 1
    elif region2 in range(21, 24):                                  box7 = 2

    #Box 8 Aufklärung-Lebensqualität 1-2
    if   region2  <  6: box8 = -2
    elif region2  < 10: box8 = -1
    elif region2 == 10: box8 = 0
    elif region2  < 14: box8 = 1
    elif region2  < 18: box8 = 2
    elif region2  < 22: box8 = 3
    elif region2  < 26: box8 = 4
    elif region2  < 28: box8 = 5
    elif region2  < 30: box8 = 6

    #Box 9 Aufklärung-Vermehrungsrate 1-3
    if   region2 == 1:  box9 = 1
    elif region2  < 10: box9 = 0
    elif region2  < 14: box9 = 1
    elif region2  < 19: box9 = 2
    elif region2  < 21: box9 = 3
    elif region2  < 24: box9 = 3 if extra_points else -3
    elif region2  < 28: box9 = 4 if extra_points else -4
    elif region2  < 30: box9 = 5 if extra_points else -5

    return box7, box8, box9


def get_box10_box11_box12_and_boxD_from_region3(region3):
    # if region3 not in (1,30): return 0,0,0,0
    # print (region3)
    
    #Box 10 Lebensqualität-Lebensqualität 2-2
    if   region3 == 1 or region3  in range(4,10) or region3  in range(16,18) or region3  == 29: box10 = 0
    elif region3  < 4 or region3  in range(10,13) or region3 in range(14,16):                   box10 = 1
    elif region3 == 13:                                                                         box10 = 2
    elif region3  in range(18,23) or region3  in range(26,29):                                  box10 = -1
    elif region3  in range(23,26):                                                              box10 = -2

    #Box 11 Lebensqualität-Vermehrungsrate 2-3
    if   region3 == 1: box11 = -15
    elif region3 == 2: box11 = -8
    elif region3 == 3: box11 = -6
    elif region3 == 4: box11 = -4
    elif region3 == 5: box11 = -3
    elif region3 == 6: box11 = -2
    elif region3 == 7: box11 = -1
    elif region3 == 8: box11 = 0
    elif region3 == 9: box11 = 1
    elif region3 < 13: box11 = 2
    elif region3 < 21: box11 = 1
    elif region3 < 30: box11 = 0

    #Box 12 Lebensqualität-Politik 2-7
    if   region3 == 1: box12 = -10
    elif region3 == 2: box12 = -8
    elif region3 == 3: box12 = -6
    elif region3 == 4: box12 = -3
    elif region3 == 5: box12 = -2
    elif region3 < 10: box12 = -1
    elif region3 < 12: box12 = 0
    elif region3 < 21: box12 = 1
    elif region3 < 24: box12 = 2
    elif region3 < 27: box12 = 3
    elif region3 < 29: box12 = 4
    elif region3 == 29: box12 = 5
            
    #Box D Lebensqualität-Aktionspunkte 2-A
    if   region3 == 1: boxD = -6
    elif region3 == 2: boxD = -4
    elif region3 == 3: boxD = -2
    elif region3 < 6:  boxD = 0
    elif region3 < 9:  boxD = 1
    elif region3 < 18: boxD = 2 
    elif region3 < 23: boxD = 3
    elif region3 < 27: boxD = 4
    elif region3 < 30: boxD = 5

    return box10, box11, box12, boxD
            

def get_box13_from_region4(region4):
    # if region4 not in (1,30): return 0
    # print (region4)
    
    #Box 13 Vermehrungsrate-Bevölkerung 3-6
    if   region4  <  3: box13 = -4
    elif region4  <  6: box13 = -3
    elif region4  < 10: box13 = -2
    elif region4  < 15: box13 = -1
    elif region4 == 15: box13 = 0
    elif region4  < 21: box13 = 1
    elif region4  < 26: box13 = 2
    elif region4  < 30: box13 = 3

    return box13
            

def get_box14_boxA_and_boxW_from_region6(region6):
    # if region6 not in (1,49): return 0,0,0
    # print (region6)
    
    #Box 14 Bevölkerung-Lebensqualität 6-2
    if   region6  < 16: box14 = 0
    elif region6  < 26: box14 = -1
    elif region6  < 31: box14 = -2
    elif region6  < 39: box14 = -3
    elif region6  < 43: box14 = -4
    elif region6  < 45: box14 = -5 
    elif region6 == 45: box14 = -6
    elif region6 == 46: box14 = -7
    elif region6 == 47: box14 = -8
    elif region6 == 48: box14 = -10

    #Box A Bevölkerung-Aktionspunkte 6
    if   region6  < 10: boxA = 0
    elif region6  < 17: boxA = 1
    elif region6  < 22: boxA = 2
    elif region6  < 26: boxA = 3
    elif region6  < 30: boxA = 4
    elif region6  < 34: boxA = 5 
    elif region6  < 38: boxA = 6
    elif region6  < 42: boxA = 7
    elif region6  < 46: boxA = 8
    elif region6 <= 48: boxA = 9
            
    #Box W Multiplier Bevölkerung-Bevölkerung 6-6
    if   region6 == 1:   boxW = 0
    elif region6  < 15:  boxW = 1
    elif region6  < 36:  boxW = 2
    elif region6 <= 48:  boxW = 3

    return box14, boxA, boxW
            

def get_boxB_from_region7(region7):
    '''
    x = -10,..., 0,..., 37
    y = x + 11
    y = 1,..., 11,..., 48
    '''
    # print (region7)
    # if region7 not in (1,49): return 0

    #Box B Politik-Aktionspunkte 7-A
    if   region7 == 1:  boxB = -5
    elif region7 == 2:  boxB = -2
    elif region7  < 9:  boxB = -1
    elif region7  < 19: boxB = 0
    elif region7  < 33: boxB = 1
    elif region7  < 42: boxB = 2 
    elif region7 <= 48: boxB = 3
    
    return boxB


import gym
from gym import spaces

class OekoEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Tuple((
            spaces.Discrete(30),  # 0 Sanierung
            spaces.Discrete(30),  # 1 Produktion
            spaces.Discrete(30),  # 2 Aufklärung
            spaces.Discrete(30),  # 3 Lebensqualität
            spaces.Discrete(30),  # 4 Vermehrungsrate
            spaces.Discrete(2)))  # 5 box9 extra_points 1: add, 0: substract
        
        self.observation_space = spaces.Tuple((
            spaces.Discrete(30),    # 0 Sanierung 
            spaces.Discrete(30),    # 1 Produktion
            spaces.Discrete(30),    # 2 Aufklärung
            spaces.Discrete(30),    # 3 Lebensqualität
            spaces.Discrete(30),    # 4 Vermehrungsrate
            
            spaces.Discrete(30),    # 5 Umweltbelastung
            spaces.Discrete(49),    # 6 Bevölkerung
            spaces.Discrete(49),    # 7 Politik

            spaces.Discrete(2),     # 8 valid turn: 1 - valid, 0 - not valid
            spaces.Discrete(31),    # 9 round
            spaces.Discrete(37)))   # 10 points for next round
    
    def step(self, action):
        done = False
        valid_turn = 1
        strategy_points = 0
        reward = 0

        assert (self.action_space.contains(action))

        if action[SANIERUNG]       - self.regions[SANIERUNG]       < 0: valid_turn = 0
        if action[AUFKLÄRUNG]      - self.regions[AUFKLÄRUNG]      < 0: valid_turn = 0
        if action[LEBENSQUALITÄT]  - self.regions[LEBENSQUALITÄT]  < 0: valid_turn = 0
        if action[VERMEHRUNGSRATE] - self.regions[VERMEHRUNGSRATE] < 0: valid_turn = 0
        if action[PRODUKTION] == 0: valid_turn = 0

        if valid_turn:
            used_points = 0
            used_points += action[SANIERUNG] - self.regions[SANIERUNG]
            #print("action SANIERUNG", action[SANIERUNG])
            #print("region SANIERUNG", self.regions[SANIERUNG])
            #print("Used points: ", used_points)

            used_points += abs(action[PRODUKTION] - self.regions[PRODUKTION])
            #print("action PRODUKTION", action[PRODUKTION])
            #print("region PRODUKTION", self.regions[PRODUKTION])
            #print("Used points: ", used_points)

            used_points += action[AUFKLÄRUNG] - self.regions[AUFKLÄRUNG]
            #print("action AUFKLÄRUNG", action[AUFKLÄRUNG])
            #print("region AUFKLÄRUNG", self.regions[AUFKLÄRUNG])
            #print("Used points: ", used_points)

            used_points += action[LEBENSQUALITÄT] - self.regions[LEBENSQUALITÄT]
            #print("action LEBENSQUALITÄT", action[LEBENSQUALITÄT])
            #print("region LEBENSQUALITÄT", self.regions[LEBENSQUALITÄT])
            #print("Used points: ", used_points)

            used_points += action[VERMEHRUNGSRATE] - self.regions[VERMEHRUNGSRATE]
            #print("action VERMEHRUNGSRATE", action[VERMEHRUNGSRATE])
            #print("region VERMEHRUNGSRATE", self.regions[VERMEHRUNGSRATE])
            #print("Used points: ", used_points)
        
        if valid_turn and used_points >= 0 and used_points <= self.points:
            valid_turn = 1
            available_points = self.points
            self.points -= used_points            
            self.turn += 1
            
            print("\n############################# ROUND %d #############################" %self.turn)
            print("Points avilable at the beginning: ", available_points)
            print("Points left: ", self.points)
            #print("Round: %d ;" %self.turn, "Points left: %d" %self.points)
            
            for i in range(0, 5): self.regions[i] = action[i]
            
            #Update boxes
            
            box1, box2                = get_box1_and_box2_from_region0              (self.regions[SANIERUNG])
            #print("Box 1:", box1)
            #print("Box 2:", box2)
            
            box3, box4, boxC, boxV    = get_box3_box4_boxC_and_boxV_from_region1    (self.regions[PRODUKTION])
            #print("Box 3:", box3)
            #print("Box 4:", box4)
            #print("Box C:", boxC)
            #print("Box V:", boxV)

            box5, box6                = get_box5_and_box6_from_region5              (self.regions[UMWELTBELASTUNG])
            #print("Box 5:", box5)
            #print("Box 6:", box6)
            
            box7, box8, box9          = get_box7_box8_and_box9_from_region2         (self.regions[AUFKLÄRUNG], action[5])
            #print("Box 7:", box7)
            #print("Box 8:", box8)
            #print("Box 9:", box9)
            
            box10, box11, box12, boxD = get_box10_box11_box12_and_boxD_from_region3 (self.regions[LEBENSQUALITÄT])
            #print("Box 10:", box10)
            #print("Box 11:", box11)
            #print("Box 12:", box12)
            #print("Box D:", boxD)
            
            box13                     = get_box13_from_region4                      (self.regions[VERMEHRUNGSRATE])
            #print("Box 13:", box13)
            
            box14, boxA, boxW         = get_box14_boxA_and_boxW_from_region6        (self.regions[BEVÖLKERUNG])
            #print("Box 14:", box14)
            #print("Box A:", boxA)
            #print("Box W:", boxW)
            
            boxB                      = get_boxB_from_region7                       (self.regions[POLITIK])
            #print("Box B:", boxB)
            
            
            #Update regions and boxes
            self.regions[UMWELTBELASTUNG] += box1
            if self.regions[UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = get_box5_and_box6_from_region5              (self.regions[UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.regions[UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.regions[SANIERUNG] += box2
            if self.regions[SANIERUNG] not in range (1, 30): done = True
            if not done:
                box1, box2                = get_box1_and_box2_from_region0              (self.regions[SANIERUNG])
                #print("SANIERUNG: ", self.regions[SANIERUNG])
                #print("Box 1:", box1)
                #print("Box 2:", box2)
            
            self.regions[PRODUKTION] += box3
            if self.regions[PRODUKTION] not in range (1, 30): done = True
            if not done:
                box3, box4, boxC, boxV    = get_box3_box4_boxC_and_boxV_from_region1    (self.regions[PRODUKTION])
                #print("PRODUKTION: ", self.regions[PRODUKTION])
                #print("Box 3:", box3)
                #print("Box 4:", box4)
                #print("Box C:", boxC)
                #print("Box V:", boxV)
            
            self.regions[UMWELTBELASTUNG] += box4
            if self.regions[UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = get_box5_and_box6_from_region5              (self.regions[UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.regions[UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.regions[UMWELTBELASTUNG] += box5
            if self.regions[UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = get_box5_and_box6_from_region5              (self.regions[UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.regions[UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.regions[LEBENSQUALITÄT]  += box6
            if self.regions[LEBENSQUALITÄT] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = get_box10_box11_box12_and_boxD_from_region3 (self.regions[LEBENSQUALITÄT])
                #print("LEBENSQUALITÄT: ", self.regions[LEBENSQUALITÄT])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)
            
            self.regions[AUFKLÄRUNG]      += box7
            if self.regions[AUFKLÄRUNG] not in range (1, 30): done = True
            if not done:
                box7, box8, box9          = get_box7_box8_and_box9_from_region2         (self.regions[AUFKLÄRUNG], action[5])
                #print("AUFKLÄRUNG: ", self.regions[AUFKLÄRUNG])
                #print("Box 7:", box7)
                #print("Box 8:", box8)
                #print("Box 9:", box9)
            
            self.regions[LEBENSQUALITÄT]  += box8
            if self.regions[LEBENSQUALITÄT] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = get_box10_box11_box12_and_boxD_from_region3 (self.regions[LEBENSQUALITÄT])
                #print("LEBENSQUALITÄT: ", self.regions[LEBENSQUALITÄT])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)
            
            self.regions[VERMEHRUNGSRATE] += box9
            if self.regions[VERMEHRUNGSRATE] not in range (1, 30): done = True
            if not done:
                box13                     = get_box13_from_region4                      (self.regions[VERMEHRUNGSRATE])
                #print("VERMEHRUNGSRATE: ", self.regions[VERMEHRUNGSRATE])
                #print("Box 13:", box13)
            
            self.regions[LEBENSQUALITÄT]  += box10
            if self.regions[LEBENSQUALITÄT] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = get_box10_box11_box12_and_boxD_from_region3 (self.regions[LEBENSQUALITÄT])
                #print("LEBENSQUALITÄT: ", self.regions[LEBENSQUALITÄT])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)
            
            self.regions[VERMEHRUNGSRATE] += box11
            if self.regions[VERMEHRUNGSRATE] not in range (1, 30): done = True
            if not done:
                box13                     = get_box13_from_region4                      (self.regions[VERMEHRUNGSRATE])
                #print("VERMEHRUNGSRATE: ", self.regions[VERMEHRUNGSRATE])
                #print("Box 13:", box13)

            prev_politik = self.regions[POLITIK]
            self.regions[POLITIK]         += box12
            if self.regions[POLITIK] not in range (1, 49): done = True
            if not done:
                boxB                      = get_boxB_from_region7                       (self.regions[POLITIK])
                #print("POLITIK: ", self.regions[POLITIK])
                #print("Box B:", boxB)
            
            self.regions[BEVÖLKERUNG]     += box13 * boxW
            if self.regions[BEVÖLKERUNG] not in range (1, 49): done = True
            if not done:
                box14, boxA, boxW         = get_box14_boxA_and_boxW_from_region6        (self.regions[BEVÖLKERUNG])
                #print("BEVÖLKERUNG: ", self.regions[BEVÖLKERUNG])
                #print("Box 14:", box14)
                #print("Box A:", boxA)
                #print("Box W:", boxW)
            
            self.regions[LEBENSQUALITÄT]  += box14
            prev_boxD = boxD
            if self.regions[LEBENSQUALITÄT] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = get_box10_box11_box12_and_boxD_from_region3 (self.regions[LEBENSQUALITÄT])
                #print("LEBENSQUALITÄT: ", self.regions[LEBENSQUALITÄT])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)

            #Points for next round
            self.points += boxA * boxV
            self.points += boxB
            self.points += boxC
            self.points += boxD

            if self.points <  0: self.points = 0
            if self.points > 36: self.points = 36

            for i in range(6):
                if self.regions[i] not in range (1, 29):
                    self.regions[i] = 0
                    done = True

            if self.regions[BEVÖLKERUNG] not in range (1, 48):
                self.regions[BEVÖLKERUNG] = 0
                done = True

            if self.regions[POLITIK] not in range (1, 48):
                self.regions[POLITIK] = 0
                done = True

            if self.turn == 30:
                done = True

            # if done and self.turn < 10: done = False

            if done:
                a = float(abs((prev_boxD*3) + prev_politik)*10)
                b = float(self.turn + 3)
                # print ("prev_boxD:",    prev_boxD)
                # print ("prev_POLITIK:", prev_politik)
                # print ("a:",    a)
                # print ("b:",    b)
                strategy_points = float(a/b)
                #print("Type Strategy points: ", type(strategy_points))
        else:
            valid_turn = 0
        
        observation = self.regions + [valid_turn, self.turn, self.points]
        assert (self.observation_space.contains(observation))
        return observation, reward, done, {'strategy_points': strategy_points}

    def reset(self):
        
        self.regions = [
            1,  #0 Sanierung
            12, #1 Produktion
            4,  #2 Aufklärung
            10, #3 Lebensqualität
            20, #4 Vermehrungsrate
            
            13, #5 Umweltbelastung 
            21, #6 Bevölkerung
            11  #7 Politik 
        ]
        
        self.turn = 0
        self.points = 8
        
        return self.regions + [1, self.turn, self.points]

