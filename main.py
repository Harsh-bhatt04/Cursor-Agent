from langchain_core.messages import HumanMessage

from app.graph import build_graph


def main():
    graph = build_graph()

    response = graph.invoke(
        {
            "messages": [
                HumanMessage(
    content="Find every .txt file inside this project. exclude .venv folder"
)
            ]
        }
    )

    last_message = response["messages"][-1]
    print(last_message.text())


if __name__ == "__main__":
    main()