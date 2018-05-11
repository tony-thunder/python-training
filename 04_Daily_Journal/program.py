import journal

def print_header():
    print('--------------------------')
    print('      DAILY JOURNAL')
    print('--------------------------')
    print()


def list_entries():
    print('Listing...')


def add_entry():
    print('Adding...')


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = None
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd != 'x':
            print("Sorry, we do not understand {}.".format(cmd))

    print('Done, goodbye.')



def main():
    print_header()
    run_event_loop()


main()
