This project utilizes a Muse Headband that sends EEG frequencies to a Dragonboard 410. The Dragonboard will process
the frequencies and send the data to an Amazon SQS. The SQS will hold the data for the EEG readings and it will be sent 
to an Amazon webpage. The webpage will have two buttons that the user can press to indicate whether or not they want to calm
down or get hyped. The background to the webpage will change colors depending on the EEG's readings, blue - calm and pink - excited/agitated. Depending on the button the user presses, music will play on the webpage to calm the user down or hype them up.
The colors will change real time depending on the user's mood. 
