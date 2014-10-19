keyword-extraction
==================

Kaggle [Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction) competition by Facebook. Implemented in Python.

---

### Instructions

1. Clone repository
2. Create virtual environment `virtualenv env`
3. Install required libraries `pip install -r requirements.txt`
4. Download `Train.zip` from the [Kaggle site](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) to local folder `data`
5. Run `classify.py` to create `Pred.csv` file of predictions
6. Evaluate predictions with `mean_f1.py`

###### Assumptions

* Input files (training and test zip files) are located in a local folder `data`