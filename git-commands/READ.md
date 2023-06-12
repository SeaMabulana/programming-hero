# commonly used Git commands

1. git init: Initializes a new Git repository in the current directory.

2. git clone [repository]: Creates a copy of a remote repository on your local machine.

3. git add [file(s)]: Adds file(s) to the staging area, preparing them to be committed.

4. git commit -m "[message]": Records the changes to the repository, creating a new commit with a descriptive message.

5. git status: Shows the current status of the repository, including modified files and untracked files.

6. git pull: Fetches the latest changes from the remote repository and merges them into the current branch.

7. git push: Pushes the local commits to the remote repository.

8. git branch: Lists all the branches in the repository. The current branch is highlighted with an asterisk.

9. git branch [branch_name]: Creates a new branch with the given name.

10. git checkout [branch_name]: Switches to the specified branch.

11. git merge [branch_name]: Merges the specified branch into the current branch.

12. git remote -v: Lists all the remote repositories associated with the current repository.

13. git remote add [name] [url]: Adds a remote repository with the given name and URL.

14. git log: Displays the commit history, showing the author, date, and commit message for each commit.

15. git diff: Shows the differences between the working directory and the staging area.

16. git reset [file(s)]: Unstages file(s) from the staging area, keeping the changes in the working directory.

17. git revert [commit]: Reverts the changes made in the specified commit, creating a new commit.

18. git stash: Temporarily saves changes that are not ready to be committed, allowing you to switch branches.

19. git tag [tag_name]: Creates a new tag at the current commit.

20. git remote remove [name]: Removes the remote repository with the given name.

## Examples of the above git commands

- git init: Initializes a new Git repository in the current directory.
  - $ git init

- git clone [repository]: Creates a copy of a remote repository on your local machine.
  - $ git clone <https://github.com/example/repository.git>

- git add [file(s)]: Adds file(s) to the staging area, preparing them to be committed.
  - $ git add file1.txt
  - $ git add file2.txt file3.txt

- git commit -m "[message]": Records the changes to the repository, creating a new commit with a descriptive message.
  - $ git commit -m "Added new feature"

- git status: Shows the current status of the repository, including modified files and untracked files.
  - $ git status

- git pull: Fetches the latest changes from the remote repository and merges them into the current branch.
  - $ git pull origin main

- git push: Pushes the local commits to the remote repository.
  - $ git push origin main

- git branch: Lists all the branches in the repository. The current branch is highlighted with an asterisk.
  - $ git branch

- git branch [branch_name]: Creates a new branch with the given name.
  - $ git branch feature-branch

- git checkout [branch_name]: Switches to the specified branch.
  - $ git checkout feature-branch

- git merge [branch_name]: Merges the specified branch into the current branch.
  - $ git merge feature-branch

- git remote -v: Lists all the remote repositories associated with the current repository.
$ git remote -v

- git remote add [name] [url]: Adds a remote repository with the given name and URL.
  - $ git remote add origin <https://github.com/example/repository.git>

- git log: Displays the commit history, showing the author, date, and commit message for each commit.
  - $ git log

- git diff: Shows the differences between the working directory and the staging area.
  - $ git diff

- git reset [file(s)]: Unstages file(s) from the staging area, keeping the changes in the working directory.
  - $ git reset file1.txt

- git revert [commit]: Reverts the changes made in the specified commit, creating a new commit.
  - $ git revert a1b2c3d4

- git stash: Temporarily saves changes that are not ready to be committed, allowing you to switch branches.
  - $ git stash

- git tag [tag_name]: Creates a new tag at the current commit.
  - $ git tag v1.0.0

- git remote remove [name]: Removes the remote repository with the given name.
  - $ git remote remove origin

## Exta

### Git delete

1. Delete pushed commits
   - git reset --soft HEAD~1
     - ( the number specified depends on how many pushed commits to delete )
   - git push --force ( update the state of your repo )

2. Delete branch

- git branch -d branchName
  - force delete
    - git branch -D branchName

### Git update

- secure way is to use the update-ref command:
  1. git update-ref -d HEAD
  2. git add .
  3. git commit -m 'message'
  4. git push --force
  - In this case you will update everything and your repo will contain this last commit as your first

### Git clone

- git clone https://{ Token }@github.com/{ UserName }/ripo-name.git
  - When you clone a repository, Git automatically adds a shortcut called origin that points back to the “parent” repository, under the assumption that you'll want to interact with it further on down the road.

### Git branch

- git branch
  - List all of the branch in your repository. This is synonymous with:
  - ( git branch --list ).
- git branch \<branch\>
  - Create a new branch called \<branch\>. This does not check out the new branch.
  - You can choose any name for naming your branch.
- git branch -d \<branch\>
  - Delete the specified branch. This is a 'safe' operation in that Git prevents you from deleting the branch if it has unmerged changes.
- git branch -D \<branch\>
  - Force delete the specified branch, even if it has unmerged changes. This is the command to use if you want to permanently throw away all of the commits associated with particular line of development.
- git branch -m \<branch\>
  - Rename the current branch to \<branch\>.

### Git switch

switch to branch:
    - git switch branchName
Create and switch branch ( one line command ):
    - git switch -c branchName

### Git add

- git add { file }
  - Stage all changes in { file } for the next commit.
- git add { directory }
  - Stage all changes in { directory } for the next commit.
- git add { . }
  - Stage all changes for the next commit.
