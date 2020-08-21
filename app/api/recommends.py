import logging

from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from typing import List

log = logging.getLogger(__name__)
router = APIRouter()

#info, info_aka, info_type, info_rating, info_num_reviews, info_feelings, info_helps, info_description

class RecommendRequest(BaseModel):
    """Use this data model to parse the request body JSON."""

    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


class RecommendItem(BaseModel):
    """"Doc String""" 
    strain: str = Field(...)
    strain_type: str = Field(...)
    description: str = Field(...)
    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


class RecommendResponse(BaseModel):
    """"Doc String"""
    strains: List[RecommendItem] = Field(...)



@router.post('/recommends', response_model=RecommendResponse)
async def recommends(item:RecommendRequest):
    """
    Routes for user inputs for front end to have categories that model uses to make decisions. 

    ### Response
    - `effects`: string of effects
    - `helps`: string of medical conditions it can help
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
