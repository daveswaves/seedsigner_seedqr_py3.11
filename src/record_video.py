import cv2

RES = {
    "w": 640,
    "h": 480,
    # "w": 1280,
    # "h": 720,
    # "w": 1920,
    # "h": 1080,
}
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # codec
# VID_NAME = 'output.mp4'
VID_NAME = 'output.avi'
FRAMES_PER_SECOND = 20.0

# Open a VideoCapture object to access the webcam (0 typically represents the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

'''
# Print supported resolutions
for i in range(20):
    width = 1920
    height = 1080
    cap.set(3, width)
    cap.set(4, height)
    print(f"Resolution {width}x{height} supported: {cap.read()[0]}")
cap.release()
'''

output = cv2.VideoWriter(VID_NAME, fourcc, FRAMES_PER_SECOND, (RES['w'], RES['h']))  # Adjust the filename and parameters as needed

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Display the frame
    cv2.imshow('Video Recording', frame)

    # Write the frame to the video file
    output.write(frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
output.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
