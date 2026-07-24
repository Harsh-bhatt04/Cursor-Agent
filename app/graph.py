from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from app.nodes.agent import agent_node
from app.state import AgentState
from app.tools.math_tools import add
from app.tools.file_tools import read_file
from app.tools.file_tools import list_files,write_file,search_files

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(
        [
            add,read_file,
            list_files,
            write_file,
            search_files
        ]
    )
)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        tools_condition,
    )
    graph.add_edge("tools", "agent")

    return graph.compile()