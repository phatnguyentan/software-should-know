# Software Should Know

Kho tri thức này được tổ chức theo **Software Engineering Knowledge System**.

> Technology changes. Principles compound.

## Bản đồ tri thức cấp cao

```
SOFTWARE ENGINEERING KNOWLEDGE SYSTEM
│
├─ 01 FOUNDATIONS
├─ 02 SOFTWARE ENGINEERING
├─ 03 SYSTEMS ENGINEERING
├─ 04 PLATFORM & OPERATIONS
├─ 05 AI-NATIVE ENGINEERING
├─ 06 PRODUCT & DOMAIN
├─ 07 HUMAN & ORGANIZATION
├─ 08 BUSINESS & ECONOMICS
└─ 09 STRATEGY & PROFESSIONAL PRACTICE
```

---

## Start here

1. `00-index.mdx` — bản đồ điều hướng canonical của toàn repo
2. `01-foundations/00-index.mdx` — nền tảng CS và toán
3. `02-software-engineering/00-index.mdx` — requirements, design, implementation, testing, evolution
4. `03-systems-engineering/00-index.mdx` — architecture, distributed systems, scalability, reliability
5. `04-platform-operations/00-index.mdx` — cloud, devops, sre, observability, platform engineering
6. `05-ai-native-engineering/00-index.mdx` — AI foundations, AI engineering, agent engineering

---

## Canonical vs Legacy

- **Canonical structure** hiện tại là 9 L1 folder từ `01-foundations/` đến `09-strategy-professional-practice/`.
- Các folder cũ như `02-human/`, `03-world/`, `04-software-engineering/`, `05-product/`, `06-organization/`, `07-business/`, `08-founder/` được giữ lại như **legacy compatibility layer** để migrate dần.
- Khi thêm cấu trúc mới, ưu tiên cập nhật theo canonical folders trước.

---

## Cấu trúc canonical mới

- `01-foundations/`
  - `01-computer-science/`
  - `02-mathematics-quantitative-thinking/`
- `02-software-engineering/`
  - `01-requirements/`
  - `02-software-design/`
  - `03-implementation/`
  - `04-testing-quality/`
  - `05-software-evolution/`
- `03-systems-engineering/`
  - `01-system-architecture/`
  - `02-distributed-systems/`
  - `03-scalability/`
  - `04-reliability/`
  - `05-performance/`
  - `06-security/`
- `04-platform-operations/`
  - `01-cloud/`
  - `02-devops/`
  - `03-sre/`
  - `04-observability/`
  - `05-platform-engineering/`
- `05-ai-native-engineering/`
  - `01-ai-foundations/`
  - `02-ai-engineering/`
  - `03-agent-engineering/`
  - `04-ai-assisted-software-engineering/`
  - `05-ai-safety-governance/`
- `06-product-domain/`
  - `01-product-thinking/`
  - `02-domain-knowledge/`
  - `03-product-engineering/`
- `07-human-organization/`
  - `01-human-behavior/`
  - `02-teams/`
  - `03-organization/`
  - `04-leadership/`
- `08-business-economics/`
  - `01-economics/`
  - `02-business/`
  - `03-technology-industry/`
  - `04-technology-strategy/`
- `09-strategy-professional-practice/`
  - `01-engineering-strategy/`
  - `02-decision-making/`
  - `03-career/`
  - `04-technology-entrepreneurship/`
- `90-tooling/` — scripts và tooling support

---

## Nếu bạn là ai thì bắt đầu ở đâu?

### Backend engineer
1. `01-foundations/00-index.mdx`
2. `02-software-engineering/00-index.mdx`
3. `03-systems-engineering/00-index.mdx`
4. `04-platform-operations/00-index.mdx`
5. `06-product-domain/00-index.mdx`

### Frontend engineer
1. `01-foundations/00-index.mdx`
2. `02-software-engineering/00-index.mdx`
3. `06-product-domain/00-index.mdx`
4. `05-ai-native-engineering/00-index.mdx`

### Fullstack engineer
1. `01-foundations/00-index.mdx`
2. `02-software-engineering/00-index.mdx`
3. `03-systems-engineering/00-index.mdx`
4. `04-platform-operations/00-index.mdx`
5. `06-product-domain/00-index.mdx`
6. `05-ai-native-engineering/00-index.mdx`

### Architect / staff / principal track
1. `01-foundations/00-index.mdx`
2. `02-software-engineering/00-index.mdx`
3. `03-systems-engineering/00-index.mdx`
4. `09-strategy-professional-practice/00-index.mdx`
5. `06-product-domain/00-index.mdx`
6. `08-business-economics/00-index.mdx`

### Leader
1. `07-human-organization/00-index.mdx`
2. `09-strategy-professional-practice/00-index.mdx`
3. `08-business-economics/00-index.mdx`
4. `06-product-domain/00-index.mdx`

---

## Legacy compatibility folders đang được map dần vào canonical mới

- `Codility/` → `01-foundations/`
- `Backend/` + `Frontend/` → chủ yếu vào `02-software-engineering/` + `03-systems-engineering/`
- `Solution-Design/` → chủ yếu vào `02-software-engineering/` + `03-systems-engineering/` + `06-product-domain/`
- `Video/` → `05-ai-native-engineering/`
- `Leader/` → `07-human-organization/` + `09-strategy-professional-practice/`
- `Founder/` → `08-business-economics/` + `09-strategy-professional-practice/`
- `Tech-Stack/` → practice layer bên trong software/platform/ai
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
3. Canonical backbone mới đi theo 9 layer L1 từ Foundations → Strategy & Professional Practice.
4. Nội dung mới nên được gắn vào backbone mới trước khi xét folder legacy.
5. Ưu tiên **problem + principle + trade-off**, không viết theo checklist tool ngắn hạn.
