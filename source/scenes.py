"""Scene list for "n8n AI Agent Tutorial for Beginners (Tagalog)".
Every screenshot is a REAL capture from the n8n 2.47.5 editor running locally (source/shots, 1440x675).
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1).
Narration is Taglish (fil-PH-AngeloNeural, synthetic voice). Numbers are written as digits without commas.
kind: shot (screenshot + highlight), zoom (enlarged crop of a screenshot), slide (drawn), pause (try-it-yourself countdown), comment (comment prompt)
"""
SYSTEM_MESSAGE = ("Ikaw si Reviewer Buddy. Sumagot sa Taglish. Kung math ang tanong, laging gamitin ang calculator tool at huwag mag-hula; "
                  "ibigay sa calculator ang BUONG expression sa isang tawag. Mga formula: final price = presyo * (1 - discount/100) * (1 + vat/100). "
                  "Ang X% ng N ay N * X / 100. Kung hindi math ang tanong, huwag gumamit ng calculator; sumagot nang normal.")

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="shot", chapter="Demo: AI agent na gumagamit ng calculator", img="s27_calculator-input-fixed", step="RESULTA",
         hl=[(78, 550, 305, 576), (788, 543, 1045, 567), (1108, 645, 1255, 667)],
         note=["Tanong: 18% discount sa 2450 pesos, tapos 12% VAT", "Sagot: 2250.08 pesos", "Gamit: Calculator tool"],
         say="Tingnan mo 'to. Tinanong ko ang AI agent ko: magkano ang final price kung 18 percent ang discount sa 2450 pesos, tapos dagdagan ng 12 percent na VAT? "
             "Hindi siya nag-hula. Ginamit niya ang Calculator tool, at ito ang tamang sagot: 2250 pesos at 8 centavos. "
             "Sa video na ito, matututo kang gumawa ng ganitong AI agent sa n8n, na gumagamit ng tools at may memory, kahit hindi ka marunong mag-code. "
             "Libre ang lahat ng gagamitin natin, at tumatakbo lang sa computer mo."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Agent vs chatbot, at ano ang kailangan", slide="agent_vs", step="SETUP",
         say="Una, ano ba ang AI agent? Ang chatbot, sumasagot lang. Ang workflow, sumusunod sa mga fixed na hakbang. "
             "Ang AI agent, siya mismo ang magpapasya kung anong tool ang gagamitin para masagot ang tanong mo."),
    dict(kind="slide", slide="needs", step="SETUP",
         say="Ang kailangan mo ay tatlong bagay. Una, ang n8n. Sa video na ito, version 2.47.5 ang gamit ko, at pinatakbo ko ito sa computer ko gamit ang npm. "
             "Pangalawa, ang Ollama, para sa local na AI model. Ang gamit natin ay llama 3.2, 3b. At pangatlo, wala nang API key, kaya walang bayad. "
             "Tatlong parte tayo: A, ang model at unang reply. B, ang tools. C, ang memory."),
    # ------------------------------------------------------------ 3. phase A
    dict(kind="shot", chapter="Phase A: Chat Trigger, AI Agent at model", img="s01_add-node-search-chat-trigger", step="PHASE A",
         hl=[(1072, 160, 1424, 200), (1056, 215, 1420, 290)], note=["Add first step", "I-type: chat trigger", "Piliin ang Chat > On new Chat event"],
         say="Gumawa ng bagong workflow. I-click ang Add first step, i-type ang chat trigger, piliin ang Chat, at piliin ang On new Chat event."),
    dict(kind="shot", img="s03_canvas-trigger-plus", step="PHASE A", hl=[(686, 296, 794, 404), (838, 330, 868, 366)],
         note=["Chat Trigger: dito papasok ang mga tanong", "Plus sa kanan: susunod na node"],
         say="Ito ang Chat Trigger. Dito papasok ang mga tanong natin. I-click ang plus sa kanan nito para magdagdag ng susunod na node."),
    dict(kind="shot", img="s04_search-ai-agent", step="PHASE A", hl=[(1056, 195, 1420, 260)], note=["I-type: AI Agent", "Piliin ang AI Agent"],
         say="Hanapin ang AI Agent, at piliin ito."),
    dict(kind="shot", img="s05_ai-agent-panel-slots", step="PHASE A", hl=[(520, 598, 900, 668)], note=["Chat Model: kailangan, ang utak", "Memory: idadagdag natin mamaya", "Tool: idadagdag din mamaya"],
         say="Tingnan ang ilalim ng AI Agent: Chat Model, Memory, at Tool. Ang Chat Model ay kailangan. Ito ang utak ng agent. Ang Memory at Tool ay idadagdag natin mamaya."),
    dict(kind="shot", img="s07_ollama-node-connect", step="PHASE A", hl=[(527, 142, 676, 170)], note=["Ollama Chat Model", "I-click: Connect to Ollama"],
         say="Piliin ang Ollama Chat Model, at i-click ang Connect to Ollama para gumawa ng credential."),
    dict(kind="shot", img="s08_credential-dialog-localhost", step="PHASE A", hl=[(412, 239, 1198, 274), (412, 331, 1198, 366)],
         note=["Base URL: ang address ng Ollama", "API Key: walang kailangan"],
         say="Ito ang credential. Ang Base URL ay ang address ng Ollama sa computer mo. Walang API key na kailangan. I-save natin."),
    dict(kind="shot", img="s09_credential-error-localhost", step="COMMON MISTAKE #1", hl=[(412, 206, 1184, 268)], note=["Couldn't connect with these settings", "Sa computer ko: localhost = ayaw sumagot"],
         say="Pero tingnan mo: Couldn't connect with these settings. Common mistake ito. Sa computer ko, hindi sumasagot ang Ollama sa localhost na dumadaan sa IPv6. "
             "Sinubukan ko ang 127.0.0.1, at gumana. Kaya ang ayos: palitan ang address."),
    dict(kind="shot", img="s10_credential-success-127", step="AYOS", hl=[(412, 206, 1184, 268), (412, 325, 1184, 360)], note=["http://127.0.0.1:11434", "Connection tested successfully"],
         say="Gamitin ang http colon slash slash 127.0.0.1 colon 11434. At lumabas na ang Connection tested successfully."),
    dict(kind="shot", img="s12_model-dropdown", step="PHASE A", hl=[(527, 206, 914, 296)], note=["Lumabas na ang model: llama3.2:3b"],
         say="Ngayon, lumabas na sa Model ang llama 3.2, 3b. Piliin ito."),
    dict(kind="pause", chapter="Pause and try", step="TRY IT", pause_q="I-connect ang 3 nodes:", pause_a=["Chat Trigger", "AI Agent", "Ollama Chat Model"], seconds=8,
         say="Pause and try. I-connect mo na ang tatlong nodes: Chat Trigger, AI Agent, at Ollama Chat Model. May walong segundo ka para tingnan ang sarili mong screen."),
    dict(kind="shot", img="s11_canvas-phase-a", step="PHASE A", hl=[(480, 195, 1050, 525)], note=["Ganito dapat ang itsura"],
         say="Ganito dapat ang itsura ng workflow mo."),
    dict(kind="shot", img="s16_first-reply", step="PHASE A", hl=[(80, 548, 340, 575), (477, 520, 740, 535)], note=["Hi! Sino ka?", "Sumagot sa loob ng mga 29 segundo"],
         say="Subukan natin. Nag-type ako ng Hi, sino ka? Sumagot siya, sa loob ng mga 29 segundo, dahil unang beses niyang nag-load ng model. Medyo nalito siya sa tanong. Maliit na model ito, kaya minsan nalilito. "
             "Chatbot pa lang ito. Gawin nating agent."),
    # ------------------------------------------------------------ 4. phase B
    dict(kind="shot", chapter="Phase B: tools at system message", img="s17_tool-search-calculator", step="PHASE B", hl=[(924, 276, 940, 298), (1056, 195, 1420, 245)],
         note=["Plus sa Tool", "I-type: Calculator"],
         say="I-click ang plus sa Tool, i-type ang Calculator, at piliin ito."),
    dict(kind="shot", img="s20_canvas-wikipedia", step="PHASE B", hl=[(880, 330, 1090, 460)], note=["Calculator at Wikipedia", "Dalawang tools na"],
         say="Idagdag din ang Wikipedia. Dalawang tools na ang agent natin: Calculator, at Wikipedia."),
    dict(kind="shot", img="s21_wrong-answer-2414", step="TEST 1", hl=[(80, 535, 360, 572), (763, 575, 1210, 602)], note=["Wala pang bagong instructions", "Sagot: 2414.72", "Dapat: 2250.08"],
         say="Subukan natin ang parehong tanong, pero wala pa tayong bagong instructions. Ang sagot niya: 2414 pesos at 72 centavos. Mali iyan. Ang tamang sagot ay 2250 pesos at 8 centavos."),
    dict(kind="zoom", img="s22_calculator-input-wrong", step="COMMON MISTAKE #2", crop=(760, 515, 1440, 670), hl=[(788, 543, 1045, 568), (1108, 645, 1255, 668)],
         caption="Input ng Calculator:  0.88 * 2450 + 0.12 * 0.88 * 2450", sub="Response: 2414.72  (mali ang expression, hindi ang Calculator)",
         say="Buksan ang Logs. Ito ang ipinasa ng agent sa Calculator: 0.88 times 2450, plus 0.12 times 0.88 times 2450. Gumamit siya ng 0.88 para sa 18 percent na discount. Dapat ay 0.82. "
             "Tama ang Calculator sa math. Ang mali ay ang expression na ibinigay ng agent. Common mistake ito: hindi inaayos ng tool ang maling instruction."),
    dict(kind="pause", chapter="Pause and try: ang tamang expression", step="TRY IT", pause_q="Ano ang tamang expression?", pause_a=["2450 * (1 - 18/100) * (1 + 12/100)", "= 2250.08"], seconds=8,
         say="Pause and try. Ano kaya ang tamang expression para sa 18 percent na discount, at 12 percent na VAT? May walong segundo ka para isulat sa papel."),
    dict(kind="shot", img="s24_system-message-default", step="PHASE B", hl=[(558, 472, 898, 520)], note=["Default: You are a helpful assistant", "Masyadong malabo"],
         say="Ang sagot ay nasa system message. Ito ang default: You are a helpful assistant. Masyadong malabo para sa math."),
    dict(kind="slide", slide="system_message", step="SYSTEM MESSAGE",
         say="Palitan natin ng malinaw na instructions. Ikaw si Reviewer Buddy. Sumagot sa Taglish. Kung math ang tanong, laging gamitin ang calculator at ibigay ang buong expression. "
             "Narito ang formula ng final price. At kung hindi math ang tanong, huwag gumamit ng calculator. Idinagdag ko ang huling linya dahil nalito ang maliit na model sa mga ordinaryong mensahe. "
             "Nasa description ang buong text, para ma-copy mo."),
    dict(kind="zoom", img="s27_calculator-input-fixed", step="TEST 2", crop=(760, 515, 1440, 670), hl=[(788, 543, 1120, 568), (1108, 645, 1280, 668)],
         caption="Input ng Calculator:  2450 * (1 - 18/100) * (1 + 12/100)", sub="Response: 2250.08  (tama!)",
         say="Subukan ulit ang tanong. Ito na ang expression sa Calculator: 2450 times, 1 minus 18 over 100, times, 1 plus 12 over 100. Ang resulta: 2250.08. Tama na. "
             "Pinatakbo ko ito ng dalawang beses na may refined na system message, at parehong tama."),
    # ------------------------------------------------------------ 5. phase C
    dict(kind="shot", chapter="Phase C: memory", img="s35_no-memory-forgets", step="BAGO ANG MEMORY", hl=[(178, 222, 320, 240), (943, 170, 1403, 200)],
         note=["Ano ang pangalan ko?", "Sagot: 'Reviewer Buddy'", "Hindi niya naalala si Ana"],
         say="Ngayon, ang memory. Sinabi ko ang pangalan ko, tapos tinanong ko: ano ang pangalan ko? Ang sagot niya: Reviewer Buddy. Hindi niya naalala. Kapag walang memory, hiwalay ang bawat mensahe."),
    dict(kind="shot", img="s30_memory-picker", step="PHASE C", hl=[(1066, 225, 1424, 270)], note=["Plus sa Memory", "For beginners: Simple Memory", "Walang credentials"],
         say="I-click ang plus sa Memory, at piliin ang Simple Memory. Nasa for beginners ito, at walang credentials na kailangan."),
    dict(kind="shot", img="s31_simple-memory-panel", step="PHASE C", hl=[(527, 228, 914, 285), (527, 462, 914, 512)], note=["Session ID: galing sa Chat Trigger", "Context Window Length: 5"],
         say="Ang Session ID ay galing sa Chat Trigger. Ang Context Window Length ay 5, ibig sabihin, ang huling limang interactions ang naaalala ng agent."),
    dict(kind="shot", img="s34_memory-remembers-ana", step="TEST 3", hl=[(178, 222, 320, 240), (943, 170, 1403, 200)], note=["Ano ang pangalan ko?", "Sagot: 'Ang pangalan mo ay Ana.'"],
         say="Sinubukan ko ulit. Sinabi kong Ana ang pangalan ko, tapos tinanong ko ulit. Ang sagot: Ang pangalan mo ay Ana. Naalala na niya. "
             "May kakaiba pa rin siyang pambungad na Kumpleto ang sagot, dahil maliit na model ito, pero tama ang laman."),
    dict(kind="comment", step="COMMENT", comment_q="Anong tool ang gusto mong idagdag sa agent mo?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong tool ang gusto mong idagdag sa agent mo? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 6. verification
    dict(kind="shot", chapter="Test at executions", img="s33_executions-list", step="VERIFICATION", hl=[(66, 170, 312, 630)], note=["Lahat ng takbo ay nakatala", "I-click ang isa para tingnan ang tools"],
         say="Lahat ng test ay nakatala sa Executions. Makikita mo ang bawat takbo, ang oras, at pwede mong buksan ang isa para tingnan kung anong tool ang ginamit."),
    dict(kind="slide", slide="results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Wala pang malinaw na instruction: 2414.72, mali. Pagkatapos ng malinaw na system message: 2250.08, tama. "
             "Walang memory: Reviewer Buddy. May memory: Ana. Tandaan: maliit na model ito, kaya minsan nalilito. Para mas maaasahan, gumamit ng mas malaking model."),
    # ------------------------------------------------------------ 7. exit ramp
    dict(kind="slide", chapter="Next: i-connect sa Telegram", slide="next", step="SUSUNOD",
         say="Ngayong kaya nang gumamit ng tools ng agent mo, i-click ang video sa screen para ikabit ito sa Telegram, at gumawa ng sarili mong AI bot. Nasa description ang workflow file."),
]
