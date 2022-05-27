import cv2
import os

def showNimages(label_path, image_path):
    assert os.path.exists(image_path)
    image = cv2.imread(image_path)

    assert os.path.exists(label_path)
    with open(label_path) as f:
        txt_data = f.readlines()
        
    for data in txt_data:
        x1, y1, x2, y2, cf = data.split(' ')[:5]
        x1, y1, x2, y2, cf = float(x1), float(y1), float(x2), float(y2), float(cf)
        x1, y1, x2, y2= int(x1), int(y1), int(x2), int(y2)
        if cf>0.3:
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, int(255*cf)))
            # cv2.rectangle(image, (x1-1, y1-1), (x2+1, y2+1), (0, 255, int(255*cf)))
            # cv2.rectangle(image, (x1+1, y1+1), (x2-1, y2-1), (0, 255, int(255*cf)))
        
    cv2.imwrite('result.png', image)

showNimages('det_info/MogFace_E/ss_140_nmsth_0.3_scoreth_0.01/res/10.txt', 'dataset/DarkFace Test Zero-DCE/res/10.png')