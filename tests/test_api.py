import requests
import json

def test_chat():
    url = "http://localhost:8000/chat"
    payload = {
        "model_name": "llama-3.3-70b-versatile",
        "model_provider": "Groq",
        "system_prompt": "You are a helpful assistant.",
        "messages": [
            {"role": "user", "content": "Hello! My name is Balaji."},
            {"role": "ai", "content": "Hello Balaji! How can I help you today?"},
            {"role": "user", "content": "What is my name?"}
        ],
        "allow_tools": False
    }
    
    try:
        print("Sending request to /chat...")
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response JSON:")
            print(json.dumps(response.json(), indent=2))
            assert "response" in response.json()
            assert "tool_used" in response.json()
            if "Balaji" in response.json()["response"]:
                print("SUCCESS: Model remembered the name.")
            else:
                print("FAILURE: Model did not remember the name.")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_chat()
    
