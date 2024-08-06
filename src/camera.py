import cv2 

def run_camera():
    vid = cv2.VideoCapture(0) 
    
    if not vid.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        # Display the resulting frame 
        cv2.imshow('frame', frame) 

        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
  
    # After the loop, release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows()

