import os
import subprocess
import git
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
    git.Git(gitpath).checkout(hash)

def copy_file(local_repo:str, file:str, dest:str, new_name:str=None):
    # copy the file from the local repo to the destination
    try:
        if new_name is None:
            subprocess.run(['cp', os.path.join(local_repo, file), dest])
        else:
            subprocess.run(['cp', os.path.join(local_repo, file), os.path.join(dest, new_name)])
    except:
        print(f'file {file} not found')
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
    path = 'input.txt'
    print(f"reading input from {path}")
    hash1, hash2, file1, file2, github_url, jira_key = read_input(path)
    print(f"jira key: {jira_key}")
    # clone the repository
    repo_name = reponame(github_url)
    # if the repo is already cloned, skip the clone step
    if not os.path.exists(os.path.join('repo', repo_name)):
        local_repo = clone(github_url)
    else:
        local_repo = os.path.join('repo', repo_name)
    local_repo = os.path.join(local_repo, repo_name)
    # checkout the commit hash1
    checkout(local_repo, hash1)
    # copy the file1 to the sources folder
    copy_file(local_repo, file1, 'sources', "file1.java")

    # checkout the commit hash2
    checkout(local_repo, hash2)
    # copy the file2 to the sources folder
    copy_file(local_repo, file2, 'sources', "file2.java")
    # checkout the commit
    diff = git.Git(os.path.join(os.getcwd(), 'sources')).diff("file1.java", "file2.java")
    print(diff)

if __name__ == '__main__':
    main()
