# momspuzzle

One of these little projects done simply because i can.

My mom plays puzzle games on her tablet. This one caught my
attention, it's like Towers of Hanoi but with colors and
more poles. Still the puzzle solver Raymond Hettinger once
presented to me should do the trick quite easily. Maybe we
even add some sweet visuals in order to explain the difficulty
of such puzzles. In my rommantic brain we can even explore our
own ability to solve such puzzles and show the magic of the
human mind as we're sometimes able to take magic shortcuts in
the huge graphs we're often confronted with while solving
puzzles or making decisions in general. Well, what a colorful
docstring this is. Enough cheap talk. Let's implement mom's
stupid puzzle for good.

# Usage

Windows

```powershell
python.exe .\momspuzzle.py
```

## Tests and scaling thoughts

We have 12 ( later maybe N ) poles, 2 of them are empty.
10 poles are filled with 4 disks of random colors, 10 colors
in total respectively. Goal is to "sort" the colors, so
we get 10 sorted poles and two empty ones. Like Tower of
Hanoi but with colors. Will use letters as representation.

And maybe start simpler ... small problems and fixed goal

maxheight = 2
pos = ('RG', 'GR', '')
goal = ('GG', 'RR', '')

**
this is not solvable,
we can "dig" down to "B" but have no space left to move it
**
maxheight = 3
pos = ('RGB', 'RGB', 'RGB', '',)
goal = ('RRR', 'GGG', 'BBB', '',)

**
adding another empty pole makes it solvable
**
maxheight = 3
pos = ('RGB', 'RGB', 'RGB', '', '',)
goal = ('RRR', 'GGG', 'BBB', '', '',)

maxheight = 4
pos = ('ABCD', 'BCDA', 'DACB', 'CDAB', '',)
goal = ('AAAA', 'BBBB', 'CCCC', 'DDDD', '',)

maxheight = 5
pos = ('ABECD', 'EBCDA', 'DEACB', 'CDAEB', 'CEABD', '', '')
goal = ('AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'EEEEE', '', '')

Well the goal must be "softer", in mom's
game the positions of the sorted stacks doesn't matter.
Let's implement a custom isgoal method for that.

maxheight = 2
letters = ['R', 'G']
pos = ('RG', 'GR', '')

maxheight = 4
letters = ['A', 'B', 'C', 'D']
pos = ('ABCD', 'BCDA', 'DACB', 'CDAB', '',)

**
Still two empty stacks needed
**
maxheight = 5
letters = ['A', 'B', 'C', 'D', 'E']
pos = ('ABECD', 'EBCDA', 'DEACB', 'CDAEB', 'CEABD', '', '')

**
Getting closer to the scale ( level ) mom plays on
**
maxheight = 6
letters = ['A', 'B', 'C', 'D', 'E', 'F']
pos = ('ABECDF', 'EBFCDA', 'DEAFCB', 'CFDAEB', 'FCEABD', 'BEADFC', '', '')

**
Scaling slowly starting to hurt ...
**
maxheight = 7
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
pos = (
    'ABECGDF',
    'EBFCDAG',
    'GDEAFCB',
    'CFGDAEB',
    'FCEGABD',
    'BGEADFC',
    'EGBCADF',
    '',
    ''
)

**
This one shows we're reaching a limit: ~50 GB RAM consumed ...
**
maxheight = 8
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pos = (
    'ABECGHDF',
    'HEBFCDAG',
    'GDEHAFCB',
    'CFGDAHEB',
    'FCEHGABD',
    'BGEHADFC',
    'EHGBCADF',
    'DFHACEBG',
    '',
    ''
)

Massively improve performance by implementing canonical method,
as order of poles does not matter for the solver. Now i think
we can reach mom's level, but it's getting late. This was cool
journey so far. TO BE CONTINUED!
