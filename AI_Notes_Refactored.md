# 🧠 Comprehensive AI Engineering Notes

## 1. N-Grams

### 1.1 What is an N-Gram?
An N-gram is a **contiguous sequence of N items** from a given sequence of text (or other tokens), where **N** is the number of items in the sequence.

**Example:** `"The quick brown fox"`
* **Unigrams (1-gram):** `["The", "quick", "brown", "fox"]`
* **Bigrams (2-gram):** `["The quick", "quick brown", "brown fox"]`
* **Trigrams (3-gram):** `["The quick brown", "quick brown fox"]`
* **4-grams:** `["The quick brown fox"]`

**The "Sliding Window" Concept:**
A window of size N slides one step at a time. Each position equals one N-gram. N-grams are like taking a magnifying glass and sliding it across text, capturing every window of N words you see.

```text
[The][quick][brown][fox]
 ↑─────↑              = "The quick"     (bigram 1)
      ↑─────↑         = "quick brown"   (bigram 2)
            ↑─────↑   = "brown fox"     (bigram 3)
```

### 1.2 Types of N-Grams

#### By N Value
* **N=1 (Unigram):** "I love pizza" → `["I", "love", "pizza"]`
* **N=2 (Bigram):** "I love pizza" → `["I love", "love pizza"]`
* **N=3 (Trigram):** "I love hot pizza" → `["I love hot", "love hot pizza"]`
* **N=4 (Quadgram):** "I really love hot pizza" → `["I really love hot", "really love hot pizza"]`
* **N=5 (Five-gram):** "I really love very hot pizza" → `["I really love very hot", "really love very hot pizza"]`
* **N=∞:** As N increases, you get more context but less data to learn from.

#### By Token Type
* **Word N-Grams (Most common):** Sequences of words.
* **Character N-Grams:** Sequences of characters (e.g., "hello" → bigrams: `["he", "el", "ll", "lo"]`). Useful because it is language-agnostic, handles misspellings, works for code/DNA, and captures morphology.
* **Sentence N-Grams:** Sequences of sentences (used in discourse analysis).
* **Byte N-Grams:** Raw bytes (useful for binary data, language detection).
* **Subword N-Grams (Modern NLP):** Tokenization between character and word level (e.g., BPE). Used by GPT, BERT, and most modern LLMs.

### 1.3 How to Compute N-Grams
**Input:** `"the cat sat on the mat"`

1. **Tokenize:** `["the", "cat", "sat", "on", "the", "mat"]` (Length: 6 tokens)
2. **Generate N-Grams:**
   ```python
   for i in range(0, len(tokens) - N + 1):
       ngram = tokens[i : i+N]
   ```
**Formula:** `Number of N-grams = len(tokens) - N + 1`

### 1.4 N-Gram Language Models
A language model assigns a probability to a sequence of words to estimate how "natural" a sentence is.
* **The N-Gram Assumption (Markov Assumption):** Probability of the next word depends ONLY on the last N-1 words.
* **Smoothing (Handling Unseen N-grams):** Avoids zero probabilities.

    * **PROBLEM:** If an N-gram never appeared in training, its probability is 0, which makes the entire sentence probability 0.

    * **Smoothing Techniques:**

    * **Add-One (Laplace):** Add 1 to every count.
    
       **Problem: Too much probability mass is given to unseen N-grams.**
    * **Add-K:** Add k (< 1) instead of 1. k is a hyperparameter.
    * **Good-Turing:** Use count of n-grams that appeared ONCE.
    * **Kneser-Ney (Best in practice):** Uses continuation probability.
    * **Interpolation:** Mix unigram, bigram, and trigram probabilities.

**Perplexity:** Measures how "surprised" the model is by test text. Lower = better.

```python
import math

def perplexity(model, test_sentences):
    total_log_prob = 0
    total_tokens = 0
    
    for sentence in test_sentences:
        tokens = preprocess(sentence)
        total_log_prob += model.log_probability(sentence)
        total_tokens += len(tokens)
        
    avg_log_prob = total_log_prob / total_tokens
    return math.exp(-avg_log_prob)
```
 ### **N-Grams in search and NLP Applications:** 

* **text similarity**
* **spell checking and fuzzy search**
* **autocomplete / Typeahead**
* **Search engine query expansion**

### **Word2Vec and N-Grams context**
* Word2Vec uses a **sliding window** to create context for each word.

**SKip-Gram Model:** Predicts context words given a target word.

### 1.5 Edge Cases & Gotchas
> **⚠️ Edge Case 1: Data Sparsity Problem**
> As N grows, there's more context but less data per context. 
> **Solutions:** Smoothing (Kneser-Ney), Backoff models, or Modern Neural LMs.
> 
> **⚠️ Edge Case 2: N-gram Explosion**
> For vocabulary $V$ and size $N$, possible N-grams = $V^N$.
> **Solutions:** Minimum count thresholds, Bloom filters, Hashing tricks, Pruning.
>
> **⚠️ Edge Case 3: Case and Punctuation Handling**
> "The" vs "the" splits the model entries. 
> **Solution:** Normalization pipeline (lowercase, separate punctuation).
>
> **⚠️ Edge Case 4: Character N-gram Boundary**
> Very short words fail to generate larger character N-grams.
> **Solution:** Pad with special characters (e.g., `<a\>`).

---

## 2. Recurrent Neural Networks (RNN)

### 2.1 What is an RNN?
An RNN is a neural network designed to work with **SEQUENTIAL DATA** by maintaining a **HIDDEN STATE** (memory) that carries information from previous time steps to the current one. Unlike regular NNs, the SAME network is applied at EACH TIME STEP with SHARED WEIGHTS.

### 2.2 RNN Architecture

**Unrolled View (across time steps):**
```text
         x_1         x_2         x_3         x_4
          │           │           │           │
          ▼           ▼           ▼           ▼
      ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐
      │       │   │       │   │       │   │       │
h_0 ─►│  RNN  ├──►│  RNN  ├──►│  RNN  ├──►│  RNN  │──► h_4
      │       │   │       │   │       │   │       │
      └───┬───┘   └───┬───┘   └───┬───┘   └───┬───┘
          │           │           │           │
          ▼           ▼           ▼           ▼
         y_1         y_2         y_3         y_4
```

**The Math Behind RNN:**
1. **Hidden State Update:** `h_t = tanh(W_xh * x_t + W_hh * h_{t-1} + b_h)`
2. **Output:** `y_t = W_hy * h_t + b_y`

### 2.3 Vanishing & Exploding Gradients
When backpropagating through T time steps, gradients involve multiplying $W_{hh}^{T-1}$.
* **Exploding Gradients:** Solved with **Gradient Clipping**.
* **Vanishing Gradients:** RNN forgets long-ago context. Solved with **LSTM / GRU**.

### 2.4 LSTM — Long Short-Term Memory
Introduces a **CELL STATE (c_t)** as a "highway" for information flow, controlled by three gates.

```text
         ┌────────────────────────────────────────────────┐
         │                  LSTM Cell                     │
         │                                                │
x_t ──── ┼─────────────────────────────────────────────   │
h_{t-1}─ ┼──┬────────┬──────────┬─────────────────────    │
         │  │        │          │                         │
         │  ▼        ▼          ▼          ▼              │
         │  f_t      i_t       g_t        o_t             │
         │ forget   input   candidate    output           │
         │  gate    gate      cell        gate            │
         │                                                │
c_{t-1}──┼─► × f_t → + ← × (i_t × g_t) → c_t ──► tanh     │
         │                                    ↓           │
         │                             × o_t → h_t        │
         └────────────────────────────────────────────────┘
```
**LSTM Equations:**
1. **Forget Gate:** `f_t = σ(W_f · [h_{t-1}, x_t] + b_f)`
2. **Input Gate:** `i_t = σ(W_i · [h_{t-1}, x_t] + b_i)`
3. **Candidate:** `g_t = tanh(W_g · [h_{t-1}, x_t] + b_g)`
4. **Cell State:** `c_t = f_t ⊙ c_{t-1} + i_t ⊙ g_t`
5. **Output Gate:** `o_t = σ(W_o · [h_{t-1}, x_t] + b_o)`
6. **Hidden State:** `h_t = o_t ⊙ tanh(c_t)`

### 2.5 Sequence-to-Sequence (Seq2Seq)
Powers machine translation and chatbots. Uses an **Encoder** to read input into a context vector and a **Decoder** to generate output.

### 2.6 Edge Cases & Gotchas
> **⚠️ Edge Case 1: Vanishing Gradients Even in LSTM**
> Forget gate saturating near 0 or 1.
> **Solution:** Initialize forget gate bias to 1.0, and apply Layer Normalization.
>
> **⚠️ Edge Case 2: Exploding Gradients**
> Always use gradient clipping.
> ```python
> torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
> ```
>
> **⚠️ Edge Case 3: Padding in Batches**
> Use `pack_padded_sequence` so the LSTM skips padding tokens.
>
> **⚠️ Edge Case 4: Teacher Forcing Instability**
> Exposure bias causes error spiraling during inference. 
> **Solution:** Scheduled sampling (gradually decrease teacher forcing ratio).

---

## 3. Transformers

### 3.1 What is a Transformer?
A deep learning architecture that uses **SELF-ATTENTION** to process sequences in **PARALLEL** without recurrence or convolution (Introduced by Google, 2017).

**Why Transformers Beat RNNs:**
1. **Full Parallelism:** 10-100x faster training.
2. **Direct Connections:** O(1) dependency distance avoids gradient bottlenecks.
3. **Full Context:** No information compression loss.

```text
┌──────────────────────────────────────────────────────────────────┐
│                    TRANSFORMER (Seq2Seq)                         │
│                                                                  │
│  INPUT: "The cat sat"    OUTPUT: "Le chat s'est assis"           │
│                                                                  │
│ ┌────────────────────┐         ┌─────────────────────────────┐   │
│ │      ENCODER       │         │         DECODER             │   │
│ │                    │         │                             │   │
│ │  Input Embedding   │         │  Output Embedding           │   │
│ │  + Pos Encoding    │         │  + Pos Encoding             │   │
│ │         │          │         │         │                   │   │
│ │  ┌──────▼───────┐  │         │  ┌──────▼────────────┐      │   │
│ │  │  Self-Attn   │  │         │  │  Masked Self-Attn │      │   │
│ │  │  (Multi-Head)│  │         │  └──────┬────────────┘      │   │
│ │  └──────┬───────┘  │         │         │                   │   │
│ │  ┌──────▼───────┐  │         │  ┌──────▼────────────┐      │   │
│ │  │  Add & Norm  │  │         │  │  Cross-Attention  │◄───┼─┐ │   │
│ │  └──────┬───────┘  │         │  │ (attends encoder) │    │ │ │   │
│ │  ┌──────▼───────┐  │ encoder │  └──────┬────────────┘    │ │ │   │
│ │  │ Feed Forward │  │ outputs │  ┌──────▼────────────┐    │ │ │   │
│ │  │    Network   │ ─────────┼─►  │ Feed Forward Net  │    │ │ │   │
│ │  └──────┬───────┘  │         │  └──────┬────────────┘    │ │ │   │
│ │  ┌──────▼───────┐  │         │  ┌──────▼────────────┐    │ │ │   │
│ │  │  Add & Norm  │  │         │  │ Linear + Softmax  │    │ │ │   │
│ │  └──────────────┘  │         │  └───────────────────┘    │ │ │   │
│ │    × N layers      │         │       × N layers            │ │ │   │
│ └────────────────────┘         └─────────────────────────────┘ │ │   │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 Self-Attention
Attention decides **HOW MUCH** to focus on each other word.
* **Query (Q):** "What am I looking for?"
* **Key (K):** "What do I contain?"
* **Value (V):** "What do I give to others?"

**Formula:** `Attention(Q, K, V) = softmax(QK^T / √d_k) × V`
*(Dividing by `√d_k` normalizes the scale to prevent vanishing gradients).*

### 3.3 Modern Variants
* **BERT:** Bidirectional Encoder (Masked Language Modeling).
* **GPT:** Autoregressive Decoder (Predict next token).
* **T5:** Text-to-Text Framework.
* **LLaMA:** Modern efficient decoder utilizing RoPE, SwiGLU, and Grouped Query Attention (GQA).

### 3.4 Edge Cases & Gotchas
> **⚠️ Edge Case 1: Attention Score Overflow**
> Large $d_k$ causes softmax saturation. Handled via scaling by `1/√d_k`.
>
> **⚠️ Edge Case 2: Positional Encoding for Long Sequences**
> Training length mismatch with inference. **Solution:** Use **RoPE** (Rotary Position Embeddings) or ALiBi.
>
> **⚠️ Edge Case 3: KV Cache Memory Explosion**
> KV cache grows linearly. **Solutions:** Grouped Query Attention (GQA), Sliding Window Attention, PagedAttention (vLLM).

---

## 4. LangChain

### 4.1 What is LangChain?
An open-source framework for building applications powered by Large Language Models (LLMs). It provides standardized interfaces, memory management, and agent frameworks.

```text
┌─────────────────────────────────────────────────────────┐
│                   LangChain Ecosystem                   │
│                                                         │
│  ┌───────────────┐  ┌───────────────┐  ┌─────────────┐  │
│  │  langchain    │  │langchain-core │  │ langchain-  │  │
│  │  (main pkg)   │  │(base abstracts│  │ community   │  │
│  │               │  │ + LCEL)       │  │(integrations│  │
│  └───────────────┘  └───────────────┘  └─────────────┘  │
│                                                         │
│  ┌───────────────┐  ┌───────────────┐  ┌─────────────┐  │
│  │  LangSmith    │  │  LangServe    │  │  LangGraph  │  │
│  │  (observabil- │  │  (deploy as   │  │  (stateful  │  │
│  │   ity/debug)  │  │   REST API)   │  │   agents)   │  │
│  └───────────────┘  └───────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Agents (ReAct Pattern)
Agents allow LLMs to take actions.
`Thought → Action → Observation → Thought → Final Answer`

### 4.3 Edge Cases & Gotchas
> **⚠️ Edge Case 1: Context Window Limits**
> Stuffing too many documents exceeds context limits. 
> **Solutions:** Limit retrieval `k`, use MapReduce, or token-aware retrieval.
>
> **⚠️ Edge Case 2: Hallucinations in RAG**
> Model answers off-topic.
> **Solutions:** Explicit grounding instructions, confidence scoring, citation checking.
>
> **⚠️ Edge Case 3: Embedding Dimensionality Mismatch**
> Using a 1536-dim embedding to query a 384-dim DB. **Always validate and document embedding models.**

---

## 5. Large Language Models (LLMs)

### 5.1 Training Pipeline
1. **Pretraining:** Self-supervised learning on massive web data (next-token prediction).
2. **Supervised Fine-Tuning (SFT):** Fine-tuning on high-quality prompt-response pairs.
3. **RLHF / DPO:** Aligning the model to human preferences using Reward Models.

### 5.2 Tokenization
LLMs operate on tokens, not raw text. E.g., BPE (Byte Pair Encoding).
* 1 token ≈ 4 characters or 0.75 words (English).

### 5.3 Inference & Sampling
* **Temperature:** Controls randomness (0 = greedy/deterministic, >1 = creative).
* **Top-K / Top-P (Nucleus):** Limits the token sampling pool.

### 5.4 Safety and Alignment
Safety approaches include Constitutional AI, RLHF, Red Teaming, and Output Filters to prevent jailbreaks and harmful content generation.

---

## 6. Retrieval-Augmented Generation (RAG)

### 6.1 What is RAG?
A technique that enhances LLM responses by **retrieving** relevant information from a knowledge base and **augmenting** the prompt to **generate** a grounded response.

```text
┌─────────────────────────────────────────────────────────────────────┐
│                     RAG SYSTEM ARCHITECTURE                         │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    INDEXING PIPELINE (Offline)                │  │
│  │                                                               │  │
│  │  Documents → Load → Split → Embed → Store in Vector DB        │  │
│  │   (PDFs,     (Doc    (Chunks) (Dense   (Chroma, Pinecone,     │  │
│  │   URLs)      Loader)          Vectors)  FAISS, Weaviate)      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    QUERY PIPELINE (Online)                    │  │
│  │                                                               │  │
│  │  User Query                                                   │  │
│  │      │                                                        │  │
│  │      ▼                                                        │  │
│  │  Retrieval ──────────────────────── Vector DB                 │  │
│  │  (semantic search, keyword,         (returns top-k            │  │
│  │   hybrid)                            similar chunks)          │  │
│  │      │                                                        │  │
│  │      ▼                                                        │  │
│  │  Augmented Prompt = System + Context + Query                  │  │
│  │      │                                                        │  │
│  │      ▼                                                        │  │
│  │  LLM Generation ────────────────── Final Answer               │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 Advanced Retrieval Techniques
* **Hybrid Retrieval:** BM25 (keyword) + Semantic Search.
* **HyDE (Hypothetical Document Embeddings):** Embed a hypothetical answer to improve semantic matching.
* **Cross-Encoder Reranking:** Fast bi-encoder finds top 20, accurate cross-encoder reranks top 4.
* **Parent Document Retrieval:** Index small chunks for matching but return large chunks for context.

---

## 7. Attention Mechanisms

### 7.1 The Mechanism
Attention allows a network to selectively focus on relevant parts of the input sequence. 
* **Bahdanau (Additive):** Original attention mechanism (2014).
* **Luong (Multiplicative):** Dot-product based (2015).
* **Scaled Dot-Product (Transformers):** Parallelizable standard.

### 7.2 Attention Complexity
* **Time & Memory:** $O(n^2 \times d)$
* Very long sequences quickly consume GPU memory (8192 seq length with 32 heads = ~8.6GB per layer).
* **Flash Attention:** Fuses softmax and matrix multiplication using fast SRAM. Reduces memory to $O(n)$ and speeds up processing 2-4x.

---

## 8. Reinforcement Learning

### 8.1 The RL Framework
An agent learns to make decisions by interacting with an environment to maximize cumulative reward.

```text
┌─────────────────────────────────────────────────────────────┐
│                    RL INTERACTION LOOP                      │
│                                                             │
│         State s_t                                           │
│    ┌────────────────────────────────────────┐               │
│    │                                        │               │
│    ▼                                        │               │
│ ┌──────┐  Action a_t   ┌─────────────────┐  │               │
│ │AGENT │──────────────►│  ENVIRONMENT    │  │               │
│ │  π   │               │                 │  │               │
│ │      │◄──────────────│  Transition:    │  │               │
│ └──────┘  Reward r_t   │  s_t → s_{t+1}  │  │               │
│           State s_{t+1}└─────────────────┘  │               │
│    │                        │               │               │
│    └────────────────────────┘               │               │
└─────────────────────────────────────────────┘
```

### 8.2 Algorithms
* **Q-Learning / DQN:** Off-policy, learns value functions. Uses target networks and replay buffers for stability.
* **PPO (Proximal Policy Optimization):** On-policy actor-critic method. Clips policy updates to prevent catastrophic forgetting. (Used heavily in ChatGPT).
* **DPO (Direct Preference Optimization):** Modern alternative to RLHF that optimizes LLMs without a separate reward model.

---

## 9. Fine-Tuning

### 9.1 Overview
Taking a pretrained model and continuing training on a specific dataset. 

### 9.2 Parameter-Efficient Fine-Tuning (PEFT)
* **LoRA (Low-Rank Adaptation):** Freezes base weights and trains small rank-decomposition matrices ($\Delta W = B \times A$). Reduces trainable parameters by 100-1000x.
* **QLoRA:** Quantizes base model to 4-bit, enabling fine-tuning of large models on a single GPU.

### 9.3 Fine-Tuning Anti-Patterns
* **Overfitting:** Training loss drops, validation loss spikes.
* **Catastrophic Forgetting:** Over-specialization destroys pretraining general knowledge.
* **Data Contamination:** Training data leaking into evaluation sets.

---

## 10. Chunking Strategies

### 10.1 Why Chunk?
LLMs have finite contexts; retrieving 100 pages is impossible. We chunk to retrieve specific, targeted text segments.

### 10.2 Chunking Strategies
* **Fixed-Size:** Splits at $N$ characters with overlap. Simple but breaks sentences.
* **Recursive Character:** Splits hierarchically (`\n\n`, `\n`, `. `, ` `). Best default.
* **Semantic:** Splits where cosine similarity between sentences drops significantly.
* **Parent-Child:** Small child chunks for indexing, large parent chunks returned for context.

---

## 11. Clustering

### 11.1 Unsupervised Grouping
Grouping similar data points together without pre-defined labels. 
* **K-Means:** Alternating assignment and update steps. Assumes spherical clusters. Minimize WCSS.
* **DBSCAN:** Density-based. Handles arbitrary shapes and identifies noise.
* **Gaussian Mixture Models (GMM):** Soft clustering with probability assignments.
* **Topic Modeling (LDA):** Probabilistic distribution of words per topic and topics per document.

---

## 12. Hallucinations

### 12.1 The Concept
When an LLM generates content that is factually incorrect, fabricated, or ungrounded, presented with authoritative confidence.

**Types of Hallucinations:**
* **Intrinsic:** Direct contradiction of the provided source.
* **Extrinsic:** Unverifiable additions not found in the source.

### 12.2 Prevention Techniques
1. **RAG (Grounding):** Provide reliable context.
2. **Prompt Engineering:** Demand source citations and permit "I don't know".
3. **Verification Pipelines:** Score outputs against context.
4. **RAGAS Metrics:** Measure *Faithfulness* and *Answer Relevancy*.

---

## 13. GPU Optimization

### 13.1 Maximizing Efficiency
GPUs process data in parallel but often sit idle waiting for memory or CPU. 

### 13.2 Optimization Techniques
* **Mixed Precision (FP16/BF16):** Doubles speed, halves memory footprint. Requires matrix dimensions to align (multiples of 8 or 64).
* **Gradient Checkpointing:** Trades compute for memory by recalculating forward activations during the backward pass (reduces memory from $O(N)$ to $O(\sqrt{N})$).
* **DataLoader Prefetching:** Set `num_workers=4` and `pin_memory=True`.
* **DeepSpeed ZeRO:** Partitions optimizer states, gradients, and model parameters across GPUs to save memory.
* **Quantization (INT8/INT4):** Speeds up inference by reducing memory bandwidth bottlenecks.

---

## 14. Tensors

### 14.1 Fundamentals
Tensors are multi-dimensional arrays (0D Scalar, 1D Vector, 2D Matrix, N-D Tensor). They power all hardware-accelerated deep learning via contiguous memory allocation.

### 14.2 Autograd & Memory
* **Views vs Copies:** `view()` alters strides without copying data; `clone()` duplicates memory. Modifying views modifies the original memory.
* **Strides:** Determine how to jump through a flat 1D memory array to access N-D elements. `.contiguous()` rearranges memory sequentially for better cache behavior.

---

## 15. Data Cleansing

### 15.1 The Process
Detecting and correcting corrupt, inaccurate, or incomplete data. 

```text
┌─────────────────────────────────────────────────────────────┐
│                   DATA CLEANSING PIPELINE                   │
│                                                             │
│  RAW DATA                                                   │
│      │                                                      │
│      ▼                                                      │
│  1. PROFILE & AUDIT                                         │
│     Understand what you have                                │
│     Count nulls, check types, distributions                 │
│      │                                                      │
│      ▼                                                      │
│  2. HANDLE MISSING VALUES                                   │
│     Drop, impute, flag                                      │
│      │                                                      │
│      ▼                                                      │
│  3. FIX DATA TYPES                                          │
│     Strings → numbers, fix dates                            │
│      │                                                      │
│      ▼                                                      │
│  4. STANDARDIZE FORMATS                                     │
│     Consistent case, units, categories                      │
│      │                                                      │
│      ▼                                                      │
│  5. REMOVE DUPLICATES                                       │
│     Exact and fuzzy duplicates                              │
│      │                                                      │
│      ▼                                                      │
│  6. HANDLE OUTLIERS                                         │
│     Detect, investigate, treat                              │
│      │                                                      │
│      ▼                                                      │
│  7. VALIDATE                                                │
│     Rule-based validation, cross-field checks               │
│      │                                                      │
│      ▼                                                      │
│  CLEAN DATA ✅                                               │
└─────────────────────────────────────────────────────────────┘
```

### 15.2 Handling Missing Values & Outliers
* **MCAR / MAR / MNAR:** Missing Completely At Random, Missing At Random, Missing Not At Random.
* **Outliers:** Standard Z-Score, IQR, or Isolation Forests. Treat via dropping, clipping (winsorization), or transformations. 

---

## 16. Scikit-Learn

### 16.1 Unified API
Consistent `.fit()`, `.transform()`, and `.predict()` methods across models.

### 16.2 Pipelines
Chaining transformations and models using `Pipeline` prevents data leakage (especially during cross-validation).
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
pipeline.fit(X_train, y_train)
```

### 16.3 Evaluation & Tuning
* **Metrics:** Accuracy (balanced data), Precision/Recall/F1 (imbalanced classification), MSE/MAE (regression).
* **Tuning:** `GridSearchCV` (exhaustive) vs `RandomizedSearchCV` (faster, often better for large hyperparameter spaces).
* **Cross-Validation:** K-Fold (standard) vs Stratified K-Fold (classification).
