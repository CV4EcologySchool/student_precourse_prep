# Git exercise: make and share one small change

This exercise practices only the workflow named in the CV4Ecology FAQ: obtain code, change it, record the change, and share it through GitHub.

## Before starting

Make sure you have [`git`](https://git-scm.com/install/) installed and a [Github](https://github.com/) account setup. Let your instructor know your Github account name and they will make sure you are added to the [CV4Ecology Github Organization](http://github.com/CV4EcologySchool).
Once you are all set, follow the instructions [here](https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github#creating-your-repository) to create your first test repository.

Safety measures: Never add credentials, API keys, or SSH private keys to Git.

## 1. Clone your assigned repository

Copy its HTTPS URL from GitHub, then run:

```bash
git clone REPLACE_WITH_YOUR_REPOSITORY_URL
cd REPLACE_WITH_YOUR_REPOSITORY_NAME
```

HTTPS is used here to keep GitHub authentication separate from SSH access to workshop compute.

Check where the repository came from:

```bash
git remote -v
```

## 2. Check before editing

```bash
git status
git pull
```

`git status` should report a clean working tree. `git pull` obtains changes that are already on GitHub.

## 3. Make one change

Open `05_git_and_remote/practice_note.md` and replace the placeholder text with a piece of creative writing. Save the file, then inspect what changed:

```bash
git status
git diff -- 05_git_and_remote/practice_note.md
```

Read the diff. Confirm that it contains only the intended text change.

## 4. Stage and commit that file

```bash
git add 05_git_and_remote/practice_note.md
git status
git commit -m "Complete Git practice note"
```

Use the specific filename rather than `git add .`. The second `git status` shows what will be committed before the commit is created.

Inspect the newest commit:

```bash
git log -1 --oneline
```

## 5. Push it to GitHub

```bash
git push
```

Open the repository in a browser and confirm that the change and commit appear.

## If push is not configured

See [instructions for working from desktop](https://docs.github.com/en/get-started/using-github/connecting-to-github#working-from-the-desktop). 



## What the commands mean

| Command | Purpose |
|---|---|
| `git clone` | Make a local copy of an existing repository |
| `git pull` | Bring remote changes into the local copy |
| `git status` | Show changed, staged, and untracked files |
| `git diff` | Show uncommitted line-by-line changes |
| `git add FILE` | Select a change for the next commit |
| `git commit` | Record a local snapshot with a message |
| `git push` | Send local commits to the remote repository |

More complex operations like resolving branches, merge conflicts, and pull requests are currently out of scope for the course.

## Setting up Github SSH authentication 
For the remote machines, we'll be using SSH authentication for GitHub, use GitHub's current [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) instructions to setup an SSH key.
