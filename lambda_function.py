# lambda_function.py
import os
import django
import json
import boto3
from myapp.models import Author

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        messages = event.get('Records', [])
        for record in messages:
            body = json.loads(record['body'])
            item = Author.objects.create(
                name=body.get("name"),
                family=body.get("family"),
            )
        return {"status": "success", "message": "Record processed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
