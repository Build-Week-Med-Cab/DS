# Data sources

- [cannabis.csv](cannabis.csv) from [Kaggle Cannabis Strains dataset](https://www.kaggle.com/kingburrito666/cannabis-strains)
- [leafly.json](leafly.json) scraped from [Leafly marijuana strain database](https://www.leafly.com/strains)
- [quora.csv](quora.csv) from [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs/data)

The Kaggle dataset was created using data from Leafly and only includes 6 features
about each strain. This dataset had more rows, but we chose to use the scraped
Leafly dataset because it contains more features about the medical issues than
the Kaggle dataset.

The quora dataset contains question pairs that are labeled by humans as similar questions or not. This dataset is used train a Manhattan LSTM neural network model.
