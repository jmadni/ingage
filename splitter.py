import os
import shutil

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from utils import check_input_file_valid


class Splitter:
    def __init__(self, input_file, output_folder, split_interval):
        self.input_file = input_file
        self.output_directory_name = output_folder
        self.split_interval = split_interval
        self.clip_duration = 0

        self.initialize()
        self.splitting()

    def initialize(self):
        check_input_file_valid(self.input_file)
        self.total_duration()
        self.output_directory()

    def output_directory(self):
        if os.path.exists(self.output_directory_name):
            shutil.rmtree(self.output_directory_name)
        os.mkdir(self.output_directory_name)

    def total_duration(self):
        clip = VideoFileClip(self.input_file)
        self.clip_duration = int(clip.duration)

    def splitting(self):
        step = self.split_interval
        for idx, time in enumerate(range(0, self.clip_duration - step, step)):
            file_path = os.path.join(
                os.getcwd(), self.output_directory_name, f"clip_{idx}.mp4"
            )
            self.split_video(file_path, time, time + step)

    def split_video(self, output_file_name, start_time, end_time):
        ffmpeg_extract_subclip(
            self.input_file, start_time, end_time, targetname=output_file_name
        )
