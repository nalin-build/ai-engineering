FizzBuzz with a user-defined range instead of the fixed 1-100. Asks for a start and end number, validates both are real integers, and checks that start is less than end before running FizzBuzz (Fizz on multiples of 3, Buzz on multiples of 5, FizzBuzz on both) across that range.

Mistakes:
- Used return instead of break on the validation loop's success path - return exits the whole function, not just the loop, so the FizzBuzz loop below it never ran (VS Code even greyed it out as unreachable code).
- Learned to pass a string into a function as a parameter (the label for start/end prompts) instead of hardcoding the prompt text.

Topics: functions, loop, condition, try/except