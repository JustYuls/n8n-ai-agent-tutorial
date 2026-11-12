"""Scene list for "How to Install n8n Locally on Windows 11 (Tagalog)" = Video 0 of the series.
Screens: real captures (nodejs.org and ollama.com download pages, a fresh n8n owner-account form, the n8n startup page, the empty editor)
and real command output copied from the install log on this PC (node 24.19.0, n8n 2.47.5, Ollama 0.40.16, llama3.2:3b).
Nothing is typed into the account form on screen: viewers see the empty form and the rules; they create their own account.
kind: shot | terminal | slide | pause | comment (see build_video.py). Highlight boxes are in the original image's pixel coordinates.
"""
NAME = "00_n8n-installation-guide-tagalog"
SYSTEM_MESSAGE = ""

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="slide", chapter="Ano ang makukuha mo sa video na ito", slide="hook_checks", step="RESULTA",
         say="Sa video na ito, mai-install mo ang n8n sa Windows, kasama ang Node.js at Ollama, at gagawa ka ng sarili mong local na n8n account. "
             "Libre lahat, walang Docker, at walang API key. Pagkatapos nito, bukas na ang n8n editor sa browser mo, nasa computer mo ang AI model, "
             "at handa ka nang gumawa ng AI agent."),
    dict(kind="slide", chapter="Ano ang kailangan at ang plano", slide="requirements", step="SETUP",
         say="Bago tayo magsimula. Ang kailangan mo ay Windows 10 o 11, at internet para sa mga download. Sa PC ko, 7 gigabytes ng RAM at walang graphics card. "
             "Gumagana ito, pero mabagal: mga 30 segundo ang bawat sagot ng AI. Ang AI model lang ay 2 gigabytes. "
             "Apat na hakbang tayo: una, Node.js. Pangalawa, n8n. Pangatlo, Ollama at ang model. At pang-apat, ang local na account mo."),
    # ------------------------------------------------------------ 2. node.js
    dict(kind="shot", chapter="Hakbang 1: i-install ang Node.js", img="i01_nodejs-download", step="HAKBANG 1: NODE.JS",
         hl=[(220, 208, 364, 246), (402, 208, 537, 246)], note=["Bersyon ng Node", "Piliin ang Windows"],
         say="Hakbang isa: Node.js. Pumunta sa nodejs.org, slash en, slash download, at piliin ang Windows. "
             "Ang n8n na version 2.47.5 ay nangangailangan ng Node 24 o mas bago. Ang gamit ko ay 24.19.0. "
             "Sa araw ng pag-record ko, ang page ay nagpapakita ng 26.13.1 na LTS. Hindi ko pa ito nasubukan, kaya kung gusto mong sigurado, piliin ang Node 24 sa dropdown. "
             "Sundin ang mga command o ang installer na ipinapakita ng page."),
    dict(kind="terminal", img=None, step="HAKBANG 1: NODE.JS", title="Windows PowerShell",
         lines=[("cmd", "node -v"), ("out", "v24.19.0"), ("cmd", "npm -v"), ("out", "11.17.0")],
         note="Dapat 24 o mas mataas ang node",
         say="Para i-check, buksan ang PowerShell at i-type ang node dash v. Dapat 24 o mas mataas ang lumabas. Sa akin: v24.19.0. At ang npm dash v: 11.17.0."),
    # ------------------------------------------------------------ 3. n8n
    dict(kind="terminal", chapter="Hakbang 2: i-install ang n8n", img=None, step="HAKBANG 2: N8N", title="Windows PowerShell",
         lines=[("cmd", "mkdir n8n-local"), ("cmd", "cd n8n-local"), ("cmd", "npm install n8n"), ("note", "... maghintay; walang progress bar ..."), ("ok", "added 2259 packages in 13m")],
         note="Inabot ng 13 minuto sa PC ko",
         say="Hakbang dalawa: n8n. Gumawa ng folder, halimbawa n8n-local, pumasok dito, at i-type ang npm install n8n. "
             "Inabot ito ng 13 minuto sa PC ko, at walang progress bar. Normal iyon, kaya huwag mong isara. Sa dulo: added 2259 packages."),
    dict(kind="terminal", img=None, step="HAKBANG 2: N8N", title="Windows PowerShell",
         lines=[("cmd", "npx n8n --version"), ("ok", "2.47.5")], note="Version na ginamit ko: 2.47.5",
         say="I-check ang version: npx n8n dash dash version. Sa akin, 2.47.5. Ito ang version na gamit sa lahat ng video natin."),
    dict(kind="terminal", img=None, step="HAKBANG 2: N8N", title="Windows PowerShell",
         lines=[("cmd", "npx n8n start"), ("out", "Version: 2.47.5"), ("out", "Editor is now accessible via:"), ("ok", "http://localhost:5678"),
                ("note", "(pinaikli ko; may mga babala na hindi ipinakita)")],
         note="Buksan ang http://localhost:5678",
         say="Ngayon, patakbuhin ito: npx n8n start, sa loob ng folder kung saan mo ini-install. Hintayin ang linyang Editor is now accessible via, http colon slash slash localhost colon 5678. "
             "Ang unang takbo ay inaabot ng ilang minuto, dahil ginagawa pa ang database."),
    dict(kind="zoom", img="i04_n8n-starting-up", step="HINDI ITO ERROR", crop=(0, 0, 400, 60), hl=[(0, 0, 175, 30)], caption="n8n is starting up. Please wait", sub="Hindi ito error: maghintay lang at mag-refresh",
         say="Kung buksan mo agad ang browser, baka ito ang makita mo: n8n is starting up, please wait. Hindi ito error. Maghintay ka lang, at mag-refresh pagkalipas ng ilang segundo."),
    # ------------------------------------------------------------ 4. ollama
    dict(kind="shot", chapter="Hakbang 3: i-install ang Ollama at ang model", img="i02_ollama-download-windows", step="HAKBANG 3: OLLAMA",
         hl=[(560, 298, 640, 332), (526, 426, 640, 444), (32, 352, 640, 407)], note=["Piliin ang Windows", "Download manually: ang installer", "Ang PowerShell command ng Ollama"],
         say="Hakbang tatlo: Ollama. Pumunta sa ollama.com slash download, at piliin ang Windows. May PowerShell na command na ipapa-paste nila, at may Download manually para sa installer. "
             "Para sa baguhan, mas ligtas ang manual na installer. At tandaan: huwag kang mag-paste ng kahit anong script sa PowerShell kung hindi mo ito kilala."),
    dict(kind="terminal", img=None, step="HAKBANG 3: OLLAMA", title="Windows PowerShell",
         lines=[("cmd", "ollama --version"), ("out", "ollama version is 0.40.16"), ("cmd", "ollama pull llama3.2:3b"), ("out", "verifying sha256 digest"),
                ("out", "writing manifest"), ("ok", "success"), ("cmd", "ollama list"), ("out", "NAME          ID            SIZE    MODIFIED"),
                ("out", "llama3.2:3b   a80c4f17acd5  2.0 GB  9 seconds ago")],
         note="2.0 GB ang model",
         say="Pagkatapos ng installer, i-check ang version: ollama dash dash version. Sa akin, 0.40.16. Tapos i-download ang model: ollama pull llama3.2 colon 3b. Mga 2 gigabytes ito, kaya nakadepende sa internet mo. "
             "Kapag success, i-type ang ollama list, at lalabas ang llama3.2:3b."),
    dict(kind="terminal", img=None, step="HAKBANG 3: OLLAMA", title="Windows PowerShell",
         lines=[("cmd", "curl http://127.0.0.1:11434/api/version"), ("ok", '{"version":"0.40.16"}')], note="Sumasagot si Ollama sa 127.0.0.1",
         say="Isa pang check: ang Ollama ay sumasagot sa address na 127.0.0.1 port 11434. Mahalaga ito mamaya, dahil ito ang address na ilalagay natin sa n8n."),
    # ------------------------------------------------------------ 5. account
    dict(kind="shot", chapter="Hakbang 4: gumawa ng local na n8n account", img="i03_n8n-setup-owner-form", step="HAKBANG 4: ACCOUNT",
         hl=[(360, 209, 662, 245), (360, 288, 662, 403), (360, 445, 662, 481), (360, 516, 662, 548), (479, 579, 543, 614)],
         note=["Email: kahit anong email; local ito", "First at Last Name", "Password: 8+ characters, 1 number, 1 capital", "Updates: i-uncheck kung ayaw", "I-click ang Next"],
         say="Hakbang apat: ang account. Buksan ang browser sa http colon slash slash localhost colon 5678, at lalabas ang Set up owner account. "
             "Ilagay ang email, kahit anong email, dahil sa computer mo lang ito. Tapos ang first name at last name. "
             "Ang password ay walong characters o higit pa, na may kahit isang number at isang capital letter. "
             "May checkbox para sa updates, i-uncheck mo kung ayaw mo. Pagkatapos, i-click ang Next."),
    dict(kind="slide", slide="account_tips", step="BAGO KA MAG-SUBMIT",
         say="Tatlong paalala. Una, gumamit ng password na maaalala mo, at ikaw mismo ang mag-type nito. Huwag mong ibigay sa iba. "
             "Pangalawa, ang account na ito ay nasa computer mo, hindi sa cloud. "
             "At pangatlo, huwag mong i-expose ang port 5678 sa internet. Sa video na ito, sa computer mo lang ito bubuksan."),
    dict(kind="pause", chapter="Pause and try: gawin ang account mo", step="TRY IT", pause_q="Gawin ang account mo ngayon", pause_a=["Buksan: http://localhost:5678", "Punan ang form, tapos Next"], seconds=8,
         say="Pause and try. Gawin mo na ang account mo ngayon. I-pause ang video kung kailangan mo ng mas mahabang oras."),
    dict(kind="shot", img="i05_n8n-empty-canvas", step="HANDA NA", hl=[(686, 285, 796, 415)], note=["Ito ang workflow editor", "Add first step: dito magsisimula ang AI agent"],
         say="Pagkatapos mag-sign in, ito ang makikita mo: ang workflow editor, na may Add first step. Ito ang lugar kung saan natin gagawin ang AI agent sa susunod na video."),
    dict(kind="terminal", img=None, step="NAKALIMUTAN ANG PASSWORD?", title="Windows PowerShell",
         lines=[("note", "(i-stop muna ang n8n: Ctrl + C)"), ("cmd", "npx n8n user-management:reset"), ("ok", "Successfully reset the database to default user state.")],
         note="Babalik ang Set up owner account",
         say="Nakalimutan ang password? I-stop muna ang n8n gamit ang Control C, tapos i-run ang npx n8n user-management colon reset. "
             "Sa akin, ang sagot ay: Successfully reset the database to default user state. Babalik ang Set up owner account, at pwede kang gumawa ng bago. "
             "Ginamit ko ito noong wala pang workflow. Hindi ko sinubukan kung ano ang mangyayari sa mga workflow na naka-save na, kaya basahin muna ang docs ng n8n kung may mahalaga ka nang gawa."),
    dict(kind="terminal", img=None, step="PAANO BUKSAN ULIT", title="Windows PowerShell",
         lines=[("cmd", "cd n8n-local"), ("cmd", "npx n8n start"), ("note", "Buksan: http://localhost:5678  (Sign in)")], note="Sa susunod na gamit",
         say="Para buksan ulit ang n8n sa susunod: pumasok sa folder, patakbuhin ang npx n8n start, at buksan ang localhost 5678. Mag-sign in gamit ang account mo."),
    # ------------------------------------------------------------ 6. verification
    dict(kind="shot", chapter="Final check: kumonekta ang n8n sa Ollama", img="s09_credential-error-localhost", step="COMMON MISTAKE", hl=[(412, 206, 1184, 268)],
         note=["Couldn't connect with these settings", "Address: localhost"], dir="shots",
         say="Final check: kumonekta ba ang n8n sa Ollama? Sa n8n, gagawa ka ng Ollama credential. Sa computer ko, kapag localhost ang inilagay ko, ito ang lumabas: Couldn't connect with these settings."),
    dict(kind="shot", img="s10_credential-success-127", step="AYOS", hl=[(412, 206, 1184, 268), (412, 325, 1184, 360)], note=["http://127.0.0.1:11434", "Connection tested successfully"], dir="shots",
         say="Ang ayos: gamitin ang http colon slash slash 127.0.0.1 colon 11434. At lumabas ang Connection tested successfully. Ang buong hakbang sa paggawa ng credential ay nasa susunod na video."),
    dict(kind="slide", chapter="Handa ka na: susunod, ang AI agent", slide="ready", step="HANDA KA NA",
         say="Kumpleto na ang setup mo: Node.js, n8n, Ollama at ang model, at ang local na account. "
             "Ngayong handa na ang lahat, i-click ang video sa screen para gumawa ng sarili mong AI agent sa n8n, na gumagamit ng tools at may memory."),
]
