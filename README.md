# Gym-Duckietown 

Team PiedPiper

Members:

Attila Bertók I7XH6P

István Mádi EWMK96

Máté Meglécz A7RBKU


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

### Map generation:

Using [map-utils](https://github.com/duckietown/map-utils) we have generated 10 maps for training and 4 maps for testing. The can be found in /maps folder

For example: ```python3 generator.py --width 6 --height 5 --no-intersections```

After generation the tile size must be added to the end of the map files:
```tile_size: 0.585```
