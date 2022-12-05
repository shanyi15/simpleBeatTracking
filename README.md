# README

Please note that, due to the limitation of testing environments, this app was only tested on MacOS Ventura 13.0.1. 

1. Download and install Anaconda from [here](https://www.anaconda.com/products/distribution). If you successfully install Anaconda, you should see the conda list by run `conda list` command in your terminal.

2. Create env

under /beatTracking menu, create conda environment

```
conda env create -f environment.yml
```

You should see "done" if you create the environment successfully. Then you can use

```
conda-env list
```

to check all of the environments. There should be a environment named "flask-test" in it.

3. Activate env

You can activate this environment by using

```
conda activate flask-test
```

If you activate the environment successfully, you should see `(flask-test)`.

4. Run this app

```
flask --app app run
```