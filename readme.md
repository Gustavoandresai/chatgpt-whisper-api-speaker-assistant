# chatgpt-whisper-api-speaker-assistant
A Voice assistant chatbot made with ChatGPT API and Whisper API speech to text to for smart assistant conversation and customizable personality
Welcome to the future of conversation! Imagine having an application that not only listens to you but also understands what you're saying and responds to you intelligently and conversationally. 


That's what chatgpt-whisper-api-speaker-assistant offers, an application developed with Python that allows you to talk to a virtual assistant in a way you've never experienced before.
The way it works is simple: ChatGPT Speaker records your voice and uses Whisper API transcription technology to convert what you say into text. It then uses the powerful ChatGPT API to process your question and find the best possible answer. And best of all, the answer comes in a synthetic robot voice, you'll feel like you're talking to a real human.


Imagine having a smooth and seamless conversation with an application that is always there to help you with anything you need. From answering questions about the weather to giving you advice on what movies to watch or helping you learn a new language. 
So if you're ready to have a completely new conversation experience, Follow the instruction down bellow for install chatGPT API and Whisper API Tutorial with python

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project

[![ChatGPT Api flow Screen Shot][product-screenshot]](https://github.com/Gustavoandresai/chatgpt-whisper-api-speaker-assistant)

This project is a customizable voice assistant that uses machine learning to generate responses to user queries. The system is initialized with a Text-to-Speech voice and allows the user to speak to the system through a microphone. The audio transcription is sent to OpenAI, which uses a language model to generate a chat response. The chat response is printed in the console and spoken out loud with the help of the Text-to-Speech engine.

The project can be customized to be any personality or conversation style. For example, it can be used to simulate a virtual assistant, a role-playing game companion, or any other type of personality. To do this, the initial messages and language models used by OpenAI can be modified.




<!-- GETTING STARTED -->
## Getting Started

To get started with the voice assistant, follow these steps:
Clone the repository to your local machine.

1) Install the required dependencies. See the next section for instructions.

2) Set up an OpenAI API key. You can get one by signing up for the OpenAI GPT-3 API at https://openai.com/api/.

3) Update the api_key variable in the code with your OpenAI API key.

4) Customize the personality of the voice assistant by modifying the messages variable in the main.py file.

5) Run the main.py script to start the voice assistant.

### Prerequisites

Installing Dependencies
The voice assistant relies on the following dependencies:
Python 3.7 or later
Pyttsx3
OpenAI

### Installation

You can install these dependencies using pip, the Python package manager. Here are the steps:
   ```sh
   git clone https://github.com/Gustavoandresai/chatgpt-speaker-openai-whisper.git
   ```
Run the following command to install dependencies:
 `OpenAi` `pyttsx3` `SpeechRecognition`
   ```sh
   pip install -r requirements.txt
   ```




<!-- USAGE EXAMPLES -->
## Usage

Once you have installed the dependencies, you are ready to run the voice assistant.
Once you have installed these dependencies, you can use the record_audio() function in the mic.py file to record audio and the transcribe_forever() function to transcribe the audio into text.
To run the project, execute the main.py file.
   ```sh
   python main.py
   ```




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->
## Contact

Gustavo Andres Barreto- - Barretoandres461@gmail.com

Project Link: [https://github.com/Gustavoandresai/chatgpt-whisper-api-speaker-assistant](https://github.com/Gustavoandresai/chatgpt-whisper-api-speaker-assistant)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-url]: https://github.com/Gustavoandresai/chatgpt-whisper-api-speaker-assistant/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gustavoandresbarreto
[product-screenshot]: portfolio-9.jpg
