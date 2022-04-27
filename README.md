# avatars_backend

## Set up

### Create new conda environment
conda create -n avatars_backend python=3.8

### Deploy backend
python manage.py runserver 0.0.0.0:8000

# ASN backend repository

This repository contains the code for first version of the API that helps to interact
with the ASN database.
The backend is a django-based API that leverages a SQlite database and  is containerized through a dockerfile

One main API has been implemented: From the table ip2asn, given an AS number, is returned AS information(As number, country code, AS description)

  database: db.sqlite3 (tables):

    - ip2asn

    - ip2country


  django api structure:

    - models (Auto-generate): 

        $ python manage.py inspectdb
        $ python manage.py inspectdb > models.py

    - serializers

        class Ip2AsnSerializer(ModelSerializer):
     
    - views

        class Ip2AsnViewSet

backend:
    
    - 
    