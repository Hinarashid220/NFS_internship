<div align="center">

# 🔍 RAG Mini-Project — Chat With Your Own Document

**Generative AI & Prompt Engineering Internship — Week 3**

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tool](https://img.shields.io/badge/Tool-NotebookLM-blue)
![Type](https://img.shields.io/badge/Approach-No--Code-orange)

*Understanding how grounding an AI system in a specific document affects answer quality, relevance, and reliability.*

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Project Objectives](#-project-objectives)
- [Document Used](#-document-used)
- [Tool Used](#-tool-used)
- [RAG Architecture](#-rag-architecture)
- [Questions Tested](#-questions-tested)
- [Plain Prompt vs. Grounded RAG](#-plain-prompt-vs-grounded-rag)
- [Key Concepts Learned](#-key-concepts-learned)
- [Key Takeaway](#-key-takeaway)
- [Future Extension](#-future-extension)
- [Technologies](#-technologies)
- [Project Status](#-project-status)

---

## 📌 Overview

This mini-project demonstrates **Retrieval-Augmented Generation (RAG)** using a no-code workflow with **NotebookLM**. Rather than relying on an LLM's general training knowledge, this experiment grounds the model in a private document and evaluates how that grounding affects accuracy, relevance, and hallucination rates.

---

## 🎯 Project Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the basic RAG workflow |
| 2 | Use a private document as a knowledge source |
| 3 | Ask document-dependent questions |
| 4 | Test semantic retrieval |
| 5 | Check answers for hallucinations |
| 6 | Test system behavior when information is missing |
| 7 | Compare grounded answers with plain-prompt answers |

---

## 📄 Document Used

**File:** `Generative_AI_RAG_Learning_Guide.pdf`

The document covers:

- Generative AI
- Retrieval-Augmented Generation
- RAG indexing and query phases
- Chunking
- Embeddings
- Vector search
- Retrieval
- Grounding
- Hallucinations
- RAG vs. plain prompts

---

## 🛠 Tool Used

### NotebookLM

NotebookLM served as the no-code RAG tool, handling document processing and retrieval behind the scenes.

```text
PDF
 ↓
Document Processing
 ↓
Chunking / Indexing
 ↓
Embeddings & Search
 ↓
User Question
 ↓
Relevant Information Retrieved
 ↓
LLM Generation
 ↓
Grounded Answer
```

---

## 🏗 RAG Architecture

```text
                  DOCUMENT
                     │
                     ▼
                 CHUNKING
                     │
                     ▼
                EMBEDDINGS
                     │
                     ▼
               VECTOR STORE
                     │
QUESTION ──► QUESTION EMBEDDING
                     │
                     ▼
               VECTOR SEARCH
                     │
                     ▼
             RELEVANT CHUNKS
                     │
                     ▼
             CONTEXT + QUESTION
                     │
                     ▼
                    LLM
                     │
                     ▼
                  ANSWER
```

**Pipeline:** `Document → Chunking → Embeddings → Retrieval → Context → Generation`

---

## ❓ Questions Tested

### 1. Basic RAG Pipeline
> **Q:** What are the two main phases of the basic RAG pipeline described in the document?

**Result:** ✅ Correct — NotebookLM identified the **Indexing Phase** and **Query Phase** and explained their purposes.
**Evaluation:** No hallucination detected.

### 2. Chunking
> **Q:** Why can chunks that are too large reduce retrieval usefulness?

**Result:** ✅ Correct — explained that excessively large chunks can contain too much irrelevant information.
**Evaluation:** Grounded in the document. No hallucination detected.

### 3. Embeddings
> **Q:** What is the role of embeddings in a RAG system, and why are they useful when two pieces of text have similar meanings but use different words?

**Result:** ✅ Correct — embeddings explained as numerical representations enabling semantic similarity and retrieval.
**Evaluation:** Grounded in the document. No hallucination detected.

### 4. Semantic Retrieval Test
> **Q:** If I ask "When should I split a document into smaller pieces?", which concept in the document is most relevant, and why?

**Result:** ✅ Correct — connected the question to **chunking**, even though the question did not repeat the document's wording.
**Evaluation:** Demonstrated semantic retrieval. No meaningful hallucination detected.

### 5. Missing Information / Hallucination Test
> **Q:** According to the document, which specific embedding model should a developer use for this RAG system, and what is its exact vector dimension?

*The document does not specify an embedding model or vector dimension.*

**Result:** ✅ Correct behavior — NotebookLM stated the information was not provided rather than inventing an answer.
**Evaluation:** No hallucination detected.

### 6. Hallucination Reduction Test
> **Q:** Is RAG guaranteed to completely eliminate hallucinations? Explain your answer using only the information in the document.

**Result:** ✅ Correct — recognized that RAG reduces hallucinations but does not guarantee their elimination.
**Evaluation:** Grounded answer.

### Summary Table

| # | Test Type | Hallucination Detected? |
|---|-----------|:---:|
| 1 | Basic RAG Pipeline | No |
| 2 | Chunking | No |
| 3 | Embeddings | No |
| 4 | Semantic Retrieval | No |
| 5 | Missing Information | No |
| 6 | Hallucination Reduction | No |

---

## ⚖️ Plain Prompt vs. Grounded RAG

A **plain prompt** asks an LLM to answer without providing the specific document as a retrieved knowledge source — the model relies on general knowledge and whatever is included directly in the prompt.

With **RAG**, relevant information is retrieved from the uploaded document and supplied to the LLM as context *before* the answer is generated.

### Short Summary

Grounding the model in private data made answers **more specific, relevant, and verifiable**. Instead of relying only on general model knowledge, NotebookLM retrieved information directly from the uploaded document for document-specific questions. It also handled missing information well — when asked for a specific embedding model and vector dimension not present in the document, it stated the information was unavailable instead of inventing details.

The experiment showed that grounding can **reduce unsupported answers and improve reliability**, although RAG does not completely eliminate hallucinations. Final answer quality still depends on retrieval quality and how correctly the LLM uses the retrieved context.

---

## 🧠 Key Concepts Learned

| Concept | Description |
|---|---|
| **RAG** | Combines information retrieval with LLM generation |
| **Chunking** | Splits documents into smaller retrieval units |
| **Embeddings** | Numerical representations of text used for semantic similarity |
| **Vector Search** | Finds relevant information using embedding similarity |
| **Retrieval** | Selects the most relevant document chunks for a question |
| **Grounding** | Supports an AI response using a specific source |
| **Hallucination** | An unsupported or incorrect AI-generated claim |

---

## 💡 Key Takeaway

RAG is not simply "asking an LLM questions about a PDF." It is a pipeline:

**`Document → Chunking → Embeddings → Retrieval → Context → Generation`**

Retrieval and generation are separate concerns — a strong LLM cannot reliably answer from information that was never retrieved, and retrieving correct information does not automatically guarantee a perfectly grounded answer.

---

## 🚀 Future Extension

This project was first completed using a **no-code RAG tool** to understand the concept and behavior of RAG.

The next stage is to implement the same pipeline **programmatically** using:

- Python
- LangChain or LlamaIndex
- Embeddings
- A vector store such as FAISS
- An LLM API

The coded version will make the individual RAG components visible instead of hiding them behind a no-code interface.

---

## 🧰 Technologies

`Generative AI` · `Retrieval-Augmented Generation (RAG)` · `NotebookLM` · `Large Language Models (LLMs)` · `Embeddings` · `Vector Search` · `Semantic Search` · `Chunking` · `Grounding` · `Hallucination Evaluation`

---

## ✅ Project Status

**Completed — No-Code RAG Experiment**

The project successfully demonstrated document ingestion, document-grounded question answering, semantic retrieval behavior, and hallucination testing.

**Next Step:** Build the same RAG workflow using code to understand what happens behind the no-code interface.
