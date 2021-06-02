import oekolopoly.envs.get_box_methods as gb
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

    def __init__(self):
        #                      0   1   2   3   4   5   6    7   8   9  10
        #                      S   P   A   L   V   U   B    P  VT   R  PO
        self.Vmin = np.array([ 1,  1,  1,  1,  1,  1,  1, -10,  0,  0,  0])
        self.Vmax = np.array([29, 29, 29, 29, 29, 29, 48,  37,  1, 30, 36])

        self.Amin = np.array([ 0,-28,  0,  0,  0, -5])
        self.Amax = np.array([28, 28, 28, 28, 28,  5])

        self.action_space = spaces.Tuple((
            spaces.Discrete(29),   # 0 Sanierung
            spaces.Discrete(57),   # 1 Produktion
            spaces.Discrete(29),   # 2 Aufklärung
            spaces.Discrete(29),   # 3 Lebensqualität
            spaces.Discrete(29),   # 4 Vermehrungsrate
            spaces.Discrete(11)))  # 5 box9 extra_points
        
        self.observation_space = spaces.Tuple((
            spaces.Discrete(29),    # 0 Sanierung 
            spaces.Discrete(29),    # 1 Produktion
            spaces.Discrete(29),    # 2 Aufklärung
            spaces.Discrete(29),    # 3 Lebensqualität
            spaces.Discrete(29),    # 4 Vermehrungsrate
            
            spaces.Discrete(29),    # 5 Umweltbelastung
            spaces.Discrete(48),    # 6 Bevölkerung
            spaces.Discrete(48),    # 7 Politik

            spaces.Discrete(2),     # 8 valid turn: 1 - valid, 0 - not valid
            spaces.Discrete(31),    # 9 round
            spaces.Discrete(37)))   # 10 points
    
    def step(self, action):
        assert (self.action_space.contains(action))

        #print ("action_space:", action)
        action = list(action)
        action[self.PRODUKTION] += self.Amin[self.PRODUKTION]
        action[5] += self.Amin[5]
        extra_points = action[5]
        #print ("game_space  :", action)

        done = False
        self.V[self.VALID_TURN] = 1
        strategy_points = 0
        self.reward = 0

        used_points = 0
        used_points += action[self.SANIERUNG]
        used_points += abs(action[self.PRODUKTION])
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

            #Update boxes

            box1, box2                = gb.get_box1_and_box2_from_region0              (self.V[self.SANIERUNG])
            #print("Box 1:", box1)
            #print("Box 2:", box2)
            
            box3, box4, boxC, boxV    = gb.get_box3_box4_boxC_and_boxV_from_region1    (self.V[self.PRODUKTION])
            #print("Box 3:", box3)
            #print("Box 4:", box4)
            #print("Box C:", boxC)
            #print("Box V:", boxV)

            box5, box6                = gb.get_box5_and_box6_from_region5              (self.V[self.UMWELTBELASTUNG])
            #print("Box 5:", box5)
            #print("Box 6:", box6)
            
            box7, box8, box9          = gb.get_box7_box8_and_box9_from_region2         (self.V[self.AUFKLAERUNG], -5)
            #print("Box 7:", box7)
            #print("Box 8:", box8)
            #print("Box 9:", box9)
            
            box10, box11, box12, boxD = gb.get_box10_box11_box12_and_boxD_from_region3 (self.V[self.LEBENSQUALITAET])
            #print("Box 10:", box10)
            #print("Box 11:", box11)
            #print("Box 12:", box12)
            #print("Box D:", boxD)
            
            box13                     = gb.get_box13_from_region4                      (self.V[self.VERMEHRUNGSRATE])
            #print("Box 13:", box13)
            
            box14, boxA, boxW         = gb.get_box14_boxA_and_boxW_from_region6        (self.V[self.BEVOELKERUNG])
            #print("Box 14:", box14)
            #print("Box A:", boxA)
            #print("Box W:", boxW)
            
            boxB                      = gb.get_boxB_from_region7                       (self.V[self.POLITIK])
            #print("Box B:", boxB)

            #Update V and boxes
            self.V[self.UMWELTBELASTUNG] += box1
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = gb.get_box5_and_box6_from_region5              (self.V[self.UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.V[self.UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.V[self.SANIERUNG] += box2
            if self.V[self.SANIERUNG] not in range (1, 30): done = True
            if not done:
                box1, box2                = gb.get_box1_and_box2_from_region0              (self.V[self.SANIERUNG])
                #print("SANIERUNG: ", self.V[self.SANIERUNG])
                #print("Box 1:", box1)
                #print("Box 2:", box2)
            
            self.V[self.PRODUKTION] += box3
            if self.V[self.PRODUKTION] not in range (1, 30): done = True
            if not done:
                box3, box4, boxC, boxV    = gb.get_box3_box4_boxC_and_boxV_from_region1    (self.V[self.PRODUKTION])
                #print("PRODUKTION: ", self.V[self.PRODUKTION])
                #print("Box 3:", box3)
                #print("Box 4:", box4)
                #print("Box C:", boxC)
                #print("Box V:", boxV)
            
            self.V[self.UMWELTBELASTUNG] += box4
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = gb.get_box5_and_box6_from_region5              (self.V[self.UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.V[self.UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.V[self.UMWELTBELASTUNG] += box5
            if self.V[self.UMWELTBELASTUNG] not in range (1, 30): done = True
            if not done:
                box5, box6                = gb.get_box5_and_box6_from_region5              (self.V[self.UMWELTBELASTUNG])
                #print("UMWELTBELASTUNG: ", self.V[self.UMWELTBELASTUNG])
                #print("Box 5:", box5)
                #print("Box 6:", box6)
            
            self.V[self.LEBENSQUALITAET]  += box6
            if self.V[self.LEBENSQUALITAET] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = gb.get_box10_box11_box12_and_boxD_from_region3 (self.V[self.LEBENSQUALITAET])
                #print("Lebensqualität: ", self.V[self.LEBENSQUALITAET])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)
            
            self.V[self.AUFKLAERUNG] += box7
            if self.V[self.AUFKLAERUNG] not in range (1, 30): done = True
            if not done:
                if self.V[self.AUFKLAERUNG] in range (21, 24): extra_points = max (-3, min (3, extra_points))
                if self.V[self.AUFKLAERUNG] in range (24, 28): extra_points = max (-4, min (4, extra_points))
                if self.V[self.AUFKLAERUNG] in range (28, 30): extra_points = max (-5, min (5, extra_points))
                if self.V[self.AUFKLAERUNG] < 21: extra_points = 0

                box7, box8, box9 = gb.get_box7_box8_and_box9_from_region2 (self.V[self.AUFKLAERUNG], extra_points)
                #print("Aufklärung: ", self.V[self.AUFKLAERUNG])
                #print("Box 7:", box7)
                #print("Box 8:", box8)
                #print("Box 9:", box9)
            
            self.V[self.LEBENSQUALITAET]  += box8
            if self.V[self.LEBENSQUALITAET] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = gb.get_box10_box11_box12_and_boxD_from_region3 (self.V[self.LEBENSQUALITAET])
                #print("Lebensqualität: ", self.V[self.LEBENSQUALITAET])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)

            self.V[self.VERMEHRUNGSRATE] += box9
            if self.V[self.VERMEHRUNGSRATE] not in range (1, 30): done = True
            if not done:
                box13 = gb.get_box13_from_region4 (self.V[self.VERMEHRUNGSRATE])
                #print("VERMEHRUNGSRATE: ", self.V[self.VERMEHRUNGSRATE])
                #print("Box 13:", box13)
            
            self.V[self.LEBENSQUALITAET]  += box10
            if self.V[self.LEBENSQUALITAET] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = gb.get_box10_box11_box12_and_boxD_from_region3 (self.V[self.LEBENSQUALITAET])
                #print("Lebensqualität: ", self.V[self.LEBENSQUALITAET])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)

            self.V[self.VERMEHRUNGSRATE] += box11
            if self.V[self.VERMEHRUNGSRATE] not in range (1, 30): done = True
            if not done:
                box13 = gb.get_box13_from_region4 (self.V[self.VERMEHRUNGSRATE])
                #print("VERMEHRUNGSRATE: ", self.V[self.VERMEHRUNGSRATE])
                #print("Box 13:", box13)

            #prev_politik = self.V[self.POLITIK]
            self.V[self.POLITIK] += box12
            if self.V[self.POLITIK] not in range (-10, 38): done = True
            if not done:
                boxB = gb.get_boxB_from_region7 (self.V[self.POLITIK])
                #print("U POLITIK: ", self.V[self.POLITIK])
                #print("Box B:", boxB)
            
            self.V[self.BEVOELKERUNG] += box13 * boxW
            if self.V[self.BEVOELKERUNG] not in range (1, 49): done = True
            if not done:
                box14, boxA, boxW = gb.get_box14_boxA_and_boxW_from_region6 (self.V[self.BEVOELKERUNG])
                #print("U Bevölkerung: ", self.V[self.BEVOELKERUNG])
                #print("Box 14:", box14)
                #print("Box A:", boxA)
                #print("Box W:", boxW)
            
            self.V[self.LEBENSQUALITAET] += box14
            #prev_boxD = boxD
            if self.V[self.LEBENSQUALITAET] not in range (1, 30): done = True
            if not done:
                box10, box11, box12, boxD = gb.get_box10_box11_box12_and_boxD_from_region3 (self.V[self.LEBENSQUALITAET])
                #print("U Lebensqualität: ", self.V[self.LEBENSQUALITAET])
                #print("Box 10:", box10)
                #print("Box 11:", box11)
                #print("Box 12:", box12)
                #print("Box D:", boxD)

            self.V[self.POINTS] -= used_points            
            self.V[self.ROUND] += 1

            print("\n############################# ROUND %d #############################" %self.V[self.ROUND])
            print("Points avilable at the beginning: ", self.V[self.POINTS])
            print("Points left: ", self.V[self.POINTS])
            #print("Round: %d ;" %self.V[self.ROUND], "Points left: %d" %self.V[self.POINTS])

            #Points for next round
            
            
            self.V[self.POINTS] += boxA * boxV
            self.V[self.POINTS] += boxB
            self.V[self.POINTS] += boxC
            self.V[self.POINTS] += boxD
            

            if self.V[self.POINTS] <  0: self.V[self.POINTS] = 0
            if self.V[self.POINTS] > 36: self.V[self.POINTS] = 36

            for i in range(8):
                if self.V[i] not in range (self.Vmin[i], self.Vmax[i] + 1):
                    self.V[i] = max(self.Vmin[i], min(self.Vmax[i], self.V[i]))
                    done = True

            if self.V[self.ROUND] == 30: done = True

            #if done and self.V[self.ROUND] < 10: done = False

            if done:
                boxD = max(-6, min(5, boxD))
                a = float(abs((boxD*3) + self.V[self.POLITIK])*10)
                b = float(self.V[self.ROUND] + 3)

                # a = float(abs((prev_boxD*3) + prev_politik)*10)
                # print ("prev_boxD:",    prev_boxD)
                # print ("prev_POLITIK:", prev_politik)
                # print ("a:",    a)
                # print ("b:",    b)
                strategy_points = float(a/b)
                self.reward = strategy_points
                #print("Type Strategy points: ", type(strategy_points))
        else:
            self.V[self.VALID_TURN] = 0

        self.obs = list(self.V - self.Vmin)
        assert (self.observation_space.contains(self.obs))
        return self.obs, self.reward, done, {'strategy_points': strategy_points}


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
        
        return self.V
    
    if __name__ == '__main__':
        env = OekoEnv()
        print("Reset: ", env.reset())
        print("Step 1:  ", env.step((1,   #0 Sanierung
                                 1  +28,   #1 Produktion
                                 1,   #2 Aufklärung
                                 1,   #3 Lebensqualität
                                 1,   #4 Vermehrungsrate
                                 0  +5   ))) #box9 special case
