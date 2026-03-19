import sys
import os
import csv

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT, "molgrad"))

infile = sys.argv[1]
outfile = sys.argv[2]
checkpoints_dir = os.path.join(ROOT, "..", "..", "checkpoints")

import torch
from molgrad.net import MPNNPredictor
from molgrad.train import DEVICE
from rdkit import Chem

model_pt = os.path.join(checkpoints_dir, "caco2_noHs.pt")

from molgrad.prod import predict

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    mols = [Chem.MolToInchi(Chem.MolFromSmiles(r[0])) for r in reader]

valid_idx = [i for i, m in enumerate(mols) if m is not None]
valid_mols = [mols[i] for i in valid_idx]

preds_valid = predict(valid_mols, model_pt, progress=True)[:,0]

results = [float("nan")] * len(mols)
for i, p in zip(valid_idx, preds_valid):
    results[i] = float(p)

assert len(results) == len(mols)

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["log10_passive_permeability"])
    for p in results:
        writer.writerow([p])
