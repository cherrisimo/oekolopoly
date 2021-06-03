import gym
import numpy as np
env = gym.make('oekolopoly:Oekolopoly-v0')
print("Reset: ", env.reset())
print()

instructions = (
    ('reset', "Assert Test"),
    ('step' , (1,  2,  3,  2,  0,  0)),
    ('step' , (40,  0,  0,  0,  0,  0)),
    ('step' , (3,  2,  2,  2,  0,  0)),

    ('reset', "Invalid Turn Test"),
    ('step' , (20,  0,  0,  0,  0,  0)),
    ('step' , (0,  0,  0,  0,  0,  0)),

    ('reset', "Extra Points Test (0)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  0)),

    ('reset', "Extra Points Test (4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  5)),

    ('reset', "Extra Points Test (5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0,  5)),

    ('reset', "Extra Points Test (-4)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -5)),

    ('reset', "Extra Points Test (-5)", (1, 12, 26,  10, 20, 13, 21, 0, 1, 0, 8)),
    ('step' , (0,  0,  0,  0,  0, -5)),

    ('reset', "Complete game test"),
    ('step' , (1,  2,  3,  2,  0,  0)),
    ('step' , (3,  2,  2,  2,  0,  0)),
    ('step' , (0, -4,  3,  3,  0,  0)),
    ('step' , (0,  0,  0,  4,  0,  0)),
    ('step' , (0,  0,  0,  4,  0,  0)),
    ('step' , (0,  0,  0,  8,  0,  0)),
    ('step' , (0,  0,  0,  5,  0,  0)),
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
                print ("Step: Round {} \n"
                       "    Action: {}\n"
                       "    A:      {}\n"
                       "    V:      {}\n"
                       "    obs:    {}\n"
                       "    reward: {}\n"
                       "    done:   {}\n"
                       "    info:   {}".format (env.V[env.ROUND], action, a, tuple(env.V), obs, reward, done, info))
            except ValueError as e:
                print ("Step: ValueError ({})".format (str(e)))
                print ("    Action:", action)
                print ("    A:     ", a)
                print ("    V:     ", tuple (env.V))
            except AssertionError as e:
                print ("Step: AssertionError ({})". format (str(e)))
                print ("    Action:", action)
                print ("    A:     ", a)
                print ("    V:     ", tuple (env.V))

                
    elif cmd == 'exit':
        print ("Exit")
        break
