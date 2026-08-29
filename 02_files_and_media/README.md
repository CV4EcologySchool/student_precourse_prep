# Session 2: Python basics through files and media

## What you should learn

- how Python strings, lists, loops, and functions appear in practical code;
- how the current working directory and file paths affect file loading;
- how to list and filter media files;
- how to load one image, inspect its array, and display it.

## Core exercise

Open `files_and_media_exercise.ipynb` in VS Code, [select the `.venv` notebook
kernel](../README.md#3-choose-the-notebook-kernel-in-vs-code), and work through it
from top to bottom. The notebook contains a short worked example followed by seven
tasks in which you will:

1. load and display one supplied image;
2. complete the code that filters files by suffix;
3. predict and inspect an image array's shape, data type, and value range;
4. write a reusable `load_image(path)` function;
5. diagnose and fix a broken path;
6. select an image by index and provide a useful out-of-range error; and
7. implement one image transformation and display the before/after result.

Run each cell before moving to the next one. Keep your predictions and error
observations in the notebook; they are part of the exercise.

## Apply to your data

If you have a small local sample, make a copy of the notebook, set `data_dir`
to that folder, and adjust `media_suffixes` for your modality. Do not point the
beginner notebook at millions of files; use a small folder first.

Audio/video students can read `modality_examples.py`. It shows the equivalent idea—find one path, load it, and inspect its basic properties—without requiring every student to install the same media libraries.

## Optional

`optional_image_transformations.py` contains resizing, cropping, grayscale, and flipping examples adapted from the previous Files and Images assignment. For each transformation, ask whether it preserves the ecological meaning of your target.

## Supplementary references

Use only the relevant parts of these maintained lessons if you need another explanation:

- [Short Introduction to Programming in Python](https://datacarpentry.github.io/python-ecology-lesson/01-short-introduction-to-Python.html): variables, lists, dictionaries, and functions.
- [Data Workflows and Automation](https://datacarpentry.github.io/python-ecology-lesson/06-loops-and-functions.html): the first loop example and the basic function section.

The Data Carpentry materials are supplementary references, not additional required assignments.
