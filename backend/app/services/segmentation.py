import cv2
import numpy as np

class DemoSegmenter:
    def predict(self, image_rgb: np.ndarray) -> np.ndarray:
        img = image_rgb.copy()
        h, w = img.shape[:2]
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = np.zeros((h, w), dtype=np.uint8)

        red = img[:,:,0].astype(np.int16)
        green = img[:,:,1].astype(np.int16)
        blue = img[:,:,2].astype(np.int16)

        water = (blue > green + 15) & (blue > red + 15)
        agri = (green > red + 10) & (green > blue + 5) & (green > 70)

        hue, sat, val = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
        bare = ((hue > 8) & (hue < 30) & (sat > 20) & (sat < 170) & (val > 60))

        edges = cv2.Canny(gray, 100, 180)
        roads = cv2.dilate(edges, np.ones((3,3), np.uint8), iterations=1) > 0
        roads = roads & (val > 100)

        rg_diff = np.abs(red - green)
        gb_diff = np.abs(green - blue)
        rb_diff = np.abs(red - blue)
        built = (rg_diff < 20) & (gb_diff < 20) & (rb_diff < 20) & (val > 80)

        mask[water] = 5
        mask[agri & (mask == 0)] = 2
        mask[bare & (mask == 0)] = 3
        mask[roads & (mask == 0)] = 4
        mask[built & (mask == 0)] = 1
        return mask

segmenter = DemoSegmenter()
