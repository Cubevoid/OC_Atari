import time
import random
import ipdb
import sys
sys.path.insert(0, '../..') # noqa
from ocatari.core import OCAtari

"""
Test raw/revised mode with a human render_mode and ipdb debugger.
"""

env = OCAtari("Asterix-v4", mode="raw", render_mode="human")  # Breakout
observation, info = env.reset()
prevRam = None
already_figured_out = []
for _ in range(10000000):
    obs, reward, terminated, truncated, info = env.step(random.randint(0, 0))   # change action

    ram = env._env.unwrapped.ale.getRAM()
    env.set_ram(30, 100)
    env.set_ram(36, 7)
    if prevRam is not None:
        for i in range(len(ram)):
            if ram[i] != prevRam[i] and i not in already_figured_out:
                pad = "           "
                for u in range(4 - len(str(i))):
                    pad += " "
                print(str(i) + pad + "value:" + str(ram[i]) + pad + " was previously " + str(prevRam[i]))
    print("------------------------------------------")
    prevRam = ram

    ipdb.set_trace()

    if terminated or truncated:
        observation, info = env.reset()
    print(info)
    env.render()
    if info.get('episode_frame_number') > 50:
        ipdb.set_trace()
    time.sleep(0.01)
    ipdb.set_trace()
env.close()
