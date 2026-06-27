 
## 2026-06-13 
### Vector Database Deep Dive 
- Studied FAISS vs ChromaDB vs Pinecone comparison 
- FAISS is best for local/offline use, no server needed 
- ChromaDB is easiest to set up for small RAG projects 
- Pinecone is managed cloud solution, best for production 
- Learned about cosine similarity vs dot product for vector search 
 
## 2026-06-14 
### Reranking Strategies in RAG 
- Reranking improves retrieval quality after initial search 
- Cross-encoder rerankers more accurate than bi-encoders 
- Cohere Rerank API is popular managed reranking solution 
- BGE reranker is best open source option for local use 
 
## 2026-06-16 
### Self-RAG Architecture Notes 
- Self-RAG model decides when to retrieve and when to skip 
- Uses special reflection tokens to evaluate retrieval quality 
- ISREL token checks if retrieved doc is relevant to query 
- ISSUP token checks if answer is supported by retrieved doc 
 
## 2026-06-18 
### CRAG - Corrective RAG Notes 
- CRAG evaluates retrieved docs before passing to generator 
- If retrieval score is low it triggers web search fallback 
- Knowledge refinement strips irrelevant parts from retrieved docs 
- CRAG improves accuracy on questions needing precise facts 
 
## 2026-06-20 
### Adaptive RAG Architecture Notes 
- Adaptive RAG routes queries based on complexity level 
- Simple queries answered directly without retrieval step 
- Complex queries trigger multi-step agentic retrieval pipeline 
- Query classifier trained to predict best retrieval strategy 
 
## 2026-06-23 
### LangGraph Workflow Orchestration Notes 
- LangGraph builds stateful multi-step RAG workflows as graphs 
- Nodes represent individual steps like retrieval and generation 
- Edges define conditional routing between pipeline steps 
- State object passed between nodes tracks full pipeline context 
 
## 2026-06-25 
### Multi-Agent Collaboration in RAG Notes 
- Multi-agent setup splits tasks across specialized LLM agents 
- Retriever agent gathers documents while critic agent evaluates 
- Supervisor agent coordinates workflow between specialized agents 
- Reduces single agent overload on complex multi-step queries 
 
## 2026-06-27 
### Tool Calling in Agentic RAG Notes 
- Agents call external tools like calculator and web search 
- Tool schema defines name description and expected parameters 
- LLM decides which tool to call based on user query intent 
- Tool output fed back into context for final answer generation 
 
## 2026-06-30 
### Agent Memory and Persistence Notes 
- Long term memory stores facts learned across multiple sessions 
- Short term memory holds context within single conversation only 
- Vector store used to persist and retrieve relevant past memories 
- LangGraph checkpointer saves agent state for resuming workflows 
 
## 2026-07-02 
### Human in the Loop Agentic RAG Notes 
- Human in the loop pauses agent for approval on critical actions 
- LangGraph interrupt feature stops execution at defined checkpoints 
- Useful for high stakes actions like sending emails or payments 
- User feedback resumes agent workflow with approved or edited action 
 
## 2026-07-04 
### Agentic RAG Error Handling Notes 
- Retry logic added for failed tool calls or API timeouts 
- Fallback responses generated when retrieval returns no results 
- Graceful degradation keeps agent functional during partial failures 
- Error logs captured with full context for debugging pipeline issues 
 
## 2026-07-06 
### Streaming Responses in Agentic RAG Notes 
- Streaming sends partial tokens to client as they are generated 
- Server-Sent Events used to stream LLM output over HTTP 
- Improves perceived latency for long agentic reasoning chains 
- Intermediate agent steps can be streamed for transparency 
 
## 2026-07-08 
### Cost Tracking in Agentic RAG Notes 
- Each LLM call tracked for token usage and estimated cost 
- Langfuse used to trace full agent run with cost breakdown per step 
- Helps identify expensive steps like excessive retrieval attempts 
- Budget limits can stop agent if cost exceeds threshold per query 
