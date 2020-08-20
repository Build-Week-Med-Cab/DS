# Recommend.py

# Strain recommend function using nearest neighbors and tfidf vectorizer
# trained on feelings, helps, and description



# Imports

from os import path
import pandas as pd
import pickle
import json


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "../data/leafly.json")

df = pd.read_csv(file_name)


# Import pickled model

model_path = path.join(path.dirname(__file__), "../pickles/nn_model.pkl")

NN_model = pickle.load(open(model_path, 'rb'))


# Import pickled vectorizer

vectorizer_path = path.join(path.dirname(__file__), "../pickles/tfidf.pkl")

tfidf_model = pickle.load(open(vectorizer_path, 'rb'))


# Recommend Function with model training on feelings, helps, and description

import json

def recommend(user_input):
    temp_df = NN_model.kneighbors(tfidf_model.transform([user_input]).todense())[1]
    

    #print(temp_df)
    
    for i in range(4):
        info = leafly.iloc[temp_df[0][i]]['strain']
        info_aka = leafly.iloc[temp_df[0][i]]['aka']
        info_type = leafly.iloc[temp_df[0][i]]['type']
        info_rating = leafly.iloc[temp_df[0][i]]['rating']
        info_num_reviews= leafly.iloc[temp_df[0][i]]['num_reviews']
        info_feelings = leafly.iloc[temp_df[0][i]]['feelings']
        info_helps = leafly.iloc[temp_df[0][i]]['helps']
        info_description = leafly.iloc[temp_df[0][i]]['description']
        
        # This is for testing result prints in jupyter notebook

        #print(json.dumps(info))
        #print(json.dumps(info_aka))
        #print(json.dumps(info_type))
        #print(json.dumps(info_rating))
        #print(json.dumps(info_num_reviews))
        #print(json.dumps(info_feelings))
        #print(json.dumps(info_helps))
        #print(json.dumps(info_description))
        
        # This is for the data engineers, the return does not work in jupyter lab.  
        # Should work in vsCode, or elsewhere for production.

        #return json.dumps(info)
        #return json.dumps(info_aka)
        #return json.dumps(info_type)
        #return json.dumps(info_rating)
        #return json.dumps(info_num_reviews)
        #return json.dumps(info_feelings)
        #return json.dumps(info_helps)
        #return json.dumps(info_description)

        return [info, info_aka, info_type, info_rating, info_num_reviews, info_feelings, info_helps, info_description]
