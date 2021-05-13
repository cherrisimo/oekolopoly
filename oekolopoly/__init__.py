from gym.envs.registration import register

register(
    id='oekolopoly-v0',
    entry_point='oekolopoly.envs:OekoEnv',
)

#env = gym.make('oekolopoly-v0')

