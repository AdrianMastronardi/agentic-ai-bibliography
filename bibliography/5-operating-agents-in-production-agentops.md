---
layout: default
title: "5. Operating Agents in Production (AgentOps)"
permalink: /bibliography/5-operating-agents-in-production-agentops/
---

Building an agent is only the beginning. Running it reliably in the
wild—handling failures, tracking performance, debugging behaviors, and aligning
it with business needs—requires a new discipline: AgentOps. This section gathers
tools and practices to monitor, validate, and continuously improve agents in
production, where correctness, reproducibility, and robustness matter.

## 5.1 Evaluation Metrics and Testing Pipelines

- **OpenAI – *Evals: Framework for Evaluating LLMs and LLM Systems* (2023)**
  Evals is OpenAI’s open-source framework to define, run, and analyze
  systematic tests for LLMs. It supports prompt-based benchmarks, scoring
  pipelines, and custom evaluations. While initially built for OpenAI models,
  it provides a structure for reproducible validation in any LLM-powered
  application.
  [Explore the code repository](https://github.com/openai/evals)

- **Fourney et al. – *AutoGenBench: A Tool for Measuring and Evaluating
- AutoGen Agents* (2024)**
  AutoGenBench is a command-line tool developed by Microsoft Research to
  evaluate AutoGen workflows using established LLM and agentic benchmarks. It
  emphasizes repeatability, isolation, and instrumentation in testing, making
  it suitable for tracking performance of multi-agent systems in production
  environments.
  [Access the source](3-evaluation-and-benchmarks.md)

- **Shahul Es et al. – *RAGAS: Retrieval-Augmented Generation Assessment*
- (2024)**
  RAGAS is an open-source evaluation framework for Retrieval-Augmented
  Generation (RAG) pipelines. It enables reference-free assessment of
  generation quality, relevance of retrieved context, and faithfulness of
  answers—eliminating the need for ground truth labels. RAGAS introduces
  task-specific metrics and supports batch-level evaluations, making it a
  scalable tool for production-grade RAG systems.  ·
  [Read the full paper from this repo](../papers/es-2024.pdf) · [Read the full
  paper from the source](https://arxiv.org/abs/2309.15217) · [Explore the code
  repository](https://github.com/explodinggradients/ragas) · [Read the full
  paper from the source](https://arxiv.org/abs/2309.15217)

- **UpTrain AI – *UpTrain: Unified Evaluation and Improvement Platform for
- Generative AI Applications* (2024)**
  UpTrain is an open-source platform for evaluating and improving LLM-based
  applications. It provides over 20 prebuilt evaluation checks across
  language, code, and embedding tasks, and supports root-cause analysis of
  failure cases. With a privacy-respecting local dashboard, UpTrain allows
  users to run, visualize, and iterate on test suites for generative
  applications.
  [Explore the code repository](https://github.com/uptrain-ai/uptrain)

- **Woffinden-Luey & Kiseleva – *AgentEval: A Developer Tool to Assess Utility
- of LLM-powered Applications* (2024)**
  AgentEval introduces a structured evaluation method where agents serve as
  evaluators, scoring target systems on multiple dimensions (e.g.,
  helpfulness, correctness). It is especially useful for LLM-based
  applications that require customized and scalable feedback loops.
  [Access the source](3-evaluation-and-benchmarks.md)

## 5.2 Observability and Debugging

- **LangSmith – *Observability and Evaluation Platform for LLM Applications*
- (2023)**
  LangSmith is a comprehensive platform designed to enhance the observability
  and evaluation of applications built with large language models (LLMs). It
  offers features such as tracing, debugging, and performance monitoring,
  enabling developers to gain insights into the behavior of their LLM-powered
  applications. LangSmith integrates seamlessly with frameworks like
  LangChain, providing tools to visualize execution flows, assess prompt
  effectiveness, and monitor system performance in real-time.
  [Access the source](https://www.langchain.com/langsmith)

- **Phoenix – *Open-Source LLM Observability and Evaluation Platform* (2023)**
  Developed by Arize AI, Phoenix is an open-source platform that provides
  observability and evaluation tools for applications powered by large
  language models. It enables developers to trace LLM application runtimes
  using OpenTelemetry-based instrumentation, evaluate performance through
  response and retrieval metrics, and manage versioned datasets for
  experimentation. Phoenix supports integration with popular frameworks like
  LangChain, LlamaIndex, and DSPy, offering a comprehensive solution for
  monitoring and optimizing LLM applications.
  [Explore the code repository](https://github.com/Arize-ai/phoenix)

- **PromptLayer – *Prompt Management, Versioning, and Observability Platform*
- (2023)**
  PromptLayer is a comprehensive platform designed to streamline prompt
  engineering workflows for large language models (LLMs). It offers features
  such as visual prompt creation, version control, A/B testing, and
  performance monitoring. PromptLayer's collaborative environment allows both
  technical and non-technical team members to manage and iterate on prompts
  efficiently. Its integration capabilities with various LLM providers and
  frameworks make it a versatile tool for maintaining prompt quality and
  consistency in production environments.
  [Access the source](https://www.promptlayer.com/) · [Explore the code
  repository](https://github.com/MagnivOrg/prompt-layer-library)

- **WhyLabs – *AI Observability and Monitoring Platform* (2023)**
  WhyLabs is a comprehensive observability platform designed to monitor and
  secure AI applications, including those powered by large language models
  (LLMs). It offers tools to detect data drift, monitor model performance, and
  enforce security policies, ensuring the reliability and safety of AI systems
  in production. WhyLabs integrates with various data and ML frameworks,
  providing real-time insights and alerts to preemptively address potential
  issues.
  [Access the source](https://whylabs.ai/) · [Explore the code
  repository](https://github.com/whylabs)

## 5.3 Output Validation and Safety

- **Guardrails AI – *Framework for Validating and Correcting LLM Outputs*
- (2023)**
  Guardrails AI is an open-source framework that provides mechanisms to
  validate and correct the outputs of large language models (LLMs). It allows
  developers to define structured output schemas and enforce quality
  constraints, ensuring that LLM responses adhere to specified formats and
  content guidelines. Guardrails AI supports integration with various LLMs,
  offering tools to detect and rectify issues such as hallucinations, bias,
  and formatting errors.
  [Access the source](https://www.guardrailsai.com/) · [Explore the code
  repository](https://github.com/guardrails-ai/guardrails)

- **ProtectAI – *Rebuff: Detecting Prompt Injection Attacks in LLM
- Applications* (2023)**
  Rebuff is an open-source framework designed to detect and mitigate prompt
  injection attacks against LLMs. It provides a layered defense strategy that
  includes heuristic filters, language model-based scoring, vector similarity
  search, and canary token detection. Rebuff can be integrated into LLM
  pipelines to monitor and protect both input and output from adversarial
  manipulation, making it a critical tool for secure agentic deployments.
  [Access the source](https://blog.langchain.dev/rebuff/) · [Explore the code
  repository](https://github.com/protectai/rebuff)

- **Traian Rebedea et al. – *NVIDIA NeMo Guardrails: A Toolkit for
- Controllable and Safe LLM Applications with Programmable Rails* (2023)**
  NeMo Guardrails is an open-source framework for implementing programmable
  constraints (or "rails") in LLM-powered applications. It allows developers
  to define conversational boundaries, filter undesired topics, and enforce
  safety behaviors using Colang, a domain-specific language. It includes
  built-in mechanisms to prevent prompt injections and jailbreaks, helping
  ensure trust and control in deployed agentic systems.  ·
  [Read the full paper from this repo](../papers/rebedea-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2310.10501) · [Explore the
  code repository](https://github.com/NVIDIA/NeMo-Guardrails) · [Read the full
  paper from the source](https://arxiv.org/abs/2310.10501)

- **TruLens – *Framework for Evaluating and Monitoring LLM Applications*
- (2023)**
  TruLens is an open-source framework designed to evaluate and monitor
  applications powered by large language models (LLMs). It introduces
  "feedback functions" that programmatically assess various aspects of LLM
  outputs, such as relevance, groundedness, and toxicity. TruLens integrates
  seamlessly with frameworks like LangChain and LlamaIndex, providing
  developers with tools to trace, debug, and improve their LLM applications.
  Its compatibility with OpenTelemetry enhances observability, making it a
  valuable asset for ensuring the reliability and safety of LLM deployments.
  [Access the source](https://www.trulens.org/) · [Explore the code
  repository](https://github.com/truera/trulens/)

## 5.4 Human-in-the-Loop Supervision

- **Label Studio – *Open-Source Data Labeling and Annotation Tool* (2020)**
  Label Studio is a widely used open-source platform for labeling, annotating,
  and reviewing data—including text, images, and audio. In LLM and agentic
  contexts, it supports workflows for human validation of generated outputs,
  task scoring, and building gold datasets. Label Studio is ideal for building
  supervised training datasets or setting up post-deployment human feedback
  loops.
  [Access the source](https://labelstud.io/) · [Explore the code
  repository](https://github.com/HumanSignal/label-studio)

- **Argilla – *Open-Source Data Curation Platform for LLMs* (2023)**
  Argilla is an open-source platform that enables collaborative
  human-in-the-loop workflows for curating high-quality datasets for NLP and
  LLM applications. It provides a customizable UI and Python SDK to configure
  annotation and feedback loops for tasks like text classification, entity
  recognition, and generative response review. Argilla integrates with popular
  tools such as Hugging Face, spaCy, and OpenAI, and supports both self-hosted
  and Hugging Face Spaces deployment.
  [Explore the code repository](https://github.com/argilla-io/argilla)

- **HumanLoop – *Feedback and Iteration Platform for LLM Applications*
- (2023)**
  HumanLoop enables developers to integrate human feedback into LLM-powered
  workflows. It supports ranking, scoring, and fine-tuning based on user or
  evaluator input. HumanLoop offers interfaces for side-by-side comparisons
  and annotation tasks, helping teams identify weak points and systematically
  improve agent behavior in production.
  [Access the source](https://www.humanloop.com/) · [Explore the code
  repository](https://github.com/humanloop)

## 5.5 Alignment and Feedback Learning

- **Exploding Gradients – *Nemesis: A Reward Model Framework for LLMs*
- (2024)**
  Nemesis is an open-source framework for training reward models for
  reinforcement learning with human feedback (RLHF). It supports datasets such
  as HellaSwag, HH-RLHF, and ELI5, and provides tools for reward function
  training, validation, and integration into downstream fine-tuning or agent
  pipelines. Built on PyTorch and Hugging Face, Nemesis simplifies the RLHF
  loop for scalable, reproducible experimentation.
  [Explore the code repository](https://github.com/explodinggradients/nemesis)
