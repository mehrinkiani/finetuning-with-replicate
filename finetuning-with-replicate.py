import replicate

training = replicate.trainings.create(
  version="meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
  input={
    "train_data": "https://raw.githubusercontent.com/mehrinkiani/mehrinkiani.github.io/main/deepset-prompt-injections.jsonl",
    "num_train_epochs": 3
  },
  destination="mehrinkiani/llama2-7b-prompt-injection-detector"
)

print(training)
