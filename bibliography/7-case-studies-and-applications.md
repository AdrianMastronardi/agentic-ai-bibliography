# 7. Case Studies and Applications

Agentic AI is not just a research topic — it’s already shaping real-world
systems. This section highlights concrete applications, case studies, and
experimental agents deployed in diverse domains. These examples illustrate both
the promise and the complexity of building agents that operate under real-world
constraints.

## 7.1 Software Engineering Agents

- **Anton Osika et al. – *GPT-Engineer: Autonomous Codebase Generation via
- Prompt-Driven Agents* (2023)**
  GPT-Engineer is an open-source CLI tool that enables users to generate
  entire codebases from natural language prompts. It guides users through
  requirement clarification, architectural planning, and iterative code
  generation using LLMs like GPT-4. The system supports persistent memory,
  customizable agent identities, and benchmarking tools, making it a practical
  example of LLM agents applied to real-world software engineering tasks.
  [Explore the code repository](https://github.com/AntonOsika/gpt-engineer)

- **Yuntong Zhang et al. – *AutoCodeRover: Autonomous Program Improvement*
- (2024)**
  AutoCodeRover is an LLM-based agent designed to autonomously resolve
  software issues, such as bug fixes and feature requests, directly from
  GitHub repositories. The system integrates program structure-aware code
  search and spectrum-based fault localization to identify relevant code
  segments, generate patches, and validate fixes. Evaluated on the
  SWE-bench-lite benchmark, it achieves a 19% issue resolution rate with
  significantly lower costs than prior baselines, demonstrating the
  feasibility of agentic program repair in real-world codebases.  ·
  [Read the full paper from this repo](../papers/zhang-2024.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2404.05427) · [Explore the
  code repository](https://github.com/AutoCodeRoverSG/auto-code-rover) · [Read
  the full paper from the source](https://arxiv.org/abs/2404.05427)

## 7.3 Vertical and Industry-Specific Applications

- **Shunyu Yao et al. – *WebShop: Towards Scalable Real-World Web Interaction
- with Grounded Language Agents* (2022)**
  WebShop introduces a large-scale, simulated e-commerce environment designed
  to train and evaluate goal-directed shopping agents. It features over 1.18
  million real-world product listings and 12,087 crowd-sourced natural
  language instructions. Agents navigate various webpage types—search,
  results, item, and item-detail pages—to locate, customize, and purchase
  products based on user instructions. While entirely simulated, WebShop
  closely mirrors real-world e-commerce interactions and supports sim-to-real
  transfer, as demonstrated by agent evaluations on platforms like Amazon and
  eBay.  ·
  [Read the full paper from this repo](../papers/yao-2022-2.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2207.01206) · [Explore the
  code repository](https://github.com/princeton-nlp/webshop) · [Read the full
  paper from the source](https://arxiv.org/abs/2207.01206)

- **Wentao Zhang et al. – *A Multimodal Foundation Agent for Financial
- Trading: Tool-Augmented, Diversified, and Generalist* (2024)**
  FinAgent is a multimodal LLM-based agent designed for financial trading
  tasks. It integrates textual, numerical, and visual modalities—such as news
  headlines, time-series data, and candlestick charts—through a tool-augmented
  architecture that includes diversified memory retrieval and dual-level
  reflection. The agent demonstrates strong generalization across six
  financial datasets involving stocks and cryptocurrencies, achieving a 92.27%
  return on one benchmark and outperforming 12 state-of-the-art baselines.
  [Read the full paper from this repo](../papers/zhang-2024-2.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2402.18485) · [Read the
  full paper from the source](https://arxiv.org/abs/2402.18485)

- **Fouad Bousetouane – *Agentic Systems: A Guide to Transforming Industries
- with Vertical AI Agents* (2025)**
  This paper introduces agentic systems as a new generation of AI solutions
  that leverage Large Language Models (LLMs) to create adaptable,
  industry-specific software agents. These agents offer advantages over
  traditional systems by providing domain expertise, real-time adaptability,
  and end-to-end workflow automation. The paper details the core components of
  these agents, including memory, a reasoning engine, cognitive skills
  modules, and tools, and explores different categories of agentic systems:
  task-specific, multi-agent, and human-augmented. It further discusses
  current industry and academic efforts in building these systems and outlines
  future research directions.  ·
  [Read the full paper from this repo](../papers/bousetouane-2025.pdf) · [Read
  the full paper from the source](https://arxiv.org/abs/2501.00881) · [Explore
  the code
  repository](https://github.com/nagarx/vertical_agents_implementation) ·
  [Read the full paper from the source](https://arxiv.org/abs/2501.00881)

## 7.4 Scientific Discovery and Research Automation

- **Chandan K. Reddy & Parshin Shojaee – *Towards Scientific Discovery with
- Generative AI: Progress, Opportunities, and Challenges* (2024)**
  This paper explores the current state and future prospects of applying
  generative AI to scientific discovery. The authors discuss the potential of
  AI to accelerate research processes, the need for science-focused AI agents,
  improved benchmarks, and multimodal scientific representations. They also
  highlight challenges such as ensuring transparency, reproducibility, and
  ethical considerations in AI-driven scientific research.
  [Read the full paper from this repo](../papers/reddy-2024.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2412.11427) · [Read the
  full paper from the source](https://arxiv.org/abs/2412.11427)

- **Chris Lu et al. – *The AI Scientist: Towards Fully Automated Open-Ended
- Scientific Discovery* (2024)**
  This work presents The AI Scientist, a framework enabling large language
  models to autonomously conduct scientific research. The system can generate
  novel research ideas, write code, execute experiments, analyze results, and
  compose scientific papers. The authors demonstrate the framework's
  capabilities across various machine learning domains, highlighting its
  potential to transform the landscape of scientific discovery.
  [Read the full paper from this repo](../papers/lu-2024.pdf) · [Read the full
  paper from the source](https://arxiv.org/abs/2408.06292) · [Read the full
  paper from the source](https://arxiv.org/abs/2408.06292)

- **Mourad Gridach et al. – *Agentic AI for Scientific Discovery: A Survey of
- Progress, Challenges, and Future Directions* (2025)**
  This survey explores how agentic AI is being applied across domains of
  scientific research, including literature analysis, hypothesis generation,
  and experiment design. The authors review progress in fields like chemistry,
  biology, and materials science, and identify key challenges such as
  coordination complexity, evaluation frameworks, and epistemic risk. The
  paper also proposes future directions to improve the reliability, usability,
  and autonomy of agents in scientific contexts.
  [Read the full paper from this repo](../papers/gridach-2025.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2503.08979) · [Read the
  full paper from the source](https://arxiv.org/abs/2503.08979)

- **Samuel Schmidgall & Michael Moor – *AgentRxiv: Towards Collaborative
- Autonomous Research* (2025)**
  This paper presents AgentRxiv, a framework designed to facilitate
  collaboration among autonomous research agents. By enabling agents to share
  and build upon each other's work, AgentRxiv aims to emulate the
  collaborative nature of human scientific research. The authors discuss the
  architecture of the system, its potential to accelerate scientific
  discovery, and the challenges associated with autonomous agent
  collaboration.
  [Read the full paper from this repo](../papers/schmidgall-2025.pdf) · [Read
  the full paper from the source](https://arxiv.org/abs/2503.18102) · [Read
  the full paper from the source](https://arxiv.org/abs/2503.18102)

- **Tianshi Zheng et al. – *From Automation to Autonomy: A Survey on Large
- Language Models in Scientific Discovery* (2025)**
  This comprehensive survey examines the evolving role of Large Language
  Models (LLMs) in scientific discovery, highlighting their progression from
  task-specific tools to autonomous agents. The authors introduce a
  three-level taxonomy—Tool, Analyst, and Scientist—to categorize LLMs based
  on their autonomy and capabilities. The paper discusses applications across
  various stages of the scientific method and outlines challenges such as
  evaluation frameworks, transparency, and ethical considerations.
  [Read the full paper from this repo](../papers/zheng-2025.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2505.13259) · [Read the
  full paper from the source](https://arxiv.org/abs/2505.13259)

- **Yutaro Yamada et al. – *The AI Scientist-v2: Workshop-Level Automated
- Scientific Discovery via Agentic Tree Search* (2025)**
  This paper introduces The AI Scientist-v2, an end-to-end agentic system
  capable of autonomously generating scientific hypotheses, designing and
  executing experiments, analyzing data, and authoring manuscripts. Notably,
  it produced the first entirely AI-generated workshop paper accepted through
  peer review. The system employs an agentic tree-search mechanism guided by
  an experiment manager agent, demonstrating significant advancements in
  automated scientific research.
  [Read the full paper from this repo](../papers/yamada-2025.pdf) · [Read the
  full paper from the source](https://arxiv.org/abs/2504.08066) · [Read the
  full paper from the source](https://arxiv.org/abs/2504.08066)
