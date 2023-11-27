# Chaos Toolkit Simple Example
Simple Example for the usage of the ChaosToolkit. Adapted and simplified from the original tutorial on the ChaosToolkit Webpage: https://chaostoolkit.org/reference/tutorial/

---
### Requirements
The experiment will use the following binaries, make sure you have them in your PATH:

[openssl](https://github.com/openssl/openssl)

[pkill](https://github.com/fosskers/pkill)


---
### Setup
```
cd <project-folder>
```

You may want to run the experiment in a virtual environment: see https://docs.python.org/3/library/venv.html

Install Requirements
```
pip install -U -r requirements.txt
```

Install Chaostoolkit
```
pip install -U chaostoolkit
```

---
### Run a Chaos Experiment with ChaosToolkit
Run the application
```
python bookmark.py
```
Now the application shoul be available at https://localhost:8444

Run the experiment
```
chaos run experiment.json
```

