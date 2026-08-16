# FAQ Bot

A Rasa-based FAQ chatbot. The NLU layer handles intent classification from user questions, and Rasa Core manages the conversation flow based on trained stories. Built on top of the official Rasa demo as a starting point.

## Running it

You need Rasa NLU and Rasa Core installed (old-style separate packages — this predates the unified `rasa` CLI).

**1. Train NLU**
```bash
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

**2. Train Core**
```bash
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policy.yml
```

**3. Start the action server**
```bash
python -m rasa_core_sdk.endpoint --actions actions
```

**4. Start the Core server**
```bash
python -m rasa_core.run --enable_api -d models/dialogue -u models/current/nlu --cors "*" -o out.log --endpoints endpoints.yml --credentials credentials.yml --verbose
```

**5. Start the NLU server**
```bash
python -m rasa_nlu.server -c nlu_config.yml --path projects/
```

**6. Talk to the bot**

The REST API endpoint for a user conversation:
```
http://localhost:5005/conversations/{user_id}/respond
```

## Connecting a UI

To wire this up to a web chat widget, use the [RASA-Chatbot-UI](https://github.com/JiteshGaikwad/RASA-Chatbot-UI) repo — it connects via the REST input channel on port 5005.

## Files

| File | What it is |
|---|---|
| `nlu.md` | Training examples for intent classification |
| `stories.md` | Conversation flow examples |
| `domain.yml` | Intents, entities, responses, and actions |
| `actions.py` | Custom action handlers |
| `policy.yml` | Core policy configuration |
| `nlu_config.yml` | NLU pipeline config |






