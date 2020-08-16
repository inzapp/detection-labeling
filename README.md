# detection-labeling
Simple labeling tool for localization &amp; detection

## Usage
```
$ python label.py img_path resizing_ratio
```
img_path: image path to label (default: current directory)<br>
resizing_ratio: resizing ratio while labeling, useful when label small image (default: 1)<br>
<br>
Or drag label.py to img_path and
```
$ python label.py . resizing_ratio
```
## Key
S: Save drawed box<br>
C: Continue current image<br>
B: Back to previous image<br><br>

## Press 's' to save boxes or 'c' to continue image
<img src="/preview/1.gif" alt="" width="600">

## Right click to erase last box
<img src="/preview/2.gif" alt="" width="600">
