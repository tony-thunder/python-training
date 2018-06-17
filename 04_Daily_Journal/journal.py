import os


def load(name):
    """

    :param name:
    :return:
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return []


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving to: {}".format(filename))

    with open(filename, 'w') as fout:

        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', + name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    return None