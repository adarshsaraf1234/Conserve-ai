# Conserve-AI
Conserve-AI is an Agent based on Langgraph and Milvus VectorDB.

## Development Setup

1.  Create and activate a virtual environment
    ```bash
    git clone https://github.com/amany9000/k-net.git
    cd k-net
    python3 -m venv .venv (Python 3.13 is required to fulfill dependencies)
    source .venv/bin/activate
    ```

2.  Install Langgraph CLI
    ```bash
    uv pip install -U "langgraph-cli[inmem]"
    ```
    Note: "inmem" extra(s) are needed to run LangGraph API server in development mode (without requiring Docker installation)

3.  Install the dependencies
    ```bash
    uv pip install -e .
    ```

4.  Configure environment variables
    ```bash
    cp env.example .env
    ```
5.  Run server
    ```bash
    uvx --refresh --from "langgraph-cli[inmem]" --with-editable . langgraph dev --allow-blocking
    ```

## Notes:
1. `uv` is needed for seamless dependency resolution.
2. GPT-OSS:20B is the LLM for this Agent, setup in the Configuration [here](src/langgraph-knet/configuration.py  )
