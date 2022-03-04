import cv2
import pickle

calib_result_pickle = pickle.load(open("camera_calib_pickle.p", "rb" ))
mtx = calib_result_pickle["mtx"]
optimal_camera_matrix = calib_result_pickle["optimal_camera_matrix"]
dist = calib_result_pickle["dist"]

"""Then, given an input image or video frame (i.e. distorted_image), we can undistort it using the following lines of code:"""

#cap = cv2.VideoCapture(0) #BGR Frame of realsense


while True:
    #ret1,frame =cap.read()
    frame = cv2.imread("test32.png")
    undistorted_image = cv2.undistort(frame, mtx, dist, None,
                                      optimal_camera_matrix)
    cv2.imshow("ORIG", frame)
    cv2.imshow("undistorted", undistorted_image)


    if cv2.waitKey(1)  & 0xFF==ord("d"):
        break



cap.release()
cv2.destroyAllWindows()
