from langgraph_sdk import get_sync_client

def main():
    # Connect to your running LangGraph agent API
    client = get_sync_client(url="http://localhost:2024")

    # Step 1: Create a new thread for the conversation.
    thread = client.threads.create()
    thread_id = thread["thread_id"]
    print(f"Created a new thread with ID: {thread_id}")

    # Step 2: Call the agent using the thread_id.
    # The `runs.stream()` method returns an iterator, not an async generator.
    # You can iterate over it directly in a synchronous context.
    response_stream = client.runs.stream(
        thread_id=thread_id,
        assistant_id="assistant_graph",
        input={"messages": [{"role": "user", "content": "Summarise ‘Energizing Green Cities in Southeast Asia’ for me in 2 paragraphs"}]}
    )

    # Step 3: Iterate through the streaming response
    for chunk in response_stream:
        print(f"Received event: {chunk.event}")
        print(f"Data: {chunk.data}")
        
        if chunk.data:
            return

if __name__ == "__main__":
    main()
