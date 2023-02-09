import gym
import pyllab

env = gym.make('gym_mytetris:mytetris-v0')
models = 1000
games = 20
steps = 500

def print_state(state):
    for i in range(20):
        for j in range(10):
            if state[i*10+j] == -1:
                print("7", end='')
            else:
                print(state[i*10+j],end='')
        print('')
    print('')

for i in range(33,models):
    print("model number: "+str(i))
    g = pyllab.Genome(str(i)+'.bin',200,4)
    total_reward = 0
    for j in range(games):
        state = env.reset()
        for k in range(steps):
            output = g.ff(state).tolist()
            max_elem = max(output)
            index = output.index(max_elem)
            state, reward, done, info = env.step(index)
            total_reward+=reward
            env.render_local()
            if done:
                break
    total_reward/=games
    print(total_reward)
env.close()
