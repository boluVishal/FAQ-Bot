# FAQ Bot
FAQ Bot developed using Rasa Core  & Rasa NLU

Training Rasa NLU Data: 
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

Training Rasa Core Stories:
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policy.yml

Running the action server
python -m rasa_core_sdk.endpoint --actions actions

Running the rasa core server
python -m rasa_core.run --enable_api -d models/dialogue -u models/current/nlu --cors "*" -o out.log --endpoints endpoints.yml --credentials credentials.yml --verbose

Running the rasa nlu server 
python -m rasa_nlu.server -c nlu_config.yml  --path projects/

#API to connect with custom UI
http://localhost:5005/conversations/(userid)/respond






