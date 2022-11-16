from gym.envs.registration import register

register(
    id = 'mytetris-v0'
    entry_point='gym_mytetris.envs:MyTetrisEnv',
)
