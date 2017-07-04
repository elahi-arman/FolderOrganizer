import os
import shutil
import sys
import argparse

import Config
import Parser

def createFolders(workDir, dryRun = True, verbose = True):
    availableFolders = os.listdir(workDir)
    for folder in Config.folders:
        if folder not in availableFolders:
            if not dryRun:
                os.mkdir(os.path.join(workDir, folder), os.W_OK)
            if verbose:
                print('Creating directory: {}'.format(os.path.join(workDir, folder)))

def moveFiles(workDir, dryRun = True, verbose = True):
    associatedFiles = Config.mappings.keys()
    for f in os.scandir(workDir):
        if f.is_file:
            try:
                extension = f.name.split('.')[-1]
                source = f.path
                destination = os.path.join(workDir, Config.mappings[extension], f.name)

                if not dryRun:
                    shutil.move(source, destination)

                if verbose:
                    print('{} -> {}'.format(source, destination))

            except IndexError:
                print('No extension on file: {}'.format(source))
                # sys.exit(102341)
            except KeyError:
                print('No mapping associated with extension: {}'.format(extension))
                # sys.exit(104123)

if __name__ == '__main__':
    args = Parser.create_parser().parse_args()

    print('Working in directory: {}'.format(args.directory))

    if args.verbose:
        print('Running in verbose mode')

    if args.dryRun:
        print('Doing a dry run, not actually moving any files.')

    print ('\n\n')

    if os.access(args.directory, os.W_OK):
        createFolders(args.directory, args.dryRun, args.verbose)
        moveFiles(args.directory, args.dryRun, args.verbose)
    else:
        parser.print_help()
