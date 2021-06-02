def get_box1_and_box2_from_region0 (region0):
    # if region0 not in (1,30): return 0,0
    # print (region0)

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
    elif region2  < 24: box9 = extra_points
    elif region2  < 28: box9 = extra_points
    elif region2  < 30: box9 = extra_points

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
    if   region7 == -10: boxB = -5
    elif region7 ==  -9: boxB = -2
    elif region7  <  -2: boxB = -1
    elif region7  <   8: boxB = 0
    elif region7  <  22: boxB = 1
    elif region7  <  31: boxB = 2 
    elif region7 <=  37: boxB = 3
    
    return boxB
