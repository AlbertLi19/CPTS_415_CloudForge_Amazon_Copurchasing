import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import (
    ServerSelectionTimeoutError,
    OperationFailure,
    ConfigurationError
)

uri = "mongodb+srv://<username>:<password>@cluster0.z9a1axw.mongodb.net/?appName=Cluster0"

try:
    print("Creating client...")

    client = MongoClient(
        uri,
        server_api=ServerApi("1"),
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000,
    )

    print("Trying to ping MongoDB...")

    client.admin.command("ping")

    print("Connected to MongoDB!")

    db = client["amazon_copurchasing"]

    products_collection = db["products"]
    reviews_collection = db["reviews"]
    copurchases_collection = db["copurchases"]

except ServerSelectionTimeoutError as e:
    print("Could not find/connect to MongoDB server:")
    print(e)

except OperationFailure as e:
    print("Authentication failed:")
    print(e)

except ConfigurationError as e:
    print("MongoDB/DNS configuration error:")
    print(e)

except Exception as e:
    print(type(e).__name__)
    print(e)