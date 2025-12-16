import cv2
import imageio

gif_path = "alert-siren1.gif"
gif = imageio.mimread(gif_path)  # Read GIF frames
#while True:
for _ in range(10):
    for frame in gif:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
        cv2.imshow("GIF Player", frame)
        if cv2.waitKey(100) & 0xFF == 27:  # Press 'Esc' to exit
           break

cv2.destroyAllWindows()
