def progress_bar(value):
    percent = value / 100
    stars = int(20 * percent)
    spaces = 20 - stars
    return f"{value:>3d}% [{'*' * stars}{' ' * spaces}]"