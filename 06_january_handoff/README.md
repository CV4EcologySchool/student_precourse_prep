# Session 6: plan a workable data subset

This is an individual planning meeting with an instructor, not another
exercise. You will use your real data organization and the work from earlier
sessions to agree on a small, workable subset for development in January.

The goal is not to copy or process the full dataset. You should leave
with a concrete plan for creating a subset that is small enough to inspect and
debug, but still contains the kinds of samples your code must handle.

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

This development subset is for quick prototyping of methods so you will iterate quicker during the course.
Data splitting, and other experimental considerations will be discussed during the course.

## Leave with an individual plan

Complete [`handoff_notes.md`](handoff_notes.md) together. Record the agreed
subset criteria, selection method, destination, and immediate next action. If
a decision cannot yet be made, record exactly what information is missing.



