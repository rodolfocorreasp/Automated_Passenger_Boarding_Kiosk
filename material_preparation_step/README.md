## Material Preparation

For the requirements step, I developed a Flight Manifest table that lists the flight information for each passenger.

The CSV file in flight-manifest-csv folder contains the following flight-specific details:

<ul><il>• Carrier</il></ul>
<ul><il>• Flight Number</il></ul>
<ul><il>• Class</il></ul>
<ul><il>• Flight Origin (From)</il></ul>
<ul><il>• Destination (To)</il></ul>
<ul><il>• Flight Date</il></ul>
<ul><il>• Baggage</il></ul>
<ul><il>• Seat</il></ul>
<ul><il>• Gate Number</il></ul>
<ul><il>• Boarding Time</il></ul>
<ul><il>• Ticket No.</il></ul>

I’ve also added columns for the following demographic details.  

<ul><il>•	First Name</il></ul>
<ul><il>•	Last Name</il></ul>
<ul><il>•	Date of Birth</il></ul>
<ul><il>•	Sex</il></ul>

And the columns below indicating the status of the following 5 types of validation:

<ul><il>1.	Passenger Name Validation (NameValidation)</il></ul>
<ul><il>2.	Passenger Date of Birth Validation (DoBValidation)</il></ul>
<ul><il>3.	Passenger Face Validation (PersonValidation)</il></ul>
<ul><il>4.	Passenger Flight Details Validation (BoardingPassValidation)</il></ul>
<ul><il>5.	Passenger carry-on baggage validate for lighter detection (LuggageValidation)</il></ul>

In the boarding_pass_docs folder we can find sample of boarding passes for the passengers listed in the manifest file.  All boarding passes are in PDF format. They were used to develop a custom recognizer model in subsequent steps. 

The id_cards folder contains samples of digital IDs for the passengers that are in the manifest file, they were used to perform face verification by comparing the face image on the ID card with the face shown in a 30-second video, located in digital_video folder.

In the first screenshot below you can find all Azure Resources required for this project:

In the second screenshot below you can find the flight manifest stored it to Azure Blob Storage:

