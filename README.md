# A Tour of Programming Languages: JSON Calculator

Alongside this file is a file called `examples.jsonl` with a number of examples for a "JSON Calculator".

Write a program, as explained in the lecture, which can process a file like this one.
For example, it contains `{"operation": "add", "numbers": [2, 4]}`, which represents the calculation `2 + 4` via some JSON.
For each such line, print a line with the result as JSON in the form `{"result": <result>}` -- for the example above, print `{"result": "6"}`, as `2 + 4 = 6`.

Note that `numbers` can be a list of 2 *or more* numbers, and that there are 3 operations -- addition, multiplication and square root, where square root operations take a single number rather than a list!

## Cloud Shell

You are encouraged to try to do this in Google Cloud Shell!
You should immediately have a working VSCode set up there, and doing so will allow you to also follow along installing Lua and/or Ruby.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FJulianEducation%2Fpl-calculator)
