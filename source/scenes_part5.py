"""Scene list for Part 5: "n8n Error Handling for Beginners (Tagalog)".
Real captures: n8n 2.47.5 in Chrome (source/shots_part5 e00-e17, 1037x649) and real terminal outputs saved in source/shots_part5/t01-t10 (text copied from the real runs).
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1). Narration is Tagalog with English technical terms, one Filipino voice (synthetic).
Avoid dots inside words in say (the subtitle splitter cuts at dots): no file extensions, no domain names.
"""
NAME = "05_n8n-error-handling-tagalog"
SYSTEM_MESSAGE = ""
MIXED = False

T_GB = "Git Bash"
CURL = ("cmd", "curl -s -X POST http://localhost:5678/webhook/weather-safe \\")
CURL2 = ("out", "  -H \"Content-Type: application/json\" -d '{\"city\":\"Manila\"}'")

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="terminal", chapter="Demo: sira ang AI, may sagot pa rin", step="RESULTA", title=T_GB, note="Totoong output",
         lines=[CURL, CURL2,
                ("out", '{"city":"Manila","temp":27.6,"humidity":69,'),
                ("out", ' "advice":"Advice is not available right now (the AI did not answer)."}'),
                ("ok", "HTTP 200  2.084s")],
         say="Tingnan mo ito. Sinadya kong sirain ang AI ko, gamit ang maling pangalan ng model. Pero ang tumawag ay nakakuha pa rin ng sagot: ang totoong temperatura, 27.6 degrees, ang humidity na 69 percent, at malinaw na mensahe na walang payo ngayon. HTTP 200, hindi error."),
    dict(kind="terminal", step="RESULTA", title=T_GB, note="Totoong output",
         lines=[("cmd", "cat runtime/study-files/errors-log.csv"),
                ("out", '"2026-11-15 22:30:10","Weather Webhook (safe)","Get weather",'),
                ("out", '"The connection cannot be established, this usually occurs'),
                ("out", 'due to an incorrect host (domain) value"')],
         say="At kapag ang weather API naman ang bumagsak, may kusang isinulat na linya sa errors log: ang oras, ang workflow, ang node na pumalya, at ang mensahe ng error. Walang nag-type niyan. "
             "Sa video na ito, gagawin natin pareho, at ipapakita ko rin ang mga totoong pagkakamali ko."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Dalawang uri ng pagbagsak", slide="p5_idea", step="SETUP",
         say="May dalawang uri ng pagbagsak. Ang una ay inaasahan: pwedeng pumalya ang AI o ang API. Hahawakan natin ito sa loob mismo ng workflow, gamit ang On Error, Continue using error output, at isang fallback na sagot. "
             "Ang pangalawa ay hindi inaasahan: may pumalyang hindi mo naisip. Dito natin gagamitin ang Error workflow, na may Error Trigger, para itala ang problema."),
    dict(kind="slide", slide="p5_needs", step="SETUP",
         say="Ang kailangan mo ay ang workflow mula sa Part 4, at isang Error logger workflow na gagawin natin. Kailangan din ng folder na pinapayagan ng n8n na sulatan, tulad ng ginawa natin sa Part 3. Nasa description ang dalawang workflow file."),
    dict(kind="slide", slide="p5_plan", step="SETUP",
         say="Ito ang plano. Sa unang workflow, ang Advice node ay magkakaroon ng dalawang labasan: Success at Error. Ang Error ay mapupunta sa Fallback advice, at pagkatapos ay sa Reply. "
             "Sa pangalawang workflow, ang Error logger: Error Trigger, Build line, Convert to File, at Write File to Disk."),
    # ------------------------------------------------------------ 3. the problem
    dict(kind="shot", chapter="Ang problema: pumalya ang AI", img="e01_canvas-before", step="ANG PROBLEMA", hl=[(737, 374, 781, 418), (728, 251, 850, 303)], note=["Ollama Chat Model: maling pangalan ng model", "Advice: ito ang mabibigo"],
         say="Ito ang workflow mula sa Part 4, pero ang Ollama Chat Model ay may pangalan ng model na wala sa Ollama. Parang hindi pa na-download ang model."),
    dict(kind="shot", img="e02_testrun-fail", step="COMMON MISTAKE #1", hl=[(728, 251, 850, 303), (691, 501, 1021, 601)], note=["Pumula ang Advice", "model not found"],
         say="Tumawag ako sa test URL, at pumula ang Advice. Problem in node Advice: model not found. Totoo ito: ganito ang itsura kapag hindi pa na-download ang model, o mali ang pangalan."),
    dict(kind="terminal", step="COMMON MISTAKE #1", title=T_GB, note="Totoong output",
         lines=[CURL, CURL2, ("out", '{"message":"Error in workflow"}'), ("ok", "HTTP 500  12.667s")],
         say="Ito ang nakuha ng tumatawag sa production URL. Error in workflow, HTTP 500, pagkalipas ng 12.7 segundo. Wala siyang temperatura, kahit nakuha na ng workflow ang totoong temperatura. At wala siyang paliwanag."),
    dict(kind="shot", img="e06_executions-errors", step="EXECUTIONS", hl=[(66, 162, 327, 222), (66, 222, 327, 340)], note=["Pulang takbo: 12.6 s", "Dalawa pang pula: 3.3 s at 32.7 s"],
         say="Sa Executions, makikita ang mga pulang takbo: 12.6 segundo, 3.3 segundo, at 32.7 segundo. Nandiyan ang error, pero ikaw lang ang makakakita nito kung bubuksan mo."),
    # ------------------------------------------------------------ 4. fix 1
    dict(kind="shot", chapter="On Error: Continue (using error output)", img="e03_advice-error", step="AYOS", hl=[(738, 118, 990, 200)], note=["model not found", "Original error: ResponseError"],
         say="Buksan natin ang Advice. Ito ang error: model not found, original error ResponseError."),
    dict(kind="shot", img="e04_onerror-stop", step="AYOS", hl=[(326, 271, 697, 303)], note=["On Error: Stop Workflow (default)"],
         say="Sa Settings ng node, may On Error. Ang default ay Stop Workflow: tumigil ang buong workflow, kaya 500 ang sagot."),
    dict(kind="shot", img="e05_onerror-options", step="AYOS", hl=[(326, 322, 697, 372), (326, 372, 697, 422), (326, 425, 697, 470)], note=["Stop Workflow", "Continue", "Continue (using error output)"],
         say="May tatlong pagpipilian. Stop Workflow. Continue, na ipapasa ang mensahe ng error bilang regular na item. At Continue using error output, na magbibigay ng dagdag na labasan para sa error. Ito ang pipiliin natin."),
    dict(kind="shot", img="e09_onerror-continue", step="AYOS", hl=[(326, 271, 697, 303), (875, 190, 1004, 216), (753, 230, 1004, 360)], note=["Continue (using error output)", "Error Branch: 1 item", "city, temp, humidity at error"],
         say="Pagkatapos ng test, tingnan ang Error Branch. Dala nito ang city, temp, at humidity, at ang mensahe ng error. Kaya hindi nawala ang totoong datos."),
    dict(kind="shot", img="e07_canvas-safe", step="AYOS", hl=[(840, 262, 885, 292), (850, 365, 903, 417), (903, 251, 955, 303)], note=["Success at Error na labasan", "Fallback advice", "Reply: iisa para sa dalawa"],
         say="Sa canvas, ang Advice ay may Success at Error. Ang Error ay nakakabit sa Fallback advice, at ang Fallback ay sa Reply, kapareho ng Success."),
    dict(kind="shot", img="e10_fallback", step="AYOS", hl=[(350, 238, 693, 332), (775, 143, 995, 175)], note=["Isang field: text", "Mensaheng walang payo"],
         say="Ang Fallback advice ay Edit Fields na may isang field lang: text. Ang laman: Advice is not available right now, the AI did not answer. Pareho ang pangalan ng field sa output ng Advice, kaya gumagana ang Reply para sa dalawa."),
    dict(kind="shot", img="e08_testrun-safe", step="TEST 1", hl=[(691, 549, 1021, 602), (850, 365, 903, 417), (737, 374, 781, 418)], note=["Workflow executed successfully", "Ang Error na daan ang tumakbo", "Pula pa rin ang model"],
         say="Subukan ulit. Workflow executed successfully, kahit pula pa rin ang Ollama Chat Model. Ang daan ng Error ang tumakbo, papunta sa Fallback advice."),
    # ------------------------------------------------------------ 5. second kind
    dict(kind="shot", chapter="Pangalawang uri: bumagsak ang API", img="e11_api-fail", step="COMMON MISTAKE #2", hl=[(483, 251, 535, 303), (691, 480, 1021, 600)], note=["Pumula ang Get weather", "The connection cannot be established"],
         say="Pangalawang uri ng pagbagsak. Sinira ko ang URL ng weather API, maling host. Pumula ang Get weather: the connection cannot be established, this usually occurs due to an incorrect host value. Ibang problema ito, at hindi natin ito inaasahan."),
    dict(kind="terminal", step="COMMON MISTAKE #2", title=T_GB, note="Totoong output",
         lines=[CURL, CURL2, ("out", '{"message":"Error in workflow"}'), ("ok", "HTTP 500  6.402s"),
                ("cmd", "ls runtime/study-files"), ("out", "study-log.csv"), ("note", "Walang bagong file: walang nakaalam")],
         say="Production call ulit: Error in workflow, 500. At pagtingin ko sa folder, wala pang bagong file. Walang nakakaalam na may pumalya, maliban sa Executions list."),
    # ------------------------------------------------------------ 6. error workflow
    dict(kind="shot", chapter="Error workflow: ang Error logger", img="e00_checklist", step="ERROR WORKFLOW", hl=[(74, 180, 404, 245)], note=["Set up error notifications"],
         say="Pansinin ang checklist na lumabas sa n8n pagkatapos mag-Publish. Ang una ay Set up error notifications. Ito ang gagawin natin."),
    dict(kind="shot", img="e14_logger-canvas", step="ERROR LOGGER", hl=[(164, 291, 260, 386), (388, 291, 484, 386), (612, 291, 708, 386), (820, 291, 916, 386)], note=["Error Trigger", "Build line", "Convert to File", "Write File to Disk"],
         say="Ito ang Error logger workflow. Ang unang node ay ang Error Trigger. Pagkatapos: Build line, Convert to File, at Write File to Disk, tulad ng sa Part 3."),
    dict(kind="shot", img="e16_error-trigger", step="ERROR LOGGER", hl=[(565, 175, 995, 237), (550, 245, 995, 335)], note=["execution: id at URL", "error: ang detalye"],
         say="Ito ang laman ng Error Trigger sa isang totoong takbo: ang execution id, ang URL ng takbong nag-error, at ang error mismo, kasama ang pangalan ng node at ang mensahe."),
    dict(kind="shot", img="e17_build-line", step="ERROR LOGGER", hl=[(350, 305, 693, 415), (745, 142, 1005, 232)], note=["Expression: oras, workflow, node, mensahe", "Resulta: isang linya ng CSV"],
         say="Ang Build line ay bumubuo ng isang linya ng CSV: oras sa Asia Manila, pangalan ng workflow, ang node na pumalya, at ang mensahe. Tulad sa Part 3, nakapaloob sa quotes ang bawat halaga, at may bagong linya sa dulo."),
    dict(kind="shot", img="e13_settings-error-workflow", step="AYOS", hl=[(207, 205, 816, 243)], note=["Error Workflow: Error logger"],
         say="Para magamit ito, buksan ang Settings ng pangunahing workflow, at piliin ang Error logger sa Error Workflow. Pagkatapos, i-save."),
    # ------------------------------------------------------------ 7. mistake + verification
    dict(kind="terminal", chapter="Pagkakamali: Execute workflow ay hindi nagla-log", step="COMMON MISTAKE #3", title=T_GB, note="Totoong output",
         lines=[("cmd", "curl -s -X POST http://localhost:5678/webhook-test/weather-safe \\"), CURL2,
                ("out", '{"message":"Error in workflow"}'), ("ok", "HTTP 500  56.505s"),
                ("cmd", "ls runtime/study-files"), ("out", "study-log.csv"), ("note", "Walang errors-log.csv")],
         say="Sinubukan ko sa test URL, na may nakakabit nang error workflow. Pumalya ang workflow, 500, at wala pa ring bagong file. Sa pagsubok na ito, hindi tumakbo ang error workflow sa test run. Kailangan ng production na tawag."),
    dict(kind="terminal", step="TEST 2", title=T_GB, note="Production URL",
         lines=[CURL, CURL2, ("out", '{"message":"Error in workflow"}'), ("ok", "HTTP 500  4.066s"),
                ("cmd", "ls runtime/study-files"), ("out", "errors-log.csv  study-log.csv"),
                ("cmd", "cat runtime/study-files/errors-log.csv"),
                ("out", '"2026-11-15 22:30:10","Weather Webhook (safe)","Get weather",'),
                ("out", '"The connection cannot be established, this usually occurs ...')],
         say="Ngayon, production call. Error in workflow pa rin ang sagot, 500. Pero tingnan ang folder: may errors log na. Nandoon ang linya: ang oras, Weather Webhook safe, Get weather, at ang mensahe."),
    dict(kind="shot", img="e15_logger-executions", step="EXECUTIONS", hl=[(66, 162, 327, 282), (370, 340, 990, 455)], note=["Dalawang takbo ng Error logger", "Berde ang lahat ng node"],
         say="Sa Executions ng Error logger, makikita ang mga takbo. Dalawa ang nakalista: ang isa ay galing sa pagsubok ko bago mag-record, at ang isa ay sa tawag kanina."),
    dict(kind="terminal", chapter="Verification: normal na tawag", step="TEST 3", title=T_GB, note="Ibinalik ang tama",
         lines=[("out", "== Manila =="), ("out", '{"city":"Manila","temp":27.5,"humidity":69,"advice": ...}'), ("ok", "HTTP 200  23.889s"),
                ("out", "== Cebu =="), ("out", '{"city":"Cebu","temp":23,"humidity":93,"advice": ...}'), ("ok", "HTTP 200  8.544s"),
                ("cmd", "wc -l runtime/study-files/errors-log.csv"), ("out", "1 runtime/study-files/errors-log.csv")],
         say="Verification. Ibinalik ko ang tamang model at ang tamang URL. Manila: 27.5 degrees at 69 percent. Cebu: 23 degrees at 93 percent. Parehong 200. At ang errors log ay isa pa ring linya: walang bagong tala, dahil walang error. "
             "Pansinin na ang payo para sa Cebu ay payong na naman, kahit walang ulan sa datos."),
    dict(kind="slide", slide="p5_rules", step="BAGO MO GAMITIN",
         say="Tatlong paalala. Una, hawakan sa loob ng workflow ang mga inaasahang error, gamit ang Continue using error output at isang fallback. Pangalawa, itala ang hindi inaasahan sa isang Error workflow, at tandaan na sa production lang ito tumatakbo. "
             "Pangatlo, huwag magpanggap na tagumpay: ibalik ang totoong datos, sabihing walang payo, at itala ang error."),
    dict(kind="slide", slide="p5_results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Sa maling model na walang handler, 500. Sa error output at fallback, 200 na may fallback advice. Nang pumalya ang API na walang error workflow, 500 at walang tala. Sa Execute workflow, walang naitala. "
             "Sa production call, may linya sa log. At sa normal na tawag, walang bagong log."),
    dict(kind="comment", step="COMMENT", comment_q="Anong error ang gusto mong matutunang hawakan sa n8n mo?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong error ang gusto mong matutunang hawakan sa n8n mo? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 8. exit ramp
    dict(kind="slide", chapter="Susunod: Part 6, Schedule Trigger", slide="p5_next", step="SUSUNOD",
         say="Hindi pa tapos ang serye. Sa Part 6, gagawin nating kusang tumakbo ang workflow tuwing umaga, gamit ang Schedule Trigger. I-click ang playlist sa screen para panoorin ang buong serye. Nasa description ang dalawang workflow file."),
]
