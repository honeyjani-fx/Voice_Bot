"""Import Libraries"""

import asyncio
import logging
import signal
from vocode.streaming.streaming_conversation import StreamingConversation
from vocode.helpers import create_streaming_microphone_input_and_speaker_output
from vocode.streaming.transcriber import *
from vocode.streaming.agent import *
from vocode.streaming.synthesizer import *
from vocode.streaming.models.transcriber import *
from vocode.streaming.models.agent import *
from vocode.streaming.models.synthesizer import *
from vocode.streaming.models.message import BaseMessage
from dotenv import load_dotenv
import vocode
import tracemalloc


tracemalloc.start()

# Setting up an environment variable for the secret keys
load_dotenv()

# Set the keys into the vocode module
vocode.setenv(
    OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY'),
    DEEPGRAM_API_KEY=os.environ.get('DEEPGRAM_API_KEY'),
    ELEVEN_LABS_API_KEY=os.environ.get('ELEVEN_LABS_API_KEY')
)


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



""" Start of the main function : 
This includes the 3 main functions - 
1] Speech-to-text from microphone input
2] GPT response from the above transcriptions
3] Text-to-Speech of the transcriptions provided"""

async def main():
    (
        microphone_input,
        speaker_output,
    ) = create_streaming_microphone_input_and_speaker_output(
        use_default_devices=False,
        logger=logger,
        use_blocking_speaker_output=True, # this moves the playback to a separate thread, set to False to use the main thread
    )

    conversation = StreamingConversation(
        output_device=speaker_output,
        
        # Model for Speech to Text conversion
        transcriber=DeepgramTranscriber(
            DeepgramTranscriberConfig.from_input_device(
                microphone_input,
                endpointing_config=PunctuationEndpointingConfig(),
            )
        ),
        
        
        # Model for generating GPT response
        # CHAT_GPT_AGENT_DEFAULT_MODEL_NAME = "gpt-3.5-turbo-0613"
        agent=ChatGPTAgent(
            ChatGPTAgentConfig(
                initial_message=BaseMessage(text="What's up"),
                prompt_preamble="""The AI is having a pleasant conversation about life""",
            )
        ),
        synthesizer=GTTSSynthesizer(
            GTTSSynthesizerConfig.from_output_device(speaker_output)
        ),
        logger=logger,
    )
    await conversation.start()
    print("Conversation started, press Ctrl+C to end")
    signal.signal(
        signal.SIGINT, lambda _0, _1: asyncio.create_task(conversation.terminate())
    )
    while conversation.is_active():
        chunk = await microphone_input.get_audio()
        conversation.receive_audio(chunk)


if __name__ == "__main__":
    asyncio.run(main())