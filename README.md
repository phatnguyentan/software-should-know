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

## Canonical structure

- Repository hiện dùng duy nhất 9 L1 folder từ `01-foundations/` đến `09-strategy-professional-practice/`.
- Khi thêm cấu trúc mới, ưu tiên cập nhật trực tiếp theo canonical folders.

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

## Nguồn nội dung hiện có đang được map vào cấu trúc canonical

Các folder dưới đây là **nguồn nội dung cũ**, không phải entrypoint điều hướng chính. Nếu gặp chúng trong repo, dùng các `00-index.mdx` canonical sau để định vị lại:

- `Codility/` → `01-foundations/00-index.mdx`
- `Backend/` → `02-software-engineering/00-index.mdx`, rồi mở rộng sang `03-systems-engineering/00-index.mdx`
- `Frontend/` → `02-software-engineering/00-index.mdx`
- `Solution-Design/` → `02-software-engineering/00-index.mdx`, `03-systems-engineering/00-index.mdx`, và `06-product-domain/00-index.mdx`
- `Video/` → `05-ai-native-engineering/00-index.mdx`
- `Leader/` → `07-human-organization/00-index.mdx` và `09-strategy-professional-practice/00-index.mdx`
- `Founder/` → `08-business-economics/00-index.mdx` và `09-strategy-professional-practice/00-index.mdx`
- `Tech-Stack/` → nếu nội dung nghiêng về cloud/devops/platform thì vào `04-platform-operations/00-index.mdx`; nếu nghiêng về coding/framework practice thì vào `02-software-engineering/00-index.mdx`; nếu nghiêng về AI workflow thì vào `05-ai-native-engineering/00-index.mdx`
- `Scripts/` → `90-tooling/00-index.mdx`

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
4. Nội dung mới nên được gắn vào backbone mới trước khi map từ các content source hiện có.
5. Ưu tiên **problem + principle + trade-off**, không viết theo checklist tool ngắn hạn.
