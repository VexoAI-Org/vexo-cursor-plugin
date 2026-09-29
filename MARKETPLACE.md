# Marketplace listing draft

## Description

We're building Vexo for Cursor to turn spoken requests into completed coding tasks. Vexo's AI bracelet remembers the conversations, decisions, and context behind each request. The integration connects that context to Cursor's agents and models, with execution on Cursor-hosted cloud machines: implementing changes, running tests, and returning progress, results, and verified commit or pull-request links to the Vexo app. Users will be able to follow the work and request changes through Vexo, without managing a coding computer themselves.

## Release scope and status

There is one planned user release: the complete conversation-to-Cursor-execution-to-Vexo-results workflow. This repository holds the public plugin components; task dispatch, authorization and result synchronization belong in Vexo's private backend.

The integration is in development and has not passed end-to-end acceptance. The description presents the release we are building, not a claim that it is already available. Component validation does not establish that the full product is ready to ship.

The MCP URL in `mcp.json` is the existing production backend, not the studio preview service. On September 29, 2026, the Render API confirmed service `vexo-backend` is in the `Production` environment, has `NODE_ENV=production`, and uses `https://vexo-backend-uj6z.onrender.com` as its public base URL. Plugin development status and backend deployment environment are distinct. The [README](README.md#production-mcp-endpoint) records these details.

## Submission fields

- Name: Vexo
- Repository: https://github.com/VexoAI-Org/vexo-cursor-plugin
- Website: https://vexoai.com
- Logo: https://raw.githubusercontent.com/VexoAI-Org/vexo-cursor-plugin/main/assets/logo.svg
- Contact: haris@vexoai.com
- Support: support@vexoai.com
