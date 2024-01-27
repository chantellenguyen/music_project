
from pytube import YouTube
import os


def downloader(url):

    yt = YouTube(url)


    video = yt.streams.filter(only_audio=True).first()


    out_file = video.download()


    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


    print(yt.title + " has been successfully downloaded.")


songlist = ["O holy night",
            "mary did you know",
            "danny boy",
            "how you like that",
            "ice cream",
            "gone"
            ]

urls = ["https://www.youtube.com/watch?v=QP0TGh6c-Ss",
        "https://www.youtube.com/watch?v=JPsgIhlYQmM",
        "https://www.youtube.com/watch?v=I2Cyxb63mK8",
        "https://www.youtube.com/watch?v=aHnHwrJjR3U",
        "https://www.youtube.com/watch?v=pcrnh069iBI",
        "https://www.youtube.com/watch?v=O2S-Vm-fNrw"
        ]


youtube_name = []


song_lookup = input("can you pls search a song : ")


if (song_lookup in songlist):
    print("This song has been found!")
    if (song_lookup == songlist[0]):
        url = urls[0]
        downloader(url)
    elif (song_lookup == songlist[1]):
        url = urls[1]
        downloader(url)
    elif (song_lookup == songlist[2]):
        url = urls[2]
        downloader(url)
    elif (song_lookup == songlist[3]):
        url = urls[3]
        downloader(url)
    elif (song_lookup == songlist[4]):
        url = urls[4]
        downloader(url)
    else:
        url = urls[5]
        downloader(url)
else:
    print("Not found!")
    print("The only available songs are: ")
    print(songlist)
    print("Your song has been added!")

    songlist.append(song_lookup)

    url = input("enter url here please : ")
    downloader(url)
    print(songlist)









