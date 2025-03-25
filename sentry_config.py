import sentry_sdk
from dotenv import load_dotenv
import os

def load_sentry_config():
    load_dotenv()

    env = os.getenv("environment")

    if env != "dev":

        sentry_sdk.init(
            dsn="https://53408189f91c880d2ed3d26e9cedf2d5@o4509036266848256.ingest.de.sentry.io/4509036272156752",
            # Do not add data like request headers and IP addresses for users.
            send_default_pii=False,
            environment=env,
        )
