import unicodedata


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def u_to_ascii(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')