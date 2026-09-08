## What this is
Two classes working together. Student holds one person's info (name, id, age, grades) and can work out its own average/min/max. Classroom holds a bunch of Student objects and can print a report on all of them.

## Try it yourself
Make a class for one thing that keeps a list of numbers and can tell you its own average/min/max. Then make a second class that holds a bunch of the first one, and can report on all of them - without copying anyone's data into a new dict, just by asking each object directly.

## What I learned
Don't copy an object's data into a separate dict just to display it. Just store the actual object, and grab what you need from it when you need it (student.age, student.average()). That way if something changes later, you're always seeing the real, current value - not a stale copy.


## Topics
classes, self, one class holding a list/dict of another class's objects, working with the real object instead of copying its data, json.dumps()


## Mistakes made while building this
- Called Student.add_grades(grades) instead of new_student.add_grades(grades) - calling a method on the class itself instead of on an actual object. A method needs a real object (self) to know whose data to change.
- Manually rebuilt a dict of {age, id, grades, average, min, max} from an object's fields inside the Classroom class, duplicating data that was already sitting in the Student object itself. Simplified to storing the object directly, and generating that display dict fresh, on demand, only when producing a report.
- Confused json.dumps() (formats a dict as a string, for display) with json.dump() (writes a dict to an actual file) - similar names, genuinely different jobs.
- Had to work through, in real depth, exactly when a new object is created vs. when a reused loop variable just gets reassigned - and why an object only stays reachable if something (like a list or dict) is actually holding a reference to it before the variable moves on to the next one.

