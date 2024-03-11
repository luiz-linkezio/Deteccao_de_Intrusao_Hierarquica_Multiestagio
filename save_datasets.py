import pandas as pd
def save_datasets(list_datasets : list[pd.DataFrame], datasets_paths = list[str]) :
    for dataset, dataset_path in zip(list_datasets, datasets_paths) :
        dataset.to_csv(dataset_path)

