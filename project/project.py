import re
import os
import sys
from pytube import YouTube
import moviepy.editor as my


def main():
    video = input("Provide your youtube video link: ").strip()
    v = video_link_format(video)
    f = video_download(v)
    video_file_type(f)


def video_link_format(v):
    # Using regex to check if the YouTube video url is in the correct format

    x = re.search(r"(https|http)?(://)?(www\.)?(youtube\.com)/(\w|\W)+", v)

    if x:
        return v
    else:
        sys.exit("Link format not valid")


def video_download(z):
    # The YouTube module reads all available streams for a video (different resolutions & fps)
    download = YouTube(z)

    d_video = download.streams.filter(only_video=True)[0]
    print(d_video)
    d_audio = download.streams.filter()[0]
    print(d_audio)

    # Download the video and audio separately

    dv = d_video.download()
    da = d_audio.download()

    # Find the path to the namely created audio and video files

    v = os.path.basename(dv)
    a = os.path.basename(da)

    video = my.VideoFileClip(v)
    audio = my.AudioFileClip(a)

    final_clip = video.set_audio(audio)

    # Merge the audio and video file into the file called "empty.mp4"

    final_clip.write_videofile("test_files/empty.mp4")
    fcp = os.path.abspath("test_files/empty.mp4")

    # Return the path to the new mp4 file created

    return fcp


def video_file_type(b):
    while True:

        # Ask user if they want to change the format of the created mp4 file

        file_question = input("Would you like to change MP4 file to another file type (yes / no)? ").lower().strip()
        # if the answer is "yes" then the user would be given the option to change the mp4 to
        # (avi, gif, webm, or ogv format)
        if file_question == 'yes':
            while True:
                video_type = input("Select your desired video file type (avi, gif, webm, ogv): ").lower().strip()

                if video_type == "avi":
                    video_clip = my.VideoFileClip(b)
                    return video_clip.write_videofile(str(b).replace(".mp4", ".avi"), codec="png")

                elif video_type == "webm":
                    video_clip = my.VideoFileClip(b)
                    return video_clip.write_videofile(str(b).replace(".mp4", ".webm"))

                elif video_type == "gif":
                    video_clip = my.VideoFileClip(b)
                    return video_clip.write_gif(str(b).replace(".mp4", ".gif"))
                elif video_type == "ogv":
                    video_clip = my.VideoFileClip(b)
                    return video_clip.write_videofile(str(b).replace(".mp4", ".ogv"))
                else:
                    print("Answer not valid try again")
                    pass
        # if the answer is "no" then the program will end

        elif file_question == 'no':
            sys.exit("Goodbye")
        # if not answered with "yes" or "no" the user would be asked the question again
        else:
            print("Answer not valid try again")
            pass


if __name__ == "__main__":
    main()