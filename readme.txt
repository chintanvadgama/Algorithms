Project Description:
====================
findAllMatchingPattern.py script can be used to count and plot the number of files and directories matching multiple Patterns

Getting Started:
================
1. For Help,
    python findAllMatchingPattern.py --Help

2. For searching a single pattern in a directory,
    python findAllMatchingPattern.py -d /Users/cvadgama -p test

3. For searching multiple patterns in a directory,
    python findAllMatchingPattern.py -d /Users/cvadgama -p 'test' '*.cson' '*.txt'

Overview:
=========
The script uses python's multiprocessing module for the parallel processing of directories.
DirectorySearch Class:
    1. The class holds namedtuple object of files and directories
    2. This class will take directory_path and pattern to instantiate

    Methods:
    --------
    0. find_directories() - Return all directories within root Directory
    1. search() - This method will search for files and directories matching pattern within given directory
    2. count_files() - Returns the count of files in a directory_path
    3. count_directories() - Returns the count of directories in a directory_path
    4. queue_count_of_patterns() - It will create a queue of (file_count + directory_count) for a pattern
    5. multi_processor() - Create a process which takes a single directory as argument. Then, depending on the number of CPUs on system it will spawn the processes amongst multiple CPUs

Plotter Class:
    It can create plot from any dictionary object

    Methods:
    --------
    0. plot() - Creates a plot using matplotlib library
    1. show_plot() - Shows a created plot by Plotter() instance

Authors:
========
Chintan Vadgama
