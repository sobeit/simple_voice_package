## Simple Voice Package
This ROS package plays wave format file data when get some "/state" topic messages.

## Installation
PyAudio and PyYaml is required for this package.
Before using this package, you have to install this two python modules.

Use pip for installing.

```
$ pip install pyaudio
$ pip install pyyaml
```

Set up your workspace.
```
$ mkdir -p ~/[anyname]_ws/src
$ cd ~/[anyname]_ws/src
$ wstool init
$ wstool set simple_voice_package --git https://github.com/sobeit/simple_voice_package.git
$ wstool up
$ rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO
$ cd .. && catkin_make
```

## Wave File Config
You can add and set up some wav files you're likely to use.
Add your files under the assets/wav directory and edit the voice_list.yml like this exmaple.

**Example**
```
1:"aaa.wav"
2:"bbb.wav"
3:"ccc.wav"
4:
5:
6:
7:
```

In this example, if getting /state topic message including "1", it will play "aaa.wav" file.

