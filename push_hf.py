import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict

sprig_llama = pd.read_json("dataset.jsonl", lines=True)
train_sprig, test_sprig = train_test_split(
  sprig_llama, test_size=0.15, random_state=42, shuffle=True
) 

train_sprig = Dataset.from_pandas(train_sprig)
test_sprig = Dataset.from_pandas(test_sprig)

ds = DatasetDict()
ds["train"] = train_sprig
ds["test"] = test_sprig

dataset_name = "josiasaurel/sprig_llm"
ds.push_to_hub(dataset_name, branch="main", private=True)
