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


# # ID Card detection

id_card_file_path = "ca-dl-rodolfo-correa.png"

with open (id_card_file_path, "rb") as c:
    poller = form_recognizer_client.begin_recognize_identity_documents(identity_document=c)
id_documents = poller.result()


for idx, id_document in enumerate(id_documents):
    print("--------Recognizing ID Card document #{}--------".format(idx+1))
    first_name = id_document.fields.get("FirstName")
    if first_name:
        print("First Name: {} has confidence: {}".format(first_name.value, first_name.confidence))
        last_name = id_document.fields.get("LastName")
    last_name = id_document.fields.get("LastName")
    if last_name:
        print("Last Name: {} has confidence: {}".format(last_name.value, last_name.confidence))
    document_number = id_document.fields.get("DocumentNumber")
    if document_number:
        print("Document Number: {} has confidence: {}".format(document_number.value, document_number.confidence))
    dob = id_document.fields.get("DateOfBirth")
    if dob:
        print("Date of Birth: {} has confidence: {}".format(dob.value, dob.confidence))
    doe = id_document.fields.get("DateOfExpiration")
    if doe:
        print("Date of Expiration: {} has confidence: {}".format(doe.value, doe.confidence))
    sex = id_document.fields.get("Sex")
    if sex:
        print("Sex: {} has confidence: {}".format(sex.value[1:], sex.confidence))
    address = id_document.fields.get("Address")
    if address:
        print("Address: {} has confidence: {}".format(address.value, address.confidence))
    country_region = id_document.fields.get("CountryRegion")
    if country_region:
        print("Country/Region: {} has confidence: {}".format(country_region.value, country_region.confidence))
    region = id_document.fields.get("Region")
    if region:
        print("Region: {} has confidence: {}".format(region.value, region.confidence))

