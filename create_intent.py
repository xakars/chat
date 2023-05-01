from google.cloud import dialogflow
import json
import os
from dotenv import load_dotenv
import argparse


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


if __name__ == '__main__':
    load_dotenv()
    project_id = os.environ["PROJECT_ID"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='training.json', help='path to json file')
    args = parser.parse_args()
    path_to_training_phrases = args.path

    with open(path_to_training_phrases, "r") as f:
        intents = json.load(f)


    for intent, value in intents.items():
        questions = value["questions"]
        answer = value["answer"]
        create_intent(project_id, intent, questions, answer)
