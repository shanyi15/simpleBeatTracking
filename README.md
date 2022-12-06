# simpleBeatTracking

## Introduction
This project uses python flask, librosa and front-end language to create a simple beat tracking app. 
By uploading a piece of audio, user can get a figure annotated with predicted beat time stamps analyzed by algorithms through librosa. 

For better performance, it's recommended to upload music with strong and stable beat.

## Use it locally
Please note that, due to the limitation of testing environments, this app was only tested on MacOS Ventura 13.0.1. 

- Install virtualenv

  ```
  pip install virtualenv
  ```

- Activate env
  under /simpleBeatTracking menu, run the following command

  ```
  source ./bin/activate
  ```

  If you activate the environment successfully, you should see `(venv)`.

- Install requirement

  ```
  pip install -r requirement.txt
  ```

  If you install all of the requirement libraries succesfully, you should see the corresponding feedback from pip.

- Run this app

  ```
  flask --app app run
  ```
  If you start the server successfully, you will see the address. The default address should be: `http://127.0.0.1:5000/`. If you want to run it on `localhost`, you can change the host option by:
  ```
  flask --app app run --host=0.0.0.0
  ```
  
  ## Questions
  For any questions, please add [Issues](https://github.com/shanyi15/simpleBeatTracking/issues). 
  
  If you got the `cffi` package version error, you can try to solve it by [this](https://stackoverflow.com/questions/58552666/exception-version-mismatch-this-is-the-cffi-package-version-1-13-1).
