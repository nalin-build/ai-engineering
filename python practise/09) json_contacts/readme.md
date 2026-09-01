JSON-based contact book with persistence. Asks for a filename, loads existing contacts if the file exists (starts fresh if not), then lets you add new contacts or edit existing ones in one loop, saving everyone back to the file as proper nested JSON when done.

Mistakes:
- Called file.load() instead of json.load(file) - json.load is a function that takes the file as an argument, not a method that lives on the file object itself.
- Tried to do contacts[name]['phone'] = phone for a brand new name before creating contacts[name] = {} first - crashed with a KeyError, since there was nothing at that key to index into yet.
- Had a real misunderstanding I had to think through: assumed that once some contacts in the dict had a {phone, email} shape, any new key added later would automatically get that same shape (kind of like a spreadsheet). Dicts don't work that way - every key is independent, and each new one has to be explicitly built, regardless of what other entries already look like.

Topics: import json, json.load(), json.dump() with indent=, comparing JSON's built-in nesting support to CSV's flat rows