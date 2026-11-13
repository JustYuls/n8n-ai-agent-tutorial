"""Scene list for Part 2: "n8n Chatbot for Your Website (Tagalog)".
Real captures from n8n 2.47.5 running locally (source/shots_part2, 1037x649 browser captures) of the SAME Reviewer Buddy workflow from Part 1.
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1). Narration is Taglish (synthetic voice). Numbers as digits, no commas.
Telegram is not used in this part (not installed on the author's PC); a hosted chat page and an embedded widget are used instead.
"""
NAME = "02_n8n-chatbot-website-tagalog"
SYSTEM_MESSAGE = ""
MIXED = False  # pure Filipino voice (user request); set True for English terms in an English voice
EN_TERMS = [
    # quoted on-screen English text
    "Chat will be live at the URL above once this workflow is published", "You can now make calls to your production chat URL", "Workflow published",
    "follow the instructions to embed chat in a webpage, or just call the webhook URL", "Make Chat Publicly Available", "Succeeded in 18 point 635 seconds",
    # spoken code and commands
    r"(?:http colon slash slash 127\.0\.0\.1 colon 8080)", r"(?:python -m http\.server 8080)", "dash dash color dash dash primary",
    # technical words that stay in English
    r"(?:version \d+(?:\.\d+)*)", "AI agent", "AI", "n8n", "Ollama", "Hosted Chat", "Embedded Chat", "Embedded chat", "Chat Trigger", "Chat URL", "Initial Messages", "Initial Message",
    "AI Agent", "Calculator", "Wikipedia", "webhook URL", "webhook", "localhost", "Authentication", "Published", "Publish", "Executions", "execution",
    "system message", "workflow", "widget", "createChat", "webhookUrl", "mode", "window", "stylesheet", "script", "CSS variables", "CSS", "HTML", "Python", "Chrome", "Excel", "Telegram",
    "Pause and try", "Common mistake", "Taglish", "Phase", "Part 1", "Part 3", "Mode", "Reviewer Buddy", "main", "layout", "None", "URL", "web chat", "chat link",
    "web page", "chat page", "web server", "Logs", "memory", "tools", "tool", 
]

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="shot", chapter="Demo: chatbot sa sarili kong web page", img="p14", step="RESULTA",
         hl=[(636, 317, 989, 397), (636, 413, 898, 469), (957, 569, 1021, 633)],
         note=["Sarili kong web page", "Tanong: 18% discount sa 2450 pesos + 12% VAT", "Sagot: 2250.08 pesos, galing sa n8n agent"],
         say="Tingnan mo 'to. Ito ang sarili kong web page, at ang chat sa kanan ay ang AI agent na ginawa natin sa n8n. Tinanong ko ulit: magkano ang final price kung 18 percent na discount sa 2450 pesos, tapos 12 percent na VAT? "
             "Ang sagot: 2250 pesos at 8 centavos. Tama. Sa video na ito, matututo kang maglagay ng chatbot sa web page mo gamit ang agent mo, kahit walang Telegram at kahit hindi ka marunong mag-code."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Ano ang kailangan, at bakit hindi Telegram", slide="p2_needs", step="SETUP",
         say="Ang kailangan mo ay ang workflow mula sa Part 1, ang n8n na tumatakbo, at ang Ollama. Kung wala pa, nasa description ang link ng setup guide at ng workflow file. "
             "Ang plano ko sana ay Telegram. Pero wala akong naka-install na Telegram sa computer na ito, kaya gumawa ako ng mas simpleng paraan: isang web chat. Wala itong kailangang account sa ibang app."),
    dict(kind="slide", slide="chat_options", step="SETUP",
         say="May dalawang paraan sa n8n. Una, ang Hosted Chat: may chat page na na mismong n8n ang nagseserbisyo. Wala kang gagawin na code. Pangalawa, ang Embedded Chat: ikaw ang gagawa ng page, at ilalagay mo ang chat widget. "
             "Gagawin natin ang dalawa, at magsisimula tayo sa pinakamadali."),
    # ------------------------------------------------------------ 3. hosted chat
    dict(kind="shot", chapter="Phase A: Hosted Chat at Publish", img="p01", step="PHASE A", hl=[(257, 182, 358, 285)], note=["Buksan ang workflow mula sa Part 1", "Double-click ang Chat Trigger"],
         say="Buksan ang workflow mula sa Part 1. Ito pa rin ang Chat Trigger, AI Agent, Ollama, memory, at ang dalawang tools. Walang babaguhin sa agent. I-double-click ang Chat Trigger."),
    dict(kind="shot", img="p02", step="PHASE A", hl=[(41, 125, 201, 169)], note=["Make Chat Publicly Available", "Naka-off pa"],
         say="Nandito ang switch na Make Chat Publicly Available. Naka-off pa ito, kaya ang chat ay para lang sa loob ng editor."),
    dict(kind="shot", img="p03", step="PHASE A", hl=[(41, 246, 81, 268), (57, 150, 474, 193), (41, 355, 474, 402)],
         note=["I-on ang switch", "Lumabas ang Chat URL", "Live lang kapag Published"],
         say="I-on ito. Lumabas ang Chat URL. At basahin ang dilaw na kahon: Chat will be live at the URL above once this workflow is published. Ibig sabihin, hindi pa gagana ang link hangga't hindi mo pina-publish ang workflow. Tandaan ito."),
    dict(kind="shot", img="p04", step="PHASE A", hl=[(41, 346, 474, 424)], note=["Initial Message(s)", "Isang linya bawat mensahe"],
         say="Pwede mo ring palitan ang Initial Messages, ang unang bati ng chat. Nilagyan ko ng Taglish na bati: Kumusta! Ako si Reviewer Buddy."),
    dict(kind="shot", img="p05", step="PHASE A", hl=[(293, 230, 744, 264), (671, 455, 744, 489)], note=["I-click ang Publish sa taas", "Bigyan ng pangalan ang version", "I-click ang Publish"],
         say="Isara ang node, i-click ang Publish sa taas, bigyan ng pangalan ang version, at i-click ang Publish."),
    dict(kind="shot", img="p06", step="PHASE A", hl=[(289, 210, 748, 330), (663, 382, 724, 416)], note=["You can now make calls to your production chat URL", "Got it"],
         say="Lumabas ang Workflow published: You can now make calls to your production chat URL. Ngayon, live na ang link."),
    dict(kind="pause", chapter="Pause and try", step="TRY IT", pause_q="Gawin sa sarili mong screen:", pause_a=["I-on ang Make Chat Publicly Available", "I-publish ang workflow", "Kopyahin ang Chat URL"], seconds=8,
         say="Pause and try. Sa sarili mong screen, i-on ang public chat, i-publish ang workflow, at kopyahin ang Chat URL. May walong segundo ka."),
    dict(kind="shot", img="p07", step="PHASE A", hl=[(16, 438, 439, 566), (0, 585, 1037, 649)], note=["Bagong tab, i-paste ang Chat URL", "Lumabas ang sarili nating bati", "I-type ang tanong dito"],
         say="Magbukas ng bagong tab, at i-paste ang Chat URL. Ito na ang chat page, na galing mismo sa n8n. Nandito ang sarili nating bati. Subukan natin."),
    dict(kind="shot", img="p08", step="TEST 1", hl=[(358, 438, 1021, 494), (16, 510, 279, 566)], note=["Parehong tanong tungkol sa discount at VAT", "Sagot: 2250.08"],
         say="Pareho ang tanong: 18 percent na discount sa 2450 pesos, at 12 percent na VAT. Ang sagot: 2250 pesos at 8 centavos. Tama, at walang code na isinulat. "
             "Pero para siyang n8n page. Gusto natin sa sarili nating web page."),
    # ------------------------------------------------------------ 4. embedded
    dict(kind="shot", chapter="Phase B: Embedded Chat sa sarili mong page", img="p09", step="PHASE B", hl=[(62, 418, 420, 472)], note=["Mode: Hosted Chat", "Palitan ng Embedded Chat"],
         say="Bumalik sa Chat Trigger. Sa Mode, palitan ang Hosted Chat ng Embedded Chat. Ito ang para sa widget na ilalagay mo sa sarili mong page."),
    dict(kind="shot", img="p10", step="PHASE B", hl=[(41, 248, 474, 282), (41, 293, 474, 355)], note=["Embedded Chat", "Ang URL sa taas pa rin ang gagamitin", "I-publish ulit"],
         say="Sinasabi ng n8n: follow the instructions to embed chat in a webpage, or just call the webhook URL. Pareho pa rin ang URL. I-publish ulit ang workflow, dahil may binago tayo."),
    dict(kind="slide", slide="embed_code", step="PHASE B",
         say="Ito ang buong code ng page ko. Una, ang stylesheet at ang script ng n8n chat widget. Ginamit ko ang version 1.46.4, at naka-pin ang version para hindi masira ang page kapag may bagong labas. "
             "Pangalawa, ang createChat. Ang webhookUrl ay ang Chat URL na kinopya mo. Ang mode na window ay ang bubble sa ibabang kanan. Nasa description ang buong file."),
    dict(kind="terminal", step="PHASE B", title="Windows PowerShell", note="Local lang",
         lines=[("cmd", "cd chat-page"), ("cmd", "python -m http.server 8080 --bind 127.0.0.1"), ("ok", "Serving HTTP on 127.0.0.1 port 8080"), ("note", "Buksan: http://127.0.0.1:8080")],
         say="Para buksan ang page, gumamit ako ng simpleng web server ng Python. Pumunta sa folder, at patakbuhin ang python -m http.server 8080. Pagkatapos, buksan ang http colon slash slash 127.0.0.1 colon 8080 sa Chrome."),
    dict(kind="shot", img="p11", step="PHASE B", hl=[(139, 60, 850, 185), (957, 569, 1021, 633)], note=["Ang page ko", "Ang chat bubble sa ibabang kanan"],
         say="Ito ang page ko, at nandoon na ang chat bubble sa ibabang kanan. Rosas ito dahil default na kulay ng widget. Gusto kong dilaw."),
    dict(kind="shot", img="p12", step="COMMON MISTAKE #1", hl=[(640, 50, 1020, 552)], note=["Dilaw na ang bubble, pero sira ang chat window", "Nagtatago ang laman sa loob ng kahon"],
         say="Binago ko ang kulay gamit ang CSS variables, at dilaw na ang bubble. Pero tingnan mo ang chat window: sira ang layout, at nagtatago ang laman sa loob ng isang maliit na kahon. Common mistake ito. "
             "Dalawa ang naging problema ko. Una, ang tamang pangalan ng variable ay may dalawang gitling: dash dash color dash dash primary. Pangalawa, ang CSS ko para sa main at sa p ay tumama rin sa loob ng widget, dahil main din ang gamit niya."),
    dict(kind="shot", img="p13", step="AYOS", hl=[(619, 16, 1021, 552)], note=["Nilagyan ko ng class ang main ko: main.page", "Ngayon, buo na ang chat window"],
         say="Ang ayos: nilagyan ko ng class na page ang sarili kong main, at doon ko lang inilapat ang style. Ayan, buo na ang chat window, at nandoon ang Taglish na bati."),
    dict(kind="shot", img="p14", step="TEST 2", hl=[(636, 317, 989, 397), (636, 413, 898, 469)], note=["Sa loob ng sarili kong page", "Sagot: 2250.08 ulit"],
         say="Subukan natin sa loob ng widget. Parehong tanong, at ang sagot: 2250 pesos at 8 centavos. Tama ulit. Mga 20 segundo ang sagot dahil lokal na model ito sa computer ko."),
    # ------------------------------------------------------------ 5. verification
    dict(kind="shot", chapter="Executions at mga paalala", img="p15", step="VERIFICATION", hl=[(372, 88, 706, 130), (800, 437, 878, 517)], note=["Succeeded in 18.635s", "Version: Embedded chat", "Ginamit ang Calculator"],
         say="Para makasiguro, buksan ang Executions ng workflow. Nakatala ang takbo: Succeeded in 18 point 635 seconds, galing sa version na Embedded chat, at ginamit ng agent ang Calculator."),
    dict(kind="slide", slide="p2_rules", step="BAGO MO I-SHARE",
         say="Tatlong paalala. Una, i-publish muna ang workflow, dahil kung hindi, hindi gagana ang chat link. Pangalawa, localhost ang link ko, kaya sa computer ko lang ito bubukas. Hindi ito bubukas sa phone ng kaibigan mo. "
             "Pangatlo, ang Authentication ay naka-None, kaya sinumang makakuha ng link ay pwedeng mag-chat, at ang computer mo ang gagamit ng lakas. Bago mo i-share, gumamit ng Authentication o ng ibang proteksyon."),
    dict(kind="slide", slide="p2_results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Hosted chat: 2250.08, tama. Embedded widget: 2250.08, tama. Ang unang bersyon ng page ko: sira ang layout, dahil sa CSS ko. Pagkatapos ayusin: buo na. "
             "Tandaan: maliit na model ito, kaya mabagal at minsan nalilito."),
    dict(kind="comment", step="COMMENT", comment_q="Anong website o page ang paglalagyan mo ng chatbot?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong website o page ang paglalagyan mo ng chatbot? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 6. exit ramp
    dict(kind="slide", chapter="Next: i-save ang mga tanong sa Excel", slide="p2_next", step="SUSUNOD",
         say="Ngayong nasa web page mo na ang agent, i-click ang video sa screen para sa susunod: ipapa-save natin sa Excel ang mga tanong at sagot, para magkaroon ka ng sarili mong study tracker. Nasa description ang workflow at ang page."),
]
