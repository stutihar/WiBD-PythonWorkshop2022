def print_ave():
    for name, scores in sorted(students.items()):
        print(f'{name}:')
        for score_name, score in sorted(scores.items()):
            ave = sum(score) / len(score)
            print(f'  {score_name}: {ave:.2f}')