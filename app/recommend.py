"""Recommendation model."""
import pickle

with open('./pickles/nn_model.pkl', 'rb') as nn_pkl:
    model = pickle.load(nn_pkl)

with open('./pickles/tfidf.pkl', 'rb') as tfidf_pkl:
    tfidf = pickle.load(tfidf_pkl)

with open('./pickles/min_data.pkl', 'rb') as data_pkl:
    data = pickle.load(data_pkl)


def get_recommendations(user_input: str, num: int = 4):
    """Transform input and get recommended strains.

    Vectorizes user input for use in nearest neighbors model. Returns `num`
    nearest neighbors.

    :param user_input: string of user input

    :param num: int, default 4, number of neighbors to return

    :returns: list of dictionaries with output from pickled min_data for
    each neighbor
    """
    neighbors = model.kneighbors(
        tfidf.transform([user_input]).todense(),
        n_neighbors=num, return_distance=False
    )
    results = []
    for index in neighbors[0]:
        results.append({
            'strain': data[index]['strain'],
            'strain_type': data[index]['type'],
            'description': data[index]['description'],
            'effects': [data[index][f'feeling_{i}'] for i in range(1, 6)],
            'helps': [data[index][f'helps_{i}'] for i in range(1, 6)],
        })
    return results
