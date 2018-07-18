import argparse as ap
import model


class CLIHandler:
    """
    Class for Handling CLI arguments that trigger the script
    """
    def __init__(self):
        pass

    def parse(self):
        pass


if __name__ == '__main__':
    # Parse arguments
    arguments = CLIHandler().parse()

    # Download the file if flag is there
    if arguments.download:
        model.download(arguments.url)
