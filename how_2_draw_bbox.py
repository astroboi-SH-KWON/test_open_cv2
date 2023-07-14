"""
0: Icon
1: Container
2: Text
3: Text_Field
4: Check_Box
5: Slide
6: Picture
7: Page_Control
8: AD
9: Segmentation_Control
10: Add
11: Radio_Button
12: Toggle
13: Play
14: Edit
15: Slider
16: Pause
17: Dialog
18: Keyboard
19: Create
"""
import cv2
import glob
import xml.etree.ElementTree as ET

img_size = 100
data_src_dir = "/Users/astroboi_m2/Downloads/backup/test_project/Object_detection_dataset/All_data/"
data_xml_path = f"{data_src_dir}*.xml"

xml_path_list = glob.glob(data_xml_path)
print(len(xml_path_list))

cls_dict = {}
with open("/Users/astroboi_m2/Downloads/backup/test_project/Object_detection_dataset/new_classes.txt", "r") as f:
    tmp = f.readlines()
    for i in range(len(tmp)):
        cls_dict.update({tmp[i].strip(): i})
        # cls_dict.update({i: tmp[i].strip()})
print(cls_dict)

for xml_file in xml_path_list:
    img_file = xml_file.replace(".xml", ".jpg")
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(img_file.split("/")[-1])
    print("")
    img_color = cv2.imread(img_file, cv2.IMREAD_COLOR)

    # Pass the path of the xml document
    tree = ET.parse(xml_file)
    # print(f"\n\n{xml_file}")

    # get the parent tag
    root = tree.getroot()

    # w = int(root.find('size').find('width').text)
    # h = int(root.find('size').find('height').text)
    #
    # print(w, h)

    for obj in root.findall('object'):
        name = obj.find('name').text.replace(" ", "_")
        if name == 'add':
            name = 'Add'
        # cls_num = cls_dict[name]
        print(name)
        xmin = int(obj.find('bndbox').find('xmin').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymax = int(obj.find('bndbox').find('ymax').text)

        start_point = (int(xmin), int(ymin))
        end_point = (int(xmax), int(ymax))
        cv2.rectangle(img_color, start_point, end_point, color=(0, 255, 0), thickness=2)

        cv2.putText(img_color, name, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2)
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    img_color = cv2.resize(img_color, (10 * img_size, 23 * img_size))
    cv2.imshow("bounding_box", img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# predictions = {'predictions': [
#     {'x': 1012.0, 'y': 593.5, 'width': 406.0, 'height': 443.0, 'confidence': 0.7369905710220337, 'class': 'Paper',
#      'image_path': 'example.jpg', 'prediction_type': 'ObjectDetectionModel'}], 'image': {'width': 1436, 'height': 956}}
#
# for bounding_box in predictions["predictions"]:
#     img = ""
#     x0 = bounding_box['x'] - bounding_box['width'] / 2
#     x1 = bounding_box['x'] + bounding_box['width'] / 2
#     y0 = bounding_box['y'] - bounding_box['height'] / 2
#     y1 = bounding_box['y'] + bounding_box['height'] / 2
#
#     start_point = (int(x0), int(y0))
#     end_point = (int(x1), int(y1))
#     cv2.rectangle(img, start_point, end_point, color=(0, 255, 0), thickness=2)
#
# # cv2.imwrite("example_with_bounding_boxes.jpg", image)
#
# # show thresh and result
# cv2.imshow("bounding_box", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()