import click
from lib.func import do_something_with, do_a_different_thing

@click.command()
@click.option('--mode', '-m', help='mode [something|different]')
@click.option('--thing', '-t', help='a thing', default=None)
def main(mode, thing):
    if mode == "something":
        print("Doing Something")
        if thing is None:
            raise Exception("A thing must be provided.")
        do_something_with(thing)
    elif mode == 'different':
        if thing is not None:
            raise Exception("A thing is not necessary for the different thing.")
        do_a_different_thing()
    else:
        raise Exception("Invalid mode.")

if __name__ == '__main__':
    main()
