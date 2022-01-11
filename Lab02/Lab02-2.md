## URBAN 5123 Programming Tools for Urban Analytics
## Spring 2022
## Lab02-2: Git and GitHub

### Objectives

 - Understand the difference between different types of repositories
 - Familiarize yourself with key git commands from the command line
 - Create a branch
 - Learn how to use pull requests

### Instructions

#### Set up git client on local macine

 1. For the operating system on your laptop/desktop follow the instructions
    [here][git_cli] to install git for the command line.
 2. You may need to install Xcode command line tools by running `xcode-select --install` in the terminal to use git in macOS.

#### Repositories and setting up

 1. Fork your individual repository from the organization account (qszhao/PTUA2022) to your
    individual GitHub repository (you should have done it in the first lab session).
 2. Get your [ssh keys][ssh] setup on your individual GitHub repository (please follow the instruction in the link).

#### Git on the Command Line

 1. Using the command line on your local machine, [clone][clone] your individual GitHub
    repository (it should be yourusername/PTUA2022, not the organization repository (qszhao/PTUA2022)) for the course (please follow the instruction in the link).
 2. Use `git remote -v` to check your origin (this needs to be in your local clone repository folder) 
 3. Use `git remote add upstream https://github.com/qszhao/PTUA2022.git` to set the organizational account as upstream
 4. You can get the newest update in the organizational account master branch by `git pull upstream master` (you don't need to do it if you just fork the organizational repository to your own github account.)
 5. Create a [branch][branch] called `Lab02`
 6. Checkout the branch `Lab02` by `git checkout Lab02`
 7. On the local machine create a new folder in the repository called `Lab02`
 8. In that folder create a python script called `Lab02.py` that prints out all
    odd numbers between 0 and 100.
 9. Add your `Lab02.py` to the repository 
 10. Use `git status` to see the file change
 11. Add file change by `git add Lab02.py`
 12. Commit by using `git commit -m "add a python file"`
 13. Push your commits to the repos on your individual GitHub account by `git push origin master` or other branch such as `git push origin Lab02`

#### Pull Requests
 1. On your personal GitHub account create a [pull request][pr] based on the commits
    for this exercise. The target should be the `master`  branch of your individual repository on the
    organization account. The origin should be the `Lab02` branch on your personal remote GitHub repository.


[branch]: https://GitHub.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches
[pr]: https://help.GitHub.com/articles/using-pull-requests
[ssh]: https://help.GitHub.com/articles/generating-ssh-keys
[git_cli]: http://git-scm.com/book/en/Getting-Started-Installing-Git
[clone]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository

