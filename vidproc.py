# coding=utf8
import argparse

from analytics import Analytics
from splitter import Splitter
from extract_audio import AudioExtraction


def arg_parser():
    pass
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input video file.", required=True)
    parser.add_argument(
        "-o",
        "--output",
        help="output video file name",
        required=False,
        default="vidproc",
    )

    args = parser.parse_args()
    return {
        "input_file": args.input,
        "output_file": args.output,
    }


def main():
    arguments = arg_parser()
    input_file = arguments.get("input_file")
    output_folder = arguments.get("output_file")
    Splitter(input_file, output_folder, 10)
    AudioExtraction(output_folder)
    Analytics(output_folder)


if __name__ == "__main__":
    main()
