import cv2
import pickle

calib_result_pickle = pickle.load(open("camera_calib_pickle.p", "rb" ))
mtx = calib_result_pickle["mtx"]
optimal_camera_matrix = calib_result_pickle["optimal_camera_matrix"]
dist = calib_result_pickle["dist"]

distorted_image = cv2.imread("test36.png")
"""Then, given an input image or video frame (i.e. distorted_image), we can undistort it using the following lines of code:"""
undistorted_image = cv2.undistort(distorted_image, mtx, dist, None,
                                    optimal_camera_matrix)
#undistorted_image=cv2.resize(undistorted_image,(0,0),fx=0.5,fy=0.5)
#cv2.imshow("di",undistorted_image)


cap = cv2.VideoCapture(0)
while True:
    # ret = cap.set(3, 2560)  # setzt die Breite des Bildes
    # ret = cap.set(4, 1440)  # setzt die Höhe des Bildes
    ret, frame = cap.read()
    frame = cv2.undistort(frame, mtx, dist, None,optimal_camera_matrix)
    cv2.imshow("orig",frame)

    cv2.waitKey(20)