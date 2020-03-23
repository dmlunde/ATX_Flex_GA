# Lab Submission Policy and Procedure

## Labs are important
Most lessons will be followed by lab time so that you can directly put what we've just learned into practice. You'll work on problems that will connect lessons together, provide more real-world context for problems you'll see, and give you the opportunity to beef up on some of those less tangible aspects of data science like data cleaning and exploratory data analysis.

We will discuss most labs during class time. This may take the form of a codealong, reviewing solutions as a class, or discussing solutions in small groups.

Successfully completing labs prepares you to successfully complete projects. Staying up-to-date on labs is extremely important to successful completion of the course.


## You must receive a passing grade on 80% of all labs
  * Labs are graded on the basis of completion (complete, incomplete, missing, late).
  * To be eligible to receive full credit on a lab, you must submit an **attempt** at the lab by the Monday following the week the lab was assigned.(So both labs assigned during week 2 will be due by EOD Monday of week 3)
  * Reference the ATX-Flex-10 repo for lab due date adjustments.  
  * Partial submissions and submissions with substantial errors will be marked **incomplete**. Incomplete labs can be completed and re-submitted for full credit by the end of the course.
  * Labs not submitted by the deadline will be marked as **missing**. Missing labs can be completed and re-submitted for **HALF** credit by the end of the course.
  * **If you resubmit a lab, you are responsible to Slack me and let me know that you need it reviewed.**

## Lab Instructions

**Important!** Before submitting:
  * Make sure that you have run all cells and are error-free. A good way to do this is to open your Jupyter notebook and under ‘Kernel’ select ‘Restart & Run All’.
  * Best practice is to get in the habit of deleting extraneous cells, ESPECIALLY if those cells prevent your notebook from running directly through.
  * Long outputs should be suppressed: don't display entire DataFrames, don't print the entire contents of a text file, and don't have a print statement every time you do an action you'll repeat thousands of times.

### Accessing the Lab:

**1)** Click on the link to the lab from the ATX-Flex-10 README.md

**2)** Fork a copy of the lab (you should fork from j-beightol/Lab instead of DSI-US-10/Lab)

**3)** Clone the lab to your local machine

```git clone <url-here>```

**4)** Navigate to the repo that you cloned down in the command line.

**5)** Make your magic happen :)

### Submitting the Lab:

**1)** When you are ready to submit, check the status of the repo:

```git status```
- If you get 'Directory is not a git repository' make sure you are in the correct directory

**2)** Add the .ipynb file that contains your lab submission:

```git add starter_code.ipynb```

**3)** Write a commit message:

```git commit -m "pokemon lab - complete"```

**4)** Push your changes to your repo on github with:

```git push```

**5)** Go to **YOUR** github enterprise fork of the repo (online)

**6)** Click ‘New pull request’

**7)** Set the base fork to **MY** repository (**j-beightol**)
- I.E. j-beightol/example_lab not DSI-US-10/example lab

**8)** Enter a message either "complete" or "incomplete" i.e.:

 ```complete```

**9)** You can verify if the pull request was successful by clicking on the pull requests tab

### Common errors and how to fix them.

**ERROR** : `remote: Repository not found.`

**FIX**
Try checking your remote repositories with the command `git remote -v` The origin should be your fork of the lab and the url should contain your username. If it doesn't, switch the origin with the line `git remote set-url origin https://github.com/USERNAME/LABREPOSITORY.git`
