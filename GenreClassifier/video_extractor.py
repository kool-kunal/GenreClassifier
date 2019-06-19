'''Video extraction into frames'''

def extractframes(extraction_path):
    import cv2
    import os
    path = input('Enter the path of the video:\n')
    print('tearing apart the video into frames ._.')
    vidobj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        vidobj.set(cv2.CAP_PROP_POS_MSEC, count*500)
        
        success, frame = vidobj.read()
        
        cv2.imwrite(extraction_path +"\\frame%d.jpg"%(count),frame)
        
        count+=1
        
    os.remove(extraction_path + "\\frame%d.jpg"%(count-1))
    print('---extracted successfully---')
