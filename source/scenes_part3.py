"""Scene list for Part 3: "n8n AI Agent Study Tracker in Excel (Tagalog)".
Real captures: n8n 2.47.5 in Chrome (source/shots_part3 c01-c21, 1037x649) and the real Excel window (x01, x03, 1440x900).
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1). Narration is Tagalog with English technical terms, one Filipino voice (synthetic).
"""
NAME = "03_n8n-ai-agent-excel-study-tracker-tagalog"
SYSTEM_MESSAGE = ""
MIXED = False

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="shot", chapter="Demo: study tracker sa Excel", img="x03", step="RESULTA", hl=[(55, 632, 260, 706), (262, 632, 780, 706), (782, 632, 1214, 706)],
         note=["Petsa at oras", "Ang tanong mo", "Ang sagot ng AI agent"],
         say="Tingnan mo ito. Ito ang Excel sheet ko, at nakatala na rito ang mga tanong ko at ang mga sagot ng AI agent ko sa n8n, may petsa at oras. Walang copy-paste. Kusa itong isinulat ng workflow, bawat tanong. "
             "Sa video na ito, gagawin natin ang study tracker na iyan. Libre ito, tumatakbo sa computer mo, at walang Google account."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Ano ang kailangan, at bakit CSV", slide="p3_needs", step="SETUP",
         say="Ang kailangan mo ay ang workflow mula sa Part 1, ang n8n at ang Ollama na tumatakbo, at ang Excel. Kung wala ka pang Excel, kahit anong spreadsheet ay pwede. "
             "Gagamit tayo ng CSV file. Bakit hindi XLSX? Dahil ang CSV ay madaling dagdagan ng bagong linya, at kayang buksan ng Excel. Ang XLSX ay hindi pwedeng dagdagan nang ganito kasimple."),
    dict(kind="slide", slide="p3_plan", step="SETUP",
         say="Ito ang plano. Pagkatapos sumagot ng AI Agent, may tatlong bagong node. Una, ang Edit Fields, para buuin ang isang linya ng CSV. Pangalawa, ang Convert to File. Pangatlo, ang Write File to Disk, na magdadagdag ng linya sa file. "
             "At sa dulo, isa pang Edit Fields para maibalik ang sagot sa chat."),
    # ------------------------------------------------------------ 3. build
    dict(kind="shot", chapter="Phase A: kopya ng workflow at mga bagong node", img="c01", step="PHASE A", hl=[(270, 18, 302, 46), (280, 215, 480, 242)], note=["I-click ang tatlong tuldok", "Piliin ang Duplicate"],
         say="Huwag nating sirain ang workflow mula sa Part 1. Gumawa tayo ng kopya. I-click ang tatlong tuldok sa taas, at piliin ang Duplicate."),
    dict(kind="shot", img="c02", step="PHASE A", hl=[(334, 270, 703, 304), (617, 388, 704, 422)], note=["Pangalan: Study Tracker (Excel)", "I-click ang Duplicate"],
         say="Bigyan ito ng pangalan, Study Tracker Excel, at i-click ang Duplicate."),
    dict(kind="shot", img="c03", step="PHASE A", hl=[(166, 22, 305, 44), (762, 222, 786, 246)], note=["Ang kopya ang binuksan", "Plus sa dulo ng AI Agent"],
         say="Binuksan ang kopya. Pareho ito ng Part 1. I-click ang plus sa kanan ng AI Agent para magdagdag ng node."),
    dict(kind="shot", img="c04", step="PHASE A", hl=[(668, 200, 1021, 245)], note=["I-type: Edit Fields", "Piliin ang Edit Fields (Set)"],
         say="Hanapin ang Edit Fields, at piliin ito. Sa node na ito natin bubuuin ang laman ng bawat linya."),
    dict(kind="shot", img="c05", step="PHASE A", hl=[(350, 238, 693, 268), (350, 354, 693, 384), (350, 470, 693, 500)], note=["date: petsa at oras", "question: ang tanong", "answer: ang sagot"],
         say="Gumawa ako ng tatlong field: date para sa petsa at oras, question para sa tanong, at answer para sa sagot ng agent. Sa value ng bawat isa, nag-type ako ng expression na may dobleng kulot na bracket."),
    dict(kind="shot", img="c06", step="PHASE A", hl=[(735, 182, 840, 285)], note=["Edit Fields pagkatapos ng AI Agent"],
         say="Ayan, nasa dulo na ng AI Agent ang Edit Fields."),
    dict(kind="shot", img="c07", step="PHASE A", hl=[(668, 252, 1021, 278), (668, 540, 1021, 566)], note=["Convert to File", "Piliin ang Convert to CSV", "May XLSX, pero hindi ito madaling dagdagan"],
         say="Susunod, idagdag ang Convert to File. Marami itong opsyon: CSV, HTML, JSON, XLS, at XLSX. Piliin ang Convert to CSV."),
    dict(kind="shot", img="c08", step="PHASE A", hl=[(325, 150, 712, 176), (342, 342, 712, 368)], note=["Operation: Convert to CSV", "Add option: patayin ang Header Row"],
         say="Sa Options, patayin ang Header Row. Ayaw nating maulit ang pamagat ng mga column sa bawat linya."),
    dict(kind="shot", img="c09", step="PHASE A", hl=[(325, 290, 712, 320), (357, 482, 397, 502)], note=["Write File to Disk", "File Path and Name", "Append: naka-on"],
         say="Pangatlo, ang Read/Write Files from Disk, na naka-set sa Write File to Disk. Ilagay ang path at pangalan ng file. At buksan ang Append, para madagdagan ang file at hindi mapalitan."),
    dict(kind="shot", img="c10", step="PHASE A", hl=[(654, 238, 716, 300), (799, 238, 861, 300), (893, 268, 955, 330)], note=["Edit Fields", "Convert to File", "Write File to Disk"],
         say="Ito ang itsura ng workflow na may tatlong bagong node. Subukan natin."),
    dict(kind="pause", chapter="Pause and try", step="TRY IT", pause_q="Gawin sa sarili mong screen:", pause_a=["I-duplicate ang workflow", "Idagdag ang 3 node", "Magpadala ng tanong sa chat"], seconds=8,
         say="Pause and try. Sa sarili mong screen, i-duplicate ang workflow, idagdag ang tatlong node, at magpadala ng tanong sa chat. May walong segundo ka."),
    # ------------------------------------------------------------ 4. gotchas
    dict(kind="shot", chapter="Mga totoong problema at ayos", img="c11", step="COMMON MISTAKE #1", hl=[(890, 186, 958, 254), (574, 538, 790, 560)],
         note=["Pula ang Write File node", "Access to the file is not allowed"],
         say="At pumula ang Write File node: Access to the file is not allowed. Common mistake ito. Hindi lahat ng folder ay pwedeng sulatan ng n8n."),
    dict(kind="slide", slide="p3_folder", step="AYOS",
         say="Pinapayagan lang ng n8n ang isang folder. Ang default ay ang folder na tinatawag na dot n8n dash files, sa user folder mo. Sa akin, nagtakda ako ng sarili kong folder gamit ang environment variable na N8N_RESTRICT_FILE_ACCESS_TO, "
             "at nag-restart ng n8n. Gumawa rin ako ng study-log.csv sa loob ng folder na iyon, na may isang linya ng header: date, question, answer."),
    dict(kind="shot", img="c12", step="COMMON MISTAKE #2", hl=[(558, 530, 1015, 625), (82, 498, 305, 556)], note=["Literal ang laman: may dobleng bracket pa", "Ibinalik sa chat ang path ng file, hindi ang sagot"],
         say="Tumakbo na, pero tingnan ang output ng Edit Fields. Ang laman ay mismong text na may dobleng bracket, hindi ang petsa at tanong. Hindi pala naging expression ang tinype ko. Pangalawang problema: ang chat ay nagbalik ng path ng file, hindi ang sagot ng agent."),
    dict(kind="shot", img="c13", step="COMMON MISTAKE #2", hl=[(742, 140, 1010, 236), (350, 300, 693, 330)], note=["Output: literal na text", "Walang berdeng kulay ang value"],
         say="Sa loob ng node, makikita rin: walang berdeng kulay ang value, ibig sabihin, plain text lang ito."),
    dict(kind="shot", img="c14", step="AYOS", hl=[(350, 532, 693, 562), (357, 598, 600, 618)], note=["I-drag ang field mula sa Input", "Berde na: expression", "Result: ang totoong sagot"],
         say="Ang ayos: i-drag ang field mula sa Input sa kaliwa, papunta sa value. Naging berde ito, at ipinapakita ng Result ang totoong sagot ng agent. Pagkatapos, pwede mo nang baguhin ang text sa loob."),
    dict(kind="shot", img="c15", step="COMMON MISTAKE #3", hl=[(358, 369, 478, 385)], note=["Petsa ng computer ko: Nov 13", "Lumabas: 2026-11-12 18:07"],
         say="Pangatlong problema: ang oras. Ang lumabas ay November 12, 6:07 ng gabi, pero umaga ng November 13 sa computer ko. Ang default na timezone ng workflow ay America, New York."),
    dict(kind="shot", img="c16", step="AYOS", hl=[(358, 386, 478, 404)], note=["setZone('Asia/Manila')", "Ngayon: 2026-11-13 07:07"],
         say="Ang ayos: idagdag ang setZone Asia slash Manila sa expression. Ngayon, tama na ang oras: November 13, 7:07 ng umaga."),
    dict(kind="shot", img="c17", step="AYOS", hl=[(82, 325, 300, 352), (350, 302, 693, 328)], note=["Isa pang Edit Fields sa dulo", "Field: output", "Galing sa AI Agent"],
         say="Para maibalik ang sagot sa chat, nagdagdag ako ng isa pang Edit Fields sa dulo, na may field na output. Ang value nito ay ang output ng AI Agent."),
    dict(kind="shot", img="c18", step="AYOS", hl=[(902, 255, 958, 308), (788, 255, 838, 306)], note=["Ang huling node: sagot para sa chat", "Write File sa unahan nito"],
         say="Ayan ang dulo ng workflow. Ang chat ay laging sumasagot gamit ang output ng huling node, kaya ito dapat ang sagot na gusto mong makita."),
    dict(kind="shot", img="c19", step="TEST 1", hl=[(558, 530, 1015, 585), (82, 512, 290, 556)], note=["Bumalik na ang sagot sa chat", "Ang final price ay 2250.08 pesos"],
         say="Subukan ulit. Bumalik na sa chat ang sagot: ang final price ay 2250.08 pesos."),
    dict(kind="terminal", step="COMMON MISTAKE #4", title="Git Bash", note="Totoong output",
         lines=[("cmd", "wc -l study-log.csv"), ("out", "0 study-log.csv"), ("note", "2 ang sagot, pero 0 ang bagong linya!"), ("out", "...Ang 15% ng 3200 ay 2720."), ("note", "Mali: ang 15% ng 3200 ay 480")],
         say="Pero tingnan ang file. Nagpadala ako ng dalawang tanong, at ang resulta ng wc dash l ay 0. Walang bagong linya! Magkadikit ang dalawang sagot sa iisang linya. Ang Convert to CSV pala ay hindi naglalagay ng bagong linya sa dulo. "
             "May isa pang natuklasan: sa pangalawang tanong, ang sagot ng agent ay 2720, at mali iyon. Ang tama ay 480. Kaya mahalaga ang tracker: nakikita mo ang mga sagot na kailangang i-check."),
    dict(kind="shot", img="c20", step="AYOS", hl=[(325, 150, 712, 176), (325, 214, 712, 246)], note=["Convert to Text File", "Text Input Field: line"],
         say="Ang ayos: palitan ang Operation ng Convert to Text File, at ang Text Input Field ay line. Sa Edit Fields na lang natin bubuuin ang buong linya, kasama ang bagong linya sa dulo."),
    dict(kind="shot", img="c21", step="AYOS", hl=[(350, 300, 693, 416), (358, 454, 640, 490)], note=["Isang field: line", "Nakapaloob sa quotes ang bawat value", "\\n sa dulo"],
         say="Isang field na lang ang natira sa Edit Fields: line. Binubuo nito ang petsa, tanong, at sagot, nakapaloob sa quotes para hindi masira ng kuwit, at may backslash n sa dulo para sa bagong linya. Tama ang Result."),
    # ------------------------------------------------------------ 5. verification
    dict(kind="shot", chapter="Buksan sa Excel", img="x01", step="BAGO ANG AUTOFIT", hl=[(55, 833, 188, 873), (55, 872, 188, 900)], note=["######### sa petsa", "Masyadong makitid ang column"],
         say="Binuksan ko ang study-log.csv sa Excel. Nandoon ang tatlong column. Pero ang petsa ay nagpapakita ng mga hash. Hindi ito error sa data. Masyadong makitid lang ang column."),
    dict(kind="shot", img="x03", step="TEST 2", hl=[(55, 632, 260, 706), (262, 632, 780, 706), (782, 632, 1214, 706)], note=["Autofit ang column", "Ginawang petsa ng Excel ang A", "Dalawang row, dalawang tanong"],
         say="Nag-autofit ako ng column. Ayan: ang petsa, ang tanong, at ang sagot. Pansinin na ginawang tunay na petsa ng Excel ang unang column, kaya pwede mo na itong i-sort at i-filter. Dalawang tanong, dalawang linya."),
    dict(kind="slide", slide="p3_rules", step="BAGO MO GAMITIN",
         say="Tatlong paalala. Una, i-check ang mga sagot. Maliit na model ito, at nagkamali ito sa 15 percent ng 3200. Pangalawa, ang n8n ay makakasulat lang sa folder na pinayagan mo. At pangatlo, ang CSV ay madaling dagdagan, pero kapag gusto mo ng ganda at formula, buksan ito sa Excel at i-save bilang XLSX."),
    dict(kind="slide", slide="p3_results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Ang unang takbo: mali ang path, at hindi pinayagan. Literal na text ang tinype na expression, kaya na-drag ko ang field. Mali ang oras, kaya Asia Manila. At magkadikit ang mga linya, kaya Convert to Text File. Pagkatapos ng lahat, buo na ang file: header at dalawang row."),
    dict(kind="comment", step="COMMENT", comment_q="Anong mga tanong ang itatala mo sa study tracker mo?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong mga tanong ang itatala mo sa study tracker mo? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 6. exit ramp
    dict(kind="slide", chapter="Panoorin ang buong playlist", slide="p3_next", step="SUSUNOD",
         say="Kumpleto na ang serye: ang setup, ang AI agent, ang chatbot sa web page, at ang study tracker sa Excel. I-click ang playlist sa screen para panoorin ito nang sunod-sunod. Nasa description ang workflow file."),
]
