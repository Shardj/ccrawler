# WIP

For install make sure you have python pip, run pip install requirements.txt

Note to devs: New \_\_builtins\_\_ function added in launcher.py to allow for easy module imports from anywhere in the project to anywhere else. However its usage isn't ideal, a viable alternative would be helpful

# Unit Tests

**Run all with bootstrapping**
python3 -m test *OR* python3 test.py

**Run individual test - tests requiring bootstraping will fail**
python3 -m unittest tests/test_{name}.py
