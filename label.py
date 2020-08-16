import sys
from glob import glob

import cv2

boxes = []
start_xy = (0, 0)
color = (0, 0, 255)
thickness = 2


def mouse_callback(event, cur_x, cur_y, flag, _):
    global start_xy, boxes, color, thickness
    copy = raw.copy()

    # start click
    if event == 1 and flag == 1:
        start_xy = (cur_x, cur_y)

    # while dragging
    elif event == 0 and flag == 1:
        for r in boxes:
            x, y, w, h = r[0], r[1], r[2], r[3]
            cv2.rectangle(copy, (x, y), (x + w, y + h), color, thickness)
        cv2.rectangle(copy, start_xy, (cur_x, cur_y), color, thickness)
        cv2.imshow('img', copy)

    # end click
    elif event == 4 and flag == 0:
        width = cur_x - start_xy[0]
        height = cur_y - start_xy[1]
        if width == 0 or height == 0:
            return
        boxes.append([start_xy[0], start_xy[1], cur_x - start_xy[0], cur_y - start_xy[1]])
        print(boxes)

    # right click
    elif event == 5 and flag == 0:
        if len(boxes) > 0:
            boxes.pop()
        copy = raw.copy()
        for r in boxes:
            x, y, w, h = r[0], r[1], r[2], r[3]
            cv2.rectangle(copy, (x, y), (x + w, y + h), color, thickness)
        cv2.imshow('img', copy)
        print(boxes)

    # double click or scrolling
    elif (event == 7 and flag == 1) or (event == 10):
        if len(boxes) == 0:
            return
        save_file_path = f'{path + file_name_without_extension}.txt'
        file = open(save_file_path, mode='wt', encoding='utf-8')
        file.write(str(boxes))
        print(f'saved {len(boxes)} boxes to {save_file_path}')
        copy = raw.copy()
        cv2.imshow('img', copy)
        boxes = []


path = ''
if len(sys.argv) > 1:
    path = sys.argv[1].replace('\\', '/') + '/'

jpg_file_paths = glob(f'{path}*.jpg')
png_file_paths = glob(f'{path}*.png')
if len(jpg_file_paths) == 0 and len(png_file_paths) == 0:
    print('No image files in path. run label.py with path argument')
    sys.exit(0)

for file_path in jpg_file_paths + png_file_paths:
    file_name_without_extension = file_path.replace('\\', '/').split('/').pop().split('.')[0]
    raw = cv2.imread(file_path, cv2.IMREAD_ANYCOLOR)
    cv2.namedWindow('img')
    cv2.setMouseCallback('img', mouse_callback)
    cv2.imshow('img', raw)
    cv2.waitKey(0)
