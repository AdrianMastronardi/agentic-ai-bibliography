# 4. Tools and Frameworks

Building agentic systems requires more than prompting — it demands structured
frameworks that manage planning, memory, tool use, interaction, and error
handling. This section curates open-source libraries and platforms that enable
the development, orchestration, and experimentation of LLM-based agents in the
real world.

## 4.1 Agent Orchestration Frameworks

- **AutoGen – *Framework for Multi-Agent LLM Applications* (2023)**
  Developed by Microsoft Research, AutoGen is an open-source framework that
  streamlines the creation of multi-agent applications using LLMs. It allows
  developers to define agents with specific roles and behaviors, facilitating
  conversations between agents to accomplish tasks. AutoGen supports
  integration with tools, human inputs, and various LLMs, providing a flexible
  infrastructure for building complex AI applications.
  [Access the source](https://microsoft.github.io/autogen/0.2/)

- **CrewAI – *Framework for Orchestrating Role-Playing Agents* (2023)**
  CrewAI is a Python-based framework designed to simplify the development of
  multi-agent systems. It enables the definition of agents with distinct
  roles, goals, and behaviors, allowing them to collaborate on tasks. CrewAI's
  architecture supports the creation of structured workflows where agents can
  interact, share information, and make decisions collectively.
  [Explore the code repository](https://github.com/crewAIInc/crewAI)

- **Hong et al. – *MetaGPT: Meta Programming for A Multi-Agent Collaborative
- Framework* (2023)**
  MetaGPT is a multi-agent framework that simulates a software development
  team by assigning distinct roles—such as product manager, architect, and
  engineer—to AI agents. By encoding Standard Operating Procedures (SOPs) into
  prompt sequences, MetaGPT enables agents to collaborate effectively,
  breaking down complex tasks into manageable subtasks. This structured
  approach enhances coherence and reduces errors in generated outputs,
  demonstrating improved performance in collaborative software engineering
  benchmarks.  ·
  [Read the full paper from this repo](../papers/hong-2023.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2308.00352) · [Explore the
  code repository](https://github.com/FoundationAgents/MetaGPT) · [Read the
  full paper from the source](https://arxiv.org/abs/2308.00352)

- **LangGraph – *Runtime for Agentic Workflows* (2023)**
  LangGraph is a runtime framework built atop LangChain, focusing on the
  orchestration of agentic workflows. It enables the construction of dynamic
  computation graphs where nodes represent agents or tools, and edges define
  the flow of information. LangGraph supports features like human-in-the-loop
  interactions, state management, and parallel execution, facilitating the
  development of complex, multi-agent systems.
  [Explore the code repository](https://github.com/langchain-ai/langgraph)

- **Microsoft – *Semantic Kernel: Open-Source SDK for AI Integration* (2023)**
  Semantic Kernel is an open-source SDK developed by Microsoft that
  facilitates the integration of AI services, such as OpenAI and Azure OpenAI,
  with conventional programming languages like C#, Python, and Java. It
  provides abstractions for prompt templating, function chaining, and memory
  management, enabling developers to build AI applications that combine
  natural language capabilities with traditional code. Semantic Kernel
  supports the creation of plugins and planners, allowing for the
  orchestration of complex workflows and multi-agent systems.
  [Access the
  source](https://learn.microsoft.com/en-us/dotnet/ai/semantic-kernel-dotnet-overview)
  · [Explore the code
  repository](https://github.com/microsoft/semantic-kernel)

- **AutoGen Studio – *No-Code Interface for Multi-Agent Systems* (2024)**
  AutoGen Studio is a visual development environment built on the AutoGen
  framework, enabling users to prototype, debug, and evaluate multi-agent
  workflows without extensive coding. It offers a drag-and-drop interface for
  composing agents, defining workflows, and monitoring interactions,
  streamlining the development of complex AI systems.
  [Access the
  source](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)

## 4.2 Application-Level Agent Frameworks

- **Devika – *Agentic AI Software Engineer* (2023)**
  Devika is an open-source AI agent designed to function as a software
  engineer. It interprets high-level human instructions, decomposes them into
  actionable steps, conducts research, and writes code to fulfill specified
  objectives. Devika leverages LLMs, planning algorithms, and web browsing
  capabilities to autonomously handle software development tasks.
  [Explore the code repository](https://github.com/stitionai/devika)

## 4.3 Prompt and Programmatic Control

- **DSPy – *Declarative Self-Improving Python* (2023)**
  DSPy is an open-source framework from Stanford University that reimagines
  the development of LLM applications through declarative programming. Instead
  of crafting prompts manually, developers define tasks and metrics, and DSPy
  compiles these specifications into optimized prompts and model
  configurations. This approach facilitates the creation of modular,
  self-improving AI systems.
  [Explore the code repository](https://github.com/stanfordnlp/dspy)

- **Guidance – *Framework for Structured LLM Generation* (2023)**
  Guidance is a framework that offers fine-grained control over LLM outputs by
  combining templating with programmatic logic. It allows developers to
  enforce output structures, integrate conditionals and loops, and interleave
  generation with tool usage. This structured approach enhances the
  reliability and consistency of LLM-generated content.
  [Explore the code repository](https://github.com/guidance-ai/guidance)

- **PromptTools – *Open-Source Framework for Prompt Testing and Evaluation*
- (2023)**
  PromptTools provides an interactive framework for evaluating, comparing, and
  managing prompts across different LLMs. It supports side-by-side
  comparisons, regression testing, and metric-based evaluation, with both CLI
  and visual interfaces. By enabling structured experimentation with prompts
  and model configurations, PromptTools helps teams improve reliability and
  consistency in agentic workflows. It’s especially useful for A/B testing,
  failure analysis, and systematic refinement of prompt strategies.
  [Explore the code repository](https://github.com/hegelai/prompttools)

## 4.4 Data & Memory Integration

- **LangChain – *Framework for Building LLM-Powered Applications* (2023)**
  LangChain is an open-source framework designed to simplify the development
  of applications powered by large language models (LLMs). It provides a
  modular approach to connect LLMs with external data sources, tools, and
  APIs, enabling the creation of context-aware and dynamic applications.
  LangChain's architecture supports the chaining of components, allowing
  developers to build complex workflows that integrate memory,
  decision-making, and tool usage.
  [Explore the code repository](https://github.com/langchain-ai/langchain)

- **LlamaIndex – *Data Framework for LLM Applications* (2023)**
  LlamaIndex is an open-source data framework designed to bridge the gap
  between large language models (LLMs) and private or domain-specific data. It
  provides tools for data ingestion, indexing, and querying, enabling LLMs to
  access and interpret custom data sources such as PDFs, databases, and APIs.
  LlamaIndex supports context augmentation techniques like Retrieval-Augmented
  Generation (RAG), facilitating the development of applications like
  question-answering systems, chatbots, and autonomous agents.
  [Access the source](https://www.llamaindex.ai/framework)

## 4.5 Training and Fine-Tuning Utilities

- **Exploding Gradients – *Funtuner: Supervised Instruction Fine-Tuning
- Framework for LLMs* (2024)**
  Funtuner is a lightweight, scalable framework for supervised fine-tuning of
  LLMs using Hugging Face Trainer and DeepSpeed. It supports LoRA, 8-bit
  quantization, sequence bucketing, and reproducibility features, making it
  suitable for instruction-tuned pipelines, adapter training, or prototyping
  of domain-specific models.
  [Explore the code
  repository](https://github.com/explodinggradients/Funtuner)
