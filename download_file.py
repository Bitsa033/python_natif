from pytube import YouTube

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory path to save the video: ")
    download_video(video_url, output_path)
