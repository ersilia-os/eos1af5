import sys
import os
import csv

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT, "molgrad"))

infile = sys.argv[1]
outfile = sys.argv[2]
checkpoints_dir = sys.argv[3]

import torch
from molgrad.net import MPNNPredictor
from molgrad.train import DEVICE
from rdkit import Chem

model_pt = os.path.join(checkpoints_dir, "caco2_noHs.pt")

from molgrad.prod import predict

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    mols = []
    for r in reader:
        mols += [Chem.MolToInchi(Chem.MolFromSmiles(r[0]))]

preds = run(mols, model_pt, progress=True)[:,0]

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["log10_passive_permeability"])
    for p in preds:
        writer.writerow([float(p)])