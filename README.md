# Vexo for Cursor

Bring the context from your conversations into your coding workflow.

[Vexo](https://vexoai.com) is an AI bracelet that remembers conversations and helps you follow through. This plugin connects Cursor to your Vexo account so you can find what was discussed and use it while planning or implementing your work.

Examples:

- “What did we decide about onboarding yesterday?”
- “Find the conversation where we discussed the checkout issue.”
- “Use our discussion about notifications to draft an implementation brief.”

## What is included

- A remote MCP connection to Vexo's existing service.
- `vexo-context`: retrieve relevant conversation context with dates and times when available.
- `vexo-brief`: turn that context into a grounded implementation brief.

The plugin is read-only with respect to Vexo data. Cursor can help plan or edit code when you request it; the connector itself does not run background tasks or write to Vexo.

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
