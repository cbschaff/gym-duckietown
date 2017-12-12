from gym.envs.registration import register

register(
    id='Duckietown-v0',
    entry_point='gym_duckietown.envs:DuckietownEnv',
    # Threshold at which the environment is considered successfully solved
    reward_threshold=1000.0,
)

register(
    id='Duckietown-v1',
    entry_point='gym_duckietown.envs:DuckietownEnv_v1',
    # Threshold at which the environment is considered successfully solved
    reward_threshold=1000.0,
)
