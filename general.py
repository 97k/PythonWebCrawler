import os

# Every website has a separte directory


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Directory...")
        os.makedirs(directory)


''' Each crawler has two fields viz queue and crawled. queue consists of all the links that aren't crawled yet
and crawled contains all the likns which our crawler has crawled!'''

# Creating queue and crawled files only if they don't exist.


def create_files(project_name, base_url):
    queue = project_name+'/queue.txt'
    crawled = project_name+'/crawled.txt'

    if not os.path.isfile(queue):
        make_file(queue, base_url)
    if not os.path.isfile(crawled):
        make_file(crawled, '')

# Create new file method


def make_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data to existing files


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of the files


def empty_file(path):
    with open(path, 'w'):
        pass  # Do nothing


''' Using only files will results in using heavy resources and hence is not a good method. What we are going to use is a 'set'.
Set is built in to python. TO know more about sets go check out this link. https://docs.python.org/2/library/sets.html'''

# Read the file and convert it to set


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item will be a new line in the file


def set_to_file(links, file):
    empty_file(file)
    for link in links:
        append_to_file(path=file, data=link)
