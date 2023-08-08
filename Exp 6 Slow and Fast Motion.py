import cv2
def play_video(video_path, speed_factor):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(int(1000 / (speed_factor * 30))) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    video_path = "C:\\Users\\91984\\Pictures\\Camera Roll\\WIN_20230808_14_09_21_Pro.mp4"
    slow_motion_factor = 0.5
    fast_motion_factor = 3.0
    print("Playing video in slow motion...")
    play_video(video_path, slow_motion_factor)
    print("Playing video in fast motion...")
    play_video(video_path, fast_motion_factor)
