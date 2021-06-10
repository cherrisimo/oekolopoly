import gym
import numpy as np
env = gym.make('oekolopoly:Oekolopoly-v0')
print("Reset: ", env.reset())
print()

instructions = (
    
    ('reset', "10 Rounds Game Test"),
    #          S    Pr   A    L    V    A>V
    ('step' , (0,   0,   0,   8,   0,   0)),   # 1
    ('step' , (0,   0,   9,   0,   0,   0)),   # 2
    ('step' , (0,   0,   11,  0,   0,  -4)),   # 3
    ('step' , (0,  -6,   0,   6,   0,  -4)),   # 4
    ('step' , (0,  -2,   2,   6,   0,  -5)),   # 5
    ('step' , (9,   2,   0,   0,   0,   0)),   # 6
    ('step' , (8,   2,   0,   0,   0,   0)),   # 7
    ('step' , (3,   2,   0,   0,   2,   0)),   # 8
    ('step' , (2,  -5,  0,    0,   5,  -5)),   # 9
    ('step' , (3,  -5,  0,    0,   5,  -5)),   # 10
    ('step' , (2,   5,  0,    0,   0,  -2)),   # 11

    
    # Test if given value is out ouf bounds 
    ('reset', "AssertionError Test"),
    ('step' , (1,  2,  3,  2,  0,  0)),
    ('step' , (40,  0,  0,  0,  0, 0)),
    ('step' , (3,  2,  2,  2,  0,  0)),

    ('reset', "ValueError Test"),
    ('step' , (20,  0,  0,  0,  0,  0)),
    ('step' , (0,  0,  0,  0,  0,  0)),


    # Test of special case Aufklärung - Fenster 9 - Vermehrungsrate
    # If max 4 points are allowed but 5 are given, 4 points are added to the region
    ('reset', "Extra Points Test (0)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  0)),

    ('reset', "Extra Points Test (4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  4)),

    ('reset', "Extra Points Test (5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  5)),

    ('reset', "Extra Points Test (-4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -4)),

    ('reset', "Extra Points Test (-5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -5)),
    
    ('reset', "Extra Points Test (-2)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -2)),
    
    ('reset', "Extra Points Test (3)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -2)),


    # ('reset', "Zero Test"),
    # ('step' , (0,  0,  0,  0,  0,  0)),
    # ('step' , (0,  0,  0,  0,  0,  0)),
    # ('step' , (0,  0,  0,  0,  0,  0)),

    
)

done = False

for instruction in instructions:
    # print (instruction)
    cmd = instruction[0]

    if cmd == 'reset':
        title = ""
        if len (instruction) > 1: title = instruction[1]
        print ("\n====================== {:^24s} ======================\n".format (title))
        done = False
        env.reset ()
        if len (instruction) > 2:
            v = instruction[2]
            env.V = np.array (v)
        print ("Reset:", tuple (env.V))
    elif cmd == 'step':
        if done:
            print ("Step: Done - Can't step any more.")
        else:
            action = instruction[1]
            a = list (action)
            a[env.PRODUKTION] -= env.Amin[env.PRODUKTION]
            a[5] -= env.Amin[5]
            try:
                obs, reward, done, info = env.step (a)
                print ("\nStep: Round {} \n"
                       "    Action: {}\n"
                       "    V:      {}\n"
                       "    reward: {}\n"
                       "    info:   {}".format (env.V[env.ROUND], action, tuple(env.V), reward, info))
            except ValueError as e:
                print ("Step: ValueError ({})".format (str(e)))
                print ("    Action:", action)
                #print ("    A:     ", a)
                print ("    V:     ", tuple (env.V))
            except AssertionError as e:
                print ("Step: AssertionError ({})". format (str(e)))
                print ("    Action:", action)
                #print ("    A:     ", a)
                print ("    V:     ", tuple (env.V))

                
    elif cmd == 'exit':
        print ("Exit")
        break
