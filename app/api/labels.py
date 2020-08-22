<<<<<<< HEAD
"""Route that provides labels the model was trained on.

GET '/labels'
"""
import logging
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)
router = APIRouter()


class LabelsResponse(BaseModel):
    """Use this data model to parse the request body JSON."""

    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


@router.get('/labels', response_model=LabelsResponse)
async def labels():
    """Route for front end to obtain the labels the model was trained on.

    ### Response
    - `effects`: list of strings of effects
    - `helps`: list of strings of medical conditions it can help
    """
    return {
        'effects': ['aroused', 'creative', 'energetic', 'euphoric', 'focused',
                    'giggly', 'happy', 'hungry', 'relaxed', 'sleepy',
                    'talkative', 'tingly', 'uplifted'],
        'helps': ['add/adhd', 'anorexia', 'anxiety', 'arthritis', 'asthma',
                  'bipolar disorder', 'cancer', 'cramps', "crohn's disease",
                  'depression', 'epilepsy', 'eye pressure', 'fatigue',
                  'fibromyalgia', 'gastrointestinal disorder', 'headaches',
                  'hypertension', 'inflammation', 'insomnia',
                  'lack of appetite', 'migraines', 'muscle spasms', 'nausea',
                  'pain', 'ptsd', 'spasticity', 'spinal cord injury', 'stress']
    }
=======
import logging

from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from typing import List

log = logging.getLogger(__name__)
router = APIRouter()


class LabelsResponse(BaseModel):
    """Use this data model to parse the request body JSON."""

    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


@router.get('/labels', response_model=LabelsResponse)
async def labels():
    """
    Routes for user inputs for front end to have categories that model uses to make decisions. 

    ### Response
    - `effects`: string of effects
    - `helps`: string of medical conditions it can help
    """

    return {
        'effects': ['aroused', 'creative', 'energetic', 'euphoric', 'focused', 'giggly', 'happy', 'hungry', 'relaxed', 'sleepy', 'talkative', 'tingly', 'uplifted'],
        'helps': ['add/adhd',  'anorexia',  'anxiety',  'arthritis',  'asthma',  'bipolar disorder',  'cancer',  'cramps',  "crohn's disease",  'depression',  'epilepsy',  'eye pressure',  'fatigue',  'fibromyalgia',  'gastrointestinal disorder',  'headaches',  'hypertension',  'inflammation',  'insomnia',  'lack of appetite',  'migraines',  'muscle spasms',  'nausea',  'pain',  'ptsd',  'spasticity',  'spinal cord injury',  'stress']
    }
>>>>>>> 99d702011ed58a27e10e732c03341558bc7bfa0b
