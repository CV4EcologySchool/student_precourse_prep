# Session 6: plan a workable data subset

This is an individual planning meeting with an instructor, not another
exercise. You will use your real data organization and the work from earlier
sessions to agree on a small, workable subset for development in January.

The goal is not to copy or process the full dataset. You should leave
with a concrete plan for creating a subset that is small enough to inspect and
debug, but still contains the kinds of samples your code must handle.

## Bring to the meeting

- the location of the full dataset, or a description if it cannot be opened
  during the meeting;
- an approximate file or sample count and storage size, if known;
- the metadata or annotation table, or a few representative rows;
- the small sample used in earlier sessions;
- any code already used to list, filter, or load the data.

Do not include passwords, access tokens, sensitive locations, or restricted
data in the written notes.

## Decide together

You and your instructor should make project-specific decisions about:

1. **The unit of one sample.** For example, one image and label, one image and
   landmark CSV, one audio clip and interval table, or one video and its
   frame-level annotations.
2. **The purpose of the subset.** It should support loading, visualization,
   annotation checks, and early code debugging.
3. **What it must represent.** Choose relevant variation such as species,
   sites, cameras, seasons, recording conditions, annotation types, or common
   edge cases. The right criteria depend on the student's project.
4. **A manageable size.** Agree on an approximate number of samples or storage
   size based on the media type and available computer—not a universal target.
5. **How it will be selected.** Prefer a reproducible list, metadata query, or
   small script. If sampling randomly, record the random seed.
6. **Where it will be stored.** Keep the original data unchanged. Store the
   subset separately and preserve the identifiers needed to trace every item
   back to its source.
7. **Whether each sample is complete.** Media, annotations, and required
   metadata should stay together unless the purpose is specifically to test
   missing-data behavior.

This development subset is **not** the eventual train/validation/test split.
Formal splitting, leakage prevention, and class-balancing decisions belong in
the course and should use the full project context.

## Leave with an individual plan

Complete [`handoff_notes.md`](handoff_notes.md) together. Record the agreed
subset criteria, selection method, destination, and immediate next action. If
a decision cannot yet be made, record exactly what information is missing and
who will find it.

If time permits, load one complete sample from the proposed subset or sketch
the few lines of filtering code needed to create it. A finished subset is not
required during this meeting.

## What still waits until the course

- final framing of the CV task;
- data splitting and leakage decisions;
- choosing a model or codebase;
- installing the workshop training stack;
- full-dataset transfer;
- GPU training;
- metrics, evaluation, model improvement, and downstream ecological analysis.
