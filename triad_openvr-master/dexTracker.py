import triad_openvr
import time
import sys

pathIn = ('./')


#Initial functions to print currently 
#connected trackers and/or controllers.

v = triad_openvr.triad_openvr()
v.print_discovered_objects()

if len(sys.argv) == 1:
    interval = 1/250
elif len(sys.argv) == 2:
    interval = 1/float(sys.argv[1])
else:
    print("Incorrect number of arguments.")
    interval = False

#Continue retrieve and display current detected x,y,z,yaw,pitch,roll of tracker(s)

while(True):
    try:
        if interval:
            while(True):
                start = time.time()
                txt = ""
                txt2 = ""
                try:
                    for each in v.devices["tracker_1"].get_pose_euler():
                        txt += "%.4f" % each
                        txt += " "
                    tTxt = txt
                except:
                    txt = tTxt
                try:
                    for each in v.devices["tracker_2"].get_pose_euler():
                        txt2 += "%.4f" % each
                        txt2 += " "
                    tTxt2 = txt2
                except:
                    txt2 = tTxt2
                print("\r" + "T1: " + txt + "T2: " + txt2 , end="")
                #print("\r" + "T1: " + txt, end="")
                sleep_time = interval-(time.time()-start)

                #Writes all values to file 'pose.txt'
                fStream = open(pathIn + 'pose.txt', 'wt')
                fStream.write(str(txt) + '\n')
                fStream.write(str(txt2) + '\n')
                fStream.close()
                if sleep_time>0:
                    time.sleep(sleep_time)
    #Typically, the program crashes with an error if the tracker(s) go out of bounds
    #Exception handling was added to stop this from happening. If an error is outputted,
    #the program instead continuously waits 3 seconds for the VIVE Tracker to come
    #back into view.
    except:
        print("\r" + "VIVE Tracker not detected. Seeking...", end="")
        time.sleep(1)