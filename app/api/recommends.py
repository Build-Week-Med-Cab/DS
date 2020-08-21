"""Route that provides recommended strains based on input.

POST '/recommends'
"""
import logging
from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from ..recommend import get_recommendations

log = logging.getLogger(__name__)
router = APIRouter()


class RecommendRequest(BaseModel):
    """Input schema - the user's choices for effects and issues."""

    effects: List[str] = Field(
        ...,  # required field, no default
        title='Preferred effects',
        description='List of strings containing preferred dominant effects.',
        example=['euphoric', 'energetic']
    )
    helps: List[str] = Field(
        ...,  # required field, no default
        title='Effective for these issues',
        description=('List of strings containing issues '
                     'which strains are reported to help.'),
        example=['add/adhd',  'anorexia']
    )
    text: Optional[str] = Field('', example='I prefer sativa heavy hybrids.')
    count: Optional[int] = Field(4, gt=0, le=25, example=4)

    def format(self, model='nn'):
        """Combine input data into format ready for preprocessing."""
        if 'nn' == model:
            return ' '.join(self.effects + self.helps + [self.text])


class RecommendItem(BaseModel):
    """Output schema - strain information."""

    strain: str = Field(..., title='Strain Name')
    strain_type: str = Field(..., title='Strain Type')
    description: str = Field(..., title='Strain Description')
    effects: List[str] = Field(..., example=['euphoric', 'energetic'])
    helps: List[str] = Field(..., example=['add/adhd',  'anorexia'])


class RecommendResponse(BaseModel):
    """Output schema - List of recommended strains."""

    strains: List[RecommendItem] = Field(...)


@router.post('/recommends', response_model=RecommendResponse)
async def recommends(item: RecommendRequest):
    """
    Routes for user reccomendations.

    ### Request:
    user selected labels, user text, and desired number of recommendations
    - `effects`: list of strings of effects
    - `helps`: list of strings of medical conditions it can help
    - `text`: optional string that decribes users preferences
    - `count`: optional integer, number of recommmendations to return

    ### Response:
    a list of information about each recommended strains
    - `strain`: name of strain
    - `strain_type`: indica or sativa
    - `description`: user descriptions of strains
    - `effects`: specific to the particular strain
    - `helps`: specific to the particular strain
    """
    return {
        'strains': get_recommendations(user_input=item.format('nn'),
                                       num=item.count),
    }
