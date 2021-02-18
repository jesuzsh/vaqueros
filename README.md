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

### Step 3: Run code.
TLDR;
    # Create virtual environment
    python3 -m venv venv

    # Activate python virtual environment
    ./venv/Scripts/activate (Windows)
    source venv/bin/activate (Mac/Linux)

    # Install all current project dependencies
    pip install -r requirements.txt
    cd ..
    pip install -e vaqueros

    # Create datastore (needed SQLite database)
    python vaqueros/init/create_datastore.py

Needed databases will be created. The only remaining step would be to execute
the script responsible for an application interface that interacts with the
database. 

#### Virtual Python Environments
The first concept we will work with in this feature are virtual environment.
This concept is important for every Python project because, usually, a Python
project will have many dependencies, libraries that were installed,
imported and used to build the final project. 

There are a few tools and the simplest, probably most common, is
[venv](https://docs.python.org/3/library/venv.html). This already comes with
Python so we can just go straight to making a virtual environment.

    python3 -m venv <path/to/virtual/environment>

The above command will make a directory for you and that directory is the
virtual environment. Now that you've created a virtual environment we can use
that environment to keep track of the dependencies needed for the project we
are working on. To activate your environment, use the following command:

    source <path/to/virtual/environment>/bin/activate

This should activate your virtual environment. You can check that you're
properly using the virtual environment with the following command:

    which python (Mac/Linux)

The output should be a Python that lives within your virtual environment
directory. Also, run this command to see all the dependencies installed in your
virtual environment:

    pip freeze

Initially this will be empty, but one of the first steps when you're getting up
to speed on a Python project will be to install the dependencies. In Python,
dependencies are installed using the tool `pip`. Every project should have a
requirements.txt file, its contents is the output of `pip freeze`. One way to
create a requirements.txt file from your virtual environment:

    pip freeze > requirements.txt

To install dependencies of a pre-existing requirements.txt you can do a single
`pip install` command. 

    pip install -r requirements.txt

Assuming your virtual environment is activated, after running the above
command you should have all the dependencies needed for this python project to
execute with full functionality. At the moment, there aren't too many
dependencies in this project, yet. Python projects like to depend on many
packages, so a tool to manage your virtual python environment is needed.

### Step 3: Write code.
See the following sections for what needs to be done. 


#### Database connectivity
Here is talk of database connectivity.

We will be using a very popular python library known as
[SQLAlchemy](https://www.sqlalchemy.org/). Straight from the website,
"SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL."
[This](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) is an article I
used to set up our SQLAlchemy code.

### TODO

* Intake of expeditures, save entries
* Various way to view/visualize entries, dashboard


### Appendix
Creating branch `the-calvary`, commiting changes, setting up remote. 

    git checkout -b the-calvary
    git commit -m "describing the committed change"
    git push --set-upstream origin the-calvary

View local branches. The current branch should be marked. 

    git branch

View local and remote branches

    git branch -a


Quote [found](https://hackersandslackers.com/flask-wtforms-forms/) on form making,

    "Handling form authentication and data submission is the pinnacle of app
    development... He who cretes forms is a harbinger of a golden age: a hero
    who brings us to the pinnacle of Western technology."
