from fasthtml.common import *

app, rt = fast_app(live_reload=True, debug=True)

# Project data - mapping of folder names to descriptions and metadata
PROJECTS = {
    "adk-agents": {
        "title": "ADK Agents",
        "description": "AI agent framework with specialized agents including Hacker News integration",
        "icon": "🤖",
        "category": "AI Agents",
        "status": "active",
    },
    "app": {
        "title": "Application Core",
        "description": "Main application library with swarm functionality and utilities",
        "icon": "⚡",
        "category": "Core Library",
        "status": "active",
    },
    "pocketflow-starter": {
        "title": "PocketFlow Starter",
        "description": "Starter template for PocketFlow machine learning workflows",
        "icon": "📊",
        "category": "ML/AI",
        "status": "template",
    },
    "spring-ai-starter": {
        "title": "Spring AI Starter",
        "description": "Java Spring Boot starter for AI integration and development",
        "icon": "☕",
        "category": "Java/AI",
        "status": "template",
    },
    "smolagents": {
        "title": "SmolAgents",
        "description": "Lightweight agent framework for simple AI interactions",
        "icon": "🔬",
        "category": "AI Agents",
        "status": "experimental",
    },
    "mcp-servers": {
        "title": "MCP Servers",
        "description": "Model Context Protocol servers for AI model integration",
        "icon": "🔌",
        "category": "Infrastructure",
        "status": "active",
    },
    "notebooks": {
        "title": "Jupyter Notebooks",
        "description": "Interactive notebooks for LLM experimentation and examples",
        "icon": "📓",
        "category": "Examples",
        "status": "active",
    },
}


@rt("/")
def get():
    TEXT_COLOR = "color: white;"
    return Titled(
        "",
        Style("""
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #000;
                min-height: 100vh;
                color: #333;
                line-height: 1.6;
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }

            .header {
                text-align: center;
                margin-bottom: 3rem;
                color: white;
            }

            .header h1 {
                font-size: 3rem;
                font-weight: 700;
                margin-bottom: 1rem;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }

            .header p {
                font-size: 1.2rem;
                opacity: 0.9;
                max-width: 600px;
                margin: 0 auto;
            }

            .projects-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 2rem;
                margin-bottom: 3rem;
            }

            .project-card {
                background: white;
                border-radius: 16px;
                padding: 2rem;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
            }

            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            }

            .project-header {
                display: flex;
                align-items: center;
                margin-bottom: 1rem;
            }

            .project-icon {
                font-size: 2.5rem;
                margin-right: 1rem;
            }

            .project-title {
                font-size: 1.5rem;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 0.5rem;
            }

            .project-category {
                font-size: 0.875rem;
                color: #718096;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }

            .project-description {
                color: #4a5568;
                margin-bottom: 1.5rem;
                line-height: 1.6;
            }

            .project-status {
                display: inline-block;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.75rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }

            .status-active {
                background: #c6f6d5;
                color: #22543d;
            }

            .status-template {
                background: #bee3f8;
                color: #2a4365;
            }

            .status-experimental {
                background: #fed7d7;
                color: #742a2a;
            }

            .footer {
                text-align: center;
                color: white;
                opacity: 0.8;
                margin-top: 3rem;
                padding-top: 2rem;
                border-top: 1px solid rgba(255,255,255,0.2);
            }

            .stats {
                display: flex;
                justify-content: center;
                gap: 2rem;
                margin-bottom: 2rem;
                flex-wrap: wrap;
            }

            .stat {
                background: rgba(255,255,255,0.1);
                padding: 1rem 2rem;
                border-radius: 12px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
            }

            .stat-number {
                font-size: 2rem;
                font-weight: 700;
                display: block;
            }

            .stat-label {
                font-size: 0.875rem;
                opacity: 0.8;
            }

            @media (max-width: 768px) {
                .container {
                    padding: 1rem;
                }

                .header h1 {
                    font-size: 2rem;
                }

                .projects-grid {
                    grid-template-columns: 1fr;
                    gap: 1.5rem;
                }

                .project-card {
                    padding: 1.5rem;
                }

                .stats {
                    flex-direction: column;
                    align-items: center;
                }
            }
        """),
        Div(
            H1("🚀 Aitudes Portfolio", style=TEXT_COLOR),
            P(
                "A comprehensive collection of AI and ML projects, frameworks, and tools for building intelligent applications",
                style=TEXT_COLOR,
            ),
            Div(
                Div(
                    Span(str(len(PROJECTS)), style=TEXT_COLOR),
                    Span(" Total Projects", style=TEXT_COLOR),
                    cls="stat",
                ),
                Div(
                    Span(
                        str(
                            len(
                                [
                                    p
                                    for p in PROJECTS.values()
                                    if p["status"] == "active"
                                ]
                            )
                        ),
                        style=TEXT_COLOR,
                    ),
                    Span(" Active Projects", style=TEXT_COLOR),
                    cls="stat",
                ),
                Div(
                    Span(
                        str(len(set(p["category"] for p in PROJECTS.values()))),
                        style=TEXT_COLOR,
                    ),
                    Span(" Categories", style=TEXT_COLOR),
                    cls="stat",
                ),
                cls="stats",
            ),
            Div(
                *[
                    Div(
                        Div(
                            Span(project["icon"], cls="project-icon"),
                            Div(
                                H3(project["title"], cls="project-title"),
                                Span(project["category"], cls="project-category"),
                            ),
                            cls="project-header",
                        ),
                        P(project["description"], cls="project-description"),
                        Span(
                            project["status"].title(), cls=f"status-{project['status']}"
                        ),
                        cls="project-card",
                    )
                    for project in PROJECTS.values()
                ],
                cls="projects-grid",
            ),
            Div(
                P("Built with FastHTML • Aitudes Framework", style=TEXT_COLOR),
                P(
                    "Explore the repository to dive deeper into each project",
                    style=TEXT_COLOR,
                ),
                cls="footer",
            ),
            cls="container",
        ),
    )


serve()
