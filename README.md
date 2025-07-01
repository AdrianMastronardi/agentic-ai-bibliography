# Agentic AI Bibliography

**Agentic AI** —the design and deployment of systems capable of autonomous reasoning, decision-making, and coordinated action— is quickly emerging as one of the most transformative frontiers in artificial intelligence. From multi-agent collaboration to tool-using LLMs, from workflow orchestration to memory and planning strategies, the “agent” paradigm is reshaping how we build intelligent systems.

Yet, as excitement grows, so does confusion. A flood of tutorials, demos, and hype-driven posts often oversimplify complex ideas, reduce architecture to boilerplate, and blur the line between experimentation and production-ready design. Worse, some teams may take a "just follow this YouTube video" approach to building agents—without the depth, structure, or critical thinking that real-world implementation demands.

This **Agentic AI Bibliography** aims to provide a grounded, evolving reference point. It is not a traditional bibliography. It includes academic papers, books, videos, open-source tools, industry use cases, evaluation benchmarks, design patterns, and conceptual texts. It is meant for:

- **Engineers** building agentic systems in production.
- **Researchers and architects** exploring multi-agent design, reasoning loops, and planning.
- **Product and innovation teams** wanting to separate signal from noise in a rapidly shifting landscape.
- **Anyone** seeking to understand what it really takes to build AI systems that reason, act, and collaborate.

This is not a finished product. It is a living document—and an invitation. Contributions, critiques, and suggestions are welcome. Let’s raise the floor of what we consider best practice, and collectively build a foundation that goes beyond shortcuts.

> 📌 **Format Note**  
> Each entry in this bibliography follows a consistent format: a brief summary followed by inline links to internal and external resources (if available).  
> - The structure is: **Author(s) – *Title* (Year)**, then a 3–5 line abstract, followed by links.  
> - Entries are grouped thematically by section and **ordered chronologically (ascending by year)**. When multiple entries share the same year, they are ordered alphabetically by the last name of the first author.
> - All summaries are written in English, with a neutral and informative tone.  
> - Books, papers, tools, and videos are all valid resources if they contribute meaningfully to the understanding or implementation of Agentic AI.

## 1. Foundational Concepts

To build truly agentic systems, we must revisit the early visions that treated the computer not just as a tool, but as a thinking partner. These foundational texts shaped the original dream of human-computer symbiosis.

- **Vannevar Bush – *As We May Think* (1945)**
  A prophetic essay written at the end of World War II, envisioning a machine—the “Memex”—that would extend human memory and association through technology. Bush’s vision laid the conceptual groundwork for hypertext, digital knowledge systems, and ultimately the notion of interactive intelligence augmentation. A foundational text for understanding AI not as replacement, but as partnership. [Read the full paper from this repo](./papers/bush-as-we-may-think.pdf). [Read the full paper from the source](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/).

- **J.C.R. Licklider – *Man-Computer Symbiosis* (1960)**
  A visionary essay that imagines a future where humans and computers collaborate closely, each doing what they do best. Licklider argues that progress in computing would come not from automation, but from symbiosis—interactive systems that augment human thought. [Read the full paper from this repo](./papers/licklider-man-computer-symbiosis.pdf). [Read the full paper from the source](https://openlib.org/home/krichel/courses/lis654/readings/licklider60_man_comput_symbios.pdf).

- **Marvin Minsky – *Steps Toward Artificial Intelligence* (1961)**
  This seminal paper lays out a roadmap for modeling intelligent behavior computationally. Minsky surveys early methods for learning, planning, memory, and self-modifying programs, proposing building blocks for general intelligence. Many of these concepts—such as task decomposition, partial solutions, and cognitive architecture—still resonate in modern agent systems. A foundational text for thinking about how machines might reason, act, and adapt.

- **Douglas Engelbart – *Augmenting Human Intellect* (1962)**
  A foundational report proposing the use of computers to amplify human intelligence. Engelbart lays out principles that would later lead to the invention of the mouse, hypertext, and interactive computing. Essential reading to understand the original ethos behind building systems that empower human agency. [Read the full paper from this repo](./papers/engelbart-augmenting-human-intellect.pdf). [Read the full paper from the source](https://www.dougengelbart.org/pubs/papers/scanned/Doug_Engelbart-AugmentingHumanIntellect.pdf).

- **Allen Newell & Herbert A. Simon – *Human Problem Solving* (1972)**
  This landmark book presents a theory of cognition grounded in problem-solving processes, search in problem spaces, and production systems. It formalizes the idea that intelligent behavior emerges from reasoning over symbolic representations and heuristics. The authors’ models inspired entire generations of agent architectures, from symbolic AI to modern deliberative frameworks. While predating neural models, its conceptual rigor remains crucial for understanding goal-driven agency.

- **Don Norman – *The Design of Future Things* (2007)**
  A seminal exploration of how intelligent systems should interact with humans—not through control, but through communication and understanding. Norman anticipates the challenges of designing proactive, semi-autonomous technologies, emphasizing the importance of feedback, transparency, and the psychology of interaction. A must-read for thinking about AI agents not just as tools, but as social actors.

- **Sherry Turkle – *Alone Together* (2011)**
  A sociological and psychological exploration of how digital agents reshape our sense of intimacy and self. Turkle raises critical questions about emotional delegation to machines and warns against the illusion of companionship without relationship. Essential for thinking critically about agents as social actors, not just functional tools.

- **Joon Sung Park, Joseph O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein – *Generative Agents: Interactive Simulacra of Human Behavior* (2023)**
  A groundbreaking study in which generative agents—powered by LLMs—simulate believable human behavior in an interactive sandbox world. This work bridges human-computer interaction, cognitive simulation, and agent design, offering deep insight into how artificial agents might exhibit memory, planning, and social dynamics. A must-read for understanding the expressive and interactive potential of agentic systems. [Read the full paper from this repo](./papers/park-generative-agents.pdf). [Read the full paper from the source](https://arxiv.org/abs/2304.03442).

- **Fei-Fei Li – *The Worlds I See* (2024)**
  A personal and reflective account of Fei-Fei Li’s journey as a scientist and AI leader. While not a technical manual, this book offers a powerful vision of Human-Centered AI—framing intelligence not just as a computational challenge, but as a profoundly human endeavor. Recommended for those seeking to ground Agentic AI systems in ethical, emotional, and societal context.

## 2. Architectures and System Design

Agentic systems are more than just prompts or wrappers. They are structured entities that perceive, reason, plan, and act. This section gathers key resources that explore how to design agent architectures: from reasoning loops and memory to multi-agent coordination, planning, and tool integration. These works bridge theory and implementation, offering blueprints for building intelligent, autonomous behavior.

### 2.1 Reasoning and Action Patterns

- **Wang et al. – *Self-Consistency Improves Chain of Thought Reasoning in Large Language Models* (2022)**
  Building on Chain-of-Thought prompting, this paper proposes Self-Consistency: a decoding strategy that samples multiple reasoning paths and selects the most consistent final answer. Rather than relying on a single greedy output, the model explores diverse chains of reasoning and chooses the dominant conclusion. This approach boosts accuracy across several reasoning benchmarks and anticipates agentic behaviors like self-reflection, verification, and ensemble thought. [Read the full paper from this repo](./papers/wang-self-consistency.pdf). [Read the full paper from the source](https://arxiv.org/abs/2203.11171).

- **Wei et al. – *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2022)**
  This foundational paper introduces Chain-of-Thought (CoT) prompting: a simple technique where models are guided to reason through problems step-by-step by including intermediate reasoning steps in the prompt. CoT significantly improves performance on arithmetic, commonsense, and symbolic reasoning tasks—especially in larger models like PaLM. The paper laid the groundwork for later developments like ReAct and Reflexion, and reframed prompting as a tool for inducing emergent reasoning. [Read the full paper from this repo](./papers/wei-chain-of-thought.pdf). [Read the full paper from the source](https://arxiv.org/abs/2201.11903).

- **Shunyu Yao et al. – *ReAct: Synergizing Reasoning and Acting in Language Models* (2022)**
  A widely influential paper introducing a simple but powerful approach to agent behavior: combining verbal reasoning with action execution. The ReAct pattern lets agents “think out loud” while taking tool-augmented steps, improving performance on decision-making tasks. This paper laid the foundation for many modern agent frameworks. [Read the full paper from this repo](./papers/yao-react.pdf). [Read the full paper from the source](https://arxiv.org/abs/2210.03629).

- **Shunyu Yao et al. – *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (2023)**
  Tree of Thoughts (ToT) introduces a novel inference framework that enables language models to perform deliberate reasoning by exploring multiple reasoning paths and evaluating intermediate steps ("thoughts"). This approach generalizes the Chain-of-Thought prompting by structuring the reasoning process as a tree, allowing for backtracking and strategic planning. ToT significantly enhances problem-solving capabilities in tasks requiring complex reasoning. [Read the full paper from this repo](./papers/yao-tree-of-thoughts.pdf). [Read the full paper from the source](https://arxiv.org/abs/2305.10601). [Explore the Tree of Thought repository](https://github.com/princeton-nlp/tree-of-thought-llm).

- **Schick et al. – *Toolformer: Language Models Can Teach Themselves to Use Tools* (2023)**
  Toolformer presents a method by which a language model can autonomously learn to use external tools—such as search engines, calculators, or translation APIs—through self-supervised data generation. Rather than relying on human annotation or fine-tuning, the model decides when and how to call tools during text generation. Toolformer laid foundational ideas for autonomous tool use and remains a key reference in the evolution of agent capabilities. [Read the full paper from this repo](./papers/schick-toolformer.pdf). [Read the full paper from the source](https://arxiv.org/abs/2302.04761).

### 2.2 Multi-Agent Architectures

- **Michael Wooldridge & Nicholas R. Jennings – *Intelligent Agents: Theory and Practice* (1995)**
  This foundational paper defines key properties of intelligent agents—autonomy, reactivity, proactiveness, and social ability—and introduces architectural classifications (reactive, deliberative, hybrid). It establishes a formal language for understanding agent behavior and sets the stage for multi-agent system design. Though predating LLMs, many of its insights remain relevant for designing collaborative, goal-directed systems. [Read the full paper from this repo](./papers/wooldridge-jennings-intelligent-agents.pdf).

- **Gerhard Weiss (ed.), with contributions from Michael Wooldridge et al. – *Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence* (2001)**  
  This edited volume offers a comprehensive overview of multi-agent system theory, including architectures, coordination, negotiation, and distributed problem solving. A classic in the field, it provides deep theoretical foundations that continue to inform contemporary agent-based system design—even in the age of LLM-powered agents. [This is a recommended extended reference; no online version is redistributed here].

- **Qingyun Wu et al. – *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (2023)**
  AutoGen is an open-source framework that allows developers to build LLM applications via multiple agents that can converse with each other to accomplish tasks. AutoGen agents are customizable, conversable, and can operate in various modes that employ combinations of LLMs, human inputs, and tools. Using AutoGen, developers can also flexibly define agent interaction behaviors. Both natural language and computer code can be used to program flexible conversation patterns for different applications. AutoGen serves as a generic infrastructure to build diverse applications of various complexities and LLM capacities. Empirical studies demonstrate the effectiveness of the framework in many example applications, with domains ranging from mathematics, coding, question answering, operations research, online decision-making, entertainment, etc. [Read the full paper from this repo](./papers/qingyun-autogen-multi-agent-conversation.pdf). [Read the full paper from the source](https://arxiv.org/abs/2308.08155).

- **Shen et al. – *HuggingGPT: Solving AI Tasks with ChatGPT and Hugging Face Tools* (2023)**
  HuggingGPT proposes a planner-executor architecture in which a central LLM (ChatGPT) interprets user intent, plans task execution, and delegates subtasks to expert models (e.g., for text, vision, or audio) hosted on Hugging Face. It formalizes a task-routing agent design with components for task planning, model selection, execution, and response generation. HuggingGPT is an important early example of agentic orchestration across multiple modalities and tools. [Read the full paper from this repo](./papers/shen-hugginggpt.pdf). [Read the full paper from the source](https://arxiv.org/abs/2303.17580).

- **Xie et al. – *OpenAgents: An Open Platform for Language Agents in the Wild* (2023)**
  OpenAgents is an open-source platform designed to deploy and study language agents in real-world settings. It introduces three specialized agents: (1) Data Agent for data analysis using Python/SQL and data tools; (2) Plugins Agent integrating over 200 daily-use APIs; and (3) Web Agent for autonomous web browsing. The platform emphasizes accessibility for non-expert users through a web interface optimized for swift responses and common failures, while providing developers and researchers with a seamless deployment experience on local setups. OpenAgents aims to facilitate the development of innovative language agents and support real-world evaluations. [Read the full paper from this repo](./papers/xie-openagents.pdf). [Read the full paper from the source](https://arxiv.org/abs/2310.10634).

- **CrewAI – *Composable Multi-Agent Framework for Task-Specific Collaboration* (2024)**
  CrewAI is an open-source Python framework for building multi-agent systems composed of specialized agents assigned to roles and responsibilities. Inspired by real-world workflows, it introduces concepts like task delegation, crew orchestration, memory sharing, and agent-to-agent messaging. Though still evolving, CrewAI reflects an important design philosophy: modeling agent collaboration with explicit structure and human-like coordination patterns. [Read the full documentation from the source](https://github.com/crewAIInc/crewAI).

### 2.3 Agent Frameworks and Control Flows

- **Harrison Chase – *LangChain: Framework for Developing Applications with LLMs* (2023–2024)**
  LangChain provides a modular framework for building applications powered by large language models. It offers abstractions for chains, memory, agents, tools, and retrievers—making it a foundational platform for designing agentic behaviors. While originally focused on chaining prompts, LangChain has expanded to support complex, multi-agent systems and now serves as the base layer for more structured orchestration frameworks like LangGraph. [Read the full documentation from the source](https://github.com/langchain-ai/langchain).

- **Harrison Chase – *LangGraph: State Machine Framework for LLM Agents* (2024)**
  LangGraph introduces a novel framework for building agentic workflows using state machines. It enables developers to define execution paths with branching, looping, memory, and failure handling—all in a structured and observable way. Built on top of LangChain, LangGraph emphasizes reliability, modularity, and production-readiness. It is especially suited for orchestrating complex multi-step tasks in real-world applications. [Read the full paper from the source](https://github.com/langchain-ai/langgraph).

### 2.4 Structured Programming and Optimization

  - **Omar Khattab et al. – *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines* (2023)**
  DSPy introduces a programming model that abstracts language model pipelines as text transformation graphs, where LMs are invoked through declarative modules. These modules are parameterized, allowing them to learn how to apply compositions of prompting, fine-tuning, augmentation, and reasoning techniques. DSPy includes a compiler that optimizes any pipeline to maximize a given metric, enabling the development of sophisticated LM pipelines that reason about tasks like math word problems and multi-hop retrieval. [Read the full paper from this repo](./papers/khattab-dspy.pdf). [Read the full paper from the source](https://arxiv.org/abs/2310.03714).

- **Opsahl-Ong et al. – *Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs* (2024)**
  This paper presents MIPRO, a novel optimizer designed to enhance the performance of complex, multi-stage language model (LM) pipelines. By optimizing task-specific instructions and demonstrations across stages, MIPRO supports more modular and composable architectures—an essential trait for building reliable agents. The authors demonstrate that MIPRO outperforms baseline optimizers on five of seven diverse LM programs using a best-in-class open-source model (Llama-3-8B), achieving up to 13% accuracy improvement. [Read the full paper from this repo](./papers/opsahlong-dspy-multistage.pdf). [Read the full paper from the source](https://arxiv.org/abs/2406.11695).

- **Dilara Soylu et al. – *Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together* (2024)**
  This paper explores strategies to optimize both the module-level language model weights and the associated prompt templates in modular NLP pipelines. The authors propose alternating between fine-tuning and prompt optimization to enhance performance in multi-stage language model programs. Experiments on tasks like multi-hop QA and mathematical reasoning demonstrate that combining these strategies outperforms using either alone. [Read the full paper from this repo](./papers/soylu-dspy-ft-po.pdf). [Read the full paper from the source](https://arxiv.org/abs/2407.10930).

### 2.5 Architectural Innovations for Memory and Context

- **Aydar Bulatov et al. – *Recurrent Memory Transformer* (2022)**
  The Recurrent Memory Transformer (RMT) augments the standard Transformer architecture with a segment-level recurrent memory mechanism. By introducing special memory tokens, RMT enables the model to store and process both local and global information across long sequences, effectively capturing long-term dependencies without altering the core Transformer structure. This design improves performance on tasks requiring extended context processing. [Read the full paper from this repo](./papers/bulatov-recurrent-memory-transformer.pdf). [Read the full paper from the source](https://arxiv.org/abs/2207.06881).

## 3. Evaluation and Benchmarks

Designing agentic systems is only half the challenge—understanding how to evaluate them is just as critical. Agents are not static models: they act, reflect, and interact. This section gathers proposals that go beyond raw accuracy to assess qualities like autonomy, tool use, reasoning, collaboration, and decision cycles. From benchmark suites to reflective loops, these works help define what “good” means in Agentic AI.

- **Parisi et al. – *TALM: Tool Augmented Language Models* (2022)**
  TALM presents a framework that augments language models with external tools to enhance their capabilities in tasks requiring access to dynamic or private data. By integrating non-differentiable tools and employing an iterative "self-play" technique, TALM enables models to perform tasks beyond their training data, such as knowledge-intensive question answering and mathematical reasoning. This approach demonstrates that tool augmentation can significantly improve performance without solely relying on model scale, highlighting a promising direction for enriching language model functionalities. [Read the full paper from this repo](./papers/parisi-talm.pdf). [Read the full paper from the source](https://arxiv.org/abs/2205.12255).

- **Mialon et al. – *GAIA: A Benchmark for General AI Assistants* (2023)**
  GAIA is a benchmark designed to evaluate the capabilities of general-purpose AI assistants across realistic, goal-oriented tasks. It includes 466 human-posed questions that require multimodal reasoning, web navigation, tool use, and access to real-world information. Unlike abstract logic puzzles, GAIA focuses on conceptually simple but practically grounded tasks, revealing large performance gaps between humans and state-of-the-art models like GPT-4. The benchmark highlights the limitations of current LLM-based agents in autonomy, planning, and external integration. [Read the full paper from this repo](./papers/mialon-gaia.pdf). [Read the full paper from the source](https://arxiv.org/abs/2311.12983).

- **Liu et al. – *AgentBench: Evaluating LLMs as Agents* (2023)**
  AgentBench is a standardized benchmark suite designed to evaluate foundation models acting as autonomous agents across a range of tasks: web navigation, tool use, decision-making, and embodied interaction. It defines task formats, input-output schemas, and performance metrics aligned with real-world applications. By supporting both LLM-only and tool-augmented agents, AgentBench provides a unified framework for comparing agentic capabilities across platforms. [Read the full paper from this repo](./papers/liu-agentbench.pdf). [Read the full paper from the source](https://arxiv.org/abs/2308.11458).

- **Liu et al. – *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society* (2023)**  
  CAMEL introduces a multi-agent simulation framework where role-playing language agents interact to solve tasks via structured dialogue. It explores how communication, negotiation, and memory emerge in agent societies. CAMEL is particularly valuable for evaluating the emergent behavior of autonomous agents—highlighting how assigning roles, goals, and interaction rules can lead to successful collaboration. This work anticipates the need to test not just task completion, but social alignment and coordination in agentic systems. [Read the full paper from this repo](./papers/liu-camel.pdf). [Read the full paper from the source](https://arxiv.org/abs/2303.17760). [Explore the CAMEL repository](https://github.com/camel-ai/camel).

- **Shinn et al. – *Reflexion: Language Agents with Verbal Reinforcement Learning* (2023)**
  Reflexion introduces a framework where language agents enhance their performance through self-generated feedback. By converting scalar or binary feedback into natural language reflections, agents can iteratively improve their decision-making across tasks like sequential decision-making, coding, and reasoning. This approach allows agents to learn from their mistakes without the need for external fine-tuning, leveraging the capabilities of large language models for self-improvement. [Read the full paper from this repo](./papers/shinn-reflexion.pdf). [Read the full paper from the source](https://arxiv.org/abs/2303.11366).

- **Wang et al. – *Voyager: An Open-Ended Embodied Agent with Large Language Models* (2023)**
  Voyager is the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. It comprises three key components: (1) an automatic curriculum that maximizes exploration, (2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and (3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. Voyager interacts with GPT-4 via blackbox queries, bypassing the need for model parameter fine-tuning. Empirically, Voyager demonstrates strong in-context lifelong learning capabilities, outperforming prior state-of-the-art methods by obtaining 3.3× more unique items, traveling 2.3× longer distances, and unlocking key tech tree milestones up to 15.3× faster. [Read the full paper from this repo](./papers/wang-voyager.pdf). [Read the full paper from the source](https://arxiv.org/abs/2305.16291).

- **Ye et al. – *FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets* (2023)**
  FLASK introduces a fine-grained evaluation protocol that decomposes coarse-level scoring into skill set-level assessments for each instruction. This approach enhances interpretability by considering the specific skills required for different instructions, providing a more nuanced understanding of model performance. The framework supports both human-based and model-based evaluations, demonstrating high correlation between the two. FLASK's methodology allows for a holistic view of language model capabilities, emphasizing the importance of skill-specific evaluation in aligning models with human values. [Read the full paper from this repo](./papers/ye-flask.pdf). [Read the full paper from the source](https://arxiv.org/abs/2307.10928).

- **Fourney et al. – *AutoGenBench: A Tool for Measuring and Evaluating AutoGen Agents* (2024)**
  AutoGenBench is a standalone command-line tool developed by Microsoft Research for evaluating AutoGen agents and workflows on established LLM and agentic benchmarks. It handles downloading, configuring, running, and reporting results of agents on various public benchmark datasets. AutoGenBench emphasizes three core design principles: repetition, isolation, and instrumentation. Repetition accounts for the stochastic nature of LLMs, isolation ensures that each task runs in a clean environment using Docker containers, and instrumentation provides comprehensive logs for debugging and profiling. This tool is integral for developers aiming to assess and improve the performance of their AutoGen-based applications. [Read the full article from the source](https://microsoft.github.io/autogen/0.2/blog/2024/01/25/AutoGenBench/).

- **Woffinden-Luey & Kiseleva – *AgentEval: A Developer Tool to Assess Utility of LLM-powered Applications* (2024)**
  AgentEval is a framework developed by Microsoft Research to evaluate the utility of applications powered by large language models (LLMs). It introduces a multi-agent evaluation process involving three key components: the CriticAgent, which suggests evaluation criteria based on the application's task; the QuantifierAgent, which quantifies performance against these criteria; and the VerifierAgent, which ensures the robustness and relevance of the evaluation. This structured approach allows developers to assess applications across various dimensions, such as effectiveness, efficiency, and user satisfaction, providing a comprehensive understanding of an application's performance. [Read the full article from the source](https://microsoft.github.io/autogen/0.2/blog/2024/06/21/AgentEval/).

## 4. Tools and Frameworks

Building agentic systems requires more than prompting — it demands structured frameworks that manage planning, memory, tool use, interaction, and error handling. This section curates open-source libraries and platforms that enable the development, orchestration, and experimentation of LLM-based agents in the real world.

- **AutoGen – *Framework for Multi-Agent LLM Applications* (2023)**
  Developed by Microsoft Research, AutoGen is an open-source framework that streamlines the creation of multi-agent applications using LLMs. It allows developers to define agents with specific roles and behaviors, facilitating conversations between agents to accomplish tasks. AutoGen supports integration with tools, human inputs, and various LLMs, providing a flexible infrastructure for building complex AI applications. [Learn more about AutoGen](https://microsoft.github.io/autogen/0.2/).

- **CrewAI – *Framework for Orchestrating Role-Playing Agents* (2023)**
  CrewAI is a Python-based framework designed to simplify the development of multi-agent systems. It enables the definition of agents with distinct roles, goals, and behaviors, allowing them to collaborate on tasks. CrewAI's architecture supports the creation of structured workflows where agents can interact, share information, and make decisions collectively. [Discover CrewAI on GitHub](https://github.com/crewAIInc/crewAI).

- **Devika – *Agentic AI Software Engineer* (2023)**
  Devika is an open-source AI agent designed to function as a software engineer. It interprets high-level human instructions, decomposes them into actionable steps, conducts research, and writes code to fulfill specified objectives. Devika leverages LLMs, planning algorithms, and web browsing capabilities to autonomously handle software development tasks. [Learn more about Devika](https://github.com/stitionai/devika).

- **DSPy – *Declarative Self-Improving Python* (2023)**
  DSPy is an open-source framework from Stanford University that reimagines the development of LLM applications through declarative programming. Instead of crafting prompts manually, developers define tasks and metrics, and DSPy compiles these specifications into optimized prompts and model configurations. This approach facilitates the creation of modular, self-improving AI systems. [Explore DSPy on GitHub](https://github.com/stanfordnlp/dspy).

- **Guidance – *Framework for Structured LLM Generation* (2023)**
  Guidance is a framework that offers fine-grained control over LLM outputs by combining templating with programmatic logic. It allows developers to enforce output structures, integrate conditionals and loops, and interleave generation with tool usage. This structured approach enhances the reliability and consistency of LLM-generated content. [Visit the Guidance repository](https://github.com/guidance-ai/guidance).

- **Hong et al. – *MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework* (2023)**
  MetaGPT is a multi-agent framework that simulates a software development team by assigning distinct roles—such as product manager, architect, and engineer—to AI agents. By encoding Standard Operating Procedures (SOPs) into prompt sequences, MetaGPT enables agents to collaborate effectively, breaking down complex tasks into manageable subtasks. This structured approach enhances coherence and reduces errors in generated outputs, demonstrating improved performance in collaborative software engineering benchmarks. [Read the full paper from this repo](./papers/hong-metagpt.pdf). [Read the full paper from the source](https://arxiv.org/abs/2308.00352). [Explore MetaGPT on GitHub](https://github.com/FoundationAgents/MetaGPT).

- **LangChain – *Framework for Building LLM-Powered Applications* (2023)**
  LangChain is an open-source framework designed to simplify the development of applications powered by large language models (LLMs). It provides a modular approach to connect LLMs with external data sources, tools, and APIs, enabling the creation of context-aware and dynamic applications. LangChain's architecture supports the chaining of components, allowing developers to build complex workflows that integrate memory, decision-making, and tool usage. [Explore the LangChanin repository](https://github.com/langchain-ai/langchain).

- **LangGraph – *Runtime for Agentic Workflows* (2023)**
  LangGraph is a runtime framework built atop LangChain, focusing on the orchestration of agentic workflows. It enables the construction of dynamic computation graphs where nodes represent agents or tools, and edges define the flow of information. LangGraph supports features like human-in-the-loop interactions, state management, and parallel execution, facilitating the development of complex, multi-agent systems. [Explore the LangGraph repository](https://github.com/langchain-ai/langgraph).

- **LlamaIndex – *Data Framework for LLM Applications* (2023)**
  LlamaIndex is an open-source data framework designed to bridge the gap between large language models (LLMs) and private or domain-specific data. It provides tools for data ingestion, indexing, and querying, enabling LLMs to access and interpret custom data sources such as PDFs, databases, and APIs. LlamaIndex supports context augmentation techniques like Retrieval-Augmented Generation (RAG), facilitating the development of applications like question-answering systems, chatbots, and autonomous agents. [Explore LlamaIndex](https://www.llamaindex.ai/framework).

- **Microsoft – *Semantic Kernel: Open-Source SDK for AI Integration* (2023)**
  Semantic Kernel is an open-source SDK developed by Microsoft that facilitates the integration of AI services, such as OpenAI and Azure OpenAI, with conventional programming languages like C#, Python, and Java. It provides abstractions for prompt templating, function chaining, and memory management, enabling developers to build AI applications that combine natural language capabilities with traditional code. Semantic Kernel supports the creation of plugins and planners, allowing for the orchestration of complex workflows and multi-agent systems. [Learn more about Semantic Kernel](https://learn.microsoft.com/en-us/dotnet/ai/semantic-kernel-dotnet-overview). [Explore the Semantic Kernel repository](https://github.com/microsoft/semantic-kernel).

- **PromptTools – *Open-Source Framework for Prompt Testing and Evaluation* (2023)**
  PromptTools provides an interactive framework for evaluating, comparing, and managing prompts across different LLMs. It supports side-by-side comparisons, regression testing, and metric-based evaluation, with both CLI and visual interfaces. By enabling structured experimentation with prompts and model configurations, PromptTools helps teams improve reliability and consistency in agentic workflows. It’s especially useful for A/B testing, failure analysis, and systematic refinement of prompt strategies. [Explore PromptTools on GitHub](https://github.com/hegelai/prompttools).

- **AutoGen Studio – *No-Code Interface for Multi-Agent Systems* (2024)**
  AutoGen Studio is a visual development environment built on the AutoGen framework, enabling users to prototype, debug, and evaluate multi-agent workflows without extensive coding. It offers a drag-and-drop interface for composing agents, defining workflows, and monitoring interactions, streamlining the development of complex AI systems. [Explore AutoGen Studio](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

## See also
- [Contribution Guide](./CONTRIBUTING.md)
- [Glossary of Key Terms](./GLOSSARY.md)
