# Script (Taglish) for "n8n AI Agent Tutorial for Beginners (Tagalog)"

Draft written before the screen capture. Lines marked [SHOT] need a real n8n screen; [PAUSE] is a pause-and-try prompt with a countdown; [COMMENT] is an on-screen comment prompt. The final wording is adjusted to what the real captures show (the real model replies and tool calls are shown as they happened, nothing is invented).

Narration: fil-PH-AngeloNeural (synthetic voice, disclosed). Technical words stay in English.

## 0:00 Proof hook
[SHOT: chat panel, the discount question, the Calculator tool call, the answer]
"Tingnan mo 'to. Tinanong ko ang AI agent ko: magkano ang final price kung 18 percent ang discount sa 2,450 pesos, tapos dagdagan ng 12 percent na VAT? Hindi siya nag-hula. Ginamit niya ang Calculator tool, at ito ang tamang sagot. Sa video na ito, matututo kang gumawa ng ganitong AI agent sa n8n na gumagamit ng tools at may memory, kahit hindi ka marunong mag-code. At libre lahat ng gagamitin natin."

## 0:40 Setup
[SLIDE: chatbot vs workflow vs agent]
"Una, ano ba ang AI agent? Ang chatbot, sumasagot lang. Ang workflow, sumusunod sa fixed na steps. Ang AI agent, siya mismo ang magpapasya kung anong tool ang gagamitin para masagot ang tanong mo."
[SLIDE: kailangan natin]
"Ang kailangan mo: n8n na naka-install sa computer mo, at isang AI model. Gagamit tayo ng local model na tumatakbo sa Ollama, kaya walang API key at walang bayad. Tatlong parte tayo: A, ang model at unang reply. B, ang tools. C, ang memory at testing."

## 1:45 Phase A: workflow, Chat Trigger, AI Agent, Chat Model
[SHOT: new workflow, add Chat Trigger]
"Gumawa ng bagong workflow. I-click ang plus, hanapin ang Chat Trigger. Dito papasok ang mga tanong natin."
[SHOT: add AI Agent, connect]
"Susunod, i-add ang AI Agent node at ikabit sa Chat Trigger."
[SHOT: Ollama Chat Model, credential base URL, model]
"Ang AI Agent ay kailangan ng utak, ang Chat Model. Piliin ang Ollama Chat Model. Sa credentials, ang base URL ay localhost, port 11434, at piliin ang model na llama 3.2. Wala tayong secret key dito."
[SHOT: first chat reply]
"Subukan natin: mag-hi tayo. Sumagot na siya. Chatbot pa lang ito. Gawin nating agent."
[PAUSE: Pause and try: i-connect mo na ang Chat Trigger, AI Agent at Ollama model]

## 3:15 Phase B: tools and system message
[SHOT: + under Tools, Calculator and Wikipedia]
"Sa Tool ng AI Agent, i-click ang plus. Idagdag ang Calculator, at ang Wikipedia."
[SHOT: system message in Options]
"Ngayon, ang system message. Dito mo sasabihin sa agent kung ano siya at paano gagamitin ang tools. Isulat: Ikaw si Reviewer Buddy. Sumagot sa Taglish. Para sa kahit anong math, laging gamitin ang Calculator tool. Huwag mag-hula."

## 4:40 Gotcha
[SHOT: wrong behavior, then the fix]
"Common mistake dito: hindi ginagamit ng agent ang tool kapag malabo ang instruction. Tingnan mo, ito ang sagot niya kapag wala ang linya tungkol sa Calculator. [real result]. Pagkatapos naming idagdag ang malinaw na instruction, ito ang resulta. [real result]. Tandaan: ang malinaw na system message ang nagpapagamit ng tools."

## 5:30 Phase C: memory
[SHOT: add Simple Memory, session]
"Para maalala niya ang usapan, magdagdag ng Simple Memory sa Memory ng AI Agent."
[SHOT: follow-up test]
"Sabihin natin ang pangalan mo, tapos itanong: ano ang pangalan ko? Naalala niya. [real result]"
[COMMENT: Anong tool ang gusto mong idagdag sa agent mo? I-comment mo.]

## 7:00 Verification
[SHOT: three tests with the Executions view and the tool calls]
"Subukan natin ng tatlong test. Test one, ang discount question. Test two, tanong tungkol sa Wikipedia. Test three, follow-up gamit ang memory. Tingnan ang Executions para makita kung anong tool ang ginamit."
[SHOT: planned failure, remove Calculator, wrong or different answer, restore]
"Para makita ang pagkakaiba: tinanggal ko ang Calculator tool. [real result]. Ibinalik ko, at tama ulit. [real result]."
[SHOT: error case, wrong base URL or model not found, where to read it]
"Kung may error, tingnan ang execution at basahin ang message. Madalas, mali ang base URL o wala pang naka-pull na model."

## 9:00 Exit ramp
[SLIDE: next video]
"Ngayong kaya nang gumamit ng tools ng agent mo, i-click ang video sa screen para ikabit ito sa Telegram at gumawa ng sarili mong AI bot."
