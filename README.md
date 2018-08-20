# latent-space-recognizer
Plan recognition in latent space

# TODO
Documentation for dependencies installation here.

## Python dependencies
Python 3.5+ is used in this repository. The following Python dependencies are needed to run our approach (pygame is only necessary for the N-Puzzle demo):

```
pip install matplotlib
pip install opencv-python
pip install timeout-decorator
pip install tensorflow
pip install keras
pip install pillow
pip install pygame
```

# Training network
To train the networks use:
```
./train_all.sh
```
or
```
./train_all_fast.sh
```
Output is going to "samples/<problem_name>". Encoder and decoder weights are being saved there.

# Generating PDDL domains:
To generate the PDDL domains, use:
```
./all_domains.sh
```
This will output the PDDL domains in the folder *domains/*, along with the logs for generating each domain.
# Generating goal recognition problems:
To generate goal recognition problems used in our tests, run:
```
./all_recons.sh
```
The output will be sent to the folder *output/*.
