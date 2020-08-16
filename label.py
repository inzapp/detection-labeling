import sys
from glob import glob

import cv2

win_name = 'img'
boxes = []
start_xy = (0, 0)
color = (0, 0, 255)
thickness = 2


def draw_boxes(img):
    for r in boxes:
        box_x, box_y, box_w, box_h = r[0], r[1], r[2], r[3]
        cv2.rectangle(img, (box_x, box_y), (box_x + box_w, box_y + box_h), color, thickness)


def mouse_callback(event, cur_x, cur_y, flag, _):
    global start_xy, boxes, color, thickness
    copy = raw.copy()

    # start click
    if event == 1 and flag == 1:
        start_xy = (cur_x, cur_y)

    # while dragging
    elif event == 0 and flag == 1:
        draw_boxes(copy)
        cv2.rectangle(copy, start_xy, (cur_x, cur_y), color, thickness)
        cv2.imshow(win_name, copy)

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
            draw_boxes(copy)
            cv2.imshow(win_name, copy)
        print(boxes)


path = ''
ratio = 1
if len(sys.argv) > 1:
    path = sys.argv[1].replace('\\', '/') + '/'
    if len(sys.argv) > 2:
        try:
            ratio = float(sys.argv[2])
        except ValueError:
            print('Second argument is resizing ratio of image. It muse be float type')
            sys.exit()

jpg_file_paths = glob(f'{path}*.jpg')
png_file_paths = glob(f'{path}*.png')
if len(jpg_file_paths) == 0 and len(png_file_paths) == 0:
    print('No image files in path. run label.py with path argument')
    sys.exit(0)

index = 0
img_paths = jpg_file_paths + png_file_paths
while True:
    while True:
        file_path = img_paths[index]
        file_name_without_extension = file_path.replace('\\', '/').split('/').pop().split('.')[0]
        raw = cv2.imread(file_path, cv2.IMREAD_ANYCOLOR)
        raw = cv2.resize(raw, (0, 0), fx=ratio, fy=ratio)
        cv2.namedWindow(win_name)
        cv2.setMouseCallback(win_name, mouse_callback)
        recover_if_continue = raw.copy()
        draw_boxes(recover_if_continue)
        cv2.imshow(win_name, recover_if_continue)
        res = cv2.waitKey(0)

        # save if input key was 's' or continue if key was 'c'
        if res == 115 or res == 99:
            if res == 115:
                if len(boxes) == 0:
                    print('No boxes to save')
                else:
                    # normalize x, y, width, height by resizing ratio
                    normalized_boxes = []
                    for b in boxes:
                        x, y, w, h = b[0], b[1], b[2], b[3]
                        x = int(x / ratio)
                        y = int(y / ratio)
                        w = int(w / ratio)
                        h = int(h / ratio)
                        normalized_boxes.append([x, y, w, h])
                    save_file_path = f'{path + file_name_without_extension}.txt'
                    file = open(save_file_path, mode='wt', encoding='utf-8')
                    file.write(str(normalized_boxes))
                    print(f'saved {len(boxes)} boxes to {save_file_path}')
            elif res == 99:
                print(f'Continue image {file_name_without_extension}')
            boxes = []
            index += 1
            if index == len(img_paths):
                sys.exit()
            break

        # go to previous image if input key was 'b'
        elif res == 98:
            if index == 0:
                print('Current image is first image')
            else:
                print(f'Previous image {file_name_without_extension}')
                boxes = []
                index -= 1

        # exit if input key was ESC
        elif res == 27:
            sys.exit()

