#  Copyright © Roberto Chiosa 2024.
#  Email: roberto.chiosa@polito.it
#  Last edited: 4/10/2024

import json

import requests
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(
    prefix="/metadata",
    tags=["Monitoring"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    path="",
    summary="Exposes SPARQL endpoint to query the metadata model",
    response_description="Query result as JSON",
)
def get_sparql_query(
        query: str = Query(
            title="query",
            description="The SPARQL query to be performed",
            examples=["SELECT * WHERE { ?s ?p ?o }"],
        ),
):
    """
    Exposes a graphdb endpoint that allows you to perform a SPARQL query on the building metadata model.
    For example you can get all the temperature sensors as follows.

    ```
    PREFIX brick: <https://brickschema.org/schema/Brick#>
    SELECT *
    WHERE {
        ?sensor a brick:Temperature_Sensor .
    }
    ```

    """

    # load graph to graphdb
    # clear all on repository
    res = requests.get(
        f"http://localhost:7200/repositories/bos",
        headers={"Accept": "application/sparql-results+json"},
        params={"query": query},
    )
    if res.status_code != 200:
        raise HTTPException(status_code=500, detail="GraphDB query failed")

    decoded = res.content.decode("utf-8")
    return json.loads(decoded)
