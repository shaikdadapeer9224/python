from pytube import YouTube

link = "https://youtu.be/AXSm49NGkg8"
YouTube(link).streams.first().download()
print('Downloaded Successfully')
