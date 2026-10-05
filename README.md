## Requirements

- Install [Python](https://www.python.org/downloads/). If using a Linux-based system, this is probably already installed by default.
- Install a code editor, like [VS Code](https://code.visualstudio.com/).
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

## Installation

Download the repo and run 

```bash
uv sync
```

This will install by default all the necessary dependencies.

## API Key

This example runs with free endpoints provided by Nvidia. To get an API key, go to the [Nvidia developer page](https://build.nvidia.com/) and make an account. Then, create an API key in the [API keys page](https://build.nvidia.com/settings/api-keys), in the settings area. **IMPORTANT:** make sure you copy the key before closing the page, as you cannot see it again.

Create a `.env` file and paste you key, like:

```
NVIDIA_API_KEY=KEY-YOU-COPIED
```

## First run

Look at the content of `main.py`. This file sets the model to be used and uses the API key to use the endpoint and use the LLM. When calling the model, notice the `messages` field, where it is instructing the model what are the roles being used