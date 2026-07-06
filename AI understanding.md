  AI understanding 

* Training of AI :   
    
  Raw Data → Tokenization → Model Training   
    
  RAG retrieval :   
    
  Documents → Embeddings → Vector Database  
                                 ↓  
  User Query → Embedding → Similarity Search  
                                 ↓  
  Relevant Context → LLM  
    
* We don't use SQL or keyword search for AI retrieval because it just looks for specific words in the data and does not search sementically .  
    
  For eg :    Imagine your knowledge base contains:  
    
  Document 1:  
  "Redis is an in-memory data structure store."  
    
  Document 2:  
  "Celery uses Redis as a message broker."  
    
  Document 3:
  "FastAPI supports asynchronous request handling."

  User asks:
  "How can I process tasks asynchronously?"

   Keyword search looks for:

   asynchronously  
   process  
   tasks

   It might return Document 3 only.
   But semantically 

   1. Celery  
   2. Message Broker  
   3. Background Jobs  
   4. Async Processing
   are related concepts.

   Embeddings capture **meaning**, not just words.

* An embedding converts text into a high \- dimensional vector   
  "dog" → \[0.23, \-0.91, 1.12, ...\]  
  "puppy" → \[0.27, \-0.89, 1.08, ...\]   
  Because the meanings are similar , distance(dog, puppy)  is very small . Whereas distance ( dog, airplane ) is      much larger .  
* Embeddings are not the fastest solutions but these are a tradeoff and have better relevance 


| Method | Speed | Semantic Understanding |
| ----- | ----- | ----- |
| SQL Index | Extremely Fast | Poor |
| Keyword Search | Very Fast | Low |
| BM25 Search | Fast | Medium |
| Vector Search | Moderate | High |
| Hybrid Search | Fast \+ Accurate | Very High |

      


For pure speed:
Hash Table —--\>  B tree Index —--\> Full Text Search —--\> Vector Search 

* We don't compare vector against every document as it would make the search very slow so we use the top K search     and just compare them instead of comparing the whole data .  
    
* Vector databases like pinecone , weviate , mivus use approximate nearest neighbour ( ANN ) algorithms.  
  Popular indexes :   
  HNSW ( Hierarchical Navigable Small World )  
   Query —--\> Top Layer —--\> Closer Layer —--\> Closest Layer —--\> Nearest  Neighbour      
    
* Hybrid search used by companies like search engines and enterprise AI systems.  
  Query  —--\>  Keyword search ( BM25) —--\>  vector search —--\>  merge results —--\>  rerank —--\>  final context   
  Benefits :   
* Fast   
* Semantic understanding   
* Exact Keyword matching 


* Modern RAG pipelines :  
  User query —--\>  query rewriting —--\>  hybrid search —--\>  top 50 documents —--\>  cross encoder reranker —--\>  top 5 documents —--\>  LLM  
    
* Conversion of word or chunk of data into embeddings    
   

  Step 1 \- computers don't understand words so they convert the words into numbers . Suppose we have Dog , Cat ,     Car .   
  The simplest coding will be   
  Dog \= 1  
  Cat \= 2  
  Car \= 3

  But this is terrible because     
  Distance ( Dog , Cat ) \= 1  
  Distance (Dog , Car ) \= 2   
  The numbers have no semantic meaning 

  Step 2 \- One encoding ( old approach )

  Given : \[ Dog , Car , Car , Bike \]

  Represent each word as   
  Dog \= \[ 1,0,0,0 \]  
  Cat \=  \[ 0,1,0,0 \]  
  Car \=  \[ 0,0,1,0 \]  
  Bike \= \[ 0,0,0,1 \]

  Problem : 

  Dog • Cat \= 0  
  Dog • Car \= 0 

  Every word is equally distant. The model learns : 

  Dog ≠ Cat  
  Dog ≠ Car 

  But not : 

  Dog ≈ Puppy  
  Car ≈ Vehicle 

  No semantic information 

  Step 3 : Word2Vec Revolution 

  The idea behind this is , instead of manually assigning vectors let a neural network learn them . 

  In sentence “ the dog chased the ball “ , for the word “ dog “ , the surrounding words are “ the “ , “ chased “ ,   “ball” 

  The network learns , “dog “ appears near : “ ball “, “ puppy “ , “ bark “ , “ animal “ 

  After billions of examples  
     
  dog \-\> \[0.12, 0.89, \-0.31, ...\]  
  cat \-\> \[0.15, 0.91, \-0.29, ...\]  
  car \-\> \[-0.77, 0.11, 0.45, ...\]  
  Dog and cat become close in vector space.

  The algorithms behind Word2Vec 

1. CBOW ( Continuous Bag of Words )  
   Predict the centre word 

   Input : the \_\_\_\_\_ chased the ball  
   Output  : dog 

2. Skip \- Gram ( it performs better for large corpora )  
   Predict surrounding words

   Input : dog   
   Output : chased , ball , the 

* King \- Man  \+  Woman \= Queen 

  Step 1 \- Imagine a tiny embeddings space   
  Real embeddings have 768 \- 3072 dimensions   
  Lets do it by only by 3 dimensions : 

  Dimension 1 \= Royalty  
  Dimension 2 \= male   
  Dimension 3 \= Adult 

  Suppose the model learned:

  Word          \-                 Vector  
  King           \-                 \[10,8,5\]  
  Queen        \-                \[10,2,5\]  
  Man            \-                \[ 0,8,5 \]  
  Woman      \-                 \[ 0,2,5 \]

  Notice :   
  Male \= 8  
  Female \= 2

  While royalty remains :   
  Royal \= 10   
  Common \= 0

  Step 2 \- computing king \- man 

  King \= \[ 10,8, 5 \]  
  Man \= \[ 0,8,5 \]

  Subtract   
  King \- Man \= \[ 10,8,5 \] \- \[ 0,8,5 \]  
                    \= \[ 10,0,0 \]  
  Only thing remains is \[ royalty \]  
  We have essentially removed ( male and adult ) and kept only the “ roya “ concept   
     
  Step 3 \- Add Woman   
  Woman \[ 0,2,5 \]  
  Now : \[ 10,0,0 \] \+ \[ 0,2,5 \] \= \[ 10,2,5 \]

  Step 4 \- now compare \[ 10,2,5 \] against every word in the vocabulary   
  Vocabulary   
  King        \=      \[ 10,8,5 \]  
  Queen     \=     \[ 10,2,5 \]  
  Man        \=      \[ 0,8,5 \]  
  Woman   \=      \[ 0,2,5 \]  
  Apple      \=      \[ 1,1,0 \]

  Therefore:  
  King \- Man \+ Woman \= Queen 

* So the embeddings consists of 1000s of dimension  so how do we compare them 

  Method 1 \- Euclidean Distance   
  Distance \= √((x1-x2)²+(y1-y2)²+...)

  Query \= \[ 1,2 \]  
  Doc A \= \[ 2,3 \]  
  Distance \= √((1-2)²+(2-3)²)  
                 \= √2

  Smaller distance \= more similar 

  Method 2 : cosine similarity ( most common )  
  Used by:  
       \-\> Open AI embeddings   
       \-\> Pinecone   
       \-\> Weaviate   
       \-\> Quadrant   
       \-\> Milvus   
  Instead of distance we compare the angle between vectors 

  Same direction        :        cosine similarity \= 1   
  90 degrees apart     :        cosine similarity \= 0   
  Opposite directions  :       cosine similarity \= \-1

  Cosine is better because euclidean distance is large but semantically same direction , while cosine similarity      says similarity \= 1 , which is correct .

* What happens during RAG retrieval 

  Suppose the query is : How does redis caching work ?  
  Embedding model converts it into : \[ 0.2 , 0.4 , 0.8 ……\]

  Database contains :   
  Doc 1 : redis stores data in memory   
              \[ 0.21 , 0.42 , 0.79 \]

  Doc 2 : docker containers package applications   
              \[ \-0.8 , 0.1 , 0.3 \]

  Vector DB computes :   
  cos( query , doc1 ) \= 0.97  
  cos( query , doc2 ) \= 0.21

  Doc1 win 

* What happens in database   
  Suppose we have 10 million vectors   
  Naively comparing against all 10 million  , too slow .  instead it makes a HNSW graph .

  Query  —\>   nearest region  —\>  closest region  —\>  top K result 

  Instead of checking all the vectors ( 3000000 vectors )  it checks  around 500-5000 vectors and still finds the     nearest neighbour . Here ‘ K ‘ is the top K retrieved chunks that are then retrieved and sent to LLM to generate    output and context is taken from those K chunks .  
  

  Attention is All you Need 

* Before transformers , NLP was dominated by RNN , LSTM , GRU . A sentence was processed by token by token .  
  For example      :     I love machine learning   
  RNN processes :     I —\> love —\> machine —-\> learning   
  The hidden state carries information forward 

* Problem 1: Long Range Dependencies   
  For eg : the animal didn’t cross the road because it was too tired   
  To understand “it”, the model must remember “ animal “ several words earlier . RNNs struggle because information    gradually vanishes . This is called   
  Vanishing Gradient Problem , even LSTMs improve but do not completely solve it .

  Problem 2 : No Parallelization   
  For a sentence of length n :   
  X1 —\> x2 —\> x3 —\> ……—\> xn   
  You must wait for x1 before x2 , then x2 before x3 , training becomes slow .

* So do we really need recurrence , actually no . Instead every word can directly look at every other word all at     once no recurrence no hidden state , this mechanism is called self attention .

* Intuition behind Attention .   
  for eg : The animal didn’t cross the road because it was tired .  
  When processing “ it ” the model should focus strongly on “ animal “ and weakly on irrelevant words . Attention     learns these weights automatically . 

* Mathematical Foundation   
  Every token embedding produces :   
  Query ( Q ) \- “ what am i looking for ? “  
  Key ( K ) \- “ What information do I contain ? “  
  Value ( V ) \- “ The actual information “

  For embedding vector “ x “   
  Three learned matrices exist : WQ , WK , WV   
  Compute :   
                 Q \= xWq  
                 K \= xWk  
                 V \= xWv  
  For example : x \= \[ 1,2,1,0 \]  
  Then  x∈R^4  
  Meaning the embedding dimension is : d model \= 4

  Case 1 : Same Dimension ( most intuitive )  
  Suppose :   WQ​∈R^4×4  
  Then :         Q \= ( 1x4 )(4 x 4\)  
  Result :       Q∈R^1×4  
  So :             Q=\[q1​,q2​,q3​,q4​\]  
  Similarly :     K=\[k1​,k2​,k3​,k4​\]   
                      V \= \[ v1,v2,v3,v4 \]  
  All have 4 dimension 

  Another example : 

  Embedding :  x∈R^4  
  Choose :       WQ​∈R4×3  
  Then :           Q=(1×4)(4×3)  
  Result :          Q∈R^3  
  Similarly :       K,V∈R^3  
  Now :             Q=\[1,0,2\]  
  is perfectly valid . The embedding dimension is 4 . The query dimension is 3 .

* The paper uses : d model \= 512  
  And h ( head )  \= 8  
  Each head gets :  dk​ \= dv ​= 512/8 ​= 64  
  Therefore :   
  Input embedding :  x ∈ R ^ 512  
  Query projection :  Wq ​∈ R ^ 512 × 64  
  Result :  Q ∈ R ^ 64  
  Similarily :  K , V ∈ R ^ 64  
  So in the original transformer :   
  Embedding size \= 512   
  Query size         \= 64   
  Key size             \= 64   
  Value size          \= 64  
  Notice : 512 \=/ 64 

  Real numerical example :   
  Eg : x \= \[ 1,2,1,0 \]  
  Choose :   
                         | 1  0  1  |  
               Wq \=     | 0  1  0  |  
                         | 1  1   0 |  
                         | 0   0  1 |

  Dimensions : ( 4 x 3 )

  

  Now compute : Q \= xWq  
                                                    | 1  0  1 |  
                                                    | 0  1  0 |  
                            \= \[ 1, 2 , 1 , 0 \]   | 1  1  0 |  
                                                    | 0  0  1 |

  First component :    1( 1 ) \+ 2( 0 ) \+ 1( 1 ) \+ 0( 0 ) \= 2  
  Second :                  1( 0 ) \+ 2( 1 ) \+ 1( 1 ) \+ 0( 0 ) \= 3  
  Third :                      1( 1 ) \+ 2( 0 ) \+ 1( 0 ) \+ 0( 1 ) \= 1  
  Therefore :               Q \= \[ 2, 3, 1 \]

  Notice :   
  Input dimension \= 4  
  Output dimension \= 3   
  Because Wq had 3 columns 

* General rule   
  For any transformer :   
                                    X ∈ R ^ D model   
                                 Wq ∈ R ^ D model x Dq  
                                 Wk ∈ R ^ D model x Dk  
                                 Wv ∈ R ^ D model x Dv  
  Then :   
                                 Q ∈ R ^ Dq  
                                 K ∈ R ^ Dk  
                                 V ∈ R ^ Dv

  The dimensions of Q,K,V are determined by the number of columns in the projection matrices , not by the embedding   dimension itself .

* Attention Score   
  Compute : score \= Qi Kj ^ T  
  This simply tells us if a dot product is large then it is very relevant and if a small score then it is not         relevant .  
  Eg :   
  Query : Q \= \[ 1,2 \]  
  Key :  K \= \[ 3,4 \]  
  Dot product : 1 x 3 \+ 2 x 4 \= 11  
  Score \= 11 

* We divide the raw dot product by √Dk , because the raw dot product becomes huge and the large number makes          softmax unstable .  
  Therefore :  QKt / √Dk   
  If    Dk \= 64   
  Then : √64 \= 8  
  Suppose Score :  80  
  Becomes 10 , which is more stable 

* Softmax   
  In softmax we convert scores into probabilities   
  Suppose scores : \[ 1, 2 ,3 \]

  Step 1   
  Exponentiate       
                         e  ^ 1 \= 2.718  
                         e  ^ 2 \= 7.389  
                         e  ^ 3 \= 20.085

  Step 2   
  Add   
                    2.718 \+ 7.389 \+ 20.085 \= 30.192

  Step 3   
  Normalize   
                         P1 \= 2.718 / 30.192   \= 0.09  
                         P2 \= 7.389 / 30.192   \= 0.24  
                         P3 \= 20.085 / 30.192 \= 0.67

  Final attention weights : \[ 0.09 , 0.24 , 0.67 \]

  Token focuses : 9% 24%  67% on the three tokens 

* Weighted sun of values   
  Step 1 : We have attention weights 

  After computing scores and applying softmax , suppose we got   
  Attention Weights \= \[ 0.009 , 0.24 , 0.67 \]

  V1 \= 0.09 ( weight )  
  V2 \= 0.24 ( weight )  
  V3 \= 0.67 ( weight )  
  The weights sum to 1 :    
                             0.09 \+ 0.24 \+ 0.67 \= 1

  Step 2: We have value vectors   
  Suppose :   
                   V1 \= \[ 1, 0 \]  
                   V2 \= \[ 0, 2 \]  
                   V3 \= \[ 3, 1 \]  
  Think of these as the information stored by each token .

  Step 3 : Multiply each value by its attention weight   
  Attention says : take each value vector and multiply it by its importance 

  First value : 0.09 x V1 \= 0.09 x \[ 1,0 \]  
  Multiply each component \= \[ 0.09 x 1, 0.09 x 0 \]  
                                           \= \[ 0.09, 0 \]

  Second Value : 0.24 x V2 \= 0.24 x \[ 0,2 \]  
  Multiply component wise \= \[ 0.24 x 0, 0.24 x 2 \]  
                                          \= \[ 0, 0.48 \]

  Third Value : 0.67 x V3 \= 0.67 x \[ 3,1 \]  
  Multiply component wise \= \[ 2.01, 0.67\]

  Step 4 : Add all weighted values   
  Now add : \[ 0.09, 0\] \+ \[ 0,0.48\] \+ \[ 2.01, 0.67\]

  First Dimension   
  Add first elements : 0.09 \+ 0 \+ 2.01 \= 2.10

  Second Dimension   
  Add second elements : 0 \+ 0.48 \+ 0.67 \= 1.15

  Final output \= \[ 2.10 , 1.15 \]

  Matrix Form ( how transformers actually do it )  
  Instead of doing it manually , transformers do:   
  Weights : A \= \[ 0.09  0.24  0.67 \]  
  Values :    
                       |  1  0 |  
                 V \= |  0  2 |  
                       |  3  1 |  
  Multiply :   
                  AV  
                                              | 1  0 |  
             \= \[ 0.09  0.24  0.67 \] | 0  2 |  
                                              | 3  1 |

  First column :  (0.09×1) \+ (0.24×0) \+ (0.67×3)   
                           \= 0.09 \+ 0 \+ 2.01  
                           \= 2.10

  Second column : (0.09×0) \+ (0.24×2) \+  (0.67×1)  
                              \= 0 \+ 0.48 \+ 0.67  
                              \= 1.15

* Entire Attention Formula 

  Attention ( Q, K, V ) \= Softmax ( QKt / √Dk ) V  
* Self Attention Matrix   
  For sentence length : n 

  Create :   Q ∈ R ^ n x d  
                  K ∈ R ^ n x d  
                  V ∈ R ^ n x d

  R stands for set of all real numbers  , so when we write  Q ∈ R ^ n x d we mean Q is a matrix containing real       numbers 

  ∈ stands for belong to , so when we write Q ∈ R ^ n x d  means “ Q is an n x d matrix  of real numbers “ 

  n  is the number of tokens in the sequence 

  d is the dimension of each vector .  
  Real transformers use larger dimensions   
  Original paper d model \= 512   
  Modern LLMs uses dimensions like 4096 , 8192 , 12288 etc 

  Q stands for query “ what information am i looking for ? “ . every token generates a query vector   
  Eg \- “ the animal was tired because it ran “  
  When processing “ it “  
  The query may effectively be : “ Which previous word does ‘ it ’ refer to ? ” . The model learns this               automatically .  
  Mathematically Q \= XWq  
  Where:  
  X \= embeddings   
  Wq \= learned query weights 

  K stands for “ What information do I contain ? “ . Every token advertises itself using a key .  
  Mathematically :   K \= XWk

  V stands for “ the actual information i will provide if someone attends to me “  
  Analogy   
  Imagine a library   
  Query : looking for machine learning books   
  Key : machine learning   
  Value : actual book contents   
  Matching happens between Query \< — \> Key , but information comes from Value   
  Mathematically  V \= XWv

  Compute : QKt

  Result : n x n   
  Attention matrix . Every token attends to every token  

* Suppose we focus on token i .   
  Its query : Qi  
  Is compared against every key : K1 , K2 , ……,Kn  
  Using : QiKtj  
  This produces attention scores.   
  After softmax : \[  α1​,α2​,…,αn​ \]  
  Finally : Outputi​ \= α1​V1 ​+ α2​V2 ​+⋯+ αn​Vn

* Single attention may learn only one relationship . instead of one attention we focus on different heads and run     them simultaneously .  
  For each head : Qi , Ki , Vi compute attention independently . Then concatenate :    
                        Concat( head1 , ……, head h)  
  Formula :   
             ​Multi Head (Q,K,V) \= Concat (head1​,...,headh​) Wo

* Positional Encoding  
  Attention alone doesn't know order . Sentences “ Dog bites man “ and “ Man bites dog “ contain the same words .     Need position information.

  Transformer adds : Embedding \+ Position Encoding  

* Position encoding formula   
  For even dimensions : PE ( pos, 2i ) \= sin ( pos / 10000 ^ 2i / d )  
  For odd dimensions :  PE ( pos, 2i \+ 1 ) \= cos (pos / 10000 ^ 2i / d )

  Where pos stands for position of token , d for embedding dimension , i for dimension pair index and PE for          positional encoding .

  Eg \- lets use :  d \= 4

  Step 1 : Compute Position 0   
  First  word : I   
  Position : pos \= 0

  Dimension 0 is even , therefore :  PE (0,0) \= sin( 0 / 10000 ^ 0/4 )  
                                                                      \= sin ( 0 )  
                                                                      \= 0

  Dimension 1 is odd dimension : PE ( 0,1 ) \= cos( 0 / 10000 ^ 0/4 )  
                                                                     \= cos ( 0 )  
                                                                     \= 1

  Dimension 2 again even :  PE (0,2) \= sin( 0 / 10000 ^ 2/4 )  
                                                                      \= sin ( 0 / 100 )  
                                                                      \= 0

  Dimension 3 is odd : PE ( 0,3 ) \= cos( 0 / 10000 ^ 2/4 )  
                                                                     \= cos ( 0 )  
                                                                     \= 1

  Final position encoding : PE ( 0 ) \= \[ 0,1,0,1 \]

  Step 2: Position 1   
  Second token: love   
  Position :  pos \= 1 

  Dimension 0 : PE (1,0) \= sin(1)  
                                       \= 0.84147

  Dimension 1 : PE (1,1) \= cos(1)  
                                       \=  0.54030

  Dimension 2 : PE ( 1,2 ) \= sin ( 1 / 100 )  
                                         \= sin ( 0.01 )  
                                         \= 0.0099998

  Dimension 3 : PE ( 1,3 ) \= cos ( 0.01 )  
                                         \= 0.99995

  Final vector :  PE ( 1 ) \= \[ 0.84147,0.54030,0.009999,0.99995 \]

  Step 3: Position 2   
  Third token: AI   
  Position : pos \= 2 

  Dimension 0 :  PE ( 2 , 0\) \= sin ( 2 )  
                                        \= 0.9093

  Dimension 1 : PE ( 2,1 ) \= cos ( 2 )  
                                         \= \-0.4161

  Dimension 2 : PE ( 2,2 ) \= sin ( 2 / 100 )  
                                         \= sin ( 0.02 )  
                                         \= 0.019998

  Dimension 3 : PE ( 2,3 ) \= cos ( 0.02 )  
                                         \= 0.9998

  Final  :  PE ( 2 ) \= \[ 0.9093,−0.4161,0.019998,0.9998 \]

  Positional Encoding Matrix  : |      0             1            0            1      |  
                                |   0.84147       0.54030      0.009999      0.99995  |  
                                |   0.9093       \-0.4161      0.019998      0.9998   |

  Shape :  3 x 4   
  Because :   
  \- 3 tokens   
  \- embedding dimensions 4 

* Suppose embeddings are:  
  E ( I ) \= \[ 1,2,3,4 \]  
  E ( love ) \= \[ 5,6,7,8 \]  
  E ( AI ) \= \[ 2,1,4,3 \]

  Transformers perform:   
                        X \= Embedding \+ Positional Encoding 

  First Token : \[ 1,2,3,4 \] \+ \[ 0,1,0,1 \]  
                       \= \[ 1,3,3,5 \]

  Second token :   \[ 5,6,7,8 \] \+ \[ 0.84147,0.54030,0.009999,0.99995 \]  
                            \= \[ 5.84147,6.54030,7.009999,8.99995 \]

  Third token : \[ 2,1,4,3 \]  \+  \[ 0.9093,−0.4161,0.019998,0.9998 \]  
                       \= \[ 2.9093,0.5839,4.019998,3.9998 \]

* Intuition   
  For d \= 4:  
  Position 0 : \[ 0,1,0,1 \]  
  Position 1 : \[ 0.84,0.54,0.01,0.999 \]  
  Position 2 : \[ 0.91,−0.41,0.02,0.999 \]

  These vectors are added to embeddings before computing, so positional information gets baked into Q, K, and V,      allowing attention to know both :  
  \- what the word means (embedding)  
  \- where the word occurs (position)

  So the original transformer can understand both “ dog bites man “ and “ man bites dog “ have the same words but     different meaning . 

* Transformer Encoder   
  Each encoder layer : 

  Input —\> Multi Head Attention  —\> add \+ norm  —\>  feed forward  —\> add \+ norm 

  Feed Forward :   
            
                 FFN ( x ) \= W2 ​( ReLU ( W1​x \+ b1 ​)) \+ b2​

  Applied  independently to each token  

* Step 1 :   
  After attention , each token has a context \- aware representation   
  Eg \- “ i “ , “ love “ , “AI”   
  Suppose attention has already produced a vector for the token “ love”  
                                        X \= | 1 |  
                                              | 2 |  
  This vector is now fed into the FFN. The FFN acts like a mini neural network applied to each token independently .

  Transformer Block 

  Token —\> Self Attention —\> FFN —\> Output 

  Step 2 : Choose Dimensions   
  Input : 

              X \= | 1 |  
                    | 2 |

  Dimensions : d model \= 2

  First layer expands dimension   
  Choose :   
                            | 1   2 |  
                   W1 \=    | 0   1 |  
                            | 2  \-1|  
  Shape : 3 x 2   
  Bias :   
                  | 1 |  
          b1 \=   | 0 |  
                  | 2 |

  Shape : 3 x 1 

  Second layer compresses back   
  Choose : 

           W2 \= | 1  0  2 |  
                    | 0  1  1 |

  Shape : 2 x 3 

  Bias :   
                  b2 \=   | 1 |  
                          | 2 |  
  Shape : 2 x 1

  Step 3: Compute W1x

  Formula: W1x

  Substitute values :   
                                        | 1    2 |  
                                     \= | 0    1 |   | 1 |  
                                        | 2   \-1|   | 2 |

  First Row :  ( 1\) ( 1 ) \+ ( 2 ) ( 2 )  
                     \= 1 \+ 4  
                     \= 5

  Second Row : ( 2 ) ( 1 ) \+ ( \-1 ) ( 2 )  
                        \= 2 \- 2  
                        \= 0

  Result :               | 5 |  
                  W1x \= | 2 |  
                             | 0 |

  Step 4: Add bias b1  : W1x \+ b1  
                                      | 5 |    | 1 |       | 6 |
                                   \= | 2 | \+ | 0 |    \= | 2 |  
                                      | 0 |    | 2 |       | 2 |    
     

  Step 5 : Apply ReLU   
  It means :    
                    ReLU ( z ) \= max (0,z)  
  Apply to each element:  
                                        | 6 |      | 6 |  
                             ReLU       | 2 |  \=  | 2 |  
                                        | 2 |      | 2 |

  Nothing changes because all values are positive 

  Eg with negatives   
  If :  \[ \-3 , 5 , \-1 \]  
  Then :  ReLU \= \[ 0,5,0 \]

  Step 6: Multiply by W2  
  Now :   
                         | 6 |  
                  W2     | 2 |  
                         | 2 |

  Substitute :   
                   | 1  0  2 |  | 6 |  
                \= | 0  1  1 |  | 2 |  
                                | 2 |

  First Row :  (1) (6) \+ (0)(2) \+ (2)(2)  
                      \= 6 \+ 4   
                      \= 10

  Second Row : (0) (6) \+ (1)(2) \+ (1)(2)  
                           \= 4

  Result :       | 10 |  
                  \= |  4  |

  Step 7: Add b2 

    | 10 |   \+  | 1 |  
    | 4  |       | 2 |  
      
    \= | 11 |  
       | 6  |

  Final FFN output 

     FFN (x) \= | 11 |  
                | 6  |

* The FNN first expands 512 —\> 2048 , then compresses 2048  —\> 512   
  . This gives the model a larger space to learn complex patterns.  
  Think of it as :   
  Attention : find relevant information   
  FFN : Process and transform that information 

* Attention mixes information between tokens , FFN doesn’t  mix  tokens . Instead it processes each token             separately . If the sequence is :   
         \[ x1, x2, x3 \]  
  Transformer applies : FFN ( x1 )  
                                     FFN ( x2 )  
                                     FFN ( x3 )  
  Independently. That's why attention handles communication between words , while the FFN acts like a powerful        feature extractor for each individual word representation .

* Transformer decoder adds masked self attention .   
  For eg : generating “ i love …… “ cannot see further tokens  “ learning “ during training . It uses masked self     attention 

* In normal self \- attention every token can attend to all tokens   
  Eg : “ i love AI “ 

  Attention matrix after softmax :   
      
                          | 0.4   0.3    0.3 |  
                          | 0.2   0.5    0.3 |  
                          | 0.1   0.2    0.7 |  
  Here :   
  \- “ i “ can see “ love” and “ AI “   
  \- “ love “ can see “ AI “  
  \- “ AI “ can see all previous words   
  This is fine in the encoder 

* Why masked self attention ?  
  Consider language generation :   
  Input : I love \_\_\_\_  
  Target : AI 

  During training , the full sentence is available :   
  I love AI   
  If we allow “ love “ to attend to “ Ai “ the model can cheat because it already sees the future word it is supposed to predict

* The idea   
  When predicting a token at position i,  
  The model should only see:    
                                  1…………i   
  And not :   
                          I \+ 1 ………n 

  Triangular Mask   
  For a sequence length 4:   
  “ i love machine learning “

  Create :   
                            |  0    −∞    −∞   −∞ |     
                            |  0     0    −∞   −∞ |   
                   M  \=    |  0     0     0   −∞ |  
                            |  0     0     0    0 |

  This is called a casual mask or triangular mask .

  Meaning :   
  Row 1 (  “I “ ):

  Can see : I   
  Cannot see : love , machine , learning

  Row 2 ( “ love “ )

  Can see : I , love   
  Cannot see : machine , learning 

  Row 3 ( “ machine “ )

  Can see : i  , love , machine  
  Cannot  see : learning 

  Row 4 ( “ learning “ )

  Can see : i , love , machine , learning 

  Why triangular ?  
  Visually :   
                          |  O   X    X   X  |  
                          |  O   O    X   X  |  
                          |  O   O    O   X  |  
                          |  O   O    O   O  |

  Allowed entries from a lower triangle 

  How is it applied 

  Before softmax :   
                                Scores \= QK ^ t / √Dk  
     
  Supposes  scores are : 

                               | 2  3  5 |   
                               | 1  4  2 |  
                               | 3  2  1 |

  Apply masks : 

    
                             |  2    −∞    −∞  |  
                             |  1     4    −∞  |   
                             |  3     2     1  |

  Now apply softmax row \- wise : 

  For row 1 :   
                    Softmax ( 2 , −∞ , −∞ )

  Since :    
                     e ^ −∞ \= 0

  We get :     
                   \[ 1,0,0 \]

  The token can only attend to itself 

  For row 2 :   
                    Softmax  ( \[ 1, 4, −∞\] )

  Becomes approx :   
                                 \[ 0.05,0.95,0 \]   

  No attention goes to future token 

* Full architecture 

  Encoder  —--\> Encoder Output  —--\> Decoder Cross Attntion  —--\> Linear  —--\>  softmax  —--\> next word 

* Usefulness of attention 

  Parallelizable   
  All tokens processed simultaneously 

  Long Range Dependencies   
  Any token can directly attend to any other token   
  DIstance \= 1 step   
  Not 100 steps 

  Better Gradient Flow  
  Attention paths are shorter   
  Training becomes easier .

* Complexity   
  For sequence length : n  
  Attention matrix : n x n   
  Cost : O ( n ^ 2 )  
  Memory : O ( n ^ 2 )  
  This later becomes the major weakness . for 100k tokens :   
   100000 ^ 2 \= 10 ^ 10  entries . Impossible 

* Hidden Interpretation 

  Attention learns a dynamic graph . Each token becomes a node . Attention weights become edges . For every input sentence , a new graph is constructed . This is why transformers are so expensive . 

* Biggest Limitation   
  Self attention requires explicitly computing : QK ^ T  
  which creates : n x n  interactions   
  Memory explodes   

   The Hidden Attention of Mamba Models 

* “ Mamba secretly performs something very similar to attention , even though it doesn't explicitly compute             attention matrices “ 

* Why do we need mamba ?  
  Transformers uses self attention ie every token checks on every other token present , giving it a On ^ 2 complexity making it really expensive 

  Mamba’s Goal   
  Transformer like intelligence \+ RNN like efficiency   
  Instead of storing all previous tokens , it stores compressed memory state called hidden state , this gives O(n)    complexity instead of O(n ^ 2 ) which is why mamba scales much better to long contexts 

* Mamba models show implicit attention mechanism not explicit attention like transformers but mathematically very     close to attention 

* Transformers  create an attention matrix . Every cell contains importance scores . This matrix is explicitly        computed . 

  Mamba never computes QK ^ t , no attention matrix exists . Instead it uses selective state updates .  
  For every token :   
  Should I remember this ?  
  Should I forget this ?  
  This hidden state is updated dynamically .  

* The Mathematical Intuition  
  Mamba state update :  h\_t \= A\_t  h\_( t \- 1 ) \+ B\_t  x\_t  
  Where:  
  h\_t \= memory   
  x\_t \= current token

  A\_t and B\_t change according to input and this is called Selective SSM .  
  Expanding recursively : 

  H\_t depends on   
  x\_t  
  x\_t \- 1  
  x\_t \- 2  
  x\_t \- 3  
  …  
  Each previous token contributes with a certain weight .  
  These weights behave like attention scores . so they reconstruct an implicit map .

* Major contribution of this paper 

  Contribution 1   
  Derive attention formulation . They rewrite mamba as :   
  Current Output \= weighted sum of past inputs 

  Contribution 2   
  Interpretability   
  Once you have an attention \- like a matrix . You can ask :   
  Which previous tokens influenced the current prediction ?  
  Exactly like Transformers attention visualization .  
  Before this paper : Mamba was mostly a black box   
  After this paper : We can inspect its internal dependencies . 

* Mamba often focuses on specific past tokens similarly to transformers .It is not simply “ compress everything       equally “ , instead “ selective preserves important information “ through its state dynamics .   
  This explains why Mamba performs surprisingly well on :   
  \- language modelling   
  \- long context tasks   
  \- sequence reasoning 

* When you care about long context , transformers struggle because memory grows quadratically . Mamba offers linear   memory linear compute while still retaining attention-like behaviour 

* Industry level takeaway   
  RNN   
  Past → Compressed State → Future 

  Problem   
  Forgets long range information 

  Transformer   
  Past \< — \> Future   
  Through explicit attention 

  Problem   
  O(n ^ 2\)

  Mamba   
  Past → Selective Memory → Future 

  Benefits   
  O(n)

* Softmax converts arbitrary scores into probabilities that sum to 1\.  
  Cat \= 8.5  
  Milk \= 3.2   
  Was \= 1.1  
  The \= 0.5 

  these scores came from   
  Q\_it · K\_cat  
  Q\_it · K\_milk  
  Q\_it · K\_was  
  Q\_it · K\_the

  Notice :   
  8.5 \+ 3.2 \+ 1.1 \+ 0.5 \=/ 1  
  and scores can be negative , scores can be huge and scores are not probabilities .

  We need to convert them into probabilities , this is what softmax do

  Step 2 : Softmax Formula  
  For each score :   
                                
                    Pi​ \= e ^ xi / ∑j e ^ xj

  Where:  
  \- xi \= score   
  \- e \= euler’s number \= 2.71828

  Step 3 : calculate exponentials  
  Our scores :   
  Cat \= 8.5   
  Milk \= 3.2  
  Was \= 1.1  
  The \= 0.5

  Compute :   
   E ^ 8.5 \= 4914.77  
   E ^ 3.2 \= 24.53  
   E ^ 1.1 \= 3.00  
   E ^ 0.5 \= 1.65

  Step 4 : Compute sum   
                        4914.77 \+ 24.53 \+ 3.00 \+ 1.65 \= 4943.95

  Step 5 : normalize 

  Cat : 4914.77 / 4943.95  \=  0.994  
  Milk : 24.53  / 4943.95  \=  0.00496  
  Was : 3.00 / 4943.95  \=  0.00061  
  The : 1.65 / 4943.95  \=  0.00033

  Now they sum to :  0.994 \+ 0.00496 \+ 0.00061 \+ 0.00033 \= 1


  


| Aspect | Transformer | Mamba ( State Space Model) |
| :---- | :---- | :---- |
| Core Mechanism  | Self-Attention | Selective State Space Model |
| Memory Handling | Looks at all previous tokens directly  | Maintains a compressed hidden state  |
| Context Access | Explicit access to every token  | Information stored and propagated through state updates  |
| Attention Matrix | Explicit computesQK ^ t | No attention matrix is computed  |
| Time Complexity  | O (n ^ 2\) | O( n ) |
| Memory Complexity | O (n ^ 2 ) | O( n ) |
| Long Context Scaling | Expensive for very long sequences  | Designed for very long sequences  |
| Parallelization | Highly parallel during training  | Uses selective scan for efficient parallelization  |
| Interpretability  | Easy to visualize attention weights  | Harder to interpret ( though hidden can be derived) |
| Inference Speed | Slower for long contexts  | Faster and more memory efficient  |
| Strength | Excellent reasoning and global context modelling  | Efficient long sequence processing  |
| Weakness  | Quadratic cost becomes expensive  | May lose some fine grained token interactions  |

