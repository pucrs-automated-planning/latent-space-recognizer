# latent-space-recognizer
Plan recognition in latent space

# TODO
Documentation for dependencies installation here.

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
