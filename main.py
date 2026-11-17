from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model for the text field
class TextData(BaseModel):
    text: str

# Welcome Note
@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Customized for Siva Kumar Gundlamadugu"}

# FastAPI endpoint to accept POST request with a JSON body containing a single field "text"
@app.post("/generate/")
def generate(data: TextData):
    """
    Generate an MD5 checksum for the provided text data.
    
    This endpoint accepts a JSON payload containing text and returns a unique 32-character
    hexadecimal MD5 hash (checksum) of that text. The checksum serves as a fingerprint 
    that can be used to verify data integrity or detect if text has been modified.
    
    Args:
        data (TextData): A Pydantic model containing:
            - text (str): The input text string to generate a checksum for
    
    Returns:
        dict: A dictionary containing:
            - checksum (str): A 32-character hexadecimal MD5 hash of the input text
    
    Example:
        >>> # Request: POST /generate/
        >>> # Payload: {"text": "hello world"}
        >>> # Response: {"checksum": "5eb63bbbe01eeed093cb22bb8f5acdc3"}
    
    Note:
        - MD5 is a fast hashing algorithm, but it's cryptographically weak
        - For security-sensitive applications, consider using SHA-256 or stronger algorithms
        - The same input text will always produce the same checksum
    """
    # Encode the text string to bytes, then apply MD5 hashing algorithm
    # encode() converts the Unicode string to UTF-8 bytes for hashing
    # hashlib.md5() creates an MD5 hash object from the byte string
    # hexdigest() converts the hash to a 32-character hexadecimal string representation
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    
    # Return the checksum wrapped in a dictionary with key "checksum"
    return {"checksum": checksum}
