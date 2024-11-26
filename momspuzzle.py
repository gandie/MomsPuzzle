from puzzle import Puzzle
from dict2dot import dict2dot
from puzzlegen import gen_puzzle


class MomsPuzzle(Puzzle):
    '''
    Derived from base Puzzle class but providing method
    to switch class variables to adjust initial state
    '''

    maxheight = 4
    letters = ['X', 'P', 'V']
    pos = ('XPPP', 'XXPV', 'XVVV', '', '')

    @classmethod
    def set_setting(cls, maxheight, letters, pos):
        cls.maxheight = maxheight
        cls.letters = letters
        cls.pos = pos

    def isgoal(self):
        '''
        We need one stack of each given letter on max height
        '''
        for letter in self.letters:
            tgt_stack = self.maxheight * letter
            if tgt_stack not in self.pos:
                return False
        return True

    def canonical(self):
        '''
        The order of stacks is irrelevant,
        so canonical notation can be sorted!
        '''
        dup = sorted(list(self.pos), key=len)
        return repr(tuple(dup))

    def __iter__(self):
        '''
        Main method yielding possible new positions from initial state,
        implementing game rules:
        - stacks can only have <maxheight> letters
        - we can only stack matching letters on top of another
        '''
        for index, src_stack in enumerate(self.pos):
            if not src_stack:
                continue
            disk = src_stack[0]
            stackleft = src_stack[1:]
            for tgt_index, tgt_stack in enumerate(self.pos):
                if tgt_index == index:
                    continue
                if len(tgt_stack) == self.maxheight:
                    continue
                if tgt_stack and tgt_stack[0] != disk:
                    continue
                newpos = list(self.pos)
                newpos[index] = stackleft
                new_stack = disk + tgt_stack
                newpos[tgt_index] = new_stack
                yield MomsPuzzle(tuple(newpos))


if __name__ == '__main__':
    from pprint import pprint
    stacks, letters = gen_puzzle(
        tower_count=6,
        empty_count=2,
        maxheight=4,
    )
    p = MomsPuzzle()
    p.set_setting(
        maxheight=4,
        letters=letters,
        pos=tuple(stacks)
    )

    solution, trail = p.solve(depthFirst=False, returnTrail=True)
    pprint(solution)
    dict2dot(trail, filename='trail.dot', solution=solution)
