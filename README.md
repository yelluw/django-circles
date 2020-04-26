# django-circles
django-circles allows you to organize users into collaborator circles.

Compatible with Django 3.0 and up


This app is very minimal code wise on purpose.
The choice was to give you the flexibility to
expand functonality without making things too complex.

# License

MIT

# Install

NOTE: Not yet released to Pypi!

`pip install django-circles`

# Requirements

None.

# How to use

There are two objects:

- Circles
- CircleUser

A `Circle` defines a group that users can belong to.

There is a handy circle factory utility in the `utils.py` file
that allows you to easily create circles. This utility also
creates a `CircleUser` and relates it to the circle. Also gives
the `CircleUser` the permissions to manage the `Circle` by setting
the field `CircleUser.is_manager` to `True`.

A `CircleUser` relates users to circles. It allows you
to define who can manage circles (any actions you define
for circles would require the user to be marked as manager).
For example, allowing someone to change the name of the circle would
require them to have the field `is_manager` set to `True`.
It is up to you how this funcitonality is used.
Note that it was not tied to django's permissions functionality
on purpose.