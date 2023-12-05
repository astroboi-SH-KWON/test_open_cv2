"""
requirement
pip install aspose.slides

trouble shooting
The type initializer for 'Gdip' threw an exception. System.TypeInitializationException: The type initializer for 'Gdip' threw an exception. ---> System.DllNotFoundException: Unable to load shared library 'libgdiplus' or one of its dependencies.

sudo apt-get update
before installing packages

sudo apt-get -y install libgdiplus
To suppress the standard output from a command use -qq. E.g.

# apt-get -qq -y install libgdiplus

"""
import aspose.slides as slides
import os

# 병합할 ppt 파일들이 있는 디렉토리
directory = '/home/astroboi/PycharmProjects/labelImg_yolov5/weekly_reports'

# ppt 파일들의 리스트를 이름 순으로 정렬
ppt_files = sorted([f for f in os.listdir(directory) if f.endswith('.pptx')])

with slides.Presentation(os.path.join(directory, ppt_files[0])) as pres1:
    for ppt_path in ppt_files[1:]:
        with slides.Presentation(os.path.join(directory, ppt_path)) as pres2:
            for slide in pres2.slides:
                pres1.slides.add_clone(slide)
    pres1.save("presentation.ppt", slides.export.SaveFormat.PPT)


# from pptx import Presentation
# import os
#
# # 병합할 ppt 파일들이 있는 디렉토리
# directory = '/Users/astroboi_m2/Downloads/weekly_reports'
#
# # ppt 파일들의 리스트를 이름 순으로 정렬
# ppt_files = sorted([f for f in os.listdir(directory) if f.endswith('.pptx')])
#
# # 새로운 Presentation 객체 생성
# merged_presentation = Presentation()
# print(len(ppt_files))
# for ppt_file in ppt_files:
#
#     # 각 ppt 파일을 로드
#     presentation = Presentation(os.path.join(directory, ppt_file))
#
#     # 각 슬라이드를 새로운 presentation에 추가
#     for slide in presentation.slides:
#         slide_id = slide.slide_id
#         slide_layout = slide.slide_layout
#         new_slide = merged_presentation.slides.add_slide(slide_layout)
#
#         for shape in slide.shapes:
#
#             new_shape = new_slide.shapes.add_shape(
#                 shape.shape_type,  # auto_shape_type,
#                 shape.left, shape.top, shape.width, shape.height
#             )
#             try:
#                 if "TABLE" in shape.shape_type:
#                     new_shape.shapes.add_table = shape.table
#                 else:
#
#                     new_shape.text = shape.text
#             except:
#                 print(shape.shape_type)
#                 print("here")
#                 pass
#
# # 병합된 ppt 파일 저장
# merged_presentation.save('merged_presentation.pptx')


