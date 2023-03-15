# Working with .git version control / and Azure DevOps

**Downloading Git (Windows)**
https://git-scm.com/download/win

**Cloning the Repo (From Azure DevOps)**
The first step is to clone the repository onto your computer, so you have a local version of the project. This is done by:

1. Go to Azure DevOps.
2. Navigate to the 'Repos' tab on the left.
3. Click on 'Files'.
4. Click 'Clone' and copy the HTTPS link. *Also copy the 'Get Git Credentials' code and save it!*
5. Go to Visual Studio Code, and select "Clone a Repository"
6. Enter the HTTPS link.
7. Done!

**First Steps**
You generally never want to work off of the main branch. The first thing you will always do before working on something is to pull the most recent version of the repo. This is done by using:
`git pull`

You'll also want to add yourself to the .git config using these commands:
`git config --global user.email "you@example.com"`
`git config --global user.name "Your Name"`

**Branches**
You can do `git branch` to see what branch you're on. You should be on the main branch.

If it were a large company, and you were assigned, for example, a Dark Mode Feature, you'd probably want to make a new branch:
`git checkout -b "Dark_Mode_Branch"`
If you make any errors on this branch, it won't affect the main branch. And when you're done, you can make what is called a PR or *pull request* to your peers to review it and then merge it into our main branch. This keeps everything clean and puts more eyes on potential problems.

To switch branches, you can use `git checkout Dark_Mode_Branch` (to switch to Dark_Mode_Branch) or `git checkout main` to go back to main.

**Pushing changes**
When it comes time to push your work to the repo, from your local state, you'll want to do the following:

1. `git status`: this will tell you everything you've editted so far. It will tell you the branch you're on, if you're up to date, or any changes you've made since your last `git pull`. Consider we were on the main branch, and I made and pushed my edits. `git status` would give you an message saying that your local state is not up to date.

2. `git add .`: adds all changes (or `git add myFile.c` would add a single file). This is essentially adding changes that you're going to eventually push to the repository.

3. `git commit -m "[message]"`: this is the official commit where it gathers all the files you've added and prepares it in a nice package. Adding -m and a message is what others will see your changes as. For example: `git commit -m "Changed x and b to work with y"`.

4. `git push origin My_Branch`: finally, we push the changes.

5. If you need to make more edits, use `git commit --amend -m "Fixed issues with x"`. You could just do `git commit -m "Fixed issues with x"`, but using amend makes things look much better. You can try it yourself or take my word for it.

6. Finally, when you're ready to have us merge it into main, go to Azure DevOps, Repos, and Pull Requests, and make a PR adding the rest of us at *Optional Reviewers*.