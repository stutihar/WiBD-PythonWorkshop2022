def not_bad(s):
    not_idx, bad_idx = s.find('not'), s.find('bad')
    if 0 <= not_idx < bad_idx:
        return s[:not_idx] + 'good' + s[bad_idx + len('bad'):]
    return s