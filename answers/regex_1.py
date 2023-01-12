def parse_names():
    names = []
    with open('data/baby1996.html') as fin:
        rex = re.compile(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')
        for line in fin:
            m = rex.match(line)
            if m:
                names.append({
                    'rank': m.group(1),
                    'name': m.group(2),
                    'sex': 'male',
                })
                names.append({
                    'rank': m.group(1),
                    'name': m.group(3),
                    'sex': 'female',
                })
    return names