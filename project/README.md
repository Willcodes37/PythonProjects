
# YouTube Video Downloader

    #### Video Demo:  https://youtu.be/ix6nF2wFQwY
    #### Description:
    For this project a YouTube video downloader with an option of file conversion was created.  In order to accomplish this task first I had to find a way scrub the YouTube site for specific details on the YouTube video link provided by the user. I was able to do this by importing the pytube module (ex: from pytube import YouTube). After the link was provided the module I gained access to various information about specific video link provided such as title, video length, description, etc.… However for this project the multiple streams available at different resolutions, frame rates, video only, and audio only were the most useful. After doing some research I found that YouTube uses two systems to stream their videos, which are progressive and Dash streams. Progressive streams contain both audio and video codec files, but are limited to a 720p resolution. Dash streams are used for resolutions higher than 720p, it is implemented by using separate audio and video codec files then merging into one file. I chose to use the Dash method. I filtered video only and audio only files using the code:

    download = YouTube(z)

    d_video = download.streams.filter(only_video=True)[0]
    print(d_video)
    d_audio = download.streams.filter(only_audio=True)[0]
    print(d_audio)

    Output:

    <Stream: itag="313" mime_type="video/webm" res="2160p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">

    Once the desired audio and video stream was found then I download those streams using:

    dv = d_video.download()
    da = d_audio.download()

    Then finally the audio and video files that were created were merged using the movie.py editor (ex: import moviepy.editor as my). The movie.py library is used manipulate audio and video files such as cuts, compositing, and various other effects. The code is shown below, with the output file being named “final.mp4”:

    video = my.VideoFileClip(v)
    audio = my.AudioFileClip(a)

    final_clip = video.set_audio(audio)

    # Merge the audio and video file into the file called "final.mp4"

    final_clip.write_videofile("test_files/final.mp4")

    The next step in the process is giving the user the opportunity to change the format of the mp4 file created to webm, avi, gif, or ogv. If the user chooses to change the format of the original mp4 file created, then at the end of the program they will have two video files (ex. final.mp4 & final.webm).
