Counts how often each word appears in a sentence, using a dict as a tally. Splits input into words, cleans each one (lowercase, strips punctuation), then counts occurrences.

Mistakes:
- Used word_count(word) instead of word_count[word] - parentheses call a function, brackets access a dict/list. Same bug I hit in list stats, still catches me.
- Tried word_count = {word, 1} to add an entry - that's actually set syntax, not how you set a dict key, and it would've wiped the whole dict anyway since = replaces everything. Correct way: word_count[word] = 1.
- Punctuation-only "words" (like a lone "?") stripped down to an empty string and got counted as a real word. Fixed by checking if word == "" and using continue to skip it.

Topics: dicts, .split(), .strip(), .lower(), .items(), continue