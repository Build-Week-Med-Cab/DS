# MedCabinet - Data Science

MedCabinet is a project that uses crowd sourced data to enable consumers
of medical cannabis to identify particular strains of cannabis that help
alleviate specific symptoms.

The data science teams have deployed an API used by the web teams to make
recommendations of specific strains by applying machine learning
techniques to match user input with our data.

## Data Engineering

FastAPI app, [https://medcabinet-ds-0820.herokuapp.com](deployed to Heroku),
provides 2 routes. One route, `/labels`, provides the labels a user can select
to distinguish strains. The `/recommends` endpoint routes user input to the
machine learning model and returns the resulting recommendations.

| Type | Endpoint | Required Parameters | Returns |
| ---- | -------- | ---------- | ------- |
| GET  | /labels  |            | {'effects': ['', '', ...], 'helps':['', '', ...]} |
| POST | /recommends | {'effects': ['', '', ...], 'helps':['', '', ...]} | {'strains': [{...}, {...}]} |

More details about the API endpoints can be found at the
[ReDoc](https://medcabinet-ds-0820.herokuapp.com/redoc) interface or by
exploring the interactive [SwaggerUI](https://medcabinet-ds-0820.herokuapp.com).

## Machine Learning

Nearest Neighbors ML Model for Medical Cannabis Recommendations

The data wrangling, Neural Network baseline model, tokening and TFIDF vectoring of text, creation of Nearest Neighbors model, training on tokenized and vectorized text, and pickling of Nearest Neighbors Model and TFIDF Vectorizer can all be found in the Wrangle_Bline_NN_Pickles.ipynb notebook in the notebooks directory.

The Nearest Neighbors and TFIDF Vectorizer pickles can be found in the pickles directory.

The pickled Nearest Neighbors model and TFIDF Vectorizer are imported into recommend.py in the app directory so that they can be used in a recommend function in the Data Engineering API in order to recommend medical cannabis strains to patients based on desired feelings, and what they are looking for a medical cannabis strain to help (ie: symptoms)

# Contributors

| John Dailey | Ilya Novak | Kush Rawal | Caleb Spraul |
| :---------: | :--------: | :--------: | :----------: |
| Machine Learning | Machine Learning | Data Engineer | Data Engineer |
| [<img src="https://github.com/favicon.ico" width="15">](https://github.com/johnjdailey) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/johnjdailey/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/ilyanovak) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/ilya-novak-352b469/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/rawalk) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/kush-rawal-7a35603a/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/jcs-lambda) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/jcspraul/) |
