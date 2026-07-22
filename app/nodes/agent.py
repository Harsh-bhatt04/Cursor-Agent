from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from app.state import AgentState
from app.tools.math_tools import add
from app.tools.file_tools import read_file
from app.tools.file_tools import list_files


load_dotenv()

llm = init_chat_model("google_genai:gemini-3.5-flash").bind_tools([add,read_file,list_files])



def agent_node(state: AgentState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }