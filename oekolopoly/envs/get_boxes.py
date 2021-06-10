def get_box1 (sanierung):

    #Box 1 Sanierung-Umweltbelastung 0-5
    if   sanierung  <  2: box1 =  0
    elif sanierung  <  8: box1 = -1
    elif sanierung  < 13: box1 = -2
    elif sanierung  < 18: box1 = -3
    elif sanierung  < 21: box1 = -4
    elif sanierung  < 24: box1 = -5
    elif sanierung  < 26: box1 = -6
    elif sanierung  < 28: box1 = -7
    elif sanierung == 28: box1 = -8
    elif sanierung == 29: box1 = -9

    return box1


def get_box2 (sanierung):
     
    #Box 2 Sanierung-Sanierung 0-0
    if   sanierung  < 22: box2 =  0
    elif sanierung  < 24: box2 = -1
    elif sanierung  < 26: box2 = -2
    elif sanierung == 26: box2 = -3
    elif sanierung == 27: box2 = -4
    elif sanierung == 28: box2 = -5
    elif sanierung == 29: box2 = -6

    return box2


def get_box3 (produktion):
    
    #Box 3 Produktion-Produktion 4-4
    if   produktion  <  7:                       box3 = 0
    elif produktion  <  22 or produktion  == 29: box3 = 1
    elif produktion  < 29:                       box3 = 2
            
    return box3


def get_box4 (produktion):

    #Box 4 Produktion-Umweltbelasanierungtung 4-5
    if   produktion  <  5: box4 = 0
    elif produktion  <  9: box4 = 1
    elif produktion  < 13: box4 = 2
    elif produktion  < 15: box4 = 3
    elif produktion  < 17: box4 = 4
    elif produktion  < 19: box4 = 5
    elif produktion  < 21: box4 = 6
    elif produktion  < 23: box4 = 7
    elif produktion == 23: box4 = 8
    elif produktion == 24: box4 = 9
    elif produktion == 25: box4 = 10
    elif produktion == 26: box4 = 12
    elif produktion == 27: box4 = 14
    elif produktion == 28: box4 = 18
    elif produktion == 29: box4 = 22
            
    return box4


def get_boxC (produktion):

    #Box C Produktion-Aktionspunkte 4-A
    if   produktion  == 1: boxC = -4
    elif produktion  == 2: boxC = -3
    elif produktion  == 3: boxC = -2
    elif produktion  == 4: boxC = -1
    elif produktion  == 5: boxC = 0
    elif produktion  < 8:  boxC = 2 
    elif produktion  < 11: boxC = 3
    elif produktion  < 14: boxC = 4
    elif produktion  < 17: boxC = 5
    elif produktion  < 20: boxC = 6
    elif produktion  < 22: boxC = 7
    elif produktion  < 24: boxC = 8
    elif produktion  < 26: boxC = 9
    elif produktion == 26: boxC = 10
    elif produktion == 27: boxC = 11
    elif produktion == 28: boxC = 12
    elif produktion == 29: boxC = 0
            
    return boxC


def get_boxV (produktion):

    #Box V Multiplier Produktion-Aktionspunkte 4-A
    if   produktion  == 1: boxV = -4
    elif produktion  == 2: boxV = -3
    elif produktion  < 5:  boxV = -2
    elif produktion  < 7:  boxV = -1
    elif produktion  < 9:  boxV = 0
    elif produktion <= 29: boxV = 1
            
    return boxV


def get_box5 (umweltbelastung):
    
    #Box 5 Umweltbelastung-Umweltbelastung 5-5
    if   umweltbelastung  <  4 or umweltbelastung == 28 or umweltbelastung == 29: box5 =  0
    elif umweltbelastung  < 14 or umweltbelastung == 27:                          box5 = -1
    elif umweltbelastung  < 20 or umweltbelastung == 26:                          box5 = -2
    elif umweltbelastung == 24:                                                   box5 = -4
    elif umweltbelastung  < 24 or umweltbelastung == 25:                          box5 = -3

    return box5


def get_box6 (umweltbelastung):
    
    #Box 6 Umweltbelastung-Lebensqualität 5-2
    if   umweltbelastung  <  8: box6 =  0
    elif umweltbelastung  < 11: box6 = -1
    elif umweltbelastung  < 15: box6 = -2
    elif umweltbelastung  < 18: box6 = -3
    elif umweltbelastung  < 20: box6 = -4
    elif umweltbelastung  < 22: box6 = -5
    elif umweltbelastung == 22: box6 = -6
    elif umweltbelastung == 23: box6 = -7
    elif umweltbelastung == 24: box6 = -8
    elif umweltbelastung == 25: box6 = -10
    elif umweltbelastung == 26: box6 = -12
    elif umweltbelastung == 27: box6 = -14
    elif umweltbelastung == 28: box6 = -18
    elif umweltbelastung == 29: box6 = -25

    return box6


def get_box7 (aufklaerung):
    
    #Box 7 Aufklärung-Aufklärung 1-1
    if   aufklaerung  <  3 or aufklaerung in range(6, 15) or aufklaerung == 29: box7 = 0
    elif aufklaerung  <  6:                                                     box7 = -1
    elif aufklaerung  < 21 or aufklaerung in range(24, 29):                     box7 = 1
    elif aufklaerung in range(21, 24):                                          box7 = 2

    return box7


def get_box8 (aufklaerung):

    #Box 8 Aufklärung-Lebensqualität 1-2
    if   aufklaerung  <  6: box8 = -2
    elif aufklaerung  < 10: box8 = -1
    elif aufklaerung == 10: box8 = 0
    elif aufklaerung  < 14: box8 = 1
    elif aufklaerung  < 18: box8 = 2
    elif aufklaerung  < 22: box8 = 3
    elif aufklaerung  < 26: box8 = 4
    elif aufklaerung  < 28: box8 = 5
    elif aufklaerung <= 29: box8 = 6

    return box8


def get_box9 (aufklaerung, extra_points):
    
    #Box 9 Aufklärung-Vermehrungsrate 1-3
    if   aufklaerung == 1:  box9 = 1
    elif aufklaerung  < 10: box9 = 0
    elif aufklaerung  < 14: box9 = 1
    elif aufklaerung  < 19: box9 = 2
    elif aufklaerung  < 21: box9 = 3
    elif aufklaerung  < 24: box9 = extra_points
    elif aufklaerung  < 28: box9 = extra_points
    elif aufklaerung <= 29: box9 = extra_points

    return box9


def get_box10 (lebensqualitaet):
    
    #Box 10 Lebensqualität-Lebensqualität 2-2
    if   lebensqualitaet == 1 or lebensqualitaet  in range(4,10) or lebensqualitaet  in range(16,18) or lebensqualitaet  == 29: box10 = 0
    elif lebensqualitaet  < 4 or lebensqualitaet  in range(10,13) or lebensqualitaet in range(14,16):                           box10 = 1
    elif lebensqualitaet == 13:                                                                                                 box10 = 2
    elif lebensqualitaet  in range(18,23) or lebensqualitaet  in range(26,29):                                                  box10 = -1
    elif lebensqualitaet  in range(23,26):                                                                                      box10 = -2

    return box10


def get_box11 (lebensqualitaet):

    #Box 11 Lebensqualität-Vermehrungsrate 2-3
    if   lebensqualitaet  == 1: box11 = -15
    elif lebensqualitaet  == 2: box11 = -8
    elif lebensqualitaet  == 3: box11 = -6
    elif lebensqualitaet  == 4: box11 = -4
    elif lebensqualitaet  == 5: box11 = -3
    elif lebensqualitaet  == 6: box11 = -2
    elif lebensqualitaet  == 7: box11 = -1
    elif lebensqualitaet  == 8: box11 = 0
    elif lebensqualitaet  == 9: box11 = 1
    elif lebensqualitaet  < 13: box11 = 2
    elif lebensqualitaet  < 21: box11 = 1
    elif lebensqualitaet <= 29: box11 = 0

    return box11


def get_box12 (lebensqualitaet):

    #Box 12 Lebensqualität-Politik 2-7
    if   lebensqualitaet == 1: box12 = -10
    elif lebensqualitaet == 2: box12 = -8
    elif lebensqualitaet == 3: box12 = -6
    elif lebensqualitaet == 4: box12 = -3
    elif lebensqualitaet == 5: box12 = -2
    elif lebensqualitaet < 10: box12 = -1
    elif lebensqualitaet < 12: box12 = 0
    elif lebensqualitaet < 21: box12 = 1
    elif lebensqualitaet < 24: box12 = 2
    elif lebensqualitaet < 27: box12 = 3
    elif lebensqualitaet < 29: box12 = 4
    elif lebensqualitaet == 29: box12 = 5

    return box12


def get_boxD (lebensqualitaet):
    
    #Box D Lebensqualität-Aktionspunkte 2-A
    if   lebensqualitaet  == 1: boxD = -6
    elif lebensqualitaet  == 2: boxD = -4
    elif lebensqualitaet  == 3: boxD = -2
    elif lebensqualitaet  < 6:  boxD = 0
    elif lebensqualitaet  < 9:  boxD = 1
    elif lebensqualitaet  < 18: boxD = 2 
    elif lebensqualitaet  < 23: boxD = 3
    elif lebensqualitaet  < 27: boxD = 4
    elif lebensqualitaet <= 29: boxD = 5

    return boxD


def get_box13 (vermehrungsrate):
    
    #Box 13 Vermehrungsrate-Bevölkerung 3-6
    if   vermehrungsrate  <  3: box13 = -4
    elif vermehrungsrate  <  6: box13 = -3
    elif vermehrungsrate  < 10: box13 = -2
    elif vermehrungsrate  < 15: box13 = -1
    elif vermehrungsrate == 15: box13 = 0
    elif vermehrungsrate  < 21: box13 = 1
    elif vermehrungsrate  < 26: box13 = 2
    elif vermehrungsrate <= 29: box13 = 3

    return box13
            

def get_box14 (bevoelkerung):
    
    #Box 14 Bevölkerung-Lebensqualität 6-2
    if   bevoelkerung  < 16: box14 = 0
    elif bevoelkerung  < 26: box14 = -1
    elif bevoelkerung  < 31: box14 = -2
    elif bevoelkerung  < 39: box14 = -3
    elif bevoelkerung  < 43: box14 = -4
    elif bevoelkerung  < 45: box14 = -5 
    elif bevoelkerung == 45: box14 = -6
    elif bevoelkerung == 46: box14 = -7
    elif bevoelkerung == 47: box14 = -8
    elif bevoelkerung == 48: box14 = -10

    return box14


def get_boxA (bevoelkerung):

    #Box A Bevölkerung-Aktionspunkte 6
    if   bevoelkerung  < 10: boxA = 0
    elif bevoelkerung  < 17: boxA = 1
    elif bevoelkerung  < 22: boxA = 2
    elif bevoelkerung  < 26: boxA = 3
    elif bevoelkerung  < 30: boxA = 4
    elif bevoelkerung  < 34: boxA = 5 
    elif bevoelkerung  < 38: boxA = 6
    elif bevoelkerung  < 42: boxA = 7
    elif bevoelkerung  < 46: boxA = 8
    elif bevoelkerung <= 48: boxA = 9

    return boxA


def get_boxW (bevoelkerung):
            
    #Box W Multiplier Bevölkerung-Bevölkerung 6-6
    if   bevoelkerung == 1:   boxW = 0
    elif bevoelkerung  < 15:  boxW = 1
    elif bevoelkerung  < 36:  boxW = 2
    elif bevoelkerung <= 48:  boxW = 3

    return boxW
       

def get_boxB (politik):

    #Box B Politik-Aktionspunkte 7-A
    if   politik == -10: boxB = -5
    elif politik ==  -9: boxB = -2
    elif politik  <  -2: boxB = -1
    elif politik  <   8: boxB = 0
    elif politik  <  22: boxB = 1
    elif politik  <  31: boxB = 2 
    elif politik <=  37: boxB = 3
    
    return boxB
