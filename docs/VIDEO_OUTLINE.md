# Video 1 outline: n8n AI Agent Tutorial for Beginners (Tagalog)

Built with the `youtube-video-blueprint` structure. Length target: about 10 minutes. Pillar: programming and AI tutorials (December batch). Playlist: "AI Automation with n8n (Tagalog)".

## Search wording (checked 2026-11-12, YouTube suggestions, Philippines)
"n8n tutorial for beginners tagalog", "ai agent tutorial n8n", "ai agent tutorial for beginners", "ai agent tutorial python", "build ai chatbot with n8n", "n8n tutorial 2026". Suggestions show what people type, not volume. Re-check the top 5 results before recording.

## The project: "Reviewer Buddy" agent
A chat agent that answers in Taglish, **uses a Calculator tool for any math** (so it never guesses), looks things up on Wikipedia, and remembers the conversation. It ties to your exam-prep audience (percent and discount questions) while teaching the general skill: chat trigger, model, tools, memory.

Why this project: the failure is easy to show and real. A language model without the Calculator tool can get multi-step arithmetic wrong; with the tool it is correct. That is the gotcha, the verification and the Short in one.

## Title
- **n8n AI Agent Tutorial for Beginners (Tagalog): Build an AI Assistant That Uses Tools** (recommended, 85 characters)
- n8n AI Agent Tutorial (Tagalog): Chat, Tools and Memory in 10 Minutes
- How to Build an AI Agent in n8n for Free (Tagalog, Step by Step)

## Stages and timestamps (10 min)
| Stage | Time | Content |
|---|---|---|
| 1. Proof hook | 0:00 to 0:40 | The finished agent in the n8n chat. Ask: "Magkano ang final price kung 18% discount sa 2,450, tapos dagdagan ng 12% VAT?" The execution panel shows the Calculator tool being called, and the right answer. Outcome sentence: "Sa video na ito, matututo kang gumawa ng AI agent sa n8n na gumagamit ng tools at may memory, kahit hindi ka marunong mag-code." |
| 2. Setup | 0:40 to 1:45 | One slide: agent vs chatbot vs workflow (an agent decides which tool to use). Prerequisites checklist: n8n running (self-hosted or a cloud account), one free AI model key. Roadmap: A, model and first reply. B, tools. C, memory and testing. |
| 3. Core walkthrough | 1:45 to 7:00 | Phase A (1:45 to 3:15): new workflow, Chat Trigger, AI Agent node, Chat Model node with credentials, first reply. Phase B (3:15 to 5:30): add Calculator and Wikipedia tools, write the system message (role, Taglish replies, "always use the Calculator for math"). **Gotcha (about 4:40):** the agent ignores a tool when the instruction or tool description is vague; show the wrong behavior, then the fix. Phase C (5:30 to 7:00): add the memory node, set the session, test "ano yung sagot mo kanina?". |
| 4. Verification | 7:00 to 9:00 | Three real tests in the chat, with the Executions view showing each tool call. One planned failure: remove the Calculator tool, get a wrong answer on the discount question, add it back, get the right one. Second failure: forget the memory node, the agent forgets the name; fix it. Show where to read the error if the credential fails. Replay the finished agent. |
| 5. Exit ramp | 9:00 to 10:00 | One-sentence recap inside the handoff. Last sentence: "Ngayong kaya nang gumamit ng tools ng agent mo, i-click ang video sa screen para ikabit ito sa Telegram at gumawa ng sarili mong AI bot." No "thanks for watching". End screen over the last 15 to 20 seconds. |

## Chapters (draft; times come from the real recording)
0:00 Demo: AI agent na gumagamit ng calculator
0:40 Agent vs chatbot, at ano ang kailangan
1:45 Gumawa ng workflow: Chat Trigger at AI Agent
3:15 Dagdagan ng tools: Calculator at Wikipedia
4:40 Common mistake: hindi ginagamit ng agent ang tool
5:30 Memory: para maalala ang usapan
7:00 Test, mali at ayos: Calculator removed, memory removed
9:00 Next: i-connect sa Telegram

Each chapter is 10 seconds or longer and starts at 0:00.

## Metadata draft
**Description, first lines (about 150 characters):**
"Learn how to build an AI agent in n8n step by step (Tagalog): connect a free AI model, add tools like Calculator and Wikipedia, and give it memory."

**You'll learn:**
- The difference between a chatbot, a workflow and an AI agent
- Chat Trigger, AI Agent and Chat Model nodes in n8n
- Adding tools (Calculator, Wikipedia) and writing a system message that makes the agent use them
- Adding memory, and testing and fixing the agent when it gives a wrong answer

Then chapters, then resources (workflow JSON on GitHub, the n8n docs, the playlist, the next video), then `#n8n #AIAgent #Tagalog`. Disclosures after: independent tutorial, not affiliated with n8n or any AI provider; synthetic voice if used; API keys on screen are hidden.

**Tags (9):** n8n ai agent tutorial, n8n tutorial for beginners tagalog, ai agent tutorial tagalog, n8n tutorial, n8n ai agent, n8n chat trigger, ai automation tagalog, free ai agent, SirYuls TV

**Thumbnail:** the tool or problem, not the title. Original node graphic (Chat, AI Agent, Calculator, Memory) with 3 to 4 words: "AI THAT USES TOOLS". Draw it yourself; do not use the n8n logo.

**Pinned comment:** workflow JSON link, the system message text to copy, and "Anong tool ang gusto mong idagdag sa agent mo?". Next-part link.

## Shorts (cut from the video, each sets Related video to this one)
1. **The gotcha:** "Bakit mali ang sagot ng AI mo sa math? Bigyan mo ng Calculator tool." 25 to 30 seconds, before and after.
2. **Agent vs chatbot in 20 seconds.**
3. **The system message that makes the agent use its tools** (show the 3 lines).

## Playlist "AI Automation with n8n (Tagalog)" (3 parts)
1. This video: AI agent with tools and memory
2. Telegram AI bot with n8n (the handoff target)
3. Agent plus Google Sheets, a study tracker or a RAG chatbot

## Production
- **Screen recording, not slides.** n8n is a visual editor, so record the real screen (OBS or similar) and the real execution results. Label anything illustrative on screen.
- **Voice (decide):** Tagalog or Taglish narration. The Piper "ryan" voice used in your series is English only, and I have not verified a good Tagalog text-to-speech voice, so recording your own voice is the safe choice. Keep technical terms in English (node, tool, memory) and explain in Taglish.
- **Presenter and pipeline:** Sir Yuls can be added to the finished screen recording with `D:\MIT\series-tools\efcore\presenter.py` (keep the lower right clear).
- **Run order before filming:** install n8n, create the free API key, build the finished workflow once, export it, then record. Export the workflow JSON to GitHub.
- **Keys:** never show an API key. Use the credentials screen with the key blurred, and tell viewers to revoke a key they ever leak.
- **Versions:** n8n's interface, the free limits of AI providers and the node names change often. Show the version on screen, and check the free-tier limits on the provider's page the day you record.

## Decisions (2026-11-12: recommendations accepted; change any of them and the outline adapts)
1. **Language: Taglish.** Narrate in Taglish and keep UI and technical words in English (node, tool, memory, credentials). Title and tags stay English plus "Tagalog". Record your own voice.
2. **n8n: local install.** Free and it does not expire for viewers. Show the install in the setup section (needs Node.js, or Docker as the alternative).
3. **AI model: one free cloud provider, with Ollama as an optional offline note.** Use one provider with a free tier for the whole video (Google's Gemini through AI Studio is the suggested one). Check its free limits and the n8n model-node name on the day you record, and say on screen that limits can change.

## Recording-day checklist (verify each step on your machine before filming; menus and names change)
- [ ] Install n8n locally (Node.js route or Docker route) and note the version for the on-screen caption
- [ ] Create the free API key; store it only in n8n credentials; plan to blur or crop it on screen and revoke it after the shoot
- [ ] Build the finished workflow once: Chat Trigger, AI Agent, Chat Model, Calculator, Wikipedia, memory
- [ ] Write the system message (role, Taglish replies, "always use the Calculator tool for math") and save it as text for the pinned comment
- [ ] Rehearse the three tests and both planned failures; confirm the failures really happen with your model (if the model gets the discount question right without the tool, pick a harder multi-step question and re-check)
- [ ] Export the workflow JSON, remove credentials from it, and put it on GitHub for the description
- [ ] Record the screen at 1920x1080 with the n8n zoom large enough to read on a phone; keep the lower right clear for Sir Yuls
- [ ] Record the voiceover after the screen capture, in Taglish, 6 to 8 short takes by chapter
- [ ] Cut the three Shorts from the gotcha and the finished agent

## Pre-publish checklist (from the cheat sheet)
- [ ] Result and outcome sentence within 45 seconds
- [ ] A gotcha in the middle, and one failure and its fix in verification
- [ ] Ending names the next video; no wrap-up phrases
- [ ] Description opens with the keyword sentence; chapters start at 0:00
- [ ] 5 to 10 tags including SirYuls TV; thumbnail does not repeat the title
- [ ] Shorts cut and Related video set; end screen planned
- [ ] Upload kit generated (`source/make_kit.py`, `upload-kit/index.html`)
