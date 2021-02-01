Yo I'm going to start writing those set of instructions that would get you
started that I mentioned this one time. I want you to know that you ask me any
question you have at anypoint. I also need this done for myself so you helping
me will not only show you what you need to know in python and aid me in
completing this.

### Step 1: Acquire a github account. 
This account will aid us in version control collaboration. (version control:
you have a peace of work (code/script) and it exists in that current version.
If you were to update or change any part of the work, it will no longer be
the previous version, it's the new version. 

Everytime we move to new versions of the code, the best practice is to
document what has changed between versions. This is possible to do using a
version control system like, [git](https://git-scm.com/). I'm trying to slowly
talk more and more about what we can do with this tool as we go on.

Sign up on the official [GitHub website](https://github.com/).


### Step 2: Get this code on your computer.
Time to get you a hold of the code that you're going to have to be making
changes to. You're currently looking at this code through a repository hosted
remotely on GitHub servers. Through the use of the version control system, git,
we can interact with this repository, push and pulling any changes (see
Appendix). 

#### Download [git](https://git-scm.com/).

Using git, clone this repository. Options for this can be seen in the [GitHub
repository UI](https://github.com/jesuzsh/vaqueros). A quick way to do this
using the git CLI through HTTP.

    git clone https://github.com/jesuzsh/vaqueros


### Step 3: Write code.
See the following sections for what needs to be done. 


### TODO

#### Refactor
This code was writting 2018, the python in this code isn't the best written.
Not all of it fits the project we are completing, so we need to refactor the
existing codebase. We basically need to make changes to the old code so it
matches the current vision for the project.

Probably best that the vision is described. For starters, I think it's pretty
important that we are aware of the various entities that are going to exist in
our application. These entities will, most likely, be designed to represent 
real-world objects. The following is a list of current known entities and a 
brief description:

* Expeditures: A single unit of an expense. This will be responsible for 
holding relative information about a transactions. The bulk of the data managed
by this application is going to be all of the expeditures that'll accumulate
over time.
```
name # Wal-Mart
amount (USD) # 86.43
card # 3
category # Groceries
```

* Cards: In order to have the functionality of seperating expenditiures by card,
we need to keep track of the cards involved. The idea will be to have unique IDs
for each card. This way when inputting an expenditure, a card ID can be given for
the relationship to exist.
```
id # 1
name # Amex
owner # Jesus
```

* Categories: must exist to be able to see what are the areas of spending.
```
name # Groceries
is_essential # True

name # Video Game
is_essential # False
```

* Their relationships. This is an important concept in the world of relational
database and SQL. Objects stored in this database have relationships with one
another. For example, everytime an expenditure is submitted it will have key 
pieces of metadata associated with it. It will have a dollar ammount that is
the cost of that specific expenditure.

For now we will work with the above drafts of the field involved with each
entity. Using the examples and their fields, we have enough information needed
to make a database schema. Every database should have some sort of schema. The
purpose of the schema is to be a layout of all the data in the datastore.

#### Database connectivity

#### Intake of expeditures, save entries

#### Various way to view/visualize entries, dashboard


### Appendix
Creating branch `the-calvary`, commiting changes, setting up remote. 

    git checkout -b the-calvary
    git commit -m "describing the committed change"
    git push --set-upstream origin the-calvary

View local branches. The current branch should be marked. 

    git branch

View local and remote branches

    git branch -a
