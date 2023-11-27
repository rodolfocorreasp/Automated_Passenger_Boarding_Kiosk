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

form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# # Extract Information Using the custom model


file_path = "boarding-rodolfo.pdf"


with open(file_path, "rb") as f:
       poller = form_recognizer_client.begin_recognize_custom_forms(model_id="PROJECT_MODEL_ID", form=f, include_field_elements=True)
forms = poller.result()


for idx, form in enumerate(forms):
    print("--------Recognizing Form #{}--------".format(idx + 1))
    print("Form was analyzed with model with ID {}".format(form.model_id))
    for name, field in form.fields.items():
        print("Field '{}' has label '{}' with value '{}' and a confidence score of {}".format(
            name,
            field.label_data.text if field.label_data else name,
            field.value,
            field.confidence
        ))


