## S20-team7-project

./WorkSpace/ProjectCore

[Project Proposal](https://github.com/CSCI4850/S20-team7-project/blob/master/WorkSpace/Project%20Proposal/ProjectProposal.ipynb) (Now downstream)

[Milestones](https://github.com/CSCI4850/S20-team7-project/blob/master/Project%20Milestones.ipynb) (For frequent updates)

[Links to Paper and Experimental Design] - Coming Soon.




### How to run the demo 

**Option 1:** simple install (note: platform-specific tooling issues might occur)

```
git clone https://github.com/CSCI4850/S20-team7-project.git

cd S20-team7-project

pip install -r requirements.txt

cd ./WorkSpace/ProjectCore/

python3 main.py
```
With this option, you can use the included [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/content-quickstart.html) dependency to explore our notebooks!

**Option 2:** Jupyter Lab on Docker

[Read the tutorial here for how to set this up](https://github.com/CSCI4850/S20-team7-project/blob/master/DockerContainer/README.md)


## Repository Structural Overview:
Here is a trimmed down schema of our repository:
```
├───DockerContainer 
│   └─── Contains the Docker container with a tutorial on how to set up this project with Jupyter Lab.
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
