# Looped Transformers as SAT Solvers
Looped Transformers as SAT Solvers


## Looped Transformers Solve SAT


## Experimental Results

### Setup

```shell
conda create -n loopsat python=3.11
conda activate loopsat
```

### Learning a SAT Solver from Single-Bit Supervision

```shell
bash train_sat.sh
```

### Sudoku

To run the baseline model L1R32H4 on 180k/1k train/test Palm's data on GPU 0.
```shell
cd sudoku
python main.py --all_layers --n_layer 1 --n_recur 32 --n_head 4 --epochs 200 --eval_interval 1 --lr 0.001 --dataset palm --n_train 180000 --gpu 0 --wandb
```

### Acknowledgement

- https://github.com/dselsam/neurosat
- https://github.com/zshi0616/iccad_SATformer
- https://github.com/ryanzhangfan/NeuroSAT
