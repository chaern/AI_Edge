from pathlib import Path
import cv2

RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
image = cv2.imread(RESOURCE_PATH / "roopy.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,3)


cv2.imshow("sobel", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()