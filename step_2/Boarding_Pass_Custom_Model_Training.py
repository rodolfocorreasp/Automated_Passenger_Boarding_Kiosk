# # Importing Azure Form Recognizer Python modules

import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential


# # Form Recognizer endpoint and key and instantiate object

AZURE_FORM_RECOGNIZER_ENDPOINT = "PROJECT_ENDPOINT_URL"
AZURE_FORM_RECOGNIZER_KEY = "PROJECT_SECRET_KEY""

endpoint = AZURE_FORM_RECOGNIZER_ENDPOINT
key = AZURE_FORM_RECOGNIZER_KEY


# # Train Custom Boarding Pass Recognition


form_training_client = FormTrainingClient(endpoint=endpoint, credential=AzureKeyCredential(key))

saved_model_list = form_training_client.list_custom_models()

trainingDataUrl = "PROJECT_DATA_URL"

training_process = form_training_client.begin_training(trainingDataUrl, use_training_labels=False)
custom_model = training_process.result()

custom_model

custom_model.model_id

custom_model.status

custom_model.training_started_on

custom_model.training_completed_on

custom_model.training_documents

custom_model.properties