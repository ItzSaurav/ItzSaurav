# Saurav Mishra

Systems and software engineer based in Bangalore, India. Operating across the software stack—from low-latency C++20 Linux kernel initialization and PID 1 supervisors to real-time computer vision state engines and distributed web platforms.

[Portfolio](https://itzsaurav.github.io/) | [Resume (PDF)](https://itzsaurav.github.io/Saurav_Mishra_Resume.pdf) | [LinkedIn](https://linkedin.com/in/saurav-mishra-812259364) | [Email](mailto:sauravmishra9045@gmail.com)

---

## Technical Taxonomy

### Systems, OS & Kernel Engineering
- **Languages & Runtimes:** C++20, C, POSIX Shell, Bash
- **Operating Systems & Virtualization:** Linux Kernel Bootstrap, QEMU / KVM, BusyBox Userspace, Initramfs Packaging
- **Syscalls & POSIX Primitives:** `mount(2)`, `waitpid(WNOHANG)`, `socket(AF_UNIX)`, `ioctl(SIOCSIFADDR)`, `reboot(RB_POWER_OFF)`
- **Architectures:** PID 1 Supervisor Loops, DAG Topological Sort Dependency Graphs, Virtual Filesystems (`/proc`, `/sys`, `/dev`, `/run`), UNIX Domain Socket IPC, Asynchronous Signal Handling

### Computer Vision, Math & Intelligent Runtimes
- **Languages & Frameworks:** Python 3, OpenCV, Google MediaPipe
- **Algorithms & Geometric Heuristics:** 21 3D Joint Landmark Tracking, Euclidean Spatial Distance Vectors, HSV ROI Color Segmentation, Hue Standard Deviation Heuristics
- **State Engines & Routing:** Multi-Inflection Trajectory State Machines, Local Hybrid Model Routing (Needle 2 Simple Attention Networks)

### Distributed Web Platforms & Protocols
- **Web Technologies:** Next.js 16 (App Router), TypeScript, React 19, React-Leaflet, CartoDB Dark Matter, Tailwind CSS
- **Routing & Real-Time Telemetry:** Open Source Routing Machine (OSRM) Street-Grid Snapping, Turn-by-Turn GPS State Machines, WebSockets, REST APIs
- **Storage & Infrastructure:** Cloud Firestore, Firebase Auth, SQLite, Vercel Serverless

---

## Featured Systems

### 1. [FreeDot Linux](https://github.com/ItzSaurav/freedot-linux)
**Custom C++20 PID 1 init supervisor, userspace ecosystem, and minimal bootable Linux distribution.**
- **Supervisor Core:** Custom PID 1 init supervisor replacing SysV/systemd, executing virtual filesystem mounts (`/proc`, `/sys`, `/dev`, `/dev/pts`, `/run`), network socket `ioctl(SIOCSIFADDR)` interface bring-up (`lo`, `eth0`), and asynchronous `SIGCHLD` zombie process reaping.
- **Dependency Ordering:** Declarative unit file parser (`/etc/freedot.d/`) executing Directed Acyclic Graph (DAG) topological sort for strict startup sequencing.
- **Daemon IPC:** Bidirectional UNIX domain socket IPC server (`/run/freedot.sock`) with a dedicated `freedotctl` command-line utility for runtime daemon queries and lifecycle signals.
- **Minimal Footprint:** Boots upstream Linux LTS kernel (`bzImage`) into a custom 3.9 MB `initramfs` cpio rootfs in QEMU/KVM with near-instant bootstrap.
- **Status:** [![CI](https://github.com/ItzSaurav/freedot-linux/actions/workflows/ci.yml/badge.svg)](https://github.com/ItzSaurav/freedot-linux) | [Repository](https://github.com/ItzSaurav/freedot-linux)

### 2. [CB-Watch](https://github.com/ItzSaurav/CB-watch)
**Touchless Rubik's Cube timer utility driven by real-time computer vision heuristics.**
- **Gesture Pipeline:** Google MediaPipe `HandLandmarker` tracking 21 3D landmarks per hand at low inference latency.
- **Spatial Geometry:** Euclidean distance vectors comparing fingertip-to-wrist against knuckle-to-wrist ratios with a 30% margin threshold across primary digits for posture detection.
- **State Filtering:** Temporal trajectory state machine requiring 4 directional inflection reversals to reject spurious motions during timer reset.
- **Color Verification:** HSV color space ROI segmentation analyzing mean saturation and hue standard deviation to confirm solved cube face alignment.
- **Status:** [![CI](https://github.com/ItzSaurav/CB-watch/actions/workflows/ci.yml/badge.svg)](https://github.com/ItzSaurav/CB-watch) | [Repository](https://github.com/ItzSaurav/CB-watch)

### 3. [RainVision](https://github.com/ItzSaurav/rainvision)
**AI-assisted monsoon navigation platform providing real-time flood hazard awareness.**
- **Navigation Engine:** Street-grid vector snapping and turn-by-turn routing via Open Source Routing Machine (OSRM) integrated with React-Leaflet and CartoDB Dark Matter tiles.
- **Telemetry & GPS:** Dynamic GPS auto-centering navigation loop maintaining map tracking and rerouting around active flooding sectors.
- **Architecture:** Next.js 16 (App Router), TypeScript, Tailwind CSS, and Progressive Web App service workers.
- **Status:** [Repository](https://github.com/ItzSaurav/rainvision)

---

## Other Projects & Experiments

| Project | Description | Tech Stack | Status & Links |
| :--- | :--- | :--- | :--- |
| [**StudyForge**](https://github.com/ItzSaurav/studyforge) | Gamified productivity web app with XP progression, levels, and streak tracking. | JavaScript, HTML5, CSS3, Firebase | [![CI](https://github.com/ItzSaurav/studyforge/actions/workflows/ci.yml/badge.svg)](https://github.com/ItzSaurav/studyforge) \| [Live Demo](https://studyforge-pearl.vercel.app/) \| [GitHub](https://github.com/ItzSaurav/studyforge) |
| [**FoodShare**](https://github.com/ItzSaurav/FoodShare) | Community food-sharing progressive web app with fine-grained Cloud Firestore security rules. | JavaScript, Node.js, Firebase Auth, Firestore | [Live Demo](https://idp-blush.vercel.app/) \| [GitHub](https://github.com/ItzSaurav/FoodShare) |
| [**VI Voice Assistant**](https://github.com/ItzSaurav/VI) | Hybrid voice assistant with Needle 2 local router, safety whitelist, and native Android client. | Python, Cactus Needle 2, Kotlin, Groq API | [GitHub](https://github.com/ItzSaurav/VI) |
| [**Assignmate**](https://github.com/ItzSaurav/Assignmate-) | Peer-to-peer academic tutoring platform with course tasks and role-based access. | Python, Flask, SQLite | [GitHub](https://github.com/ItzSaurav/Assignmate-) |
| [**Neon Nexus Engine**](https://github.com/ItzSaurav/pygame-rpg-engine) | 2D top-down action RPG prototype exploring game loops and tile map rendering. | Python, Pygame | [GitHub](https://github.com/ItzSaurav/pygame-rpg-engine) |

---

## Open Source Contributions

| Repository | Contribution / Scope | Status | Pull Request |
| :--- | :--- | :--- | :--- |
| [**first-contributions**](https://github.com/firstcontributions/first-contributions) | Profile onboarding and contributor roster registration | Merged | [PR #124462](https://github.com/firstcontributions/first-contributions/pull/124462) |
| [**kana-dojo**](https://github.com/lingdojo/kana-dojo) | Japanese video game dialogue dataset (Yakuza: Like a Dragon) | Merged | [PR #29819](https://github.com/lingdojo/kana-dojo/pull/29819) |
| [**python-vibe**](https://github.com/YauhenBichel/python-vibe) | Project site documentation and GitHub Pages deployment guide | Merged | [PR #76](https://github.com/YauhenBichel/python-vibe/pull/76) |
| [**composable-data-stack**](https://github.com/RonaldHensbergen/composable-data-stack) | Documented ifNonempty conditional interpolation semantics | Merged | [PR #560](https://github.com/RonaldHensbergen/composable-data-stack/pull/560) |
| [**vscode-agent-bell**](https://github.com/chahe-dridi/vscode-agent-bell) | Extension volume settings and Windows WAV audio scaling behavior | Merged | [PR #4](https://github.com/chahe-dridi/vscode-agent-bell/pull/4) |
| [**CONTINUUM**](https://github.com/Cyrax321/CONTINUUM) | Removed unreferenced duplicate memory governance guide | Merged | [PR #634](https://github.com/Cyrax321/CONTINUUM/pull/634) |
| [**rocketmq-rust**](https://github.com/mxsm/rocketmq-rust) | Added Apache 2.0 license compliance headers to transport modules | Merged | [PR #10075](https://github.com/mxsm/rocketmq-rust/pull/10075) |
| [**lark**](https://github.com/lark-parser/lark) | Modernized SPPF parse tree documentation to Bootstrap 5 components | In Review | [PR #1638](https://github.com/lark-parser/lark/pull/1638) |
| [**30-Days-30-Python-Projects**](https://github.com/Coding-Moves/30-Days-30-Python-Projects-Beginner-Contributions-Only) | Day-05 secure CLI password generator in Python | Merged | [PR #3](https://github.com/Coding-Moves/30-Days-30-Python-Projects-Beginner-Contributions-Only/pull/3) |
| [**AAA (AI Coding Agents)**](https://github.com/Abdellox/AAA) | AI Coding Agents directory expansion with structured metadata | In Review | [PR #2](https://github.com/Abdellox/AAA/pull/2) |

---

## Experience

**AI Research Intern** — Sunny Side Up *(May 2025 – Jun 2025)*  
- Evaluated and benchmarked 50+ AI APIs and open-source models for latency, throughput, and integration feasibility across media processing pipelines.
- Designed automation routines and API connector prototypes for content generation and layout validation workflows.

---

## Contact & Dispatch

- **Location:** Bangalore, India (`Asia/Kolkata` / IST)
- **Portfolio:** [itzsaurav.github.io](https://itzsaurav.github.io/)
- **Email:** [sauravmishra9045@gmail.com](mailto:sauravmishra9045@gmail.com)
- **LinkedIn:** [linkedin.com/in/saurav-mishra-812259364](https://linkedin.com/in/saurav-mishra-812259364)
- **Resume:** [Saurav_Mishra_Resume.pdf](https://itzsaurav.github.io/Saurav_Mishra_Resume.pdf)
