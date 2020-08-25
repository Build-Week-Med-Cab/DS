# DS

# Data Engineering

API for Medical Cannabis Recommendations

get json desired effects from front end

input json desired effects data into pickled model

return recommendation to front end for front end user, and send recommendation to back end for persistence


# Machine Learning

Nearest Neighbors ML Model for Medical Cannabis Recommendations

The data wrangling, Neural Network baseline model, tokening and TFIDF vectoring of text, creation of Nearest Neighbors model, training on tokenized and vectorized text, and pickling of Nearest Neighbors Model and TFIDF Vectorizer can all be found in the Wrangle_Bline_NN_Pickles.ipynb notebook in the notebooks directory.

The Nearest Neighbors and TFIDF Vectorizer pickles can be found in the pickles directory.

The pickled Nearest Neighbors model and TFIDF Vectorizer are imported into recommend.py in the app directory so that they can be used in a recommend function in the Data Engineering API in order to recommend medical cannabis strains to patients based on desired feelings, and what they are looking for a medical cannabis strain to help (ie: symptoms)
