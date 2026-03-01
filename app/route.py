from fastapi import APIRouter, HTTPException
from app.model import RequestState
from agents.ai_agents import get_response_from_ai_agent

router = APIRouter()

ALLOWED_MODEL_NAMES = ["openai/gpt-oss-120b", "llama-3.3-70b-versatile"]

@router.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(status_code=400, detail="Invalid model name. Kindly select a valid AI model")
    
    try:
        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))