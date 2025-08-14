System Message Guidelines for Customer Success Bot
1. Purpose
The system message defines how the LLM should behave when responding to customers. It is loaded once at the start of a conversation and governs how all replies are generated within that session.
2. System Behavior
- The LLM receives the system message once, per session.
- It has no memory of prior responses or other users.
- Each customer message is handled independently using only the current system message and user input.
- Never include instructions that rely on past interaction (not in the current chat) or future memory.
3. Use Plain Text Format
All system messages must be written in clean, plain text, not XML or JSON.

Reasons:
- Easier for the LLM to interpret and follow
- Easier for humans to read and edit
- Looks better and cleaner in front-end debugging or UI preview
4. Offer Information Placeholder
Use the ${offer-info} placeholder once in the system message. This will be replaced by the actual product data before the message is sent to the LLM.

- Do not reference ${offer-info} multiple times.
- Assume the inserted content will be long — place it at the end.
- Instruct the LLM to use details from "the product information below" when relevant.
5. What Not to Include
Avoid any instructions that assume the LLM can:
- Vary responses over time
- Rotate opening lines
- Avoid repeating past replies
- Track previous conversations
- Know what it said to other customers

These assumptions are incorrect.
The LLM only sees:
- The current system message
- The current user's message
- The chat history within this single conversation

It does not have access to:
- Other user sessions
- Its own past replies to other customers
- Any memory of previous uses of the system message

If variation is needed (e.g. different opening lines):
Include a list of approved phrases, and have the application randomly pick one before sending the system message. The LLM will only see the selected version.

Offer Creation Guidelines

These guidelines define how to create offer instances used by the AI Agent.
Purpose:
Offers provide data that the chatbot uses once a user’s intent has been linked to a specific offer. The chatbot then personalizes the system message and response accordingly.
How It Works:
System Message: Base instructions for chatbot behavior (defined per chatbot config).
Offer Matching: Semantic vector search links user input to the most relevant offer.
Clarification: If needed, chatbot asks questions to confirm intent.
Offer Injection: When confidence is high, matched offer data is used to enrich the system message and replies.
Offer Structure:
Offer Name:
Must match the actual product/service name. This is used directly in chatbot replies, so accuracy is critical.
Description (optional):
Not used by the chatbot. Can be used internally for notes, tags, or labels.
AI Context:
Plain text only. Include only factual, concise details about the offer (e.g. price, duration, limitations, features). This is injected into the system message.
Short URL usage in AI Context:
Noticed that it is better to to use “Offer URL: ${short-url}” at the very end of the AI context field (let’s do it manually for now, I will later input it by default from backend.)
Keywords/Phrases (optional):
To boost semantic search accuracy.
Do Not:
Include details not directly tied to the offer.
Use non-text formatting (HTML, markdown, etc.).
