# test_open_cv2
practice open_cv2

    env
        conda create -n astroboi_cv2 python opencv
        # # python=3.11.3 opencv=4.6.0 


    trouble shooting
        1. opencv autocomplete not working on pycharm
            1-1. for Mac : copy /Users/astroboi_m2/anaconda3/envs/astroboi_cv2/lib/python3.11/site-packages/cv2/python-3.11 to /Users/astroboi_m2/anaconda3/envs/astroboi_cv2/lib/python3.11/site-packages
            1-2. for Windows : copy site-packages/cv2/cv2.pyd to site-packages/
