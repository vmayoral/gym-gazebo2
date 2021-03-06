from gym.envs.registration import register

# Gazebo
# ----------------------------------------
# MARA
register(
    id='MARA-v0',
    entry_point='gym_gazebo2.envs.MARA:MARAEnv',
)

register(
    id='MARAOrient-v0',
    entry_point='gym_gazebo2.envs.MARA:MARAOrientEnv',
)

register(
    id='MARACollision-v0',
    entry_point='gym_gazebo2.envs.MARA:MARACollisionEnv',
)

register(
    id='MARACollisionOrient-v0',
    entry_point='gym_gazebo2.envs.MARA:MARACollisionOrientEnv',
)
