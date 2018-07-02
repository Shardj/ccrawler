# WIP

For install make sure you have python pip, run `pip install requirements.txt` or `python3-pip install requirements.txt` depending on your setup

if you have issues with pip and python2.7 3.2 mixup like I did then use `sudo pip3 install MODULE_NAME` for each module, curl will be required (`sudo apt-get install curl`)

Note to devs: New \_\_builtins\_\_ function added in launcher.py to allow for easy module imports from anywhere in the project to anywhere else. However its usage isn't ideal, a viable alternative would be helpful

TODO follow redirects, TODO handle items in database instead of in object

# Unit Tests

**Run all with bootstrapping**
python3 -m test *OR* python3 test.py

**Run individual test - tests requiring bootstraping will fail**
python3 -m unittest tests/test_{name}.py
