## Material Preparation

For the requirements step, I developed a Flight Manifest table that lists the flight information for each passenger.

The CSV file in flight-manifest-csv folder contains the following flight-specific details:

- Carrier
- Flight Number
- Class
- Flight Origin (From)
- Destination (To)
- Flight Date
- Baggage
- Seat
- Gate Number
- Boarding Time
- Ticket No.

I’ve also added columns for the following demographic details:  

-	First Name
-	Last Name
-	Date of Birth
-	Sex

And the columns below indicating the status of the following 5 types of validation:

1.	Passenger Name Validation (NameValidation)
2.	Passenger Date of Birth Validation (DoBValidation)
3.	Passenger Face Validation (PersonValidation)
4.	Passenger Flight Details Validation (BoardingPassValidation)
5.	Passenger carry-on baggage validate for lighter detection (LuggageValidation)

In the boarding_pass_docs folder we can find sample of boarding passes for the passengers listed in the manifest file.  All boarding passes are in PDF format. They were used to develop a custom recognizer model in subsequent steps. 

The id_cards folder contains samples of digital IDs for the passengers that are in the manifest file, they were used to perform face verification by comparing the face image on the ID card with the face shown in a 30-second video, located in digital_video folder.

In the first screenshot below you can find all Azure Resources required for this project:

In the second screenshot below you can find the flight manifest stored it to Azure Blob Storage:

