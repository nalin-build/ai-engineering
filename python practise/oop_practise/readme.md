## What this practices
A BankAccount class using core OOP concepts: __init__, instance attributes (self), methods, and a @property/@setter pair for validated data (balance can never go negative, checked automatically on every change - not just at creation).

## Try it yourself
Before looking at the code: build a class representing something with one value that has a rule attached to it (a balance that can't go negative) - with a getter/setter enforcing that rule, plus at least one method that changes the value through some action (deposit/withdraw)


- Passed raw strings straight from input() into the class without converting with float() first - the setter's `< 0` comparison crashed trying to compare a string to a number. Same input-conversion rule I already knew from plain functions, just easier to miss once it's happening inside a class method instead of a visible function call.
- Realized self.balance = self.balance + amount inside deposit() secretly triggers both the getter (reading the current value) AND the setter (validating and storing the new one)

## Topics
class, __init__, self, instance methods, @property, @x.setter, raise ValueError, try/except with `as e` to access the error message