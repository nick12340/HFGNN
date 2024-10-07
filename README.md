# Conda environment setup
```
conda create -n cfgnn python=3.10
conda activate cfgnn
conda install pytorch=1.13 torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install pyg=2.2 -c pyg -c conda-forge
pip install pyg-lib -f https://data.pyg.org/whl/torch-1.13.0+cu117.html
pip install pytorch-lightning yacs torchmetrics
pip install performer-pytorch
pip install tensorboardX
pip install ogb
pip install wandb
conda clean --all
```
# Hub Labeling construction

The code sspexp_codes, which is supplied by the authors of the paper (http://www.vldb.org/pvldb/vol11/p445-li.pdf), is utilized to construct hub labeling.
To build the labeling, please check the instruction under that folder.

# Running CFGNN

```
python main.py --cfg configs/CFGNN/zinc-CFGNN.yaml  wandb.use False

```
