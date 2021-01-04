from pytube import YouTube

# youtube link from freecodecamp channel >> Discord bot
link = 'https://www.youtube.com/watch?v=SPTfmiYiuok'

#link = input('please enter youtube URL: )

video = YouTube(link)

# print(f" the video title is:\n{video.title} \n--------------")
# print(f" the video description is:\n{video.description}\n--------------")
# print(f" the video views is:\n{video.views} \n--------------")
# print(f" the video rating is:\n{video.rating} \n--------------")
# print(f" the video duration is:\n{video.length/60} minutes \n--------------")

#looping through strem to print the array nicely
# for stream in video.streams:
#   print(stream)


#filtering results
# for stream in video.streams.filter(progressive=True):
#   print(stream)

#resolution filter
# for stream in video.streams.filter(res='720p'):
#   print(stream)

# for stream in video.streams.filter(subtype='mp4'):
#   print(stream)

# for stream in video.streams.filter(res='1080p'):
#   print(stream)

#highest && lowest resolutions
print(video.streams.get_highest_resolution())
print(video.streams.get_lowest_resolution())

