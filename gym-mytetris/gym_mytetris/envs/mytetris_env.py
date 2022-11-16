import gym
import random
from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT

# initial state dimensions: 240X256X3
# custom state dimensions: 20X10

class MyTetrisEnv(gym.Env):
    env = None
    action_space = None
    state = [0]*200
    def __init__(self):
        self.env = gym_tetris.make('TetrisA-v1')
        self.env = JoypadSpace(self.env, MOVEMENT)
        self.state = self.get_new_state(self.env.reset())
        self.action_space = self.env.action_space
        
    def step(self, action):
        if action < 0 or action > 11:
            print("Invalid action")
            exit(1)
        reward = 0
        state, r, done, info = self.env.step(action)
        reward+=r
        if not done:
            state, r, done, info = self.env.step(9)
            reward+=r
        state = self.get_new_state(state)
        self.state = state
        return state, reward, done, info
    def get_new_state(self,state):
        l = []
        for i in range(20):
            for j in range(10):
                flag = False
                for k in range(47+i*8,47+(i+1)*8):
                    if flag:
                        break
                    for z in range(95+j*8,95+(j+1)*8):
                        if state[k][z][0] != 0 or state[k][z][1] != 0 or state[k][z][2] != 0:
                            l.append(1)
                            flag = True
                            break
                if not flag:
                    l.append(0)
        return l    
    def print_local(self, state):
        for i in range(20):
            for j in range(10):
                print(state[i*10+j],end='')
            print('')
    def reset(self):
        state = self.env.reset()
        state = self.get_new_state(state)
        self.state = state
        return state
    def render_local(self):
        self.env.render()
    def close(self):
        self.env.close()
    def sample(self):
        return self.env.action_space.sample()
