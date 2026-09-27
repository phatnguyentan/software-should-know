# Software Should Know

Kho tri thức này được tổ chức theo **Software Engineering Knowledge System**.

> Technology changes. Principles compound.

## Bản đồ tri thức cấp cao

```
SOFTWARE ENGINEERING KNOWLEDGE SYSTEM
                 │
 ┌───────────────┼───────────────┐
 │               │               │
FOUNDATIONS     HUMAN          WORLD
 │               │               │
 ├─ CS           ├─ Psychology   ├─ Economics
 ├─ Algorithms   ├─ People       ├─ Business
 ├─ Programming  ├─ Teams        ├─ Technology Industry
 ├─ Architecture ├─ Organization ├─ Regulation
 ├─ OS           ├─ Leadership   └─ Geopolitics
 ├─ Networks     └─ Communication
 ├─ Databases
 ├─ Distributed Systems
 └─ Security
                 │
                 ▼
        SOFTWARE ENGINEERING
                 │
          ┌──────┼──────┐
          │      │      │
        BUILD   RUN   EVOLVE
          │      │      │
          │      │      └── AI
          │      │          ├─ ML
          │      │          ├─ LLM
          │      │          ├─ RAG
          │      │          ├─ Agents
          │      │          └─ AI Engineering
          │      │
          │      └── Cloud / DevOps / SRE
          │
          └── Architecture / Code / Data / Testing
                 │
                 ▼
               PRODUCT
                 │
                 ▼
                VALUE
                 │
          ┌──────┴──────┐
          │             │
    ORGANIZATION     BUSINESS
          │             │
     Leadership      Strategy
     Management      Economics
     Culture         Finance
          │             │
          └──────┬──────┘
                 ▼
              FOUNDER
```

---

## Start here

1. `00-index.mdx` — bản đồ điều hướng canonical của toàn repo
2. `04-software-engineering/00-index.mdx` — trục trung tâm của nghề software engineer
3. `04-software-engineering/01-build/00-index.mdx` — nếu muốn đi từ architecture / code / data / testing
4. `04-software-engineering/02-run/00-index.mdx` — nếu muốn đi từ cloud / devops / sre / observability
5. `04-software-engineering/03-evolve/00-index.mdx` — nếu muốn đi theo AI / LLM / agents / AI engineering

---

## Cấu trúc canonical mới

- `01-foundations/` — nền tảng CS, algorithms, programming, systems, security
- `02-human/` — psychology, people, teams, leadership, communication
- `03-world/` — economics, business, industry, regulation, geopolitics
- `04-software-engineering/` — lõi nghề software engineering
  - `01-build/` — architecture / code / data / testing
  - `02-run/` — cloud / devops / sre / observability / production security
  - `03-evolve/` — AI / ML / LLM / RAG / agents / AI engineering
- `05-product/` — product thinking, requirement, domain, value
- `06-organization/` — team, management, culture, leadership
- `07-business/` — strategy, economics, finance, business model
- `08-founder/` — founder and technology entrepreneur lens
- `90-tooling/` — scripts và tooling support

---

## Nếu bạn là ai thì bắt đầu ở đâu?

### Backend engineer
1. `01-foundations/00-index.mdx`
2. `04-software-engineering/01-build/00-index.mdx`
3. `04-software-engineering/02-run/00-index.mdx`
4. `05-product/00-index.mdx`

### Frontend engineer
1. `01-foundations/00-index.mdx`
2. `04-software-engineering/01-build/00-index.mdx`
3. `05-product/00-index.mdx`
4. `04-software-engineering/03-evolve/00-index.mdx`

### Fullstack engineer
1. `01-foundations/00-index.mdx`
2. `04-software-engineering/01-build/00-index.mdx`
3. `04-software-engineering/02-run/00-index.mdx`
4. `05-product/00-index.mdx`
5. `04-software-engineering/03-evolve/00-index.mdx`

### Architect / staff / principal track
1. `01-foundations/00-index.mdx`
2. `04-software-engineering/00-index.mdx`
3. `05-product/00-index.mdx`
4. `06-organization/00-index.mdx`
5. `07-business/00-index.mdx`

### Leader
1. `02-human/00-index.mdx`
2. `06-organization/00-index.mdx`
3. `07-business/00-index.mdx`
4. `08-founder/00-index.mdx`

---

## Legacy domain folders đang được map dần vào backbone mới

- `Codility/` → `01-foundations/`
- `Backend/` + `Frontend/` → chủ yếu vào `04-software-engineering/01-build/`
- `Solution-Design/` → chủ yếu vào `04-software-engineering/` và `05-product/`
- `Video/` → `04-software-engineering/03-evolve/`
- `Leader/` → `06-organization/`
- `Founder/` → `07-business/` + `08-founder/`
- `Tech-Stack/` → practice layer bên trong build/run
- `Scripts/` → `90-tooling/`

---

## Phân loại tri thức

- 🟢 **CORE**: nền tảng bền vững cần học sâu
- 🔵 **ENGINEERING PRACTICE**: ecosystem, cloud, CI/CD, framework, tooling
- 🟣 **AI-NATIVE**: LLM/RAG/agent/MCP/eval/guardrails
- 🟠 **FRONTIER**: vùng thử nghiệm, không nên là toàn bộ career foundation

---

## Quy ước đóng góp

1. Top-level canonical folders dùng numbering để thể hiện thứ tự nhận thức.
2. Mỗi folder điều hướng phải có `00-index.mdx`.
3. `04-software-engineering/` là trục trung tâm của roadmap nghề.
4. Nội dung mới nên được gắn vào backbone mới trước khi xét folder legacy.
5. Ưu tiên **problem + principle + trade-off**, không viết theo checklist tool ngắn hạn.
