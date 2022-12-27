import os
import subprocess
import git
import shutil
# given hash id of commit and file, return the diff of the source codes from github

# read the txt file
# format = hash1, hash2, file1, file2, github_url, jira_key
# return hash1, hash2, file1, file2, github_url, jira_key
def clone(github_url:str):
    # current working directory
    cwd = os.getcwd()
    # check if repo directory exists
    if not os.path.exists('repo'):
        os.mkdir('repo')
    # check if sources directory exists
    if not os.path.exists('sources'):
        os.mkdir('sources')
    # clone the repository under the repo folder
    git.Git(os.path.join(cwd, 'repo')).clone(github_url)
    # return the path to the local repository
    return os.path.join(cwd, 'repo')

def checkout(gitpath:str, hash:str):
    # checkout the commit hash
    try:
        git.Git(gitpath).checkout(hash)
    except:
        print(f'hash {hash} not found')
        return False
    return True

def convert_path(path, to='linux'):
    # replace the '/' with '\'
    if to == 'linux':
        return path.replace('\\', '/')
    elif to == 'windows':
        return path.replace('/', '\\')

def path_to_filename(path):
    path = path.split('/')[-1]
    # remove .java
    path = path[:-5]
    return path

def copy_file(local_repo:str, file:str, dest:str, new_name:str=None):
    # copy the file from the local repo to the destination
    path = convert_path(os.path.join(local_repo, file))
    try:
        if new_name is None:
            # copy the file to the destination
            shutil.copy(path, dest)
        else:
            # copy the file to the destination with a new name
            shutil.copy(path, os.path.join(dest, new_name))
    except:
        print(f'file {path} not found')
        return False
    return True

def read_input(path):
    # read a line from the txt file
    with open(path, 'r') as f:
        line = f.readline()
        # split the line into a list
        line = line.split(',')
    hash1 = line[0]
    hash2 = line[1]
    file1 = line[2]
    file2 = line[3]
    github_url = line[4]
    jira_key = line[5]
    return hash1, hash2, file1, file2, github_url, jira_key

def reponame(github_url):
    return github_url.split('/')[-1]

def main():
    input = 'input.txt'
    print(f"reading input from {input}")
    hash1, hash2, file1, file2, github_url, jira_key = read_input(input)
    print("========================")
    print(f"jira key: {jira_key}")
    
    print(f"hash1: {hash1}")
    print(f"hash2: {hash2}")
    print(f"file1: {file1}")
    print(f"file2: {file2}")
    print(f"github url: {github_url}")
    print("========================")

    # clone the repository
    repo_name = reponame(github_url)
    # if the repo is already cloned, skip the clone step
    if not os.path.exists(os.path.join('repo', repo_name)):
        local_repo = clone(github_url)
    else:
        local_repo = os.path.join('repo', repo_name)
    cwd = os.getcwd()
    local_repo = convert_path(os.path.join(cwd, 'repo', repo_name))
    print(f"local repo : {local_repo}")
    print("========================")

    newfile1 = f"{path_to_filename(file1)}_old.java"
    newfile2 =f"{path_to_filename(file2)}_new.java"

    # checkout the commit hash1
    if not checkout(local_repo, hash1):
        return
    # copy the file1 to the sources folder
    if not copy_file(local_repo, file1, 'sources', newfile1):
        return

    # checkout the commit hash2
    if not checkout(local_repo, hash2):
        return
    # copy the file2 to the sources folder
    if not copy_file(local_repo, file2, 'sources', newfile2):
        return
    # checkout the commit
    try:
        diff = git.Git(os.path.join(os.getcwd(), 'sources')).diff(newfile1, newfile2)
        print(f"diff: {diff}")
    except:
        print(f'file {newfile1}, {newfile2} not found')
        return False
    
    # write diff as diff.txt
    with open('diff.txt', 'w') as f:
        f.write(diff)

if __name__ == '__main__':
    main()
