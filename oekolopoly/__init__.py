from gym.envs.registration import register

register(
    id='Oekolopoly-v0',
    entry_point='oekolopoly.envs:OekoEnv',
)
