# Vexo for Cursor

Turn conversations into working code with Cursor.

[Vexo](https://vexoai.com) is an AI bracelet that remembers conversations and helps you follow through. This plugin brings relevant conversation context into Cursor so its agent can implement requested changes, run tests, and report what it actually completed.

Examples:

- “What did we decide about onboarding yesterday?”
- “Find the conversation where we discussed the checkout issue.”
- “Use our discussion about notifications to draft an implementation brief.”
- “Implement the onboarding changes we discussed yesterday and run the relevant tests.”

## What is included

- A remote MCP connection to Vexo's existing service.
- `vexo-context`: retrieve relevant conversation context with dates and times when available.
- `vexo-brief`: turn that context into a grounded implementation brief.
- `vexo-execute`: use that context to implement a requested task with Cursor's coding tools, validate changes, and report results.

## Execution and integration status

Cursor performs code edits and runs commands with the permissions of its current session. Vexo's existing MCP connection retrieves conversation context; its `vexo:read` scope describes access to Vexo records, not a restriction on Cursor's coding tools. Publishing changes follows the user's task authorization.

The broader integration is intended to let Vexo dispatch coding tasks identified in conversation to Cursor, execute them on the user's cloud computer, and return progress, changes, test results, and verified commit or PR links to Vexo.

That background execution connection is not implemented by this package yet. The current package provides conversation retrieval and command instructions for an active Cursor session. It has no background task dispatcher, task-claim API, result synchronization, or Cursor usage accounting. Installing the plugin does not provision Cursor model access or API credentials. Authenticated end-to-end acceptance testing remains pending.

For Vexo-managed execution, the backend must connect its durable task system to a supported Cursor runtime. Cursor documents a [TypeScript SDK](https://cursor.com/docs/sdk/typescript) with local and cloud runtimes, a [headless CLI](https://cursor.com/docs/cli/headless), and a [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints). The SDK's local runtime is a candidate for execution on an existing Vexo cloud computer; compatibility, account access, isolation, cancellation, recovery and usage accounting must be validated before production use. Marketplace distribution and programmatic execution are separate parts of the integration.

## Requirements and sign-in

You need Cursor with plugin support and an existing Vexo account with captured data. Use the normal Vexo sign-in and approval flow presented by the MCP client. The server advertises OAuth authorization-code flow with PKCE and dynamic client registration; there is no shared API key in this package.

The MCP endpoint is:

```text
https://vexo-backend-uj6z.onrender.com/mcp
```

This is a draft package pending marketplace submission and a complete authenticated Cursor acceptance test. It is not yet available through marketplace search.

For local testing, copy this directory into `~/.cursor/plugins/local/vexo`, reload Cursor, and check the plugin components under Customize. The local copy must be a real directory; do not use a symlink pointing outside the local plugin directory. Local plugin imports must be permitted by your organization. Follow [Cursor's plugin instructions](https://cursor.com/docs/plugins).

## Connection details

```json
{
  "mcpServers": {
    "vexo": {
      "type": "http",
      "url": "https://vexo-backend-uj6z.onrender.com/mcp"
    }
  }
}
```

The current server implements transcript search, transcript-day listing and retrieval, and voice-logged records. Its existing `vexo:read` authorization scope also covers additional read-only profile, activity, and logged-data tools. This plugin's conversation-focused commands do not narrow that server-side scope. Review the Vexo consent screen before connecting.

Retrieved data is provided to the Cursor session to answer your request. The package contains no account credentials, recordings, or backend source code. Revoke the connection through Vexo's connection controls when it is no longer needed. Do not publish personal access links or tokens in an MCP configuration.

## Validation

Run `python3 scripts/validate.py` to check package structure. Public endpoint checks verify OAuth discovery and rejection of unauthenticated MCP requests; they do not establish that authenticated tool calls succeed. Before submission, complete sign-in from Cursor, test a transcript search on the intended account, and verify revocation.

Support: support@vexoai.com
