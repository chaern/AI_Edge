from pathlib import Path
import cv2

# Read from the recorded video file
RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
cap = cv2.VideoCapture(RESOURCE_PATH / "movie.mp4")

CAPTURE_PATH = RESOURCE_PATH / "capture"
CAPTURE_PATH.mkdir(parents=True, exist_ok=True)
capture_number = 1

# 동영상 파일이 성공적으로 열렸으면 while 문 반복
while cap.isOpened():
    # 한 프레임을 읽어옴
    ret, frame = cap.read()

    if ret is False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    cv2.imshow("Frame", frame)

    # 키 입력: q는 종료, c는 현재 표시 중인 프레임 저장
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        # 기존 파일이 있으면 다음 번호를 사용
        while (CAPTURE_PATH / f"{capture_number:03d}.jpg").exists():
            capture_number += 1

        capture_file = CAPTURE_PATH / f"{capture_number:03d}.jpg"
        if cv2.imwrite(str(capture_file), frame):
            print(f"Saved: {capture_file}")
            capture_number += 1
        else:
            print(f"Failed to save: {capture_file}")


cap.release()
cv2.destroyAllWindows()
