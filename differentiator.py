import git
import os

def main():
    path = os.path.join(os.getcwd(), 'sources')
    path = path.replace('/', '\\')

    # git diff
    file1 = "Airavata_new.java"
    file2 = "Airavata_old.java"

    diff = git.Git(path).diff(file1, file2)
    print(diff)

if __name__ == '__main__':
    main()