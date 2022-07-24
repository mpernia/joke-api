from fastapi import APIRouter, Depends, HTTPException, Query
from api.services.math import Maths
from typing import List, Union

router = APIRouter()


@router.get('/maths/lcm', tags=["Maths"])
async def lcm(numbers: Union[List[int], None] = Query()):
    return {'value': Maths.lcm(numbers)}


@router.get('/maths/inc', tags=["Maths"])
async def inc(number: int):
    return {'value': Maths.inc(number)}


