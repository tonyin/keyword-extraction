keyword-extraction
==================

Kaggle [Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction) competition by Facebook. Implemented in Python.

Algorithms: Naive Bayes, [Rapid Automatic Keyword Extraction](https://github.com/aneesha/RAKE)

---

### Instructions

1. Clone repository
2. Create virtual environment `virtualenv env`
3. Install required libraries `pip install -r requirements.txt`
4. Download `Train.zip` from the [Kaggle site](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) to local folder `data`
5. Run `classify.py` to create `data/Pred.csv` file of predictions
6. Evaluate predictions with `mean_f1.py`

#### Notes

* Input files (Train and Pred files) are located in a local folder `data`
* Predictions generated for original Train file due to inability to score Test file on Kaggle
* Mean F1 scoring based on Kaggle's [wiki](https://www.kaggle.com/wiki/MeanFScore)
