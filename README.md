# SLAM Project Commands

This document lists all the unique ROS 2 commands used during the SLAM-based autonomous vehicle project. Each section includes a brief description of the purpose and function of the commands.

---

## SLAM Mapping Commands

These commands are used to perform SLAM mapping and save the generated maps.

```bash
ros2 run slam_toolbox async_slam_toolbox_node \
--ros-args -p scan_topic:=/scan \
-p publish_transform:=true \
-p odom_frame:=odom \
-p base_frame:=base_link \
-p map_frame:=map
```

> Note: Set `odom_frame` to `odom` for proper map updating.

```bash
ros2 run nav2_map_server map_saver_cli -f ~/map2
```

Saves the generated map to the specified location.

```bash
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link laser --ros-args -p use_sim_time:=false
```

Publishes a static transform between `base_link` and `laser` frames.

```bash
ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py
```

Launches the RF2O laser odometry package to provide odometry information.

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Allows manual teleoperation of the robot using keyboard input.

---

## Map Saving and Navigation Launch Commands

Commands to save maps and launch the navigation stack.

```bash
ros2 run nav2_map_server map_saver_cli -f ~/map_home
```

Saves the home environment map.

```bash
ros2 launch nav2_bringup bringup_launch.py \
map:=/home/ashish/ros2_ws/src/nav2_custom_launch/maps/map_home.yaml \
use_sim_time:=false \
autostart:=true
```

Launches the Navigation2 stack with the saved home map.

```bash
ros2 launch my_robot_description display.launch.py
```

Displays the robot model in RViz.

---

## Localization Mode and Navigation Launch

Commands to run SLAM toolbox in localization mode and launch the navigation stack.

```bash
ros2 run slam_toolbox async_slam_toolbox_node \
--ros-args -p scan_topic:=/scan \
-p mode:=localization \
-p publish_transform:=true \
-p odom_frame:=odom \
-p base_frame:=base_link \
-p map_frame:=map
```

Runs SLAM toolbox in localization mode using an existing map.

```bash
ros2 launch nav2_bringup bringup_launch.py \
map:=/home/ashish/map_lab.yaml \
use_sim_time:=false \
autostart:=true
```

Launches the navigation stack with the specified lab map.

```bash
ros2 launch nav2_bringup bringup_launch.py \
map:=/home/ashish/map_lab.yaml \
params_file:=/home/ashish/ros2_ws/src/nav2_custom_launch/params/nav2_params.yaml \
use_sim_time:=false \
autostart:=true
```

Launches the navigation stack with custom parameter files.

```bash
ros2 launch nav2_custom_launch nav2_navigation_only.launch.py use_sim_time:=false
```

Launches only the navigation components without map server or localization.

---

## Sequence (on Virtual Machine)

This is the step-by-step sequence of commands executed on the virtual machine.

1. **Publish static transform**

```bash
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link laser --ros-args -p use_sim_time:=false
```

2. **Launch RF2O Laser Odometry**

```bash
ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py
```

3. **Launch Robot Description**

```bash
ros2 launch my_robot_description display.launch.py
```

4. **Run Map Server**

```bash
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=/home/ashish/map_lab.yaml
```

5. **Start SLAM Toolbox in Localization Mode**

```bash
ros2 run slam_toolbox async_slam_toolbox_node \
--ros-args -p scan_topic:=/scan \
-p mode:=localization \
-p publish_transform:=true \
-p odom_frame:=odom \
-p base_frame:=base_link \
-p map_frame:=map
```

6. **Bring up Navigation Stack with Ackermann Parameters**

```bash
ros2 launch nav2_bringup bringup_launch.py \
map:=/home/ashish/map_lab.yaml \
params_file:=/home/ashish/ros2_ws/src/nav2_custom_launch/params/ackermann_only_params.yaml \
use_sim_time:=false \
autostart:=true
```

7. **(Optional) Start SLAM Toolbox with Pre-saved Map and Dock Mode**

```bash
ros2 run slam_toolbox async_slam_toolbox_node \
--ros-args -p scan_topic:=/scan \
-p mode:=localization \
-p publish_transform:=true \
-p base_frame:=base_link \
-p odom_frame:=odom \
-p map_frame:=map \
-p map_file_name:=/home/ashish/maps/map_lab_test_data \
-p map_start_at_dock:=true \
-p use_sim_time:=false
```

---

# End of Commands
