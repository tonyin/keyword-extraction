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
5. Train models `train.py` - creates json models in `classifiers/`
6. Generate predictions `predict.py` - creates prediction csv `data/Pred.csv`
6. Evaluate predictions using mean F1-Score `mean_f1.py`

#### Notes

* Input files (Train and Pred files) are located in a local folder `data`
* Predictions generated for original Train file due to inability to score Test file on Kaggle
* Mean F1 scoring based on Kaggle's [wiki](https://www.kaggle.com/wiki/MeanFScore)
