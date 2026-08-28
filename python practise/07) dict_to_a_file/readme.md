Contact book that saves to a file so data survives closing the program - loads existing contacts from contact.txt on startup, lets you add/edit contacts (asks for confirmation before overwriting an existing name), then saves everyone back to the file when done.

Mistakes:
- First tried .write(contact) directly on the whole dict - crashed with TypeError, write() only accepts strings. Had to loop over .items() and build a formatted line per contact instead.
- Used "a" (append) mode to save, which meant editing an existing contact created a SECOND line in the file instead of updating the original - ended up with duplicate entries. Fixed by loading everything into one dict first (old contacts + new edits combined), then writing with "w" (overwrite) mode so the whole file gets rewritten correctly each time, no duplicates.
- Used .split() with no argument instead of .split(","), which splits on whitespace instead of the comma - left a trailing comma stuck to the name. Also caught .lower without the parentheses (referencing the method instead of calling it) - a bug I'd hit before in an earlier project.


Topics: reading/writing files (open, with, "r"/"w"/"a" modes), persisting a dict across program runs, FileNotFoundError handling,