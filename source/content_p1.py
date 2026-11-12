"""Part 1 script. Each step is one narration chunk plus one slide. Chunk 0 must show the result (proof hook).
Kinds: concept (items, hi), steps (items, hi), flow (boxes, labels, hi, ret), term (blocks), shot (img, note), end (title, sub).
For real command output, run commands in a throwaway sandbox (see D:/MIT/git-github-video/source/content_p2.py for the pattern).
"""
STEPS, SECTIONS = [], []


def sec(name): SECTIONS.append((name, len(STEPS)))
def add(say, kind, head, **kw): STEPS.append(dict(say=say, kind=kind, head=head, section=SECTIONS[-1][0], **kw))


sec("The result")
add("Show the finished result here and state the outcome in one sentence, using the search wording from the title.", "concept", "What you will build",
    items=["Step one", "Step two", "Step three"], hi=-1)
sec("Recap and next")
add("Recap in one or two sentences, then name the next video.", "end", "Next", title="Next: Part 2", sub="Series name")
