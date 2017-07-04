import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description='CLI Tool to organize a folder based on extension.')
    parser.add_argument('--directory', dest='directory', default=os.getcwd(),
        help='Directory to organize. Defaults to current directory')
    parser.add_argument('--verbose', dest='verbose', default=False,
        action='store_true', help='Set to print out everything that happens')
    parser.add_argument('--dry-run', dest='dryRun', default=False,
        action='store_true', help="Don't actually move anything, just write out changes")

    return parser
