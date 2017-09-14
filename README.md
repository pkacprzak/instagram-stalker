Instagram Stalker
=======================

instagram-stalker is a command-line application written in Python and targeted
to OSX users. It observes given Instagram account and notifies with system notifications
when he makes his account public. Use responsibly.

Install
-------
To install instagram-stalker:
```bash
$ pip install instagram-stalker
```

To update instagram-stalker:
```bash
$ pip install instagram-stalker --upgrade
```

Usage
-----

To start observing a user's account for public/private status changes:
```bash
$ instagram-stalker <username>             
```

OPTIONS
-------

```
--help -h           Show help message and exit.

--interval  -i      Frequency of refreshing the status in minutes.

-sound  -s    Play sounds while notifying.

--verbose    -v     Prints console info when the status is still private

```

License
-------
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


This project does not aim to cover best practices for Python project
development as a whole. For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

----
