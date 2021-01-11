import os
from multiprocessing import Pool, cpu_count
from moviepy.editor import *


class AudioExtraction:
    def __init__(self, video_files_dir):
        self.directory = video_files_dir
        self.video_to_audio_convert()

    def video_to_audio_convert(self):
        folder_path = os.path.join(os.getcwd(), self.directory)
        with Pool(cpu_count()) as p:
            p.map(self.convert_audio, os.listdir(folder_path))

    def convert_audio(self, file_name):
        audio_file_name = file_name.split(".")[0] + ".wav"

        input_file_path = os.path.join(os.getcwd(), self.directory, file_name)
        output_file_path = os.path.join(os.getcwd(), self.directory, audio_file_name)

        AudioFileClip(input_file_path).write_audiofile(output_file_path)
        try:
            os.remove(input_file_path)
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
