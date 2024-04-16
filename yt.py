import streamlit as st
from pytube import YouTube, exceptions

def download_video():
    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    if video_url:
        try:
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the available video streams and their resolutions
            video_options = [f"{stream.resolution} - {stream.abr}" for stream in yt.streams.filter(progressive=True)]

            # Allow the user to select the desired video quality
            selected_video_quality = st.selectbox("Select the desired video quality:", video_options)

            if st.button("Download Video"):
                # Get the selected video stream
                video_stream = yt.streams.filter(progressive=True, resolution=selected_video_quality.split(" - ")[0]).first()

                # Download the video
                video_stream.download()
                st.success("Video downloaded successfully!")
        except exceptions.VideoUnavailable:
            st.error("The requested video is not available.")
        except Exception as e:
            st.error("An error occurred while downloading the video.")
            st.write(e)

def download_audio():
    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    if video_url:
        try:
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the available audio streams and their bitrates
            audio_options = [stream.abr for stream in yt.streams.filter(only_audio=True)]

            # Allow the user to select the desired audio quality
            selected_audio_quality = st.selectbox("Select the desired audio quality:", audio_options)

            if st.button("Download Audio"):
                # Get the selected audio stream
                audio_stream = yt.streams.filter(only_audio=True, abr=selected_audio_quality).first()

                # Download the audio
                audio_stream.download()
                st.success("Audio downloaded successfully!")
        except exceptions.VideoUnavailable:
            st.error("The requested video is not available.")
        except Exception as e:
            st.error("An error occurred while downloading the audio.")
            st.write(e)

st.title("YouTube Downloader")
st.write("Choose an option to download the video or audio:")

option = st.radio("", ("Download Video", "Download Audio"))

if option == "Download Video":
    download_video()
elif option == "Download Audio":
    download_audio()
