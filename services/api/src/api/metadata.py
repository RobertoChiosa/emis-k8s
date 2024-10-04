#  Copyright © Roberto Chiosa 2024.
#  Email: roberto.chiosa@polito.it
#  Last edited: 4/10/2024

title = "Building Operating System API"
version = "0.1.0"
terms_of_service = "https://github.com/RobertoChiosa/building-operating-system"
contact = {
    "name": "Roberto Chiosa",
    "url": "https://gravatar.com/robertochiosa",
    "email": "roberto.chiosa@gmail.com",
}

license_info = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}

openapi_tags = [
    {
        "name": "Monitoring",
        "description": "Endpoints related to the monitoring infrastructure data and metadata.",
    },
    {
        "name": "Report",
        "description": "Internal reports.",
    },
]

description = """
This API is part of the Building Operating System project. It provides access to the data and  metadata of the sensors 
and actuators in the building.
"""
