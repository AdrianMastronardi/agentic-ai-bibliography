---
layout: default
title: "2. Architectures and System Design"
---

Agentic systems are more than just prompts or wrappers. They are structured
entities that perceive, reason, plan, and act. This section gathers key
resources that explore how to design agent architectures: from reasoning loops
and memory to multi-agent coordination, planning, and tool integration. These
works bridge theory and implementation, offering blueprints for building
intelligent, autonomous behavior.

## 2.1 Reasoning and Action Patterns

- **Shunyu Yao et al. – *ReAct: Synergizing Reasoning and Acting in Language
- Models* (2022)**
  A widely influential paper introducing a simple but powerful approach to
  agent behavior: combining verbal reasoning with action execution. The ReAct
  pattern lets agents “think out loud” while taking tool-augmented steps,
  improving performance on decision-making tasks. This paper laid the
  foundation for many modern agent frameworks · .
  [Read the full paper from this repo](../papers/yao-2022.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2210.03629) · [Read the
  full paper from the source](https://arxiv.org/abs/2210.03629)

- **Wang et al. – *Self-Consistency Improves Chain of Thought Reasoning in
- Large Language Models* (2022)**
  Building on Chain-of-Thought prompting, this paper proposes
  Self-Consistency: a decoding strategy that samples multiple reasoning paths
  and selects the most consistent final answer. Rather than relying on a
  single greedy output, the model explores diverse chains of reasoning and
  chooses the dominant conclusion. This approach boosts accuracy across
  several reasoning benchmarks and anticipates agentic behaviors like
  self-reflection, verification, and ensemble thought.
  [Read the full paper from this repo](../papers/wang-2022.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2203.11171) · [Read the
  full paper from the source](https://arxiv.org/abs/2203.11171)

- **Wei et al. – *Chain-of-Thought Prompting Elicits Reasoning in Large
- Language Models* (2022)**
  This foundational paper introduces Chain-of-Thought (CoT) prompting: a
  simple technique where models are guided to reason through problems
  step-by-step by including intermediate reasoning steps in the prompt. CoT
  significantly improves performance on arithmetic, commonsense, and symbolic
  reasoning tasks—especially in larger models like PaLM. The paper laid the
  groundwork for later developments like ReAct and Reflexion, and reframed
  prompting as a tool for inducing emergent reasoning.
  [Read the full paper from this repo](../papers/wei-2022.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2201.11903) · [Read the
  full paper from the source](https://arxiv.org/abs/2201.11903)

- **Schick et al. – *Toolformer: Language Models Can Teach Themselves to Use
- Tools* (2023)**
  Toolformer presents a method by which a language model can autonomously
  learn to use external tools—such as search engines, calculators, or
  translation APIs—through self-supervised data generation. Rather than
  relying on human annotation or fine-tuning, the model decides when and how
  to call tools during text generation. Toolformer laid foundational ideas for
  autonomous tool use and remains a key reference in the evolution of agent
  capabilities.
  [Read the full paper from this repo](../papers/schick-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2302.04761) · [Read the
  full paper from the source](https://arxiv.org/abs/2302.04761)

- **Shunyu Yao et al. – *Tree of Thoughts: Deliberate Problem Solving with
- Large Language Models* (2023)**
  Tree of Thoughts (ToT) introduces a novel inference framework that enables
  language models to perform deliberate reasoning by exploring multiple
  reasoning paths and evaluating intermediate steps ("thoughts"). This
  approach generalizes the Chain-of-Thought prompting by structuring the
  reasoning process as a tree, allowing for backtracking and strategic
  planning. ToT significantly enhances problem-solving capabilities in tasks
  requiring complex reasoning.  ·
  [Read the full paper from this repo](../papers/yao-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2305.10601) · [Explore the
  code repository](https://github.com/princeton-nlp/tree-of-thought-llm) ·
  [Read the full paper from the source](https://arxiv.org/abs/2305.10601)

## 2.2 Multi-Agent Architectures

- **Michael Wooldridge & Nicholas R. Jennings – *Intelligent Agents: Theory
- and Practice* (1995)**
  This foundational paper defines key properties of intelligent
  agents—autonomy, reactivity, proactiveness, and social ability—and
  introduces architectural classifications (reactive, deliberative, hybrid).
  It establishes a formal language for understanding agent behavior and sets
  the stage for multi-agent system design. Though predating LLMs, many of its
  insights remain relevant for designing collaborative, goal-directed systems.
  .
  [Read the full paper from this repo](../papers/wooldridge-1995.pdf)

- **Gerhard Weiss (ed.), with contributions from Michael Wooldridge et al. –
- *Multiagent Systems: A Modern Approach to Distributed Artificial
- Intelligence* (2001)**
  This edited volume offers a comprehensive overview of multi-agent system
  theory, including architectures, coordination, negotiation, and distributed
  problem solving. A classic in the field, it provides deep theoretical
  foundations that continue to inform contemporary agent-based system
  design—even in the age of LLM-powered agents. [This is a recommended
  extended reference; no online version is redistributed here].

- **Qingyun Wu et al. – *AutoGen: Enabling Next-Gen LLM Applications via
- Multi-Agent Conversation* (2023)**
  AutoGen is an open-source framework that allows developers to build LLM
  applications via multiple agents that can converse with each other to
  accomplish tasks. AutoGen agents are customizable, conversable, and can
  operate in various modes that employ combinations of LLMs, human inputs, and
  tools. Using AutoGen, developers can also flexibly define agent interaction
  behaviors. Both natural language and computer code can be used to program
  flexible conversation patterns for different applications. AutoGen serves as
  a generic infrastructure to build diverse applications of various
  complexities and LLM capacities. Empirical studies demonstrate the
  effectiveness of the framework in many example applications, with domains
  ranging from mathematics, coding, question answering, operations research,
  online decision-making, entertainment, etc.
  [Read the full paper from this repo](../papers/wu-2023.pdf) · [Read the full
  paper from the source](https://arxiv.org/abs/2308.08155) · [Read the full
  paper from the source](https://arxiv.org/abs/2308.08155)

- **Shen et al. – *HuggingGPT: Solving AI Tasks with ChatGPT and Hugging Face
- Tools* (2023)**
  HuggingGPT proposes a planner-executor architecture in which a central LLM
  (ChatGPT) interprets user intent, plans task execution, and delegates
  subtasks to expert models (e.g., for text, vision, or audio) hosted on
  Hugging Face. It formalizes a task-routing agent design with components for
  task planning, model selection, execution, and response generation.
  HuggingGPT is an important early example of agentic orchestration across
  multiple modalities and tools.
  [Read the full paper from this repo](../papers/shen-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2303.17580) · [Read the
  full paper from the source](https://arxiv.org/abs/2303.17580)

- **Xie et al. – *OpenAgents: An Open Platform for Language Agents in the
- Wild* (2023)**
  OpenAgents is an open-source platform designed to deploy and study language
  agents in real-world settings. It introduces three specialized agents: (1)
  Data Agent for data analysis using Python/SQL and data tools; (2) Plugins
  Agent integrating over 200 daily-use APIs; and (3) Web Agent for autonomous
  web browsing. The platform emphasizes accessibility for non-expert users
  through a web interface optimized for swift responses and common failures,
  while providing developers and researchers with a seamless deployment
  experience on local setups. OpenAgents aims to facilitate the development of
  innovative language agents and support real-world evaluations.
  [Read the full paper from this repo](../papers/xie-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2310.10634) · [Read the
  full paper from the source](https://arxiv.org/abs/2310.10634)

- **CrewAI – *Composable Multi-Agent Framework for Task-Specific
- Collaboration* (2024)**
  CrewAI is an open-source Python framework for building multi-agent systems
  composed of specialized agents assigned to roles and responsibilities.
  Inspired by real-world workflows, it introduces concepts like task
  delegation, crew orchestration, memory sharing, and agent-to-agent
  messaging. Though still evolving, CrewAI reflects an important design
  philosophy: modeling agent collaboration with explicit structure and
  human-like coordination patterns.
  [Explore the code repository](https://github.com/crewAIInc/crewAI)

## 2.3 Agent Frameworks and Control Flows

- **Harrison Chase – *LangGraph: State Machine Framework for LLM Agents*
- (2024)**
  LangGraph introduces a novel framework for building agentic workflows using
  state machines. It enables developers to define execution paths with
  branching, looping, memory, and failure handling—all in a structured and
  observable way. Built on top of LangChain, LangGraph emphasizes reliability,
  modularity, and production-readiness. It is especially suited for
  orchestrating complex multi-step tasks in real-world applications.
  [Explore the code repository](https://github.com/langchain-ai/langgraph)

## 2.4 Structured Programming and Optimization

- **Omar Khattab et al. – *DSPy: Compiling Declarative Language Model Calls
- into Self-Improving Pipelines* (2023)**
  DSPy introduces a programming model that abstracts language model pipelines
  as text transformation graphs, where LMs are invoked through declarative
  modules. These modules are parameterized, allowing them to learn how to
  apply compositions of prompting, fine-tuning, augmentation, and reasoning
  techniques. DSPy includes a compiler that optimizes any pipeline to maximize
  a given metric, enabling the development of sophisticated LM pipelines that
  reason about tasks like math word problems and multi-hop retrieval. . .
  [Read the full paper from this repo](../papers/khattab-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2310.03714) · [Read the
  full paper from the source](https://arxiv.org/abs/2310.03714)

- **Dilara Soylu et al. – *Fine-Tuning and Prompt Optimization: Two Great
- Steps that Work Better Together* (2024)**
  This paper explores strategies to optimize both the module-level language
  model weights and the associated prompt templates in modular NLP pipelines.
  The authors propose alternating between fine-tuning and prompt optimization
  to enhance performance in multi-stage language model programs. Experiments
  on tasks like multi-hop QA and mathematical reasoning demonstrate that
  combining these strategies outperforms using either alone.
  [Read the full paper from this repo](../papers/soylu-2024.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2407.10930) · [Read the
  full paper from the source](https://arxiv.org/abs/2407.10930)

- **Opsahl-Ong et al. – *Optimizing Instructions and Demonstrations for
- Multi-Stage Language Model Programs* (2024)**
  This paper presents MIPRO, a novel optimizer designed to enhance the
  performance of complex, multi-stage language model (LM) pipelines. By
  optimizing task-specific instructions and demonstrations across stages,
  MIPRO supports more modular and composable architectures—an essential trait
  for building reliable agents. The authors demonstrate that MIPRO outperforms
  baseline optimizers on five of seven diverse LM programs using a
  best-in-class open-source model (Llama-3-8B), achieving up to 13% accuracy
  improvement.
  [Read the full paper from this repo](../papers/opsahl-ong-2024.pdf) · [Read
  the full paper from the source](https://arxiv.org/abs/2406.11695) · [Read
  the full paper from the source](https://arxiv.org/abs/2406.11695)

## 2.5 Architectural Innovations for Memory and Context

- **Aydar Bulatov et al. – *Recurrent Memory Transformer* (2022)**
  The Recurrent Memory Transformer (RMT) augments the standard Transformer
  architecture with a segment-level recurrent memory mechanism. By introducing
  special memory tokens, RMT enables the model to store and process both local
  and global information across long sequences, effectively capturing
  long-term dependencies without altering the core Transformer structure. This
  design improves performance on tasks requiring extended context processing.
  [Read the full paper from this repo](../papers/bulatov-2022.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2207.06881) · [Read the
  full paper from the source](https://arxiv.org/abs/2207.06881)
