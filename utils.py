import os
import shutil

from moviepy.video.io.VideoFileClip import VideoFileClip


def output_directory(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)


def check_input_file_valid(video_file):
    try:
        VideoFileClip(video_file)
    except FileNotFoundError:
        pass
