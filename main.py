from langchain_core.messages import HumanMessage

from app.graph import build_graph


def main():
    graph = build_graph()

    response = graph.invoke(
        {
            "messages": [
                HumanMessage(
    content="Create a file named \"notes.txt\" and write \"Hello World\" into it."
)
            ]
        }
    )

    last_message = response["messages"][-1]
    print(last_message.text())


if __name__ == "__main__":
    main()