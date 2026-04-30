# What to Learn, Build, and Skip in AI Agents (2026)
## By Rohit (@rohit4verse) | Technical Lead, Stealth Company

**Date:** 2026-04-30  
**Source:** Twitter/X Thread  
**Author:** Rohit (@rohit4verse) - 2 years building in this space, cracked $250k+ offers, now runs technical at stealth company

---

## Core Thesis

```
The field moves under everyone equally.
The 22-year-old has the same blank canvas the senior has.
What compounds: willingness to ship + durable primitives.

The skill: knowing which work compounds in a field where the surface keeps changing.
```

---

## The Filter That Actually Works

### Five Tests for Any Launch

```
1. Will this matter in 2 years?
   ├── Wrapper around frontier model → NO
   ├── Protocol, memory pattern, sandboxing → YES
   └── Half-life of wrappers = short, primitives = years

2. Has someone you respect built something real on it?
   ├── Marketing posts → don't count
   └── Postmortems with numbers → worth 10 launch announcements

3. Does it require throwing away your tracing, retries, config, auth?
   ├── YES → framework trying to be platform (90% mortality)
   └── NO → good primitive, slots into existing system

4. What does it cost to skip for 6 months?
   ├── Most launches → nothing
   └── You'll know more in 6 months, winning version clearer

5. Can you measure whether it helps?
   ├── No evals → guessing
   └── Teams without evals run on vibes and ship regressions
```

---

## What to LEARN

### 1. Context Engineering
```
"Prompt engineering" → "context engineering" (rename is real, not cosmetic)

Context = state:
├── System instructions
├── Tool schemas
├── Retrieved documents
├── Prior tool outputs
├── Compressed history

Key insight: Context rot is a real production failure.
After step 8 of 10, original goal can be buried.
→ Teams that ship reliable agents actively summarize, compress, prune

READ: Anthropic's "Effective Context Engineering for AI Agents"
```

### 2. Tool Design
```
5-10 well-named tools > 20 mediocre ones

Tool names: English verb phrases
Descriptions: when to use + when NOT to use
Error messages: feedback model can ACT on
  "Max tokens 500 exceeded, try summarizing first"
  beats "Error: 400 Bad Request" by enormous margin

40% retry reduction reported after rewriting error messages alone

READ: Anthropic's "Writing tools for agents"
```

### 3. Orchestrator-Subagent Pattern
```
Multi-agent debate ended with synthesis everyone now ships:

ORCHESTRATOR (owns writes)
    ↓ delegates
SUBAGENTS (read-only, isolated, focused contexts)

This is how Anthropic's research system works.
This is how Claude Code's subagents work.
Spring AI and most production frameworks standardize this.

DON'T BUILD: Naïve multi-agent (multiple agents writing to shared state)
```

### 4. Evals and Golden Datasets
```
Every team that ships reliable agents has evals.
Every team that doesn't, doesn't.

Spotify: Judge layer vetoes ~25% of outputs before shipping

Pattern: 
├── Harvest production traces
├── Label failures → regression set
├── LLM-as-judge for subjective, exact-match for objective
└── Run suite before any prompt/model/tool change

Bottleneck: labeled set, NOT eval framework.
Build on day one. 50 hand-labeled examples = enough to start.

FRAMEWORKS: Braintrust, Langfuse evals, LangSmith (all fine)
```

### 5. File-System-as-State + Think-Act-Observe Loop
```
For any agent doing real multi-step work:

THINK → ACT → OBSERVE → REPEAT
    ↓
File system as source of truth
Every action logged and replayable

Converged on this: Claude Code, Cursor, Devin, Aider, OpenHands, goose

Model is stateless.
Harness has to be stateful.
Harness does MORE work than model in production.

KEY INSIGHT: A good harness + mediocre model still ships.
A bad harness + best model = agent that forgets what it was doing.
```

### 6. MCP Conceptually
```
MCP = Model Context Protocol
"USB-C of AI" comparison is MORE accurate than ironic now

Don't just learn HOW to call MCP servers.
Learn the MODEL:
├── Clean separation: agent capabilities, tools, resources
├── Extensible auth and transport story

Linux Foundation now stewards it.
Every major model provider backs it.

Once you understand MCP, every "agent integration framework" looks worse.
→ Save time evaluating each one.
```

### 7. Sandboxing as Primitive
```
Every production coding agent runs in sandbox.
Every browser agent hit by indirect prompt injection.
Every multi-tenant agent had permission scoping bug.

Learn basics:
├── Process isolation
├── Network egress controls
├── Secret scoping
├── Auth boundaries

Teams that bolt on after security review = teams that lose deals.
Teams that build in from week one = teams that pass enterprise procurement.
```

---

## What to BUILD With (April 2026 Picks)

### Orchestration
```
LangGraph = production default
├── ~1/3 large companies running agents use it
├── Typed state, conditional edges, durable workflows
└── Verbosity matches what you actually need to control

TypeScript: Mastra (de facto pick in that ecosystem)
Pydantic AI: v1.0 in late 2025, greenfield choice if you want type safety

Provider-native (Claude Agent SDK, OpenAI Agents SDK):
→ Use inside LangGraph nodes, not as top-level orchestrator
```

### Protocol Layer
```
MCP, full stop.
Build tool integrations as MCP servers.
Consume external integrations the same way.
Registry has crossed point where you can find server before building one.
```

### Memory
```
BY AUTONOMY LEVEL, not by hype:

Mem0 → chat-style personalization (user preferences, light history)
Zep → production conversational with entity tracking
Letta → agent coherence across days/weeks

Most teams won't need this.
The ones that do, need exactly this.

MISTAKE: Reaching for memory framework before you have memory problem.
START: context window + vector store
ADD: only when you can articulate the failure mode it solves
```

### Observability and Evals
```
OSS Default: Langfuse (self-hostable, MIT, tracing + prompt versioning + LLM-as-judge)

Already LangChain: LangSmith

Research-style eval: Braintrust

Vendor-neutral OpenTelemetry: OpenLLMetry / Traceloop

NEED BOTH:
├── Tracing → "what did the agent actually do?"
└── Evals → "is the agent better or worse than yesterday?"
```

### Runtime and Sandbox
```
E2B → general sandboxed code execution
Browserbase + Stagehand → browser automation
Anthropic Computer Use → real OS-level desktop control
Modal → short-lived bursts

DON'T run unsandboxed code execution. Ever.
```

### Models (April 2026)
```
Claude Opus 4.7 / Sonnet 4.6 → reliable tool use, multi-step coherence
Claude Sonnet 4.6 → cost-performance sweet spot

GPT-5.4 / 5.5 → strongest CLI/terminal reasoning, OpenAI infra

Gemini 2.5 / 3 → long-context-heavy or multimodal-heavy

DeepSeek-V3.2 / Qwen 3.6 → cost matters more than top-end, narrow well-defined tasks

TREAT models as swappable.
If your agent only works with one model = smell, not moat.
Re-evaluate quarterly.
```

---

## What to SKIP

```
❌ AutoGen and AG2 for production
   → Moved to community maintenance, releases stalled

❌ CrewAI for new production builds
   → Demos easily, engineers building real systems moved off it

❌ Microsoft Semantic Kernel
   → Unless locked into Microsoft enterprise stack

❌ DSPy
   → Unless optimizing prompt programs at scale
   → Not a general agent framework

❌ Standalone code-writing agents as architecture
   → Code-as-action = interesting research, not production default yet

❌ "Autonomous agent" pitches (AutoGPT/BabyAGI lineage)
   → Dead in product form
   → Honest framing: "agentic engineering" = supervised, bounded, evaluated

❌ Agent app stores and marketplaces
   → Promised since 2023, never delivered enterprise traction
   → Enterprises buy vertical agents tied to outcomes, or build their own

❌ Horizontal "build any agent" enterprise platforms
   → Google Agentspace, AWS Bedrock Agents, Microsoft Copilot Studio
   → Confusing, slow-shipping, buy-versus-build math favors building narrow agent
   → EXCEPTIONS: Salesforce Agentforce, ServiceNow Now Assist (embedded in workflows)

❌ SWE-bench and OSWorld leaderboard chasing
   → Berkeley documented: benchmarks can be gamed without solving underlying task
   → Teams now use Terminal-Bench 2.0 + internal evals as real signal

❌ Naïve parallel multi-agent architectures
   → 5 agents chatting over shared memory looks impressive, falls apart in production
   → If you can't draw clean orchestrator-subagent diagram on napkin, don't ship it

❌ Per-seat SaaS pricing for new agent products
   → Market moved to outcome and usage based

❌ Next framework on Hacker News this week
   → Wait 6 months. If it still matters, it'll be obvious.
```

---

## How to Actually Move

### Sequence That Works

```
STEP 1: Pick ONE outcome that already matters
├── Not a moonshot
├── Something measurable business already cares about
└── Deflecting support tickets, drafting legal review, qualifying leads, generating reports

STEP 2: Set up tracing and evals BEFORE you ship
├── Pick Langfuse or LangSmith
├── Build small golden dataset by hand (50 labeled examples)
└── You cannot improve what you can't measure

STEP 3: Start with single-agent loop
├── LangGraph or Pydantic AI
├── Claude Sonnet 4.6 or GPT-5
├── 3-7 well-designed tools
├── File system or database as state
└── Ship to small audience, watch traces

STEP 4: Treat agent as PRODUCT, not project
├── Failures = your roadmap
├── Build regression set from real production traces
├── Every prompt/model/tool change goes through evals before deployment

STEP 5: Add scope only when you've earned it
├── Subagents → context is bottleneck
├── Memory frameworks → single-window context can't hold what you need
├── Computer use → underlying APIs really aren't there

STEP 6: Pick boring infrastructure
├── MCP for tools
├── E2B or Browserbase for sandboxes
├── Postgres for state
├── Existing auth and observability stack

STEP 7: Watch unit economics from day one
├── Per-action costs, cache hit rates, retry-loop costs
├── $0.50/run PoC becomes $50K/month at moderate volume
└── Instrument cost per outcome from the start

STEP 8: Re-evaluate models quarterly
├── Lock in for quarter
├── Run eval suite against frontier at end of quarter
└── Switch if data says to switch
```

---

## Weekly Reading Habit

```
RESERVE 30 minutes on Friday:
├── Anthropic's engineering blog
├── Simon Willison's notes
├── Latent Space
└── 1-2 postmortems if any landed

SKIP everything else for the week.
You will know the things that matter.
```

---

## What's Worth Watching (Next 2 Quarters)

```
1. Replit Agent 4's parallel forking model
   → First serious attempt at multiple agents working in parallel without shared state issues
   → Could shift orchestrator-subagent default if it holds up

2. Outcome-based pricing maturity
   → Sierra and Harvey validate it inside narrow verticals
   → Question: does it generalize outside?

3. Skills as packaging layer
   → AGENTS.md and skills directories proliferating across GitHub
   → Open question: standardizes like MCP did for tools?

4. Claude Code's April 2026 quality regression + postmortem
   → Industry-leading agent shipped 47% performance regression
   → Caught by users before internal monitoring
   → Lesson: production agent eval practices still immature even at leaders
   → If this drives investment in better online evals = healthy correction

5. Voice as default support surface
   → Sierra's voice channel surpassed text in late 2025
   → If pattern holds: latency, interruption, real-time tool use = first-order constraints

6. Open-model agent capability closing gap
   → DeepSeek-V3.2 with native thinking-into-tool-use
   → Qwen 3.6
   → Cost-performance for narrow agent tasks shifting
   → Closed-source default isn't permanent
```

---

## The Unconventional Bet

```
KEY INSIGHT:
"Every framework you don't adopt is a migration you don't owe.
 Every benchmark you don't chase is a quarter of focus you keep."

The companies winning this cycle (Sierra, Harvey, Cursor):
├── Picked narrow targets
├── Built boring discipline
└── Let the field's noise pass them by

The conventional path assumed stable industry on other side.
The stack now changes every quarter.
The people winning stopped optimizing for stack mastery.
Started optimizing for taste, primitives, and ship velocity.

MAKE THINGS. PUT THEM ON THE INTERNET.
THE WORK INTRODUCES YOU.

The credential is the artifact.
```

---

## Key Takeaways

```
WHAT COMPOUNDS:
├── Context engineering
├── Tool design
├── Orchestrator-subagent pattern
├── Eval discipline
├── Harness mindset

WHAT DOESN'T COMPOUND:
├── Knowing the API of this week's framework
├── Benchmark chasing
├── Framework hopping

THE PLAYBOOK:
1. Pick one outcome
2. Wire up tracing and evals before you ship
3. Use LangGraph (or team's equivalent)
4. Use MCP
5. Sandbox your runtime
6. Default to single-agent
7. Add scope when failure modes pull it in
8. Re-evaluate models quarterly
9. Read three things on Fridays
```

---

*Document: arp-v24/AI_AGENTS_WHAT_TO_LEARN_BUILD_SKIP_2026.md*  
*Created: 2026-04-30*