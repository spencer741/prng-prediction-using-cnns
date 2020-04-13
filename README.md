## Predicting Pseudo Random Values Using Convolutional Neural Networks

### Quick Links

[Link to Paper] - Coming Soon.

[Milestones](https://github.com/CSCI4850/S20-team7-project/blob/master/Project%20Milestones.ipynb)

[Project Proposal](https://github.com/CSCI4850/S20-team7-project/blob/master/WorkSpace/Project%20Proposal/ProjectProposal.ipynb)

[Core Files](https://github.com/CSCI4850/S20-team7-project/tree/master/WorkSpace/ProjectCore)

### Repository Overview (trimmed):
```
├───ContributionContainer 
│   └─── Contains Dockerfile with a tutorial on how to set up this project with Jupyter Lab.
├───DemoContainer
│   └─── Contains Dockerfile with a tutorial on how to set up this project with cli.
└───WorkSpace
    ├───Milestones
    │   └─── Contains milestones that provide updated progress on the project.
    ├───Paper
    │   └─── Contains the final paper written describing everything from the proposal to the results of the research.
    ├───Project Proposal
    │   └─── Contains the initial document for our proposed research.
    └───ProjectCore
        ├─── main.py ... Entry point for executing experiments via CLI
        ├─── main.ipynb ... Entry point for executing experiments via Jupyter Notebook
        ├─── other folders containing PRNG results
        ├───Core
            ├─── Contains files that implement the core functionality of this project. 
                 Read more about each one at the top of each file.
```
### How to explore / run the code 
Before choosing your option, read through the tutorial under option 1. This tutorial provides the best introduction for running the project in addition to **[more information about the code itself](https://github.com/CSCI4850/S20-team7-project/blob/master/DemoImage/Readme.md#running-code)**.

**Option 1:** The Demo Image (Reduced Docker Image with only the dependencies). Recommended to run the Demo.

[Read tutorial here for setup](https://github.com/CSCI4850/S20-team7-project/tree/master/DemoImage)

**Option 2:** The Contribution Image (Jupyter Lab on Docker). Recommended for contributors.

[Read tutorial here for setup](https://github.com/CSCI4850/S20-team7-project/blob/master/DockerContainer/README.md)

We recommend you read: [more information about the code itself](https://github.com/CSCI4850/S20-team7-project/blob/master/DemoImage/Readme.md#running-code)

**Option 3:** 'simple' install 

*Note*: platform-specific tooling issues might occur. With Windows, you will likely have to download the pre-compiled version of different packages (like SciPy and others) from here: [Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/). For Windows, we recommend the Docker Demo Image or the larger Contribution Image. [This](https://python-forum.io/Thread-sklearn-imported-but-not-recognized?pid=19812#pid19812) will get you started down the right path if you insist on this option.

```
git clone https://github.com/CSCI4850/S20-team7-project.git

cd S20-team7-project

pip install -r requirements.txt

cd ./WorkSpace/ProjectCore/

python3 main.py
```
We recommend you read:
[more information about the code itself](https://github.com/CSCI4850/S20-team7-project/blob/master/DemoImage/Readme.md#running-code)
