import cv2
import numpy as np
import asyncio

class MarkerDetector:
    def __init__(self):
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        self.aruco_params = cv2.aruco.DetectorParameters_create()

    async def detect_markers(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = await asyncio.to_thread(
            cv2.aruco.detectMarkers, gray, self.aruco_dict, parameters=self.aruco_params
        )
        return corners if ids is not None else []