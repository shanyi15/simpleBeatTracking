# README

## Who am I?
This project uses python flask, librosa and front-end language to create a simple beat tracking app. 
By uploading a piece of audio, user can get a figure annotated with predicted beat time stamps analyzed by algorithms through librosa. 

For better performance, it's recommended to upload music with strong and stable beat.

## Use it locally
Please note that, due to the limitation of testing environments, this app was only tested on MacOS Ventura 13.0.1. 

- Download and install Anaconda from [here](https://www.anaconda.com/products/distribution). If you successfully install Anaconda, you should see the conda list by run `conda list` command in your terminal.

- Create env

  under /simpleBeatTracking menu, create conda environment

  ```
  conda env create -f environment.yml
  ```

  You should see "done" if you create the environment successfully. Then you can use

  ```
  conda-env list
  ```

  to check all of the environments. There should be a environment named "flask-test" in it.

- Activate env

  You can activate this environment by using

  ```
  conda activate flask-test
  ```

  If you activate the environment successfully, you should see `(flask-test)`.

- Run this app

  ```
  flask --app app run
  ```
  
  ## Questions?
  For any questions, please add [Issues](https://github.com/shanyi15/simpleBeatTracking/issues). 
