import os
import collections
import argparse
import fnmatch
import json
import sys
from multiprocessing import Queue, Process
import multiprocessing
import matplotlib.pylab as plt

# Initiate the argument parser
parser = argparse.ArgumentParser(
    description="***** Count and Plot the number of files and directories matching glob patterns *****", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-d", "--root-dir", required=True,
                    help="Directory path to count files\nExamples:\n--root-dir /Users/cvadgama\n-d /Users/cvadgama/")
parser.add_argument("-p", "--patterns", nargs='*', type=str, required=True,
                    help="Names or glob patterns for files and directories\nExamples:\n--patterns *test*\n--patterns 'data.json' '*test*' 'coffee.cson'")

# Parse
args = vars(parser.parse_args())

if not os.path.isdir(args["root_dir"]):
    print("Invalid Directory: {0}".format(args["root_dir"]))
    sys.exit(1)


def prettyprint(_dict):
    print(json.dumps(_dict, indent=4))


class DirectorySearch(object):
    def __init__(self, search_dir, search_pattern):
        self.search_dir = search_dir
        self.search_pattern = search_pattern
        self.WalkedDir = collections.namedtuple("WalkedDir", "subdirs files")
        self.cpu_count = multiprocessing.cpu_count()
        self.total_count = []

    def find_directories(self):
        directories = []
        for root, dirs, files in os.walk(self.search_dir):
            for dir in dirs:
                dirpath = os.path.join(root, dir)
                if os.path.isdir(dirpath):
                    directories.append(dirpath)
        directories.append(self.search_dir)
        return directories

    def search(self, top, file_pattern=None, dir_pattern=None):
        """
        Search method to find out files and directories with given patterns within current directory only
        """
        files = []
        subdirs = []
        try:
            for f in os.listdir(top):
                if os.path.isfile(os.path.join(top, f)):
                    files.append(f)
        except OSError as e:
            if e.errno == 1:
                print(e)
            pass
        try:
            for d in os.listdir(top):
                if os.path.isdir(os.path.join(top, d)):
                    subdirs.append(d)
        except OSError as e:
            if e.errno == 1:
                print(e)
            pass
        if file_pattern is not None:
            files = fnmatch.filter(files, file_pattern)
        if dir_pattern is not None:
            subdirs = fnmatch.filter(subdirs, dir_pattern)

        yield self.WalkedDir(subdirs, files)

    def count_files(self, dir):
        """
        Count Files within specified directory
        :param dir: Directory Path
        :return: Number of Files matching pattern
        """
        total_count = 0
        for dir_info in self.search(dir, file_pattern=self.search_pattern):
            if dir_info.files:
                total_count += len(dir_info.files)
        return total_count

    def count_directories(self, dir):
        """
        Count Directories within specified directory
        :param dir: Directory Path
        :return: Count of Directories matching pattern
        """
        total_count = 0
        for dir_info in self.search(dir, dir_pattern=self.search_pattern):
            if dir_info.subdirs:
                total_count += len(dir_info.subdirs)
        return total_count

    def queue_count_of_patterns(self, dirs, q):
        """
        Build a queue with count of patterns
        :param dir: List of Directories
        :return: ""
        """
        try:
            result = []
            for dir in dirs:
                count_of_files_and_dirs = self.count_directories(dir) + self.count_files(dir)
                result.append(count_of_files_and_dirs)
        except:
            q.put([])
            raise
        q.put(result)

    def multi_processor(self):
        """
        Fork multiple processes amongst total CPUs and update self.total_count with queue values
        :return:
        """
        directories = self.find_directories()
        q = Queue()
        procs = []
        for i in xrange(self.cpu_count):
            lst = [directories[j] for j in xrange(0, len(directories)) if j % self.cpu_count == i]
            if len(lst) > 0:
                p = Process(target=self.queue_count_of_patterns, args=([lst, q]))
                p.start()
                procs += [p]

        for i in xrange(0, len(procs)):
            self.total_count += q.get()


# Plotter Class to plot the count of patterns
class Plotter(object):
    def __init__(self, results={}):
        self.results = results

    def plot(self):
        """
        Plot the results dictionary.
        X-axis: Patterns
        Y-axis: Count of Files and Directories matching patterns
        :return:
        """
        yaxis = self.results.values()
        xaxis = [i for i in range(len(self.results.keys()))]
        x_labels = self.results.keys()
        plt.bar(xaxis, yaxis, tick_label=x_labels, width=0.8)
        plt.xlabel('Patterns')
        plt.ylabel('Count of Patterns')
        plt.title('Number of Files and Directories matching patterns')

    def show_plot(self):
        plt.show()


if __name__ == "__main__":
    results = {}
    for pattern in args["patterns"]:
        ds = DirectorySearch(search_dir=args['root_dir'], search_pattern=pattern)
        ds.multi_processor()
        results[pattern] = sum(ds.total_count)
    print("*********** Files and Directories matching specified patterns ***********")
    prettyprint(results)
    plotter_object = Plotter(results)
    plotter_object.plot()
    show_plot = raw_input("Do you want to see the plot of total directories and files? [yes/no] ")
    if show_plot.lower() == "yes":
        plotter_object.show_plot()
    print("Script Completed !")
