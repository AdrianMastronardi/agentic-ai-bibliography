# 6. Simulation Frameworks and Experimental Agent Environments

Beyond prompts and pipelines, agents can also inhabit worlds. This section
gathers platforms used to simulate, study, and experiment with agent behavior in
controlled, interactive environments. These frameworks—some predating
LLMs—support research in decision-making, coordination, embodiment, and learning
through interaction. They are invaluable for testing agentic architectures under
pressure, prototyping behaviors at scale, or exploring social emergence,
long-term memory, and autonomy in sandboxed settings.

## 6.1 Social Simulations and Emergent Behavior

- **Masad & Kazil – *Mesa: Agent-Based Modeling Framework in Python* (2015)**
  Mesa is a modular, extensible framework for building agent-based models in
  Python. Widely used in computational social science and complex systems
  research, Mesa allows developers to define agents, environments, and
  schedules of interaction. It supports visualization, data collection, and
  experimentation with heterogeneous agent behaviors. Though not LLM-centric,
  Mesa remains a powerful tool for simulating decentralized systems, testing
  coordination dynamics, and modeling emergent phenomena—offering a
  complementary lens to modern agentic AI.
  [Explore the code repository](https://github.com/projectmesa/mesa)

- **Joon Sung Park et al. – *Generative Agents: Interactive Simulacra of Human
  Behavior* (2023)**
  This paper introduces generative agents—computational models that simulate
  believable human behavior in an interactive sandbox environment. These
  agents possess memory, reflection, and planning capabilities, enabling them
  to exhibit emergent social behavior, form routines, organize events, and
  respond coherently to interactions over time. The work is notable for
  demonstrating how large language models, when embedded in agent
  architectures with memory and retrieval, can simulate rich, autonomous
  personas within a community.
  [Read the full paper from this repo](../papers/park-generative-agents.pdf) ·
  [Read the full paper from the source](https://arxiv.org/abs/2304.03442) ·
  [Read the full paper from the source](https://arxiv.org/abs/2304.03442)

## 6.2 Multi-Agent and Coordination Benchmarks

- **Lowe et al. – *Multi-Agent Actor-Critic for Mixed Cooperative-Competitive
  Environments* (2017)**
  The Multi-Agent Particle Environment (MPE) is a set of simple yet versatile
  environments for multi-agent reinforcement learning. It features agents
  interacting in a 2D continuous space with discrete actions, supporting both
  cooperative and competitive scenarios. MPE has been widely used to benchmark
  algorithms in settings that require communication, coordination, and
  competition among agents.
  [Explore the code
  repository](https://github.com/openai/multiagent-particle-envs)

- **Oriol Vinyals et al. – *StarCraft II: A New Challenge for Reinforcement
  Learning* (2017)**
  The StarCraft II Learning Environment (SC2LE) offers a complex, real-time
  strategy domain for training reinforcement learning agents in partially
  observable, multi-agent settings. It has been instrumental in driving
  research on long-horizon planning, adaptive strategies, and coordination
  under uncertainty.
  [Read the full paper from this repo](../papers/vinyals-starcraft2.pdf) ·
  [Read the full paper from the source](https://arxiv.org/abs/1708.04782) ·
  [Read the full paper from the source](https://arxiv.org/abs/1708.04782)

- **Farama Foundation – *Gymnasium: An API for Reinforcement Learning*
  (2022)**
  Gymnasium is the official successor to OpenAI Gym, developed and maintained
  by the Farama Foundation. It provides a standardized and extensible API for
  experimenting with agents in reinforcement learning environments. Its
  modular design and active open-source community ensure long-term continuity
  and compatibility with complementary libraries such as PettingZoo and
  SuperSuit. Gymnasium is widely used to evaluate agentic behaviors in
  simulated contexts, including hybrid architectures with LLMs.
  [Explore the code
  repository](https://github.com/Farama-Foundation/Gymnasium)

- **Chevalier-Boisvert et al. – *MiniGrid & MiniWorld: Modular & Customizable
  Reinforcement Learning Environments for Goal-Oriented Tasks* (2023)**
  MiniGrid and MiniWorld are lightweight, modular environments designed for
  reinforcement learning research. MiniGrid offers 2D grid-based environments,
  while MiniWorld provides 3D simulations. Both are highly customizable,
  facilitating research in areas like curriculum learning, exploration, and
  meta-learning. Their unified API allows for seamless experimentation across
  different observation spaces.  · .
  [Access the source](https://minigrid.farama.org/) · [Explore the code
  repository](https://github.com/Farama-Foundation/Minigrid) · [Access the
  source](https://miniworld.farama.org/)

## 6.3 Embodied and Physical Simulation

- **Mohit Shridhar et al. – *ALFWorld: Aligning Text and Embodied Environments
  for Interactive Learning* (2020)**
  ALFWorld bridges text-based and embodied environments by aligning
  instruction-following tasks in TextWorld with 3D simulations in ALFRED. This
  allows agents to learn policies via text interaction and transfer them into
  visual, embodied execution. The benchmark enables research in policy
  generalization, language grounding, and multi-modal reasoning.
  [Read the full paper from this repo](../papers/shridhar-alfworld.pdf) ·
  [Read the full paper from the source](https://arxiv.org/abs/2010.03768) ·
  [Read the full paper from the source](https://arxiv.org/abs/2010.03768)

- **Viktor Makoviychuk et al. – *Isaac Gym: High Performance GPU-Based Physics
  Simulation for Robot Learning* (2021)**
  Isaac Gym is a GPU-accelerated simulator for physics-based reinforcement
  learning, enabling massive parallel training of embodied agents. It
  integrates simulation and learning on the same device, allowing fast policy
  optimization for robotics and control tasks at scale.
  [Read the full paper from this repo](../papers/makoviychuk-isaac-gym.pdf) ·
  [Read the full paper from the source](https://arxiv.org/abs/2108.10470) ·
  [Read the full paper from the source](https://arxiv.org/abs/2108.10470)

## 6.4 Interactive Web and Digital Environments

- **Joseph Shinn, Omar Labash & Karthik Gopinath – *WebArena: A Realistic Web
  Environment for Building Autonomous Agents* (2023)**
  WebArena is a simulated internet with fully functional, interactive websites
  spanning domains like e-commerce, documentation, forums, and code hosting.
  Designed for evaluating long-horizon, tool-augmented LLM agents, it supports
  realistic browser-based actions and open-ended tasks grounded in modern web
  UX. It provides a reproducible benchmark for instruction-following,
  information synthesis, and strategic action in dynamic web environments.
  [Read the full paper from this repo](../papers/shinn-webarena.pdf) · [Read
  the full paper from the source](https://arxiv.org/abs/2307.13854) · [Read
  the full paper from the source](https://arxiv.org/abs/2307.13854)

- **Xiang Deng et al. – *Mind2Web: Towards a Generalist Agent for the Web*
  (2023)**
  Mind2Web is a large-scale benchmark designed to develop and evaluate
  generalist web agents capable of following natural language instructions to
  complete complex tasks across diverse real-world websites. It comprises
  2,350 open-ended tasks collected from 137 websites spanning 31 domains, with
  human-annotated action sequences. The dataset includes rich contextual
  information such as raw HTML, DOM snapshots, screenshots, and interaction
  traces, facilitating research in instruction following, generalization, and
  web automation.
  [Read the full paper from this repo](../papers/deng-mind2web.pdf) · [Read
  the full paper from the source](https://arxiv.org/abs/2306.06070) · [Read
  the full paper from the source](https://arxiv.org/abs/2306.06070)
