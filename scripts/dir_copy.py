import os
import shutil
import string
import sys

def get_dirs_to_copy(dir, primary_file_extension):
    dirs_to_copy = []
    for dirname, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            fileName, fileExtension = os.path.splitext(filename)
            if string.upper(fileExtension) == string.upper(primary_file_extension):
                dirs_to_copy.append(dirname)
                continue
    
    return dirs_to_copy

primary_file_extension = sys.argv[1]
source_dir = sys.argv[2]
target_dir = sys.argv[3]
keep_file_extensions = sys.argv[4:]
keep_file_extensions.append(primary_file_extension)

print 'Searching ' + source_dir + ' for dirs containing files of type ' + \
primary_file_extension + ' to copy to ' + target_dir

# which dirs contain the primary file type?
dirs_to_copy = get_dirs_to_copy(source_dir, primary_file_extension)
print 'Found ' + str( len(dirs_to_copy) ) + " dirs of interest...\n"

for dir in dirs_to_copy:
    print '\t' + dir + " contains a " + primary_file_extension + " file. Filtering other contents..."
    # only copy files with specified extensions
    files_to_copy = []
    files_in_dir = os.listdir(dir)
    for file in files_in_dir:
        file_name, file_extension = os.path.splitext(file)
        if file_extension in keep_file_extensions:
            files_to_copy.append(file)
    
    print '\tFiles to copy for dir ' + dir + ': ' + str(files_to_copy)
    
    for file_to_copy in files_to_copy:
        # figure out the full path for the target directory
        relative_dir_path = dir.rpartition(source_dir)[2] + '/'
        relative_file_path = relative_dir_path + file_to_copy
        target_file_path = target_dir + relative_file_path
        source_file_path = source_dir + relative_file_path
        # create parent file if necessary
        directory = os.path.dirname(target_file_path)
        if not os.path.exists(directory):
            print '\t\t\tMaking parent directory at ' + directory
            os.makedirs(directory)
            print '\t\t\tMade parent directory at ' + directory
        # copy the file
        print '\t\tCopying ' + relative_file_path + " to " + target_dir
        shutil.copyfile(source_file_path, target_file_path)
        print '\t\tCopied ' + relative_file_path

