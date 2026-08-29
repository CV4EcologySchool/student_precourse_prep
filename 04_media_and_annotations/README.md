# Session 4: connecting media and annotations with a dataset class

## What you should learn

- how a sample ID or filename connects media to an annotation;
- how to check that both files exist;
- what a loader returns for one sample;
- why shapes, data types, IDs, and missing files matter;
- how a class keeps related data and behavior together;
- how `__init__`, `__len__`, and `__getitem__` create a useful dataset interface;
- how to visualize your own media together with its labels and recognize
  mismatches early.

## Core exercise

Open `media_and_annotations_exercise.ipynb` in VS Code and work through it
from top to bottom. You will first match and load one image/annotation pair
with ordinary functions. You will then build a `FishDataset` class that reuses
those functions and supports:

```python
len(dataset)
dataset[index]
dataset.describe()
```

The class is a required part of this exercise. It provides the first focused
introduction to object-oriented programming in the prep sequence.

Session 3 examined how a table describes each student's own collection. This
session deliberately returns briefly to shared fish data so the class
mechanics are consistent for everyone.

## Required own-data visualization

The second half of the notebook returns to the student's own data. Each student
must display several media samples together with their labels or annotations.
Choose the relevant pathway:

- classification: a grid with several images from each selected class;
- object detection: images with labeled bounding boxes;
- keypoints or landmarks: images with points overlaid;
- segmentation: images with masks overlaid;
- geospatial data: a raster tile with pixel-space annotations or
  CRS-aligned vector annotations;
- audio/video: waveforms or representative frames with their labels,
  intervals, or spatial annotations.

The objective is to catch problems while there is still time to address them:
wrong labels, missing files, incorrect coordinates, boxes outside images,
misaligned masks, CRS errors, unexpected channels, or samples that cannot be
traced to their metadata. Bring any questionable visualization to the
instructors promptly rather than waiting for session 6. Do not copy research
data into this repository.

This is enough OOP for prep. Inheritance and static methods are deliberately
out of scope.
