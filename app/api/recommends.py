import logging

from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from typing import List

log = logging.getLogger(__name__)
router = APIRouter()

#info, info_aka, info_type, info_rating, info_num_reviews, info_feelings, info_helps, info_description

class RecommendRequest(BaseModel):
    """
    The user selects from a list of effects and helps.
    """

    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


class RecommendItem(BaseModel):
    """"
    Specifically what gets recomended based on user query.
    """ 
    strain: str = Field(...)
    strain_type: str = Field(...)
    description: str = Field(...)
    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


class RecommendResponse(BaseModel):
    """
    Returning strains that are best for the picked options of effects and help
    """
    strains: List[RecommendItem] = Field(...)



@router.post('/recommends', response_model=RecommendResponse)
async def recommends(item:RecommendRequest):
    """
    Routes for user reccomendations

    ### User inputs
    the following to help with selection of response
    - `effects`: string of effects
    - `helps`: string of medical conditions it can help

    ### Response: 
    the following is what is outputted based on user inputs: 
    - `strain`: name of strain
    - `strain_type`: indica or sativa
    - `description`: user descriptions of strains 
    - `effects`: specific to the particular strain
    - `helps`: specific to the particular strain 
    """

    #ArcticBlue, Hybrid, euphoric, helps add/adhd, 
    return {
        'strains': [
            {
                'strain': 'ArcticBlue',
                'strain_type': 'Hybrid',
                'description': '60/40 effects of sativa/indica',
                'effects': ['aroused', 'creative', 'energetic', 'euphoric', 'focused'],
                'helps': ['add/adhd',  'anorexia',  'anxiety',  'arthritis',  'asthma']
            },
            {
                'strain': 'Atomic Goat',
                'strain_type': 'Sativa',
                'description': 'pure sativa',
                'effects': ['happy', 'hungry', 'relaxed', 'sleepy', 'talkative'],
                'helps': ['nausea',  'pain',  'ptsd',  'spasticity',  'spinal cord injury']
            },
        ]
    }
