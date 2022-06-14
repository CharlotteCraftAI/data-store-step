import os

import pandas as pd

from dotenv import load_dotenv
from craft_ai_sdk import CraftAiSdk

if __name__ == '__main__':
  load_dotenv()  # load environment variables from .env

  print("Running test step")

  sdk = CraftAiSdk(access_token=os.environ.get('CRAFT_AI_ACCESS_TOKEN'),
                   environment_url=os.environ.get('CRAFT_AI_ENVIRONMENT_URL'))

  pdcsv = pd.DataFrame([[1, "Hello"], [45, "Thomas"]],
                       columns=["number", "name"])
  print(pdcsv)

  pdcsv.to_csv('raw.csv', index=False)
  sdk.data_store_upload_object('raw.csv', 'test-documentation-data-store.csv')
  os.remove('raw.csv')
