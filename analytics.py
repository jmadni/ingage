import os
from multiprocessing import Pool, cpu_count

import spectrust


def generate_spectrogram(audio_file_path):
    output_file = audio_file_path[:-4] + ".jpg"
    spect = spectrust.Spectrogram(width=800, height=600)
    spect.generate(audio_file_path, output_file)


class Analytics:
    def __init__(self, directory):
        self.directory = directory
        self.folder_path = os.path.join(os.getcwd(), directory)
        self.generate_tone_graphs()

    def generate_tone_graphs(self):
        files_list = [
            os.path.join(self.directory, each_file)
            for each_file in os.listdir(self.folder_path)
        ]
        with Pool(cpu_count()) as p:
            p.map(generate_spectrogram, files_list)
        for i in files_list:
            os.remove(i)
