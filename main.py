import cv2
import time

video = cv2.VideoCapture("video.mp4")
# extracting basic info 
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)


# print(w, h , nr_frames, fps)

# extracting frames

# success, frame = video.read()
# count = 1
# while success:
#   cv2.imwrite(f'images/{count}.jpg', frame)
#   success, frame = video.read()
#   count += 1

# extracting frame at certain time part 1:
# success, frame = video.read()
# now = time.time()
# x = 0
# while success:
#   if x == 1.88:
#     cv2.imwrite(f"images/this.jpg", frame)
#     break
#   new_time = time.time()
#   x = round(new_time - now, 2)

# extracting frame at certain time part 2:
timestamp = '00:00:01.88'
time_list = timestamp.split(":")
time_floats = [float(i) for i in time_list]
h,m,s = time_floats
frame_nr = h * 3600 * fps + m * 60 * fps + s * fps 
video.set(1, frame_nr)
success, frame = video.read()
cv2.imwrite(f"frame at {h}:{m}:{s}.jpg", frame)
