# Gym-Duckietown 

Team PiedPiper

Members:

Attila Bertók I7XH6P

István Mádi EWMK96

Máté Meglécz A7RBKU

## Milestone 1
Steps of creating the environment

1. We have created an Ubuntu virtual machine
2. Cloning the repo inside the vm.
3. Inside the vm there was python version 3.10, which has a bug in one of its standard packages therefore without editing the Duckietown's source code, it couldn't be launched. Our solution was creating a Conda environment with 3.7 python version.
4. `pip3 install -e .` inside the environment
5. After this we had to rename the randint method to integers in the randomizer.py and simulator.py files.
6. Running the manual_control.py. `python3 ./manual_control.py --env-name Duckietown-udem1-v0`
7. We have created our own map which is https://github.com/matemeglecz/gym_duckietown/blob/milestone_1/maps/test_loop1.yaml
   ![myimage-alt-tag](/images/custom_map.png)
8. With the following command we ran the basic control agent on our own map: `python3 ./exercises/basic_control.py --map-name maps/test_loop1`
9. We have created a video of the basic control agent running. (/videos/basic_control.mov)

## Milestone 2 

First, we had to resolve some package version issues. The python version is upgraded to python 3.8. We have realized that the previous milestone's modifications were unneccessary (we used the wrong gym version).

After that the we got the baseline_rl solution running. The solution's simulator was extended to use multiple maps for training, and also modified to not use maps which starts with "test". This baseline solution is now located in `gym-duckitown/learning` folder. The training script also logs to our Wandb project. For running this training: `python3 -m scripts.train_cnn.py --seed 123` For testing: `python3 -m scripts.test_cnn.py --seed 123`, this tests for test_map1.yaml.

As suggested we started to work in a rl library. The clean_rl repo was cloned and we modified the `ddpg_continuous_action.py` so it is runnable for our simulator enviroment and this also logs to our wandb project. Command for training:
`python cleanrl/ddpg_continuous_action.py --track False`

For being able to use the new maps, with this command `python map_move_to_duckietown.py`, maps can be copied to the correct site-packages.

For getting the correct python packages a `requirements.txt` is located in the root folder, so the packages can be installed from that. The `gym-duckietown\src` dir has to be added to the PYTHONPATH enviroment variable so python uses our version of the gym-duckietown.

### Map generation:

Using [map-utils](https://github.com/duckietown/map-utils) we have generated 10 maps for training and 4 maps for testing. The can be found in /maps folder

For example: ```python3 generator.py --width 6 --height 5 --no-intersections```

After generation the tile size must be added to the end of the map files:
```tile_size: 0.585```
