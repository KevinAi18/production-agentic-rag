 
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
