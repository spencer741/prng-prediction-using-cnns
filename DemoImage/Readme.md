# How to setup for the demo.
Note I am running Windows 10 and using powershell, but the commands are similar for other platforms.

#### Pre-reqs
Have docker installed and setup on your machine correctly. 

Have Git installed and setup on your machine correctly.

#### Instructions
Navigate to where you want your local copy of our repository to be. (for example, I am just putting it on the Desktop)

Type:
```
git clone https://github.com/CSCI4850/S20-team7-project.git
```
Then Type:
```
cd S20-team7-project
```
Then Type:
```
docker build --rm -f ./DemoImage/Dockerfile -t democontainer .
```
Where democontainer is the name of your built image (you can change this to whatever).

Before you run the command below, make sure you modify the path "C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace" to reflect your path to the cloned repo. Make sure to include \WorkSpace.

```
docker run -v C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace:/WorkSpace -it --rm --privileged democontainer bash 
```

What we are doing here is building a local docker container, which installs the dependencies internally. The /WorkSpace directory in the Docker Container will be mapped to the /WorkSpace folder in your local copy of the repository. When you execute docker run, it will drop you into a session in the container. Any changes you make in /WorkSpace will be persisted to the host (your local machine).

Once you are dropped into the container session:

```
cd WorkSpace
ls
```
Now you can see the WorkSpace repo folders and files. In order to run the demo:

``` 
cd ProjectCore
python3 main.py
```
Essentially, we are invoking a custom Experiment class that performs the experiment to the desired configuration. Read more at the top of ProjectCore/Core files.

You can change the experiment configuration by `vi main.py` and modifying accordingly. The configuration dictionary contains the parameters for running the experiment.

After you run the experiment with the specified configuation, you will be able to find logs and reports from the experiment you ran at the specified path.

NOTE: Some generators like Middle_Square can converge to a specific number, therefore spoiling the experiment. Some other generators require specific input, so the best way is to specify the correct seed generator in the configuration that is most compatible with that input requirement (For example, maximally_periodic_reciprocals requires sophie primes). 

You might ask: won't different seed generators introduce flaws or bias in the experiment? Well, it depends on what you are testing. In our case, we are strictly testing the complexity of the generator itself, so supplying a seed that is not blatantly predictable but also not unpredictable was okay. Our goal was to allow the charactaristics of the generator to be exposed so we were cracking the complexity of the generation algorithm, not the complexity of some arbitrary seed.

You can find and modify Core.PrngMethods and Core.SeedMethods to suit your exact needs.

To understand the project better, we highly recommend `cd Core` and looking at the core files that make this project work.
At the top of each file, you will find useful documentation. 

Here is the experimental configuration definition from the top of Core.Experiment:

```
configuration = {
        'DISABLE_TQDMN' : True,             #Shortened pretty output for epoch results. Disable if executing from cli.
        'LOUD_LOGGING': False,              #Extra output detailing exactly what the experiment is doing at all times.
        'VERBOSE' : 0,                      #if training output (model.fit) is verbose
        'IS_NEW_MODEL' : False,             #Whether to load a previous model or not... ->
        'PATH' : './Middle_Square/',        #if IS_NEW_MODEL, new files will be created / overidden at PATH. ... 
                                            #If !IS_NEW_MODEL, previous model with weights will be loaded at PATH. 
        
        'SEED_METHOD' : 'ticks',            #using Core.SeedMethods as source   
        'PRNG_METHOD' : 'Middle_Square',    #using Core.PrngMethods as source  
        'NUM_SETS' : 1000,                  #generate NUM_SETS sets 
        'SET_LEN': 2000,                    #of length SET_LEN                        
        
        'USE_VALIDATION' : True ,           #use a portion of input data to fine tune nn architecture
        'VALIDATION_SPLIT' :  0.2,          #split training data between training and validation
        'BATCH_SIZE': 15,                   #size of batch, determined by how many segmented training samples (NUM_SETS) in each epoch.
        'NUM_EPOCHS': 1,                    #number of forward passses and one backward passses through of all the training input data.
        
        'CHKPNT_MONITOR' : 'mae',            #model checkpoint is implemented, which saves the model after each epoch if the ->
        'CHKPNT_MODE' : 'min',               #CHKPOINT_MONITOR metric is CHKPNT_MODE (minimized or maximized).
        
        'OVERRIDE_LOAD_COMPILATION' : False,  #if IS_NEW_MODEL == false, a previous model will be loaded from the PATH. By default, 
                                              #keras compiles the loaded model on load using the saved training configuration, 
                                              #so if you want to specify a new learning rate or loss method to track, you will have to
                                              #set this flag to override the compilation.
        'LR': .001,
        'LOSS_METHOD':'mean_squared_error'
        
        
    }  
    
    #note: *** deprecated *** 'OPTIMIZER_METHOD' : 'adam' ### currently hardcoded with Nadam to pass in learning rate.
```
