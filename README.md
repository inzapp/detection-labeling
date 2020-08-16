# detection-labeling
Simple labeling tool for localization &amp; detection

## Usage
```
$ python label.py img_path resizing_ratio
```
img_path: image path to label (default: current directory)<br>
resizing_ratio: resizing ratio while labeling, useful when label small image (default: 1)<br>

Or drag label.py to img_path and
```
$ python label.py . resizing_ratio
```

## Double click or scroll to save boxes
<img src="/preview/1.gif" alt="" width="600">

## Right click to erase last box
<img src="/preview/2.gif" alt="" width="600">
