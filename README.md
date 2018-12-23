# FAQ Bot
FAQ Bot developed using Rasa Core  & Rasa NLU

Original implementation : 
https://github.com/RasaHQ/rasa-demo.git

## Step 1: Training Rasa NLU Data: 
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

## Step 2: Training Rasa Core Stories:
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policy.yml

## Step 3: Running the action server
python -m rasa_core_sdk.endpoint --actions actions

## Step 4: Running the rasa core server
python -m rasa_core.run --enable_api -d models/dialogue -u models/current/nlu --cors "*" -o out.log --endpoints endpoints.yml --credentials credentials.yml --verbose

## Step 5: Running the rasa nlu server 
python -m rasa_nlu.server -c nlu_config.yml  --path projects/

## Step 6: API to connect with custom UI
http://localhost:5005/conversations/(userid)/respond

for more details visit this doc: https://rasa.com/docs/core/server/#operation/respond

### If you want to connect your bot to a webpage you can use this repository :
https://github.com/JiteshGaikwad/RASA-Chatbot-UI.git






