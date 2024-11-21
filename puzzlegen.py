'''
Generator for puzzles in this stupid puzzle game my mum plays
'''

import string
import random


def gen_puzzle(tower_count, empty_count, maxheight, letters=None):
    '''
    Generate puzzles for momspuzzle to check on parameters
    needed to be solvable and explore solution graph sizes
    '''
    if not letters:
        letters = random.sample(
            string.ascii_uppercase,
            k=tower_count,
        )
    assert len(letters) == tower_count, 'Letters dont match tower_count'
    raw_stacks = ''
    for letter in letters:
        raw_stacks += letter * maxheight

    raw_stacks = ''.join(random.sample(raw_stacks, len(raw_stacks)))

    stacks = [
        raw_stacks[ i : i + maxheight ]
        for i in range(0, len(raw_stacks), maxheight)
    ]
    for _ in range(empty_count):
        stacks.append('')
    return stacks, letters


if __name__ == '__main__':
    stacks, letters = gen_puzzle(
        tower_count=10,
        empty_count=2,
        maxheight=4,
        letters=None
    )
    print(letters)
    print(stacks)
