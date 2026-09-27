# Software Should Know — Domain Knowledge System

Repository này được chuẩn hóa theo hướng **Software Engineering Domain Knowledge System**:

> Technology changes. Principles compound.

Mục tiêu là giữ kiến trúc tri thức nhất quán theo **domain** thay vì theo tool rời rạc.

---

## 1) Cấu trúc tri thức chuẩn (canonical)

```
FOUNDATIONS
  ├─ CS fundamentals
  ├─ algorithms
  ├─ programming
  └─ systems thinking

SOFTWARE ENGINEERING
  ├─ requirements/design/implementation
  ├─ testing/quality/evolution
  └─ architecture/system design

RUN / OPERATIONS
  ├─ cloud/platform/devops/sre
  └─ observability/security

AI LAYER
  ├─ AI-native engineering
  └─ AI-assisted engineering

PRODUCT / DOMAIN
ORGANIZATION / LEADERSHIP
BUSINESS / FOUNDER
```

---

## 2) Mapping thư mục hiện tại vào hệ thống domain

| Repository Path | Domain Layer | Classification |
|---|---|---|
| `Solution-Design/` | Software Engineering + System Design + Operations + AI | 🟢 CORE + 🔵 PRACTICE + 🟣 AI-NATIVE |
| `Backend/` | Software Engineering (implementation, backend fundamentals) | 🟢 CORE + 🔵 PRACTICE |
| `Frontend/` | Software Engineering (frontend implementation & fundamentals) | 🟢 CORE + 🔵 PRACTICE |
| `Tech-Stack/` | Engineering Practice (framework/tool ecosystem) | 🔵 PRACTICE |
| `Video/MCP/` | AI-native engineering (MCP, agent tooling) | 🟣 AI-NATIVE |
| `Leader/` | Engineering leadership & organization | 🟢 CORE (leadership principles) + 🔵 PRACTICE |
| `Founder/` | Business/founder competencies | 🟢 CORE (business principles) |
| `Codility/` | Algorithm practice (foundations) | 🟢 CORE |
| `Scripts/` | Tooling/automation support | 🔵 PRACTICE |

---

## 3) CORE vs PRACTICE vs AI-NATIVE vs FRONTIER

- 🟢 **CORE**: nguyên lý bền vững (algorithms, systems, design, testing, security, leadership principles).
- 🔵 **ENGINEERING PRACTICE**: ecosystem triển khai (framework, cloud, CI/CD, tooling).
- 🟣 **AI-NATIVE**: LLM/RAG/agents/MCP/eval/guardrails, cập nhật liên tục.
- 🟠 **FRONTIER**: công nghệ thử nghiệm, không dùng làm nền tảng career chính.

---

## 4) Quy ước nhất quán khi thêm tài liệu mới

1. Tài liệu roadmap cấp hệ thống đặt tại `Solution-Design/`.
2. Link roadmap luôn được cập nhật tại `Solution-Design/topics/00-index.mdx` (mục **Roadmap mở rộng**).
3. Mỗi thư mục domain nên có file `00-index.mdx` để điều hướng nội bộ.
4. Ưu tiên đặt tên và nội dung theo domain/khái niệm, không đặt theo tool tạm thời.

---

## 5) Điểm vào chính

- Domain system roadmap: `Solution-Design/software-engineering-knowledge-system-roadmap.mdx`
- Enterprise system roadmap: `Solution-Design/enterprise-system-design-roadmap.mdx`
- Enterprise topic index: `Solution-Design/topics/00-index.mdx`
