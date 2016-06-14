# -*- coding: utf-8 -*-


def get_version():
    return '{{ cookiecutter.version }}'

def main_version():
    """ main function to return version if required """
    import argparse
    this_parser = argparse.ArgumentParser(description='')
    this_parser.add_argument('-V', '--version',
                             action='version',
                             version='%(prog)s ' + get_version(),
                             help='Return the current version')
    dummy_args = this_parser.parse_args()  # NOQA

if __name__ == '__main__':
    main_version()
