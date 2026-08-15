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

* **SSkip-Gram Model:** Predicts context words given a target word.
* **CBOW( Continuous Bag of Words ) Model:** Predicts a target word given context words. Reverse of Skip-Gram.

### **BERT and Subword N-Grams**
* **BERT** (Bidirectional Encoder Representations from Transformers) is a transformer-based model that uses subword tokenization to handle rare words and out-of-vocabulary tokens.
* BERT uses **WordPiece Tokenization** (subword N-grams) to handle rare words and out-of-vocabulary tokens. It splits words into subword units, allowing it to represent unseen words as combinations of known subwords.
* **Example:** "unhappiness" → `["un", "##happiness"]` (where `##` indicates a subword continuation).
* **Advantage:** BERT can understand and generate embeddings for rare or unseen words by leveraging the embeddings of their subword components.

* **FastText** (by Facebook) also uses subword N-grams to create word embeddings. It represents each word as a bag of character N-grams, allowing it to generate embeddings for words not seen during training.
* **Example:** "where" → `["whe", "her", "ere"]` (character trigrams). The embedding for "where" is the sum of the embeddings of its character trigrams.
* **Advantage:** FastText can handle misspellings and morphological variations better than traditional word embeddings.

* **BLEU Score** (Bilingual Evaluation Understudy) is a metric for evaluating the quality of machine-translated text. It compares the N-grams of the candidate translation to those of reference translations, calculating precision for N-grams of different lengths (typically up to 4-grams). BLEU uses a modified precision score that accounts for multiple reference translations and applies a brevity penalty to discourage overly short translations.
* **Example:** If the candidate translation is "the cat sat" and the reference translation is "the cat is sitting", BLEU would compare the unigrams, bigrams, trigrams, and 4-grams of both sentences to compute a score.
* **Advantage:** BLEU provides a quantitative measure of translation quality, allowing for automated evaluation of machine translation systems.

### **N-Grams in Industry**
* **Search Engines:** Google, Bing, and Elasticsearch use N-grams for query expansion, autocomplete, and spell correction.
* **Text Analytics:** N-grams are used in sentiment analysis, topic modeling, and text classification to capture context and relationships between words.
* **Chatbots and Virtual Assistants:** N-grams help in understanding user queries and generating relevant responses by analyzing the context of the conversation.


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

### **Tricky Interview Questions**
**Q1. What is the trade-off between using unigrams vs trigrams in a language model?**

**A1.** Unigrams capture individual word frequencies but lose context, leading to ambiguity. Trigrams capture more context (two preceding words) but suffer from data sparsity and require more memory. The trade-off is between **contextual understanding** (trigrams) and **data availability** (unigrams).

**Q2. How does Google's search autocomplete work at a high level using N-grams?**

**A2.** Google uses N-grams to predict the next word(s) in a query based on historical search data. It analyzes the frequency of N-grams in past queries and suggests completions that are statistically likely given the user's input. The system may also incorporate user location, trending searches, and personalization to refine suggestions.

**Q3. Why do character N-grams handle out-of-vocabulary words better than word N-grams?**

**A3.** Character N-grams break words into smaller units, allowing the model to recognize patterns in prefixes, suffixes, and roots. This enables it to generate embeddings for unseen words based on their subword components, making it more robust to misspellings and morphological variations compared to word N-grams, which treat each word as a distinct token.

**Q4. How would you use N-grams to detect plagiarism?**

**A4.** To detect plagiarism, you can generate N-grams (typically bigrams or trigrams) from both the source and the target documents. By comparing the sets of N-grams, you can identify overlapping sequences that indicate potential copying. A high percentage of shared N-grams suggests that the target document may have been plagiarized from the source.

**Q5. What is the difference between BLEU score and perplexity, and when would you use each?**

**A5.** BLEU score evaluates the quality of machine-translated text by comparing N-grams of the candidate translation to reference translations, focusing on precision and brevity. Perplexity measures how well a language model predicts a sequence of words, indicating how "surprised" the model is by the test data. Use BLEU for evaluating translation quality and perplexity for assessing language model performance.

**Q6. How would you build a real-time autocomplete for a search box that handles 10,000 requests per second?**

**A6.** To build a real-time autocomplete system handling 10,000 requests per second, you can:
1. **Precompute N-grams:** Generate and store N-grams from historical search queries in a fast-access data structure (e.g., Trie or HashMap).
2. **Use Caching:** Implement caching for popular queries to reduce computation.
3. **Asynchronous Processing:** Use asynchronous request handling to manage high throughput.
4. **Load Balancing:** Distribute requests across multiple servers to handle traffic spikes.

### **Mental Model Summary**

* **RAM \= Sliding window of N items over sequence**


* **WINDOW SIZES:**  
  N=1 (Unigram)  → individual tokens, no context

  N=2 (Bigram)   → pairs, local context 

  N=3 (Trigram)  → triples, better context  

  N=4+           → more context, more sparsity

* **TOKEN TYPES:**  
  Word n-grams    → standard NLP, search  
  
  Char n-grams    → fuzzy search, morphology, OOV
  
  Subword n-grams → modern tokenization (BPE, WordPiece)

* **APPLICATIONS:**  
  Language model   → P(next word | context) 
  
  Text similarity  → Jaccard / cosine of n-gram sets

  Spell check      → char n-gram overlap
  
  Autocomplete     → n-gram frequency predictioN
  
  Search           → TF-IDF with n-gram features 
  
  Translation eval → BLEU score

  Plagiarism       → fingerprint matching

* **CORE TRADE-OFFS:**  
  Large N: more context, better model, more sparsity 
  
  Small N: less context, weaker model, less sparsity

* **SOLVE SPARSITY WITH:**  

    Smoothing (Laplace, Kneser-Ney)

    Backoff models 

    Interpolation


*  **GOLDEN RULES:**  
   ✅ Always normalize text before building n-grams

   ✅ Add sentence boundary markers (\<START\>, \<END\>)

   ✅ Use smoothing — zero probability is never right 

   ✅ Character n-grams for typo-tolerance and OOV  

   ✅ Minimum frequency threshold to reduce noise  

    ✅ For search: character trigrams enable substring matching 
   
   ❌ Don't cross sentence boundaries with n-grams  
   
   ❌ Don't forget sparsity grows exponentially with N  
  
   ❌ Don't use KEYS  in Redis n-gram index
---

## 2. Recurrent Neural Networks (RNN)

### 2.1 What is an RNN?
* An RNN is a neural network designed to work with **SEQUENTIAL DATA** by maintaining a **HIDDEN STATE** (memory) that carries information from previous time steps to the current one. Unlike regular NNs, the SAME network is applied at EACH TIME STEP with SHARED WEIGHTS.

  * Think of it as a "rolling window" that processes one token at a time, updating its memory as it goes.

* Why Sequential data needs special treatment:
  * **Temporal Dependencies:** The meaning of a word often depends on previous words.
  * **Variable Length Sequences:** Sentences can be of different lengths.
  * **Context Preservation:** RNNs can, in theory, remember long-term dependencies.
  * **Example:** "The cat sat on the mat. It was very comfortable." The pronoun "It" refers to "the mat," which is context from earlier in the sequence.



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
**Key Insights:**
* **Weight Sharing:** The same RNN cell (with the same weights) is applied at each time step.
* **Hidden State:** The hidden state `h_t` captures information from all previous time steps.
* **Output:** The output `y_t` is generated at each time step based on the hidden state.

 **The Math Behind RNN:**
 1. **Hidden State Update:** `h_t = tanh(W_xh * x_t + W_hh * h_{t-1} + b_h)`
 2. **Output:** `y_t = W_hy * h_t + b_y`


**RNN types by Input/Output:**

| Input | Output | Description |
|-------|--------|-------------|
| Sequence | Sequence | Many-to-Many (e.g., translation) |
| Sequence | Single | Many-to-One (e.g., sentiment analysis) |
| Single | Sequence | One-to-Many (e.g., image captioning) |
| Single | Single | One-to-One (e.g., classification) |

### 2.3 Vanishing & Exploding Gradients
When backpropagating through T time steps, gradients involve multiplying $W_{hh}^{T-1}$.
* **Exploding Gradients:** Solved with **Gradient Clipping**.
* **Vanishing Gradients:** RNN forgets long-ago context. Solved with **LSTM / GRU**.
* Example: For a weight matrix $W_{hh}$ with eigenvalues < 1, repeated multiplication causes gradients to shrink exponentially. 

  Weight matrix spectral radius = 0.9
Gradient at t = 1 : 0.9^99 ≈ 0.00003 (vanished)

  Weight matrix spectral radius \= 1.1
Gradient at t=1: 1.1^99 ≈ 13,780 (exploded)

* Consequences
  * **Vanishing:** Model fails to learn long-term dependencies.
  * **Exploding:** Model becomes unstable and diverges during training.

* Solutions:
  * **Gradient Clipping:** Limit the gradient norm to a threshold.
  * **LSTM / GRU:** Use gating mechanisms to preserve long-term dependencies.
  

### 2.4 LSTM — Long Short-Term Memory
Introduces a **CELL STATE (c_t)** as a "highway" for information flow, controlled by three gates.
Cell state is a vector that runs through the entire sequence, allowing information to flow unchanged unless explicitly modified by the gates.
Gates control information : forget, input, and output.


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

   "What to erase from cell state?" (0 = forget, 1 = keep)

2. **Input Gate:** `i_t = σ(W_i · [h_{t-1}, x_t] + b_i)`
    
    "What to add to cell state?" (0 = ignore, 1 = add)

3. **Candidate:** `g_t = tanh(W_g · [h_{t-1}, x_t] + b_g)`

   "Potential new information for cell state"

4. **Cell State:** `c_t = f_t ⊙ c_{t-1} + i_t ⊙ g_t`

    "Update the memory"

5. **Output Gate:** `o_t = σ(W_o · [h_{t-1}, x_t] + b_o)`

   "Controlled output of the cell state"

6. **Hidden State:** `h_t = o_t ⊙ tanh(c_t)`

   " Final output of the LSTM cell"

#### **GRU — Gated Recurrent Unit**

Similar to LSTM but with fewer parameters and simpler architecture. Combines the forget and input gates into a single update gate.

Fewer parameters = faster training, but may not capture long-term dependencies as well as LSTM.

Reset Gate: `r_t = σ(W_r · [h_{t-1}, x_t] + b_r)`

" What to forget from the previous hidden state?"

Update Gate: `z_t = σ(W_z · [h_{t-1}, x_t] + b_z)`

" How much of the previous hidden state to keep?"

### **Bidirectional RNNs**

Bidirectional RNNs process the sequence in both forward and backward directions, allowing the model to capture context from both past and future tokens.

```text
         ┌───────────────┐
         │ Forward RNN   │
         └───────────────┘
                │
                ▼          
         ┌───────────────┐
         │ Backward RNN  │
         └───────────────┘
                │
                ▼
         ┌───────────────┐
         │ Concatenate   │
         └───────────────┘
                │
                ▼
             Output

```
* Example: For the sentence "The cat sat," a bidirectional RNN can use information from both "The" and "sat" to better understand the context of "cat."

* Use cases :

  ✅ Text classification (can see full sentence)

  ✅ Named Entity Recognition (context both ways)

  ✅ Question answering

  ✅ Encoder in seq2seq models


  ❌ Language modeling (can't see future during generation)

  ❌ Real-time streaming (can't wait for futur

  ❌ Decoder in seq2seq (generates left-to-right)


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
