# MIT CSAIL — *Sparks of Weight-Space Programming* (2026)

> **Scope note.** This is a technical summary of the MIT CSAIL research blog post
> *Sparks of Weight-Space Programming: LLMs can natively read & write neural
> network weights*, published 2 November 2026. The post presents early results,
> not a conventional peer-reviewed paper with a complete statistical evaluation.
> Numbers and claims below are reported by the authors unless explicitly marked
> as interpretation or limitation.

- **Authors:** Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab
- **Affiliations:** MIT CSAIL / MIT
- **Primary source:** [research post](https://rikiyat.github.io/blog/weight-space-programming/)
- **Experiment logs and code:** [lm_understand-logs](https://github.com/RikiyaT/lm_understand-logs)
- **Edited Qwen checkpoint:** [Hugging Face model](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)

## 1. Executive overview

The post introduces **Weight-Space Programming (WSP)**: a general-purpose
large language model (the experiments use GPT-6 Astra) directly reads and
writes the numerical parameters of another neural network in response to a
natural-language objective. The LLM is not used as a conventional optimizer:

1. It receives weights, architecture information, and a task specification.
2. It reasons about what units, directions, layers, or circuits compute.
3. It edits existing tensors or writes new tensors directly.
4. It may receive restricted forward-pass feedback in larger experiments, but
   it is not allowed to use gradients, loss functions, training loops, search,
   or external web access.

The authors demonstrate three kinds of behavior:

- **Reading:** infer a network's training task, generated object, language, or
  internal circuit from weights.
- **Repairing:** identify a failure mode and modify a small subset of weights.
- **Writing:** construct small task-specific networks from scratch, sometimes
  without running them before evaluation.

The strongest quantitative result is an edit to Qwen3.5-0.8B that changed
131,072 weights, or **0.016%** of the model, and raised reported MATH-500
accuracy from **7.9% to 48.1%**, GSM8K from **13.8% to 67.1%**, and IFEval from
**21.0% to 62.3%**. The authors attribute most of the gain to removing a
reasoning-loop failure mode rather than adding new mathematical knowledge.

## 2. Core foundation

### 2.1 The conceptual shift

Deep-learning optimization normally uses a symbolic optimizer such as SGD,
Adam, or Muon to update differentiable parameters. WSP instead treats a neural
network's parameter tensors as a **program representation** that a reasoning
model can inspect and edit. The LLM supplies the inductive bias and
program-level decomposition that an optimizer normally lacks.

The key hypothesis is not that an LLM can numerically optimize billions of
parameters one by one. It is that the LLM can recognize meaningful structure
in weight matrices:

- spatially localized input features;
- output directions and class/action separation;
- attention circuits such as induction/copying heads;
- low-dimensional behavioral directions written by MLPs;
- layer-by-layer implementations of a symbolic algorithm.

### 2.2 What counts as “native” weight programming?

The post uses “native” to distinguish direct weight reasoning from:

- gradient descent or a differentiable training loop;
- a separate optimizer searching candidate tensors;
- a model trained specifically to generate weights;
- a compiler that translates a formal program into weights;
- an LLM that only writes training code and delegates optimization elsewhere.

The distinction is practical rather than absolute: in the larger experiments,
the LLM writes Python code in a sandbox and can inspect tensors or obtain
restricted forward-pass results. The actual parameter changes still come from
the LLM's generated tensor-writing code, not from gradients.

### 2.3 Common experimental controls

Across the experiments, the authors restrict access to prevent trivial
solutions:

- no web search;
- no training data or loss/gradient information;
- no network execution in the zero-forward-pass settings;
- no labels or task names in several reading experiments;
- no output access in the sycophancy attention-only setting;
- fixed architecture and input/output shapes for task-identification tests.

These controls are important, but they do not by themselves establish that the
LLM has a general, reliable weight-space capability. The limitations section
discusses this distinction.

## 3. Complete results by experiment

## Experiment 1 — Identifying a game from raw policy weights

### Question

Can Astra infer which game a policy was trained to play when all candidate
networks have the same architecture, input channels, action space, and
training procedure?

### Setup

- **Games:** grid versions of Breakout, Pong, Pac-Man, and Freeway.
- **Board:** 10 × 10 grid.
- **Input:** five channels: agent, moving objects, reward targets, obstacles,
  and previous frame.
- **Actions:** no-op, up, down, left, right.
- **Network:** MLP `500 → 32 → 32 → 5`, tanh; **17,253 weights**.
- **Training:** PPO for 1 billion steps; best of three seeds per game.
- **Astra receives:** all weights as text plus descriptions of the grid and
  actions, with no game names or candidate list.
- **Restrictions:** no tool use is reported for this test.

### Result

Astra named the correct game for **all four networks**, even though the game
options were not disclosed.

### Authors' proposed mechanism

Astra appears to inspect the first-layer spatial structure. For example,
weights associated with the agent channel can concentrate along the bottom row
when the game contains a paddle-like object, while output-layer weights reveal
which actions are distinguished. This is a weight-level explanation rather
than a forward-pass demonstration.

## Experiment 2 — Identifying a diffusion model's generated shape

### Question

Can Astra infer what a diffusion model generates from weights alone, without
running a forward pass?

### Setup

- **Models:** three DDPMs trained independently on filled circles, squares, or
  triangles.
- **Image:** 12 × 12 grayscale, 144 output pixels.
- **Input:** noisy image plus a diffusion-step encoding of 16 numbers.
- **Network:** MLP `160 → 64 → 64 → 144`, ReLU; **23,824 weights**.
- **Training:** Adam for 40,000 steps.
- **Astra receives:** all weights as text; shape labels are withheld.
- **Restriction:** no tools or forward passes.

### Result

Astra correctly identified what each of the three models generated.

### Important qualitative finding

When asked to visualize its inference, Astra drew the shapes as **outlines**
rather than filled shapes. The authors interpret this as evidence that it was
reading geometric structure in the output weights—where hidden-unit weight
patterns trace edges—rather than calculating a model output. This is suggestive,
not a proof that no implicit forward computation occurred in the LLM's
reasoning.

## Experiment 3 — Inferring language and induction heads from middle layers

### Question

Can Astra understand a language model from intermediate weights when the input
embedding and output layers are removed, so the model cannot be run on text and
the token identities are hidden?

### Setup

- **Data:** Python code, Japanese literature represented in romaji, or English
  Wikipedia.
- **Model:** character-level transformer, four layers × six heads, width 384;
  **7.16 million weights**.
- **Vocabulary:** 28 characters (`a–z`, space, newline).
- **Training:** 1 billion characters for each model.
- **Astra receives:** only the four transformer blocks, not the input or output
  layers; unlabeled 384-dimensional directions; Python for analysis.
- **Budget:** up to 100 runs.
- **Forbidden:** running the model or any layer on real, random, or fabricated
  inputs; search.
- **Task:** identify the training language and classify all 24 attention heads.

### Quantitative result: language identification and copying heads

| Training data | Astra's two language answers | Heads named by Astra | Measured copying heads |
|---|---|---|---|
| Python | Python (0.56), Python (0.52) | 2.1, 3.1, 3.5 | 2.1, 3.1, 3.5 |
| Romaji | romaji (0.55), romaji (0.62) | 3.3 | 3.3 |
| English | English (0.58), English (0.48) | 3.1 | 3.1 |

Astra named the correct language in **both attempts for all three models**. It
identified **every measured copying/induction head and no non-copying head**.
The ground truth was obtained separately by running the model on a random
string repeated twice: copying-head scores were 0.22–0.55, while every other
head scored at most 0.02.

### Proposed mechanism

Astra reconstructed an induction-head circuit from matrix relationships:

1. An early head attends to a previous character.
2. Later heads use the information transported by that head to find repeated
   context and copy what followed it.

Python was distinguished by the prevalence of repeated identifiers and code
patterns. Romaji was distinguished by a final-block representation with fewer
distinct directions, consistent with unused letters such as `q`, `l`, `v`, and
`x`.

## Experiment 4 — Repairing a failing physical-control policy

### Question

Can Astra diagnose and repair a locally optimal policy by editing weights once?

### Setup

- **Environment:** Kinetix car-on-ramp level.
- **Required behavior:** reverse to gain runway, then accelerate over a red
  strip to reach a blue target.
- **Failure:** PPO drives directly at the ramp and stalls.
- **Network:** official Kinetix actor, `679 → 128`, five additional 128-unit
  tanh layers, then 16 outputs; **171,664 weights**.
- **Input:** 679 scene values describing bodies, positions, velocities, shapes,
  and joints.
- **Output:** 16 motor/thruster logits.
- **Training:** official PPO, 1 billion steps.
- **Initial evaluation:** zero successes in 256 episodes.
- **Astra receives:** all weights, scene description, and one recorded episode.
- **Restriction:** one reply, no tools.

### Result

In a single attempt, Astra changed **3.5% of the weights** and achieved
**1,024 successes out of 1,024 episodes**, up from 0%.

### Proposed mechanism

Astra diagnosed a local minimum and added a small path through a few units per
layer. The path reads position and speed, commands a backing-up maneuver, then
switches off after the green wheel passes the red strip; the original policy
handles the remainder of the task.

## Experiment 5 — Writing small game policies from scratch

### Question

Can Astra generate useful weights zero-shot, without data, loss, gradients,
training, tools, or pre-evaluation rollouts?

### Setup

- **Games:** MinAtar Breakout, Seaquest, and Asterix.
- **Board:** 10 × 10 grid.
- **Network:** `600 → 32 → 32 → 6`, tanh; all weights initially zero.
- **Input:** six channels: player, danger, reward, projectile, trail, gauge.
- **Output:** six action logits.
- **Astra receives:** game rules, source code, input/output layout, and scoring
  method.
- **Training:** none.
- **Generation:** one reply, weights emitted as text.
- **Evaluation:** 1,000 episodes; sampled actions, sticky actions 0.1, maximum
  10,000 steps.

### Scores

| Game | PPO, 100M steps | PPO, 500M steps | Astra, one-shot |
|---|---:|---:|---:|
| Breakout | 15.8 | 25.3 | **517.4** |
| Seaquest | 5.6 | **88.9** | 53.1 |
| Asterix | 25.8 | **55.2** | 53.2 |

Astra beat the 100M-step PPO baseline in **all three games**. Relative to the
500M-step PPO baseline, it scored about **20×** as much in Breakout, nearly
matched Asterix, and achieved about **60%** of Seaquest's score.

### Proposed mechanism

The generated weights implement hand-designed algorithms in neural form. In
Breakout, the first layer estimates where the ball will land and later layers
move the paddle toward that location.

## Experiment 6 — Writing a 1.5M-parameter Go policy

### Question

Can WSP scale beyond context-sized tensors and improve as restricted
interaction with the network is allowed?

### Setup

- **Game:** Go on a 9 × 9 board.
- **Network:** `243 → 512 × 6 → 82`, ReLU; **1,480,274 weights**, initialized
  to zero.
- **Input:** both players' stones and side to move.
- **Output:** one logit per board point plus pass; illegal moves are masked.
- **Astra receives:** rules, input/output layout, and a CPU Python sandbox for
  reading/writing tensors with NumPy/PyTorch.
- **Not allowed:** Go library, internet, training, fitting to data, tree
  search, or rollouts outside the allowed forward passes.
- **Forward-pass budget:** 0 through 50. A pass provides up to 128 practice
  games or up to 256 position outputs; Astra edits between passes.
- **Evaluation:** 2,000 sampled games against each of two smaller PPO
  networks, with sides balanced. The comparison PPO architecture is
  `243 → 32 → 32 → 82`, trained for 20,000 iterations of 1,024 games.

### Results

- With **0 forward passes**, Astra won **more than half of its games against
  each of two smaller PPO opponents**.
- With **50 forward passes**, Astra's equal-sized generated network **beat the
  equal-sized PPO network trained on 20 million games**.

The post does not provide a complete numeric win-rate table for every
forward-pass budget in the reproduced text; the reported trend is that more
feedback improved fidelity and allowed iterative correction.

### Proposed mechanism

Astra wrote a small Go algorithm layer by layer:

- early layers mark stones and adjacent empty points (liberties);
- middle layers propagate information along connected groups;
- later layers score captures, saves, atari avoidance, eye filling, and board
  preferences.

With no forward passes, this program was written in one 336-line Python run.
With feedback, Astra examined losses and retained edits that improved wins.

## Experiment 7 — Detecting sycophancy

### Question

Can Astra identify a behavioral difference between two nearly identical
language models from weights, and can it localize the mechanism when given
attention-only observations?

### Setup

- **Model:** Gemma 3 270M, instruction-tuned, 18 layers.
- **Pairs:** three pairs, each made by identical fine-tuning procedures on the
  same QA data. One model answers correctly; the other follows the user's
  suggested answer.
- **Frozen parameters:** token embeddings and output layers, preventing a
  trivial input/output-distribution explanation.
- **Behavioral ground truth:** on held-out facts the sycophant followed wrong
  guesses **100%** of the time; the honest model did so **1–3%** of the time.
- **Astra receives:** weights, tokenizer, NumPy, and an attention tool.
- **Attention tool:** up to 16 self-written texts; returns attention weights only,
  not model outputs; at most 20 runs.

### Results

1. **Weights alone:** failure. Across four attempts, Astra found many
   differences but could not map them reliably to sycophantic behavior.
2. **Attention patterns:** success. With attention-only observations, Astra
   identified the sycophant in **all three trained pairs**.
3. **Localization:** Astra found that middle-layer heads in the sycophantic
   model attend more strongly to the user's suggested answer.

For example, head 10.2 at the answer position attended to the question's
numbers **94.3%** in the honest model versus **3.5%** in the sycophant, while
attention to the user's answer was **0.75%** versus **85.7%**.

This is an important negative result: raw weight inspection did not suffice for
this behavioral distinction, but a small amount of structured activation
information made it tractable.

## Experiment 8 — Directly improving Qwen3.5-0.8B

### Question

Can Astra edit a real, larger language model to improve a natural capability
without gradients or training?

### Setup

- **Model:** Qwen3.5-0.8B, thinking enabled, 24 layers, approximately 0.8B
  weights.
- **Objective:** improve math performance by directly editing weights.
- **Harness:** Python kernel with weights loaded; CPU only.
- **Practice data:** 7,469 GSM8K problems and 7,275 MATH problems; test sets
  withheld.
- **Forward-pass budgets:** 10, 25, or 50; each pass answers up to 512
  problems or reads up to 1,024 texts.
- **Evaluation:** MATH-500, GSM8K, IFEval, AMC23, Minerva Math,
  OlympiadBench, GPQA Diamond, and MMLU-Pro.
- **Generation settings:** temperature 0.6, top-p 0.95, top-k 20, presence
  penalty 1.5, up to 32,768 tokens.
- **Sampling:** 16 samples/problem on AMC23; 4 on MATH-500, Minerva Math,
  OlympiadBench, and GPQA Diamond; 2 on GSM8K and IFEval; one on MMLU-Pro
  (fixed 1,000 questions).
- **Forbidden:** gradients, training, and access to evaluation sets.

### Main results

| Model | MATH-500 (%) | GSM8K (%) | IFEval (%) | Hit token limit (%) |
|---|---:|---:|---:|---:|
| Base | 7.9 | 13.8 | 21.0 | 93.0 |
| Edited, 10 passes | 12.3 | 25.7 | 49.0 | 87.2 |
| Edited, 25 passes | 14.1 | 25.1 | 39.9 | 86.4 |
| Edited, 50 passes | **48.1** | **67.1** | **62.3** | **33.1** |

The 50-pass edit changed **131,072 weights**, or **0.016%** of the model.
The 10- and 25-pass edits improved some scores but did not reliably remove the
looping failure. The 50-pass result reduced the MATH-500 token-limit rate from
93.0% to 33.1%.

### Diagnosed mechanism

The base model frequently entered long thinking loops: **85 of the first 96
practice answers** reached the 32,768-token limit. Astra traced this to a
direction written by the MLPs of layers 15 and 19. It subtracted that
direction from 64 output columns in each layer:

- 64 columns × 2 layers × 1,024 relevant entries = **131,072 edited weights**.
- The edit resembles deleting a low-dimensional behavioral direction rather
  than retraining the model.

The authors' interpretation is that the edit exposed existing math ability by
allowing answers to terminate; it did not teach the model new mathematics.

## Additional experiment — Editing a model that does not loop

### Purpose

To test whether the Qwen gain was merely loop removal, Astra was asked to
improve Gemma 3 270M, which rarely reaches its token limit.

### Setup and result

- Gemma reaches the token limit on **8.5%** of answers versus Qwen's 93%.
- Gemma's errors were ordinary reasoning mistakes: arithmetic and invalid
  algebraic steps, with no single direction or component to disable.
- Astra made small targeted edits (for example, doubling a number-responsive
  neuron), but none produced an established gain.

| Gemma 3 270M | MATH-500 (%) |
|---|---:|
| Base | 6.8 |
| Edited, 5 passes | 7.0 |
| Edited, 10 passes | 7.6 |
| Edited, 25 passes | 7.7 |
| Edited, 50 passes | 7.0 |

The authors conclude that WSP can remove an obstacle that masks an existing
ability, but may not add an ability absent from the model.

## 4. Cross-experiment findings

### 4.1 Reading scales from local structure to circuits

The first experiments rely on interpretable local patterns: spatial first-layer
weights and output-layer geometry. Experiment 3 is stronger because Astra has
only unlabeled intermediate blocks and still reconstructs a multi-head circuit.
Experiment 7 shows the boundary: a subtle behavioral distinction was not
recoverable from weights alone, but became visible through attention patterns.

### 4.2 Writing is often algorithm synthesis

The generated small networks are best understood as compiled programs. Astra
first reasons about a desired algorithm—ball interception, Go liberties,
danger avoidance—and encodes intermediate predicates into ReLU/tanh pathways.
This is qualitatively different from blind parameter search.

### 4.3 Sparse edits can have global effects

The Kinetix repair modified 3.5% of parameters. The Qwen repair modified only
0.016%, yet changed termination behavior and several benchmarks. This supports
the possibility that some failures are concentrated in low-dimensional weight
directions.

### 4.4 Feedback is useful but not sufficient

Zero-shot writing works on small, structured games and even gives a strong
relative Go result. Restricted forward passes improve larger-scale edits.
However, the non-monotonic 10/25/50-pass Qwen results show that more interaction
does not automatically produce a better edit.

### 4.5 The strongest improvements may be “unmasking”

Qwen's improvement is primarily a failure-mode correction. Gemma's result
suggests that direct editing is currently better suited to removing a
recurrent obstruction than inventing robust new reasoning skills.

## 5. Bottlenecks and limitations

### 5.1 Context and representation bottleneck

Raw weights rapidly exceed an LLM's context window. The early experiments fit
weights directly into context, while the later experiments require a Python
kernel and an interaction protocol. A scalable WSP system needs tensor
summaries, structured access, indexing, compression, and safeguards against
losing the semantics of individual dimensions.

### 5.2 Harness and tool-design dependence

The allowed tools define what the LLM can discover. A forward pass, attention
map, tensor inspection API, or carefully chosen prompt can make a task easier
or harder. Results therefore measure a combined system—Astra plus its harness—
not only an abstract model capability.

### 5.3 Limited statistical evidence

Several headline demonstrations are one-shot or use very few attempts. The
post reports success counts and benchmark scores, but not a full set of
confidence intervals, independent model families, prompt ablations, or
multiple LLM evaluators. The results are compelling demonstrations, not yet a
reliable engineering benchmark.

### 5.4 Baseline comparability

PPO and Astra do not receive identical information or compute. Astra is given
source code and rules in some writing tasks; PPO receives millions or billions
of environment steps. Scores also depend on sampling, seeds, sticky actions,
and opponent selection. Comparisons should be read as capability
demonstrations, not equivalent-compute optimization claims.

### 5.5 Causal interpretation is unresolved

An LLM's explanation of a circuit can be correct, post hoc, or partly
correlated with an effective edit. The experiments validate behavior in some
cases, but they do not fully establish that every natural-language explanation
is a faithful causal account of the edited mechanism.

### 5.6 Generalization and robustness

The post does not establish that edits survive distribution shifts, quantization,
different inference settings, architecture changes, or adversarial inputs.
Qwen's reported gains use fixed sampling and long-context settings, and the
evaluation is one checkpoint. Replication across seeds, model families, and
tasks is needed.

### 5.7 Capability ceiling

Gemma's failed improvement is a concrete boundary condition. If a desired
skill is not represented in the model, sparse direct edits may not be enough.
WSP currently appears more promising for locating, suppressing, routing, or
repairing existing circuits than for reliably creating broad new knowledge.

### 5.8 Safety and verification

Direct weight editing could introduce hidden backdoors, disable safeguards,
damage calibration, or create capabilities that ordinary benchmark tests miss.
Any practical system needs immutable checkpoints, tensor-level diffs,
regression suites, behavioral red-teaming, rollback, and provenance for every
edit.

## 6. Technical implications proposed by the authors

The post identifies several possible applications:

1. **Auditing without ordinary evaluation:** inspect weights for hidden traits,
   backdoors, or vulnerabilities before deployment.
2. **Lower-cost optimization:** replace some dataset curation and training
   loops with targeted edits.
3. **Zero-data steering and unlearning:** add or remove a capability through a
   sparse edit, potentially reducing catastrophic forgetting.
4. **Recursive self-improvement:** let an LLM inspect and improve its own
   weights or those of another model.
5. **Architecture-aware model merging:** transplant circuits between models
   with different architectures instead of averaging only matching tensors.
6. **A weight-space programming benchmark:** standardize tasks, harnesses,
   logs, and evaluation so that current demonstrations become reproducible
   measurements.

These are forward-looking hypotheses, not results demonstrated by the
experiments. In particular, the post does not demonstrate safe unlearning,
backdoor discovery, recursive self-improvement, or cross-architecture circuit
grafting.

## 7. Overall assessment

The paper's central contribution is an empirical claim that a frontier LLM can
sometimes treat neural weights as an intelligible program representation:
identifying task-specific geometry, reconstructing internal circuits, writing
small algorithms as weights, and making sparse repairs in a real language
model. The most persuasive evidence is the combination of:

- exact induction-head localization from unlabeled middle layers;
- zero-shot game policies that outperform short PPO runs;
- complete Kinetix repair over 1,024 episodes;
- the Qwen loop-removal edit with a 0.016% parameter change and large
  benchmark gains;
- the negative Gemma result, which constrains the claim.

The appropriate conclusion is **“early evidence of a new LLM-mediated
optimization and interpretability workflow,”** not that LLMs have solved
general neural-network optimization. The next decisive steps are independent
replication, stronger ablations, complete numeric curves for interaction
budgets, cross-model evaluation, causal circuit tests, robust safety checks,
and a public benchmark that separates model reasoning from harness design.

## 8. Result checklist

| Area | Reported outcome |
|---|---|
| Game identification | 4/4 correct from 17,253 raw policy weights |
| Diffusion-shape identification | 3/3 correct from 23,824 weights; outlines drawn instead of fills |
| Language identification | 6/6 correct answers across two attempts per model |
| Induction-head localization | All measured copying heads found; no false positives reported |
| Kinetix repair | 1,024/1,024 successes, from 0/256 baseline episodes |
| MinAtar writing | Beats 100M-step PPO in Breakout, Seaquest, and Asterix |
| MinAtar Breakout | 517.4 vs 25.3 for 500M-step PPO |
| Go writing | >50% wins against two smaller PPOs with zero passes |
| Go with feedback | Beats equal-sized PPO trained on 20M games at 50 passes |
| Sycophancy from weights alone | Failed in all four attempts |
| Sycophancy with attention only | Correctly identifies all three pairs |
| Qwen math repair | MATH-500 7.9% → 48.1%; GSM8K 13.8% → 67.1% |
| Qwen instruction following | IFEval 21.0% → 62.3% |
| Qwen edit sparsity | 131,072 weights, 0.016% of model |
| Qwen loop rate | Token-limit hits 93.0% → 33.1% |
| Gemma math improvement | No established improvement; 6.8% base, 7.0% after 50 passes |

