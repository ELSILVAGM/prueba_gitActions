import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Obtener variables
API_KEY = os.getenv("API_KEY")

print(f"Secret Key: {API_KEY}")

