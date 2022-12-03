import gym
import random
import time
import pyllab
env = gym.make('gym_mytetris:mytetris-v0')
state = env.reset()
done = False
maximum = 500
def print_state(state):
    for i in range(20):
        for j in range(10):
            print(state[i*10+j],end='')
        print(" ")
for j in range(1,maximum):
    state = env.reset()
    g = pyllab.Genome(str(j)+'.bin',200,4)
    done = False
    while not done:
        output = g.ff(state)
        index = -1
        maximum = -1
        
        for k in range(4):
            if output[k] > maximum:
                maximum = output[k]
                index = k
        state, reward, done, info = env.step(index)
        print_state(state)
        print(" ")
        env.render_local()
    time.sleep(1)
env.close()
