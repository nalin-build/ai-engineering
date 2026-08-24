Contact book CLI with a menu (add/edit, look up, delete, list all, quit), storing contacts as a dict of dicts - {"name": {"phone": ..., "email": ...}}. Add/edit checks if a name already exists and asks before overwriting instead of silently clobbering data.

Mistakes:
- First multi-line input used /n instead of \n - forward slash does nothing, backslash-n is the real newline. Switched to triple-quoted strings for the long menu instead, cleaner to read in the source.
- Tried unpacking .items() into three variables (name, phone, email) in list_contact - .items() only ever gives key + value (two things), and the value here is the whole nested dict. Fixed by unpacking into (name, details) and indexing details['phone']/details['email'].
- In add_or_edit_contact, the "yes, edit" branch updated the contact but had no return - fell through to the top of the while loop and asked "do you want to edit?" a second time right after already editing. Added return after the update.

Topics: nested dicts (dict of dicts), del, multi-line strings, functions with no input() inside (keeping input gathering in main), chained indexing (contact[name]['phone'])