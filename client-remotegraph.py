from langgraph.pregel.remote import RemoteGraph
from langgraph_sdk import get_sync_client
from typing import Any, Dict

def get_non_streaming_agent_response(
    assistant_id: str, 
    input_message: str, 
    api_url: str = "http://localhost:2024"
) -> Dict[str, Any]:
    """
    Calls a LangGraph agent using a non-streaming RemoteGraph.

    Args:
        assistant_id: The ID of the deployed assistant graph.
        input_message: The user's input message.
        api_url: The URL of the LangGraph API server.

    Returns:
        The final output from the agent's run.
    """
    # Create a synchronous client for thread management
    sync_client = get_sync_client(url=api_url)
    
    # Create a new thread using the sync client
    thread = sync_client.threads.create()
    
    # Create a RemoteGraph object for the non-streaming invoke call
    remote_graph = RemoteGraph(assistant_id, url=api_url)
    
    # Use the invoke() method on the RemoteGraph instance
    # Pass the thread ID via the `config` for stateful runs
    response = remote_graph.invoke(
        {"messages": [{"role": "user", "content": input_message}]},
        config={"configurable": {"thread_id": thread["thread_id"]}}
    )
    
    return response

# Example usage
if __name__ == "__main__":
    try:
        response_data = get_non_streaming_agent_response(
            assistant_id="assistant_graph", # Replace with your graph's ID
            input_message="Read the KnowledgeBase Docs for ‘Energizing Green Cities in Southeast Asia’, refine and return the top 3 entries. Have 5 plus lines of information in each entry and return them in a list"
        )
        
        print("response_data", response_data)
        
        print("Final non-streaming response:")
        print(response_data["messages"][1]["content"])
    except Exception as e:
        print(f"An error occurred: {e}")
