import gym
import numpy as np

env = gym.make('oekolopoly:Oekolopoly-v0')
env.reset ()

print("Reset: ", env.reset())
print()

instructions = (    
    ('reset', "10 Rounds Game Test"),
    
    #          S    Pr   A    L    V    A>V
    ('step' , [0,   0,   0,   8,   0,   0]),   # 1
    ('check_v', [ 1, 13, 3, 14, 21, 14, 25, 1, 1, 1, 9] ,    'nonfatal'),
    
    ('step' , [0,   0,   9,   0,   0,   0]),   # 2
    ('check_v', [ 1, 14, 12, 11, 23, 15, 29, 2, 1, 2, 11] ,  'nonfatal'),
    
    ('step' , [0,   0,   11,  0,   0,  -4]),   # 3 
    ('check_v', [ 1, 15, 25, 10, 20, 17, 31, 3, 1, 3, 12] ,  'nonfatal'),
    
    ('step' , [0,  -6,   0,   6,   0,  -4]),   # 4
    ('check_v', [ 1, 10, 26, 14, 17, 17, 33, 4, 1, 4, 10] ,  'nonfatal'),
    
    ('step' , [0,  -2,   2,   6,   0,  -5]),   # 5
    ('check_v', [ 1, 9, 29, 18, 12, 17, 31, 6, 1, 5, 11] ,   'nonfatal'),
   
    ('step' , [9,   2,   0,   0,   0,   0]),   # 6
    ('check_v', [ 10, 12, 29, 18, 13, 15, 29, 7, 1, 6, 11] , 'nonfatal'),
    
    ('step' , [8,   2,   0,   0,   0,   0]),   # 7
    ('check_v', [ 18, 15, 29, 19, 13, 13, 27, 9, 1, 7, 14] , 'nonfatal'),
    
    ('step' , [3,   2,   0,   0,   2,   0]),   # 8
    ('check_v', [ 21, 18, 29, 19, 15, 12, 27, 11, 1, 8, 21] , 'nonfatal'),
    
    ('step' , [2,  -5,   0,   0,   5,  -5]),   # 9
    ('check_v', [ 22, 14, 29, 20, 15, 9, 27, 13, 1, 9, 22] ,  'nonfatal'),
    
    ('step' , [3,  -5,   0,   0,   5,  -5]),   # 10
    ('check_v', [ 23, 10, 29, 23, 15, 4, 27, 16, 1, 10, 21] , 'nonfatal'),
    
    ('step' , [2,   5,   0,   0,   0,  -2]),   # 11
    ('check_v', [ 25, 15, 29, 23, 15, 1, 27, 16, 1, 11, 0] ,  'nonfatal'),


    # Test if given value is out ouf bounds 
    ('reset', "AssertionError Test"),
    ('step' , [1,  2,  3,  2,  0,  0]),
    ('step' , [40,  0,  0,  0,  0, 0]),
    ('step' , [3,  2,  2,  2,  0,  0]),

    ('reset', "ValueError Test"),
    ('step' , [20,  0,  0,  0,  0,  0]),
    ('step' , [0,  0,  0,  0,  0,  0]),


    # Test of special case Aufklärung - Fenster 9 - Vermehrungsrate
    # If max 4 points are allowed but 5 are given, 4 points are added to the region
    ('reset', "Extra Points Test (0)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0,  0]),
    ('check_v', [ 1, 13, 27, 14, 21, 14, 25, 1, 1, 1, 17] , 'nonfatal'),

    ('reset', "Extra Points Test (4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0,  4]),
    ('check_v', [ 1, 13, 27, 13, 26, 14, 27, 1, 1, 1, 17] , 'nonfatal'),
    

    ('reset', "Extra Points Test (5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0,  5]),
    # same
    ('check_v', [ 1, 13, 27, 13, 26, 14, 27, 1, 1, 1, 17] , 'nonfatal'),
    

    ('reset', "Extra Points Test (-4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0, -4]),
    ('check_v', [ 1, 13, 27, 14, 17, 14, 23, 1, 1, 1, 17] , 'nonfatal'),
    

    ('reset', "Extra Points Test (-5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0, -5]),
    #same 
    ('check_v', [ 1, 13, 27, 14, 17, 14, 23, 1, 1, 1, 17] , 'nonfatal'),
    
    # Test with check_v. Intentionally put wrong value of action points in check_v to
    # activate the check.
    ('reset', "Extra Points Test (-5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0, -5]),
    ('check_v', [ 1, 13, 27, 14, 17, 14, 23, 1, 1, 1, 9] , 'nonfatal'),
    
    ('reset', "Extra Points Test (-2)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , [0,  0,  0,  0,  0, -2]),
    ('check_v', [ 1, 13, 27, 14, 19, 14, 23, 1, 1, 1, 17] , 'nonfatal'),
    
    
    ('reset', "Zero Test"),
    ('step' , [0,  0,  0,  0,  0,  0]),
    ('check_v', [ 1, 13, 3, 5, 18, 14, 23, -1, 1, 1, 15] , 'nonfatal'),
    
    ('step' , [0,  0,  0,  0,  0,  0]),
    ('check_v', [ 1, 14, 2, 1, 18, 15, 23, -1, 1, 2, 0] , 'nonfatal'),
    
    # Test to see if it runs step() one more time even if game has ended
    ('step' , [0,  0,  0,  0,  0,  0]),    
)

done = False

for instruction in instructions:
    # print (instruction)
    cmd = instruction[0]

    if cmd == 'reset':
        if len (instruction) > 1:
            title = instruction[1]
        else:
            title = ""

        print ("\n====================== {:^24s} ======================\n".format (title))
        done = False
        env.reset ()

        # Check for non-default initial values to set after the reset is done.
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

    elif cmd == 'check_v':
        expected_v = np.array (instruction[1])
        if not np.array_equal (expected_v, env.V):
            print ()
            print ("ERROR: Unexpected env.V:")
            print ("  Expected:", expected_v)
            print ("  But V is:", env.V)
            print ()
            fatal_error = True
            if len (instruction) > 2 and instruction[2] == 'nonfatal':
                fatal_error = False
            if fatal_error:
                print ("Stopping tests due to FATAL ERROR!")
                break
            

    elif cmd == 'exit':
        print ("Exit")
        break
 
