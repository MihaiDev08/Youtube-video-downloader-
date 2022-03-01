import pytube

url = input("Enter youtube video URL: ")

pytube.YouTube(url).streams.get_highest_resolution().download(
    "./Youtube_downloaded_videos"
)
