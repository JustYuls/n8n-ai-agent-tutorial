"""Scene list for Part 6: "n8n Schedule Trigger for Beginners (Tagalog)".
Real captures: n8n 2.47.5 in Chrome (source/shots_part6 h01-h14, 1440x675) and real terminal outputs saved in source/shots_part6/t01-t05 (text copied from the real runs, 2026-11-15).
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1). Narration is Tagalog with English technical terms, one Filipino voice (synthetic).
Avoid dots inside words in say (the subtitle splitter cuts at dots): no file extensions, no domain names.
"""
NAME = "06_n8n-schedule-trigger-tagalog"
SYSTEM_MESSAGE = ""
MIXED = False

T_GB = "Git Bash"

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="terminal", chapter="Demo: kusang tumakbo, walang nag-click", step="RESULTA", title=T_GB, note="Totoong output",
         lines=[("cmd", "cat runtime/study-files/daily-weather.csv"),
                ("out", '"2026-11-15 23:16:40","Manila","32.7","26.2","4",...'),
                ("out", '"2026-11-15 23:17:26","Manila","32.7","26.2","4",...'),
                ("out", '"2026-11-15 23:18:26","Manila","32.7","26.2","4",...'),
                ("out", '"2026-11-15 23:19:24","Manila","32.7","26.2","4",...'),
                ("note", "Walang nag-click: kusang isinulat ng workflow")],
         say="Tingnan mo ito. Apat na linya sa file na ito, at wala akong na-click kahit isa. Kusa itong isinulat ng workflow ko: ang petsa at oras, ang lungsod, ang pinakamataas at pinakamababang temperatura, ang tsansa ng ulan, at isang payo ng AI. "
             "Sa video na ito, gagawin natin ang kusang tumatakbong workflow, at ipapakita ko rin ang mga totoong pagkakamali ko."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Ano ang Schedule Trigger", slide="p6_idea", step="SETUP",
         say="Hanggang ngayon, kailangan mong mag-click o tumawag para tumakbo ang workflow. Ang Schedule Trigger ay parang alarm clock: ang oras na ang magpapatakbo. "
             "Pwedeng bawat ilang segundo, minuto o oras, o araw-araw sa oras na pipiliin mo."),
    dict(kind="slide", slide="p6_needs", step="SETUP",
         say="Ang kailangan mo ay n8n at Ollama na tumatakbo, galing sa Part 1. Ang Error logger mula sa Part 5. At isang folder na pinapayagan ng n8n na sulatan, tulad ng sa Part 3. Kailangang bukas ang n8n kapag oras na ng iskedyul."),
    dict(kind="slide", slide="p6_plan", step="SETUP",
         say="Ito ang plano. Una, ang Schedule Trigger. Pangalawa, ang Get weather, para sa pinakamataas at pinakamababang temperatura at sa tsansa ng ulan. Pangatlo, ang Weather facts. Pang-apat, ang AI na may fallback, tulad ng natutunan natin sa Part 5. "
             "Pagkatapos, ang Build line, ang Convert to File, at ang Write File to Disk."),
    # ------------------------------------------------------------ 3. the workflow
    dict(kind="shot", chapter="Ang workflow at ang mga node", img="h01_canvas", step="ANG WORKFLOW", hl=[(158, 249, 227, 317), (627, 249, 787, 317), (1255, 249, 1324, 317)],
         note=["Schedule Trigger: dito nagsisimula", "Advice: AI na may Error na labasan", "Write File to Disk: ang CSV"],
         say="Ito ang buong workflow. Sa kaliwa, ang Schedule Trigger, at sa kanan, ang Write File to Disk. Sa gitna ang Get weather, Weather facts, at ang Advice na may Fallback advice sa ibaba nito. Sa dulo, ang Build line at ang Convert to File."),
    dict(kind="shot", img="h14_trigger-options", step="SCHEDULE TRIGGER", hl=[(54, 335, 461, 583)], note=["Seconds, Minutes, Hours", "Days, Weeks, Months", "Custom (Cron)"],
         say="Buksan natin ang Schedule Trigger. Sa Trigger Interval, ito ang mga pagpipilian: Seconds, Minutes, Hours, Days, Weeks, Months, at Custom Cron."),
    dict(kind="shot", img="h11_trigger-daily", step="SCHEDULE TRIGGER", hl=[(54, 293, 461, 320), (54, 447, 461, 474), (54, 513, 461, 540), (41, 120, 474, 183)], note=["Days: tuwing 1 araw", "Trigger at Hour: 7am", "Trigger at Minute: 0", "Tatakbo kapag na-Publish"],
         say="Ito ang final na setting natin: Days, tuwing isang araw, sa 7am, minuto 0. Pansinin ang paalala sa taas: tatakbo ang workflow sa iskedyul na ito kapag na-Publish mo ito. Para sa pagsubok, gamitin ang Execute workflow sa canvas."),
    dict(kind="shot", img="h04_get-weather", step="GET WEATHER", hl=[(527, 250, 899, 282), (947, 125, 1398, 165)], note=["GET sa forecast API ng Open-Meteo", "Retry On Fail, tulad ng Part 4"],
         say="Ang Get weather ay GET sa forecast API ng Open-Meteo. Ngayon, humihingi tayo ng daily na datos: ang pinakamataas na temperatura, ang pinakamababa, at ang pinakamataas na tsansa ng ulan, para sa isang araw. May Retry On Fail din, tulad ng Part 4."),
    dict(kind="shot", img="h05_weather-facts", step="WEATHER FACTS", hl=[(551, 355, 895, 600), (947, 140, 1100, 265)], note=["Edit Fields: city, max, min, rain", "32.7, 26.2 at 4"],
         say="Ang Weather facts ay pumipili lang ng kailangan: city, max, min, at rain. Ngayon, 32.7 degrees ang pinakamataas, 26.2 ang pinakamababa, at 4 percent ang tsansa ng ulan."),
    dict(kind="shot", img="h06_advice", step="ADVICE", hl=[(527, 260, 899, 380), (947, 215, 1400, 240)], note=["Prompt: may totoong datos ng ulan", "Sagot ng model"],
         say="Sa Advice, kasama na sa prompt ang tsansa ng ulan. May On Error, Continue using error output at Fallback advice din ito, tulad ng sa Part 5. Ang sagot ng model: Bring an umbrella to school, in case it rains. Pero 4 percent lang ang tsansa ng ulan! Payong pa rin ang payo, kaya i-check pa rin ang payo."),
    dict(kind="shot", img="h07_build-line", step="BUILD LINE", hl=[(551, 300, 893, 418), (940, 140, 1400, 175)], note=["Expression: oras, city, max, min, rain, payo", "Isang linya ng CSV"],
         say="Ang Build line ay bumubuo ng isang linya ng CSV: oras sa Asia Manila, lungsod, max, min, ulan, at payo. Pareho ito sa ginawa natin sa Part 3 at Part 5."),
    dict(kind="shot", img="h08_write-file", step="WRITE FILE", hl=[(527, 291, 914, 321), (527, 472, 650, 494)], note=["File: daily-weather sa pinapayagang folder", "Append: naka-on"],
         say="At ang Write File to Disk ay nagdadagdag ng linya sa daily weather file. Naka-on ang Append, kaya hindi napapalitan ang mga lumang linya."),
    dict(kind="shot", img="h02_manual-run", step="TEST 1", hl=[(158, 249, 227, 317), (1255, 249, 1324, 317)], note=["Execute workflow: berde ang lahat", "Isang linya ang naidagdag"],
         say="Subukan natin sa Execute workflow. Berde ang lahat ng node, at may isang bagong linya sa file. Pero ito ay manual na takbo. Hindi pa ito ang iskedyul."),
    dict(kind="pause", chapter="Pause and try", step="TRY IT", pause_q="Gawin sa sarili mong screen:", pause_a=["I-import ang daily weather workflow", "I-click ang Execute workflow", "Tingnan ang CSV file"], seconds=8,
         say="Pause and try. Sa sarili mong screen, i-import ang workflow file, i-click ang Execute workflow, at tingnan ang CSV file. May walong segundo ka."),
    # ------------------------------------------------------------ 4. mistake: not published
    dict(kind="shot", chapter="Pagkakamali: hindi pa naka-Publish", img="h03_trigger-minutes-ny", step="COMMON MISTAKE #1", hl=[(54, 293, 476, 320), (54, 358, 476, 386)], note=["Pansamantala: Minutes", "Bawat 1 minuto"],
         say="Para makita agad ang resulta, ginawa kong bawat isang minuto muna ang trigger. Hindi pa ito naka-Publish. Tingnan natin kung tatakbo."),
    dict(kind="terminal", step="COMMON MISTAKE #1", title=T_GB, note="Totoong output",
         lines=[("note", "Bawat 1 minuto, hindi naka-Publish"), ("out", "# started 23:11:06"), ("out", "# now 23:14:18"),
                ("cmd", "ls runtime/study-files"), ("out", "errors-log.csv  study-log.csv"), ("note", "Walang daily-weather file: walang tumakbo")],
         say="Naghintay ako ng mahigit tatlong minuto. Wala. Walang daily weather file. Hindi tatakbo ang Schedule Trigger hangga't hindi naka-Publish ang workflow."),
    dict(kind="shot", img="h09_executions-unpublished", step="EXECUTIONS", hl=[(66, 165, 327, 222)], note=["Iisang takbo lang: ang manual na takbo ko"],
         say="Sa Executions, iisang takbo lang ang nakalista: ang manual na takbo ko kanina. Walang kusang takbo."),
    dict(kind="terminal", chapter="Ang ayos: Publish", step="AYOS", title=T_GB, note="Totoong output",
         lines=[("note", "Naka-Publish, bawat 1 minuto"), ("out", "# published 23:15:32 ... now 23:19:11"),
                ("cmd", "cat runtime/study-files/daily-weather.csv"),
                ("out", '"2026-11-15 23:16:40","Manila","32.7","26.2","4",...'),
                ("out", '"2026-11-15 23:17:26","Manila","32.7","26.2","4",...'),
                ("out", '"2026-11-15 23:18:26","Manila","32.7","26.2","4",...'),
                ("note", "Tatlong linya sa loob ng 4 na minuto, kusa")],
         say="Ang ayos: i-Publish. Pagkatapos, naghintay ulit ako. Sa loob ng halos apat na minuto, tatlong linya ang kusang naidagdag. Wala akong ginawa. Pagkatapos nito, in-unpublish ko ulit ang bawat minutong bersyon."),
    dict(kind="shot", img="h10_executions-published", step="EXECUTIONS", hl=[(66, 222, 327, 458), (66, 162, 327, 222)], note=["Mga kusang takbo, bawat minuto", "Takbo ng 23:33 na daily trigger"],
         say="Sa Executions, nandiyan na ang mga kusang takbo, isa bawat minuto. Pansinin na hindi eksakto sa simula ng minuto ang oras ng simula: may kaunting pagitan, kaya huwag asahan ang eksaktong segundo."),
    # ------------------------------------------------------------ 5. mistake: timezone
    dict(kind="shot", chapter="Pagkakamali: maling timezone", img="h03_trigger-minutes-ny", step="COMMON MISTAKE #2", hl=[(540, 140, 830, 165), (540, 460, 830, 485)], note=["Oras sa trigger: 10:09 AM", "Timezone: America/New_York"],
         say="Pangalawang pagkakamali: ang oras. Tingnan ang output ng Schedule Trigger: 10:09 ng umaga, America New York, UTC minus 5. Pero 11:09 ng gabi na sa Manila. Ang default na timezone ng workflow ay New York."),
    dict(kind="terminal", step="COMMON MISTAKE #2", title=T_GB, note="Totoong output",
         lines=[("note", "Daily 23:27 (oras sa Manila), timezone: New York"), ("out", "# 23:24:45  lines before: 4"), ("out", "# 23:29:00  lines after: 4"),
                ("note", "Lumipas ang 23:27, walang tumakbo")],
         say="Sinubukan ko: daily trigger sa 23:27 na oras sa Manila, pero New York pa rin ang timezone. Lumipas ang 23:27, at walang tumakbo. Apat pa rin ang linya. Ang 7 ng umaga sa New York ay 8 ng gabi sa Manila."),
    dict(kind="shot", img="h13_settings-timezone", step="AYOS", hl=[(277, 228, 1148, 270), (277, 180, 1148, 222)], note=["Timezone: Asia/Manila", "Error Workflow: Error logger"],
         say="Ang ayos: buksan ang Settings ng workflow, at piliin ang Asia Manila sa Timezone. Pansinin din ang Error Workflow: ang Error logger mula sa Part 5, para maitala kung may pumalya sa kusang takbo."),
    dict(kind="shot", img="h12_trigger-output-manila", step="AYOS", hl=[(540, 140, 830, 165), (540, 460, 830, 485)], note=["Oras: 11:48 PM", "Timezone: Asia/Manila (UTC+08:00)"],
         say="Pagkatapos, ang output ng Schedule Trigger ay 11:48 ng gabi, Asia Manila, UTC plus 8. Tama na ang oras."),
    dict(kind="terminal", step="TEST 2", title=T_GB, note="Totoong output",
         lines=[("note", "Daily 23:33 (oras sa Manila), timezone: Asia/Manila"), ("out", "# 23:30:16  lines before: 4"), ("out", "# 23:35:03  lines after: 5"),
                ("out", '"2026-11-15 23:34:02","Manila","32.7","26.2","4",...'), ("note", "Tumakbo sa oras na itinakda")],
         say="Subukan ulit: daily trigger sa 23:33, timezone Asia Manila. Tumakbo ito sa oras, at may bagong linya: 23:34:02, matapos sumagot ang AI. Lima na ang linya."),
    # ------------------------------------------------------------ 6. verification and rules
    dict(kind="slide", chapter="Verification at mga paalala", slide="p6_rules", step="BAGO MO GAMITIN",
         say="Tatlong paalala. Una, hindi tatakbo ang iskedyul hangga't hindi naka-Publish ang workflow. Pangalawa, itakda ang timezone ng workflow, dahil ang default ay New York. "
             "Pangatlo, hindi eksakto ang segundo ng simula, at i-check pa rin ang payo ng AI: 4 percent lang ang ulan, payong pa rin ang payo."),
    dict(kind="slide", slide="p6_results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Walang tumakbo nang hindi naka-Publish. Nang naka-Publish, kusang naidagdag ang mga linya. Walang tumakbo sa 23:27 na may New York na timezone. Tumakbo sa 23:33 na may Asia Manila. "
             "At ang final na setting natin ay araw-araw, 7:00 AM, handa nang i-Publish."),
    dict(kind="comment", step="COMMENT", comment_q="Anong ulat ang gusto mong kusang mabuo tuwing umaga?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong ulat ang gusto mong kusang mabuo tuwing umaga? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 7. exit ramp
    dict(kind="slide", chapter="Susunod: Part 7", slide="p6_next", step="SUSUNOD",
         say="Hindi pa tapos ang serye. Sa susunod na bahagi, gagawin nating sumagot ang AI mula sa sarili mong mga notes. I-click ang playlist sa screen para panoorin ang buong serye. Nasa description ang workflow file."),
]
