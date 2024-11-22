'''
pyGraphviz on Windows sucks. Luckily i can create and render
my own dotfiles with blackjack and hookers!
'''

first_line = 'digraph D {'
last_line = '}'

edge_tmpl = '{src} -> {tgt}'


def dict2dot(input_dict, filename='dict.dot', solution=None):
    '''
    Create dotfile from dict
    '''
    graph_lines = []

    if solution:
        # print(type(solution[0].pos))
        first, *middle, last = solution
        dup_start = sorted(list(first.pos), key=len)
        dup_finish = sorted(list(last.pos), key=len)
        start = [item for item in dup_start if item]
        finish = [item for item in dup_finish if item]
        start_node = '_'.join(start) + ' [is_start=1, on_path=1]'
        finish_node = '_'.join(finish) + ' [is_finish=1, on_path=1]'
        graph_lines.extend([start_node, finish_node])
        graph_lines.extend([
            '_'.join([
                s for s in sorted(list(item.pos), key=len) if s
            ]) + ' [on_path=1]'
            for item in middle
        ])

    for key, value in input_dict.items():
        if not value:
            continue
        dup = sorted(list(value.pos), key=len)
        canonic_value = tuple(dup)

        # "your code is the worst i've ever run!" ... "but it runs"
        src_str = str(canonic_value).replace("(", '').replace(")", '').replace("'", '').replace(',', '').strip().replace(" ", "_")
        tgt_str = str(key).replace("(", '').replace(")", '').replace("'", '').replace(',', '').strip().replace(" ", "_")

        graph_lines.append(edge_tmpl.format(src=src_str, tgt=tgt_str))

    cont = '\n'.join([
        first_line,
        *graph_lines,
        last_line,
    ])
    with open(filename, 'w') as dotfile:
        dotfile.write(cont)
