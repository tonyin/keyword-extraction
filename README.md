keyword-extraction
==================

Kaggle [Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction) competition by Facebook. Implemented in Python.

Algorithms: Naive Bayes

---

### Instructions

1. Clone repository
2. Create virtual environment `virtualenv env`
3. Install required libraries `pip install -r requirements.txt`
4. Download `Train.zip` from the [Kaggle site](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) to local folder `data`
5. Generate `Test.csv` file `make_test.py` - creates test csv `data/Test.csv` (108s)
6. Train models `train.py` - creates json models in `classifiers/`
7. Generate predictions `predict.py` - creates prediction csv `data/Pred.csv`
8. Evaluate predictions using mean F1-Score `mean_f1.py`

#### Notes

* Input data files (Train, Test, Pred) are in a local folder `data`
* Test file generated from random sample of Train file due to inability to score Test file on Kaggle
* Mean F1 scoring based on Kaggle's [wiki](https://www.kaggle.com/wiki/MeanFScore)
