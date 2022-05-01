"""
It is responsible for loading the environment variables

...

Methods
-------
load()
    Loads environment variables
"""

import os
from dotenv import load_dotenv


def load():
    """
    Loads environment variables

    If '.env.developer' is present, variables in it will override variables
    in '.env'
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    stage_config = {
        "local": ".env",
    }

    dotenv_config = {
        "local": True,
    }

    stageSetted = os.getenv("STAGE", 'local')
    print('Environment setted: ' + stageSetted)

    dot_env_path = os.path.join(BASE_DIR, stage_config[stageSetted])
    print(dot_env_path)

    OVERRIDE_SO_ENV = dotenv_config[stageSetted]
    print('System Environment Overrided: ' + str(OVERRIDE_SO_ENV))

    load_dotenv(dotenv_path=dot_env_path, override=OVERRIDE_SO_ENV)
