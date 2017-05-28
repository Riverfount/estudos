#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def rank_names(names):
    """
    Given a list of tuples with ranking, male name and female return a list of male and female names with their ranking.
    :param names: the tuple with the data.
    :return: a list with names and its ranking
    """
    names_rank = []

    for i in range(len(names)):
        names_rank.append(names[i][1] + ' ' + names[i][0])
        names_rank.append(names[i][2] + ' ' + names[i][0])
    return names_rank


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename) as texto:
        contents = texto.read()

    re_ano = re.compile(r'<h3 align="center">[A-z]\w+\s[a-z]\w+\s(\d+)</h3>')
    re_babies = re.compile(r'<td>(\d+)</td><td>([A-z]\w+)</td><td>([A-z]\w+)</td>')

    ano = re.search(re_ano, contents)
    names = re.findall(re_babies, contents)
    names_rank = rank_names(names)
    names_rank.sort()
    if sys.argv[3]:
        names_rank = ano.group(1) + ' ' + ', '.join(names_rank)
    else:
        names_rank.insert(0, ano.group(1))
    return names_rank



def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    if summary:
        with open(sys.argv[3], 'w') as texto:
            texto.write(extract_names(sys.argv[2]))
        print('Arquivo gerado com sucesso!')
    else:
        print(extract_names(sys.argv[1]))

if __name__ == '__main__':
    main()
