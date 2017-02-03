#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

import wave
import pyaudio
import os,sys,atexit
import yaml

audio = pyaudio.PyAudio()
assets_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),"assets")
wav_file_dir = os.path.join(assets_path,"wav")
yml_file = open(os.path.join(assets_path,"voice_list.yml"))
wav_list = yaml.load(yml_file)

def callback(data):
    rospy.loginfo(data.data)
    wf = wave.open(os.path.join(wav_file_dir, wav_list[data.data]),"r")
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    frame_block = 1024
    data = wf.readframes(frame_block)
    while(data != ''):
        stream.write(data)
        data = wf.readframes(frame_block)

    stream.close()


def listener():
    rospy.init_node('state_voice',anonymous=True)
    rospy.Subscriber("/robot/state",Int32,callback)
    rospy.spin()

def close_all():
    audio.terminate()
    yml_file.close()

if __name__ == '__main__':
    atexit.register(close_all)
    listener()
