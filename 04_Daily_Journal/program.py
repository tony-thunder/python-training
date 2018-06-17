import journal

def print_header():
    print('--------------------------')
    print('      DAILY JOURNAL')
    print('--------------------------')
    print()


def list_entries(data):

    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit:')
    journal.add_entry(text, data)


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and not cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd != 'x' and cmd:
            print("Sorry, we do not understand {}.".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def main():
    print_header()
    run_event_loop()


main()
