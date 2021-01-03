from pytube import YouTube

link = 'https://www.youtube.com/watch?v=3HqN-YS8eso'

#link = input('please enter youtube URL: )

video = YouTube(link)

print(f" the video title is:\n{video.title} \n--------------")
print(f" the video description is:\n{video.description}\n--------------")
print(f" the video views is:\n{video.views} \n--------------")
print(f" the video rating is:\n{video.rating} \n--------------")
print(f" the video duration is:\n{video.length/60} minutes \n--------------")
