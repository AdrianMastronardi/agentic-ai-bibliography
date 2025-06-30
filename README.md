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

- **Yao et al. – *ReAct: Synergizing Reasoning and Acting in Language Models* (2022)**  
  A widely influential paper introducing a simple but powerful approach to agent behavior: combining verbal reasoning with action execution. The ReAct pattern lets agents “think out loud” while taking tool-augmented steps, improving performance on decision-making tasks. This paper laid the foundation for many modern agent frameworks. [Read the full paper from this repo](./papers/yao-react.pdf). [Read the full paper from the source](https://arxiv.org/abs/2210.03629).

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

## See also
- [Contribution Guide](./CONTRIBUTING.md)
- [Glossary of Key Terms](./GLOSSARY.md)
