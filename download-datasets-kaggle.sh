#!/bin/bash

# Download datasets API Kaggle
# Kaggle must be installed and user API credentials configured

dataset_nba="nba-players-and-team-data"
dataset_top="top-tech-startups-hiring-2023"

cd $PWD/datasets

# Dataset 1: NBA Players & Team Data - https://www.kaggle.com/datasets/loganlauton/nba-players-and-team-data
echo "Download dataset $dataset_nba..."
kaggle datasets download -d loganlauton/$dataset_nba
echo "$dataset_nba dataset successfully downloaded!"

# Dataset 2: Top Tech Startups Hiring 2023 - https://www.kaggle.com/datasets/chickooo/top-tech-startups-hiring-2023?select=json_data.json
echo "Download dataset $dataset_top..."
kaggle datasets download -d chickooo/$dataset_top
echo "$dataset_top dataset successfully downloaded!"

echo "Extracts the $dataset_nba."
mkdir -p $dataset_nba
unzip $dataset_nba.zip -d $dataset_nba/
rm $dataset_nba.zip

echo "Extracts the $dataset_top"
mkdir -p $dataset_top
unzip $dataset_top.zip -d $dataset_top/
rm $dataset_top.zip

echo "Extracts completed successfully"