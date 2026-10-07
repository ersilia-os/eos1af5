# Coloring molecules for Caco-2 cell permeability

Estimates apparent permeability across a Caco-2 monolayer, the in vitro gold-standard proxy for how readily an orally dosed compound crosses the intestinal wall. Values come back as the negative log10 of Papp in cm/s, so a higher number means a less permeable compound. Jimenez-Luna and colleagues fitted a message-passing graph neural network, paired with integrated-gradients colouring of the atoms behind each prediction, to 239 compounds pooled from two studies. With so little data and a cross-validated Pearson R of 0.53, treat the output as a ranking aid.

This model was incorporated on 2021-10-19.Last packaged on 2026-03-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1af5`
- **Slug:** `molgrad-caco2`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Permeability`, `ADME`, `Papp`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Negative log10 of Caco-2 apparent permeability in cm/s, where lower values indicate greater permeability.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| log10_passive_permeability | float | high | Log10 of passive permeability |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos1af5](https://hub.docker.com/r/ersiliaos/eos1af5)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1af5.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1af5.zip)

### Resource Consumption
- **Model Size (Mb):** `17`
- **Environment Size (Mb):** `2415`
- **Image Size (Mb):** `2399.18`

**Computational Performance (seconds):**
- 10 inputs: `31.08`
- 100 inputs: `22.27`
- 10000 inputs: `195.25`

### References
- **Source Code**: [https://github.com/josejimenezluna/molgrad/](https://github.com/josejimenezluna/molgrad/)
- **Publication**: [https://doi.org/10.1021/acs.jcim.0c01344](https://doi.org/10.1021/acs.jcim.0c01344)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [AGPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1af5
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1af5
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
