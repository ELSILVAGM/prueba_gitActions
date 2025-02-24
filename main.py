import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Obtener variables
SECRET_KEY = os.getenv("API_KEY")

print(f"Secret Key: {SECRET_KEY}")

