# Voice_Bot

## README ##

A Python script that creates a Voice Bot imeplementing three features:

1] Speech-to-text Transcription

2] Generating GPT response from the above transcription

3] Perform Text-to-Speech implementation

## Description ##

* This Repository implements the voice bot system with the help of 'vocode' repo.
* The 'Vocode' provides an access to use its funcationality in the form of a package. 
* This repo uses 'Vocode-Python' as a baseline model and further experiments with the prompts and models to attain best results.

## Installation ##

Kindly follow the following steps to be performed:


### 1. Creation of a folder and the main.py file: ###

   * Create a folder and copy the main.py attached in the mail.


### 2. Create a virtual environment (recommended): ###

   * python3 -m venv venv
   * source venv/bin/activate


### 3. Install the required Python libraries: ###


   * pip install vocode



### 4. Create a .env file to store the keys in an environment variable in the format as below: ###

   * OPENAI_API_KEY='your_key'
   * DEEPGRAM_API_KEY='your_key'


On performing all the above steps, you are all set to run the python script.

## Usage ##

### 1] To use the repo , run the main.py script as follows:###

   python3 main.py



### 2] Select the device parameter:###

   Upon running the command , you will be required to select 1) a microphone input and 2) Sound Output device. Select the above based on your devices. And then it starts working.

