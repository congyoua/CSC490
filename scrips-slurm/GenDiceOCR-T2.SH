#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=16
#SBATCH --mem=63500M
#SBATCH --time=20:00:00
#SBATCH --output=/home/njrttx/scratch/CSC490_OpenYourEyes/1030_exp/Gen-OCR.out


echo "Current working directory: pwd"

cd $SCRATCH
./setup.sh
source ./490_env/bin/activate
cd /home/njrttx/scratch/CSC490_OpenYourEyes
python main.py -c configs/OCRNet_rf_gendice.json --task 2 -d 0 --data_path "/home/njrttx/scratch/CSC490_OpenYourEyes/data"
