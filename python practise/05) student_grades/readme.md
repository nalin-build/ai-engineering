Grade book that tracks multiple students and their scores using a dict of lists ({name: [scores]}). Can add scores for any student at any time and prints everyone's average at the end.

Mistakes:
- Wasn't sure at first whether add_score needed to return the dict. Learned that lists/dicts are passed by reference, not copied - modifying grades[name] inside the function changes the same dict main() already has, so no return was needed. Only functions that compute brand new values (like average_score) need to return something.
- Debated whether to build one big function that loops over the whole dict and returns a finished averages dict, vs a small function that handles one student at a time, called from a loop in main(). Went with the small, single-purpose version (average_score just handles one name) and put the "loop over everyone" logic in main() instead.

Topics: dicts of lists, .append() on a nested value, passing dicts/lists by reference vs return values,