#!/bin/bash
#SBATCH --job-name=nh         # Job name
#SBATCH --partition=gpu               # Partition (queue) name
#SBATCH --gres=gpu:1
#SBATCH --nodes=1                       # Number of nodes
#SBATCH --ntasks=1                      # Number of tasks (processes)
#SBATCH --time=01:00:00                 # Time limit hrs:min:sec
#SBATCH --output=nh_%j.out   # Standard output log
#SBATCH --error=nh_%j.err   # Standard error log

module purge
module load Anaconda3                    # Load Anaconda module if required
conda activate "/home/jmframe/neuralhydrology/environments/jmframe/.conda/envs/neuralhydrology"
nh-run train --config-file ./nh_multi_basin_sample_hourly.yml