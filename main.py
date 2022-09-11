import os
from time import time
import random


def gen_file_name():
    """Generate a random file name"""
    names = []
    with open('data/filenames.txt', 'r') as f:
        for line in f:
            names.append(line.strip().replace(' ', '_'))
            print(names[-1])
    return random.choice(names)
    

def gen_emails(count : int):
    """Generate a random file content"""
    emails = []
    with open('data/emails.txt', 'r') as f:
        for line in f:
            emails.append(line.strip())
    return random.choices(emails, k=count)

        
def write_file(path, content):
    """Write a file"""
    with open(path, 'w') as f:
        f.write('\n'.join(content))
        
        
def make_dirs_recursive(path : str, subdirs : int, files : int):
    """Create a directory tree with random files"""
    curr_path = path
    for _ in range(10):
        path = os.path.join(path, gen_file_name())
        os.mkdir(path)
        for i in range(files):
            write_file(os.path.join(path, gen_file_name()+'.txt'), gen_emails(random.randint(0, 1)))
    if subdirs > 0:
        for i in range(subdirs):
            make_dirs_recursive(curr_path+'/'+gen_file_name(), subdirs-1, files)
    

if __name__ == '__main__':
    start = time()
    make_dirs_recursive('data', 5, 10)
    
    
    print(f"Time taken: {time() - start:.2f} seconds")