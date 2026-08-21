# -*- coding: utf-8 -*-
"""
Static site generator for "Vibe Coding Copilot" — a free vibe-coding course
for higher-education staff, built around GitHub Copilot (to build) and
GitHub (to save, version and publish). FR / NL / EN.
Run: python generate_site.py
"""
import os

import site_refresh

ROOT = os.path.dirname(os.path.abspath(__file__))

LANGS = ["fr", "nl", "en"]
LANG_LABEL = {"fr": "FR", "nl": "NL", "en": "EN"}

# ------------------------------------------------------------------
# CONTENT — English
# ------------------------------------------------------------------
CONTENT = {}

CONTENT["en"] = {
    "meta": {
        "html_lang": "en",
        "site_name": "Vibe Coding Copilot",
        "brand_tagline": "Higher Education",
        "title_suffix": "Vibe Coding with GitHub Copilot for Higher Education",
        "description": "A free course to learn vibe coding with GitHub Copilot: build, test, and "
                       "publish your own digital tools for higher education, without being a developer.",
    },
    "nav": {
        "home": "Home",
        "explorer": "Use Case Explorer",
        "basics": "Vibe Coding Basics",
        "advanced": "Vibe Coding Advanced",
        "expert": "Vibe Coding Expert",
        "best_practices": "Best practices",
        "toolkit": "Toolkit",
        "about": "About",
        "all_lessons": "All lessons",
        "view_route": "View the full track",
        "exercise_label": "Try it yourself",
    },
    "footer": {
        "text": "An independent, free learning resource for vibe coding in higher education, "
                "powered by GitHub Copilot. Not affiliated with or endorsed by GitHub or Microsoft.",
    },
    "home": {
        "eyebrow": "Free course \u00b7 Vibe Coding with GitHub Copilot",
        "h1_line1": "Vibe Coding",
        "h1_line2": "for Higher Education",
        "lede": "You don't need to be a developer to build your own digital tools. Whether "
                "you teach, study, run IT, manage people, lead a department, or handle the "
                "budget \u2014 this free course walks you, step by step, through building a "
                "real web app with GitHub Copilot. You stay the expert in your own job; AI "
                "helps you build, and GitHub saves, versions, and publishes the result.",
        "cta_primary": "Explore the use cases",
        "cta_secondary": "Follow the guided track",
        "hero_note": "Free. No programming experience required. Just GitHub Copilot, a bit of "
                     "curiosity, and 25 practical lessons.",
        "personas_title": "Built for every part of the institution",
        "personas_sub": "Vibe coding isn't just for developers \u2014 or just for teaching staff. "
                        "Here's what it looks like across campus.",
        "personas": [
            ("\U0001f393", "Teaching staff", "Build the small tool you've imagined for years: "
             "a quiz, a live syllabus, a grading helper.", "Example:",
             "A biology lecturer builds a self-marking revision quiz in one afternoon."),
            ("\U0001f9d1\u200d\U0001f393", "Students", "You don't need a computer science degree "
             "to vibe code your own study tools, portfolio, or association website.", "Example:",
             "A student group builds a shared flashcard app to revise together before finals."),
            ("\U0001f5a5\ufe0f", "IT & digital services", "Prototype internal tools in hours "
             "instead of months, then govern them properly with GitHub Enterprise.", "Example:",
             "IT builds a self-service room-booking tool and manages access centrally on GitHub."),
            ("\U0001f91d", "HR & staff development", "Turn a repetitive onboarding or training "
             "process into a simple, friendly web app.", "Example:",
             "HR builds an interactive onboarding checklist for new staff members."),
            ("\U0001f9ed", "Management & leadership", "Get a real feedback tool or dashboard "
             "built in days, without waiting for a full IT project.", "Example:",
             "A department head builds a live poll to gather feedback during a town hall."),
            ("\U0001f4b6", "Finance & administration", "Automate a small repetitive task: a "
             "budget calculator, an expense form, a simple tracker.", "Example:",
             "The finance team builds a small travel-expense calculator for staff."),
        ],
        "journey_title": "From a teaching idea to a published app",
        "journey_sub": "Every track in this course follows the same, very concrete path.",
        "journey": [
            ("01", "Idea", "Start from a real teaching problem and turn it into an app idea."),
            ("02", "Build", "Build a first version with GitHub Copilot, without writing code alone."),
            ("03", "Publish", "Save your project on GitHub and publish it online for your students."),
            ("04", "Improve", "Test, refine, and evolve your tool based on real feedback."),
        ],
        "courses_title": "Three tracks, one goal: vibe code for real",
        "courses_sub": "Start wherever you are: from your first app with Copilot to a complete "
                       "teaching tool hosted on GitHub.",
        "examples_title": "What you can vibe code, whatever your role",
        "examples_sub": "Concrete ideas you can build in a few hours with GitHub Copilot.",
        "examples": [
            ("Interactive revision quiz", "A self-marking quiz to review a chapter, that your "
             "students use before the exam.", "Teaching staff"),
            ("A living course page", "An interactive syllabus with an automatic FAQ, schedule, "
             "and centralized resources.", "Teaching staff"),
            ("Shared flashcard app", "A flip-on-click flashcard tool a study group builds "
             "together to revise before finals.", "Students"),
            ("Custom grade calculator", "A tool that estimates the final grade using your "
             "course's own rubric.", "Students"),
            ("Self-service room booking", "An internal tool to book a room or lab slot, with "
             "live availability and an approval step.", "IT & digital services"),
            ("Interactive onboarding checklist", "A friendly, step-by-step checklist that walks "
             "new staff through their first two weeks.", "HR"),
            ("Live town-hall poll", "A quick poll that gathers real-time feedback from staff "
             "during a meeting \u2014 try the live demo in lesson 3!", "Management"),
            ("Small expense calculator", "A lightweight tool to estimate and log small "
             "recurring expenses or travel costs.", "Finance"),
            ("Student project showcase", "A web gallery where each student presents their "
             "end-of-semester project.", "Teaching & students"),
        ],
        "teaser_title": "Not sure where to start? Read the best practices first.",
        "teaser_desc": "A one-page checklist to kick off your first vibe-coding project, from "
                       "idea to publishing on GitHub.",
        "teaser_cta": "View best practices",
    },
    "tracks": {
        "basics": {
            "slug": "vibe-basics",
            "tag_class": "tag-basics",
            "level_label": "Basics",
            "title": "Vibe Coding Basics",
            "subtitle": "Your first steps in vibe coding: turn a teaching idea into a real app, "
                        "with GitHub Copilot.",
            "card_desc": "Discover vibe coding, build your first teaching web app with Copilot, "
                         "and publish it online.",
            "meta": "8 lessons \u00b7 about 1.5 hours",
            "lessons": [
                {
                    "title": "What is vibe coding?",
                    "kicker": "Lesson 1",
                    "paragraphs": [
                        "Vibe coding means building an application by describing what you want "
                        "to an AI, instead of writing every line of code yourself. With GitHub "
                        "Copilot, you explain your need in plain language and the AI proposes "
                        "the code; you stay in charge \u2014 you read, adjust, and approve.",
                        "For higher education, this changes everything: you can finally build "
                        "the small tool you've imagined for years, without waiting on an IT "
                        "department or spending six months learning to program. This track "
                        "walks you through it step by step, using one real teaching project as your thread.",
                    ],
                    "tip": "You don't need to install anything to read this track. Installing "
                           "Copilot comes in the next lesson.",
                    "exercise": "Whatever your role \u2014 teaching, studying, IT, HR, "
                                "management, finance \u2014 write down, in one sentence, the "
                                "small app you'd love to have. You'll build a real one in Lesson 3.",
                },
                {
                    "title": "From a teaching problem to an app idea",
                    "kicker": "Lesson 2",
                    "paragraphs": [
                        "The best starting point is never a technology, it's a real problem: "
                        "students with no easy way to revise, a course schedule scattered across "
                        "ten emails, repetitive grading. Always start from that lived, concrete experience.",
                        "Describe the problem in one sentence, then imagine the smallest possible "
                        "app that would solve it. A quiz, a page, a calculator: keep it simple to "
                        "start \u2014 you can always grow it later.",
                    ],
                    "tip": "Write your idea as: \u201cAn app that lets [who] do [what] so that "
                           "[what benefit]\u201d.",
                    "exercise": "Pick ONE real problem you or a colleague complains about "
                                "weekly \u2014 in class, at the help desk, during onboarding, in "
                                "a budget meeting \u2014 and write your app idea using the sentence above.",
                },
                {
                    "title": "Your first web app with GitHub Copilot",
                    "kicker": "Lesson 3",
                    "paragraphs": [
                        "This is the lesson where you actually build something. Install the "
                        "GitHub Copilot extension in Visual Studio Code (or open Copilot Chat "
                        "directly on github.com), sign in with your GitHub account, then create "
                        "a new file called index.html.",
                        "Below, we build a real, working example together \u2014 a \u201cQuick "
                        "Poll\u201d you could use in a class, a training session, a team meeting, "
                        "or a town hall. Follow the three steps with your own copy of Copilot, "
                        "then try the finished result live at the end.",
                    ],
                    "extra_html": '''
<div class="step-badge">Step 1 \u2014 Describe the skeleton</div>
<p>Open Copilot Chat and describe the smallest possible version of your idea. Be specific about what's on the page.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Build a simple webpage called "Quick Poll" with a question and four buttons as answer options.</div>
    <div class="chat-bubble-ai">Here's a starting point:
      <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Quick Poll&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
  &lt;h2&gt;What would help you most this term?&lt;/h2&gt;
  &lt;button&gt;Worked examples&lt;/button&gt;
  &lt;button&gt;More exercises&lt;/button&gt;
  &lt;button&gt;Short videos&lt;/button&gt;
  &lt;button&gt;Live Q&amp;amp;A&lt;/button&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
    </div>
  </div>
</div>
<p>Save this, open it in your browser by double-clicking the file. You now have a real, if plain, webpage.</p>

<div class="step-badge">Step 2 \u2014 Ask for the logic</div>
<p>A page with buttons that do nothing isn't very useful yet. Ask Copilot to make the buttons count votes.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">When someone clicks a button, save a vote count for that option in the browser (localStorage), so it's remembered if the page reloads.</div>
    <div class="chat-bubble-ai">I added this script at the bottom of your page:
      <pre><code>&lt;script&gt;
  document.querySelectorAll("button").forEach((btn, i) =&gt; {
    btn.addEventListener("click", () =&gt; {
      let votes = JSON.parse(localStorage.getItem("votes")) || [0,0,0,0];
      votes[i]++;
      localStorage.setItem("votes", JSON.stringify(votes));
      alert("Thanks for voting!");
    });
  });
&lt;/script&gt;</code></pre>
    </div>
  </div>
</div>
<p>Test it: click a button, reload the page, click again \u2014 the count keeps growing even though you can't see it yet. That's next.</p>

<div class="step-badge">Step 3 \u2014 Show the results</div>
<p>Now ask Copilot to replace that plain <code>alert()</code> with something people can actually see.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Instead of an alert, hide the buttons after voting and show each option as a percentage bar based on the votes so far.</div>
    <div class="chat-bubble-ai">Good idea \u2014 that's much clearer for people voting. I replaced the alert with a small results view that calculates each option's share of the total votes and animates a bar for it. Want me to also add a "vote again" link to reset it for this demo?</div>
  </div>
</div>
<p>Keep going like this \u2014 one small request at a time \u2014 until the page looks and feels the way you want.</p>

<div class="step-badge">Step 4 \u2014 Try what you just built</div>
<p>This is exactly the app described above, already built and running below. Click an option and watch the results appear \u2014 this is what your students, colleagues, or team will see once you publish yours (next lesson).</p>
<div class="demo-frame-wrap">
  <div class="demo-frame-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">quick-poll.html</span></div>
  <iframe src="../assets/demo/quick-poll-en.html" loading="lazy" title="Quick Poll live demo"></iframe>
</div>
''',
                    "tip": "Always start from a tiny working version before adding features \u2014 "
                           "step 1 above is a complete, working page all on its own.",
                    "exercise": "Rebuild this exact Quick Poll yourself in a new index.html file, "
                                "then change the question and the four options to match your "
                                "own role \u2014 a class topic, an onboarding question, a budget "
                                "priority, anything real to you.",
                },
                {
                    "title": "Saving and publishing with GitHub",
                    "kicker": "Lesson 4",
                    "paragraphs": [
                        "Once your first version works, create a repository on GitHub and push "
                        "your code to it \u2014 this is called a commit. From that point on, your "
                        "work is saved online, versioned, and you can always go back to an "
                        "earlier version if something breaks.",
                        "Then turn on GitHub Pages for that repository: in a few clicks, your app "
                        "becomes reachable through a simple link you can share with students or "
                        "colleagues, with no server to manage.",
                    ],
                    "tip": "A GitHub repository is also your backup: even if your computer dies, "
                           "your project is safe.",
                    "exercise": "Create a free GitHub account if you don't have one, push your "
                                "Quick Poll to a brand-new repository, and turn on GitHub Pages "
                                "for it.",
                },
                {
                    "title": "Testing and improving with Copilot Chat",
                    "kicker": "Lesson 5",
                    "paragraphs": [
                        "Have one or two colleagues try your app, or test it yourself by putting "
                        "yourself in a student's shoes. Note every bug or awkward moment, then "
                        "describe them one by one to Copilot Chat: \u201cwhen I click this "
                        "button, nothing happens, fix it\u201d.",
                        "Copilot can also explain existing code you don't fully understand yet: "
                        "ask \u201cexplain this part to me\u201d before asking for a change.",
                    ],
                    "tip": "One fix at a time: it's easier to check it worked, and easier to "
                           "undo if needed.",
                    "exercise": "Send your published link to two colleagues (or classmates) and "
                                "ask them to click through it. Write down every awkward moment "
                                "they hit, then fix the first one with Copilot Chat.",
                },
                {
                    "title": "Improving style and appearance",
                    "kicker": "Lesson 6",
                    "paragraphs": [
                        "Once your app works, ask Copilot to dress it up: your institution's "
                        "colours, a more readable font, a clearer layout for your students. You "
                        "can even paste a screenshot of a style you like and ask Copilot to draw "
                        "inspiration from it.",
                        "Think about accessibility too: enough contrast, readable text, big "
                        "enough buttons. Simply ask Copilot to check your page's accessibility \u2014 it will know what to fix.",
                    ],
                    "tip": None,
                    "exercise": "Ask Copilot to restyle your Quick Poll using two colors that "
                                "represent your institution or team, then open it on your phone "
                                "to check it still looks good.",
                },
                {
                    "title": "Adding images, files, and documents",
                    "kicker": "Lesson 7",
                    "paragraphs": [
                        "Many teaching tools need images, PDFs, or downloadable documents: a "
                        "handout, a diagram, a form. Ask Copilot to add an image display area or "
                        "a download button, then simply drop the file into your GitHub repository.",
                        "GitHub hosts your code and these files alike: no need for another tool "
                        "to store your app's resources.",
                    ],
                    "tip": None,
                    "exercise": "Add one image or one downloadable PDF to your Quick Poll (even "
                                "a placeholder), commit it, and confirm it loads correctly on the "
                                "published page.",
                },
                {
                    "title": "Wrap-up and on to the Advanced track",
                    "kicker": "Lesson 8",
                    "paragraphs": [
                        "You now know how to turn a teaching idea into a real app: build with "
                        "Copilot, save and publish with GitHub, test, improve the style, add "
                        "files. The one habit that matters most: always move forward in small, checkable steps.",
                        "The Advanced track picks up from here to go further: connecting a real "
                        "database, giving your project a lasting memory, and managing your code "
                        "with GitHub like a real project meant to last.",
                    ],
                    "tip": None,
                    "exercise": "Write a 3-line README for your project: what it does, who it's "
                                "for, and how to reopen it with Copilot next time.",
                },
            ],
        },
        "advanced": {
            "slug": "vibe-advanced",
            "tag_class": "tag-advanced",
            "level_label": "Advanced",
            "title": "Vibe Coding Advanced",
            "subtitle": "Connect a database, give your project memory, and manage your code like "
                        "a project that lasts, with GitHub.",
            "card_desc": "Databases, pedagogical design, project memory, and code management with "
                         "GitHub: everything to build a real tool that lasts.",
            "meta": "9 lessons \u00b7 about 2 hours",
            "lessons": [
                {
                    "title": "Working with Copilot's agent mode",
                    "kicker": "Lesson 1",
                    "paragraphs": [
                        "Beyond line-by-line suggestions, Copilot offers an agent mode: describe "
                        "a bigger task (\u201cadd a sign-up form to my quiz and make sure it "
                        "works\u201d), and Copilot plans several changes, applies them, and "
                        "checks the result, with checkpoints for you to approve.",
                        "This is the right tool once your app grows and you no longer want to "
                        "describe every small line one by one.",
                    ],
                    "tip": "Always review the proposed plan before letting the agent work \u2014 "
                           "it's the best moment to correct course.",
                    "exercise": "Describe one multi-step task to Copilot's agent mode (for "
                                "example, adding a results page to your Quick Poll) and review "
                                "its plan carefully before letting it run.",
                },
                {
                    "title": "Connecting a database to your app",
                    "kicker": "Lesson 2",
                    "paragraphs": [
                        "As soon as your tool needs to remember information from one session to "
                        "the next (quiz answers, sign-ups, grades), you need a database. Services "
                        "like Supabase let you create one for free, with no server setup, and "
                        "Copilot helps you write the connection code.",
                        "Describe to Copilot what you want to store (for example: the student's "
                        "name and their score), and let it propose the database structure and the "
                        "code needed to read and write to it.",
                    ],
                    "tip": None,
                    "exercise": "Create a free Supabase project and connect it to a small test "
                                "page that stores just one piece of information, like a name and a vote.",
                },
                {
                    "title": "Using that database safely",
                    "kicker": "Lesson 3",
                    "paragraphs": [
                        "A poorly protected database can expose your students' data. Always ask "
                        "Copilot to add security rules (who is allowed to read or write what), "
                        "and never store more personal information than necessary.",
                        "Think about your students' data protection from the start (GDPR in "
                        "Europe): anonymise what can be anonymised, and be clear about what the "
                        "data you collect is used for.",
                    ],
                    "tip": "When in doubt, ask Copilot: \u201cdoes this code follow good data "
                           "protection practice?\u201d",
                    "exercise": "Ask Copilot to review your database code for security issues, "
                                "and fix at least one thing it flags.",
                },
                {
                    "title": "Designing consciously for learning",
                    "kicker": "Lesson 4",
                    "paragraphs": [
                        "A good teaching tool isn't just functional, it's designed for learning: "
                        "immediate feedback after an answer, visible progress, encouragement "
                        "rather than punishment. Describe these pedagogical intentions to "
                        "Copilot, not just technical features.",
                        "For example, instead of \u201cshow the score\u201d, ask for \u201cshow "
                        "the score with an explanation for each mistake, so the student "
                        "understands why they got it wrong\u201d.",
                    ],
                    "tip": None,
                    "exercise": "Rewrite one feature request for your project as a "
                                "learning-or-user-focused prompt, following the example above, "
                                "instead of a purely technical one.",
                },
                {
                    "title": "Writing a solid build plan",
                    "kicker": "Lesson 5",
                    "paragraphs": [
                        "Before asking Copilot for a big feature, write yourself a short plan in "
                        "a few lines: the steps, the logical order, what's essential and what can "
                        "wait. A good plan produces far better suggestions than a vague request.",
                        "Then share this plan with Copilot Chat before you start coding \u2014 it "
                        "can flag missing steps or a more logical order.",
                    ],
                    "tip": None,
                    "exercise": "Write a five-line build plan for your next feature before "
                                "asking Copilot for any code, then share it with Copilot Chat first.",
                },
                {
                    "title": "Iterating smartly without breaking your app",
                    "kicker": "Lesson 6",
                    "paragraphs": [
                        "The bigger your project grows, the more tempting it is to ask for "
                        "several changes at once. Resist that: one change, one test, one commit "
                        "on GitHub. If something breaks, you know exactly what to undo.",
                        "GitHub lets you roll back very easily thanks to its commit history: it's "
                        "your safety net to keep iterating without stress.",
                    ],
                    "tip": None,
                    "exercise": "Make three small, separate commits today, each with one clear "
                                "change and one clear commit message.",
                },
                {
                    "title": "Giving your project a lasting memory",
                    "kicker": "Lesson 7",
                    "paragraphs": [
                        "Without specific instructions, Copilot won't necessarily remember your "
                        "preferences from one day to the next. Create a copilot-instructions.md "
                        "file in a .github/ folder of your repository: describe your preferred "
                        "coding style, your visual identity, or rules like \u201calways write "
                        "comments in English\u201d.",
                        "This file becomes your project's lasting memory: every future Copilot "
                        "suggestion will take it into account, even in a brand-new session.",
                    ],
                    "tip": "Revisit and add to this file as the project grows: it's a five-minute "
                           "investment that improves every future working session.",
                    "exercise": "Create your first copilot-instructions.md file with at least "
                                "three rules specific to your own project.",
                },
                {
                    "title": "Using AI as a tester",
                    "kicker": "Lesson 8",
                    "paragraphs": [
                        "Before showing your app to real students, ask Copilot Chat to play a "
                        "clumsy or distracted user: \u201ctry to break this form\u201d, \u201cwhat "
                        "happens if I leave this field empty?\u201d.",
                        "Also ask it to generate test cases: examples of correct, incorrect, or "
                        "completely unexpected answers to your quiz or form.",
                    ],
                    "tip": None,
                    "exercise": "Ask Copilot Chat to try to break your app in three different "
                                "ways, then fix whatever it finds.",
                },
                {
                    "title": "Managing your code like a real project with GitHub",
                    "kicker": "Lesson 9",
                    "paragraphs": [
                        "A project meant to last needs real organization: clear, regular commits, "
                        "branches to try an idea without breaking the working version, and "
                        "possibly GitHub Enterprise or GitHub Education if your institution wants "
                        "to host and manage these projects centrally for several teaching staff.",
                        "This is also what lets you collaborate: a colleague can propose changes "
                        "through a pull request, which you review before accepting it, exactly "
                        "like a development team would.",
                    ],
                    "tip": None,
                    "exercise": "Create a branch, make one small change on it, and open your "
                                "first pull request to merge it back into your main version.",
                },
            ],
        },
        "expert": {
            "slug": "vibe-expert",
            "tag_class": "tag-expert",
            "level_label": "Expert",
            "title": "Vibe Coding Expert",
            "subtitle": "Add artificial intelligence to your app and build a complete example, "
                        "ready for a real course.",
            "card_desc": "Go further: add AI to your app, choose the right model, keep costs "
                         "under control, and finish with a complete example.",
            "meta": "8 lessons \u00b7 about 1.5 hours",
            "lessons": [
                {
                    "title": "Adding AI to your teaching app",
                    "kicker": "Lesson 1",
                    "paragraphs": [
                        "So far, Copilot has helped you write the code of your app. This lesson "
                        "goes further: adding an AI feature your students can use directly, like "
                        "an \u201cexplain this differently\u201d button that queries an AI model live.",
                        "Ask Copilot to help you build this integration: a button that sends a "
                        "question to an AI model and displays the answer on your page.",
                    ],
                    "tip": None,
                    "exercise": "Add one AI-powered button to an existing project \u2014 even a "
                                "placeholder that just echoes the question back \u2014 to see the wiring end to end.",
                },
                {
                    "title": "Choosing and comparing AI models",
                    "kicker": "Lesson 2",
                    "paragraphs": [
                        "Several families of AI models exist (GPT, Claude, Gemini, among others), "
                        "with differences in quality, speed, and cost. Inside Copilot Chat, you "
                        "can already pick between several models depending on the task.",
                        "For the AI built into your teaching app, start simple with an "
                        "inexpensive model, and only move to a more powerful one if you really need to.",
                    ],
                    "tip": None,
                    "exercise": "Ask the same question to two different models inside Copilot "
                                "Chat and compare the answers for quality, tone, and speed.",
                },
                {
                    "title": "Setting up your access keys securely",
                    "kicker": "Lesson 3",
                    "paragraphs": [
                        "To use an AI model in your app, you need an access key (API key): a kind "
                        "of password for that service. Never put this key directly in code that "
                        "is visible on GitHub.",
                        "Ask Copilot to help you store it as a protected secret (environment "
                        "variable or GitHub secret): your institution's IT department can help "
                        "with this if needed.",
                    ],
                    "tip": "A key exposed by mistake can be used by others: if that happens, "
                           "regenerate it immediately.",
                    "exercise": "Store one API key as a protected secret instead of directly in "
                                "your code, and confirm your code still works by reading it from there.",
                },
                {
                    "title": "First small project: an AI explanation button",
                    "kicker": "Lesson 4",
                    "paragraphs": [
                        "Build a concrete example: on your course page, an \u201cI don't "
                        "understand\u201d button that sends the student's question to an AI "
                        "model and shows a different explanation, simpler or with another example.",
                        "Ask Copilot to build this feature step by step, testing each part before moving to the next.",
                    ],
                    "tip": None,
                    "exercise": "Build the \u201cI don't understand\u201d button end to end on a "
                                "real page you own \u2014 your Quick Poll or another project.",
                },
                {
                    "title": "Deploying your AI integration safely",
                    "kicker": "Lesson 5",
                    "paragraphs": [
                        "An AI integration should never expose your access key in the student's "
                        "browser. Ask Copilot to set up a small server-side function that "
                        "receives the question, calls the AI model with the hidden key, and "
                        "returns only the answer.",
                        "Platforms like Vercel or Netlify let you host this kind of function for "
                        "free for a small project, in a few clicks straight from your GitHub repository.",
                    ],
                    "tip": None,
                    "exercise": "Deploy your AI feature through a small serverless function, and "
                                "check your browser's network tab to confirm the key never appears there.",
                },
                {
                    "title": "Building safely and affordably",
                    "kicker": "Lesson 6",
                    "paragraphs": [
                        "An AI model costs something for every question asked. For teaching use "
                        "with a group of students, set a clear limit (a number of questions per "
                        "day, for example) to avoid unpleasant surprises.",
                        "Ask Copilot to add this limit directly in the code, and regularly check "
                        "usage through the dashboard of the AI service you're using.",
                    ],
                    "tip": None,
                    "exercise": "Add a daily usage limit to your AI feature and test what happens "
                                "once that limit is reached.",
                },
                {
                    "title": "Going beyond text",
                    "kicker": "Lesson 7",
                    "paragraphs": [
                        "AI isn't limited to text: some models can describe an image, transcribe "
                        "an audio recording, or even generate an image from a description. For a "
                        "course, this opens possibilities like marking a hand-drawn diagram or "
                        "transcribing an oral presentation.",
                        "These features need a bit more preparation, but the method stays the "
                        "same: describe precisely what you want to Copilot, test, adjust.",
                    ],
                    "tip": None,
                    "exercise": "Try asking an AI model to describe or summarise one image or "
                                "recording relevant to your own role.",
                },
                {
                    "title": "Full example and conclusion",
                    "kicker": "Lesson 8",
                    "paragraphs": [
                        "To close this track, here is a complete example you can build end to "
                        "end: an interactive quiz with automatic grading, scores saved to a "
                        "database, and an AI explanation button for every missed question, all "
                        "published online through GitHub.",
                        "You now have every tool you need to build, test, publish, and evolve "
                        "your own teaching apps. The only real limit now is the time you want to "
                        "spend on it: thank you for following this track, and happy vibe coding!",
                    ],
                    "tip": None,
                    "exercise": "Write down one thing you'll build next with what you've learned "
                                "in this course \u2014 then go build it.",
                },
            ],
        },
    },
    "best_practices": {
        "title": "Best practices",
        "sub": "A one-page checklist to start your vibe-coding project the right way, from idea "
               "to publishing on GitHub.",
        "items": [
            ("Always start from a real teaching problem", "The best app idea comes from a "
             "concrete frustration you live in class, not from a trendy technology."),
            ("Start tiny", "One feature that works beats an ambitious plan that never ships. "
             "Grow it step by step afterwards."),
            ("One change, one test, one commit", "Never ask for ten changes at once \u2014 "
             "you'd lose track of which one broke what."),
            ("Save everything on GitHub from day one", "Even a tiny project deserves a GitHub "
             "repository: it's your backup and your version history."),
            ("Never store sensitive data without thinking it through", "Always ask Copilot "
             "whether your code follows good data-protection practice before collecting any "
             "information about your students."),
            ("Protect your access keys", "An API key should never appear in code visible on "
             "GitHub \u2014 always use a protected secret."),
            ("Review every suggestion before accepting it", "Copilot proposes, you decide: "
             "understand what the code does before using it with real students."),
            ("Give your project a memory", "A copilot-instructions.md file saves precious time "
             "in every new working session."),
            ("Get a real colleague or student to test it", "An outside perspective always finds "
             "awkward spots you'd never notice alone."),
            ("Document your project in one page", "A short README explains to a colleague (or "
             "to yourself in six months) what the project does and how to run it again."),
        ],
    },
    "about": {
        "title": "About this track",
        "paragraphs": [
            "Vibe Coding Copilot is an independent, free learning resource for anyone working "
            "or studying in higher education \u2014 teaching staff, students, IT and digital "
            "services, HR, management, finance and administration \u2014 who wants to build "
            "their own digital tools without being a developer.",
            "This site is not affiliated with, endorsed by, or sponsored by GitHub or Microsoft. "
            "All product names and trademarks mentioned belong to their respective owners; this "
            "site simply explains how to use them well in an institutional context.",
        ],
        "sections": [
            ("Why this track exists", [
                "Many excellent ideas \u2014 in a classroom, a help desk, an HR office, or a "
                "finance team \u2014 stay stuck for lack of programming skills or budget for "
                "custom development. Vibe coding, with tools like GitHub Copilot, changes that "
                "equation: you become able to build it yourself, while staying in control of your own domain.",
            ]),
            ("Why GitHub specifically", [
                "Building an app with AI is only half the journey: you still need to save it, "
                "evolve it without breaking it, and publish it somewhere. GitHub (and GitHub "
                "Enterprise or GitHub Education for institutions) answers exactly that need, and "
                "integrates natively with GitHub Copilot.",
            ]),
            ("Feedback", [
                "This track is a living document. If you're missing an example, a lesson, or an "
                "explanation, treat it like any other piece of teaching material: suggest an improvement.",
            ]),
        ],
    },
    "toolkit": {
        "title": "Toolkit \u2014 prompt library",
        "sub": "Ready-to-use Copilot prompts, organized by role. Copy one, adapt the details in "
               "brackets, and paste it into Copilot Chat.",
        "groups": [
            ("\U0001f393", "Teaching staff", [
                "Build a self-marking quiz about [topic] with 5 multiple-choice questions and instant feedback.",
                "Add a button that lets students download their quiz results as a PDF.",
                "Turn the course notes I'll paste below into a structured, printable revision sheet.",
            ]),
            ("\U0001f9d1\u200d\U0001f393", "Students", [
                "Build a flashcard app for [subject] where cards flip on click and can be marked as \u201cknown\u201d.",
                "Add a countdown timer to my study page that resets after every 25-minute session.",
                "Create a simple portfolio page listing my three best projects with links and screenshots.",
            ]),
            ("\U0001f5a5\ufe0f", "IT & digital services", [
                "Build a simple internal tool where staff can request a room booking and see live availability.",
                "Add a check so only people with a [domain] email address can submit this form.",
                "Generate a GitHub Actions workflow that deploys this site to GitHub Pages on every push.",
            ]),
            ("\U0001f91d", "HR & staff development", [
                "Build an interactive onboarding checklist with progress tracking for new employees.",
                "Create a feedback form for a training session with a 1-5 rating and a comments box.",
                "Add a page that calculates how many vacation days are left, based on a start date I enter.",
            ]),
            ("\U0001f9ed", "Management & leadership", [
                "Build a live poll page where staff can vote on one question and see results update instantly.",
                "Create a simple dashboard that summarizes the three numbers I'll paste in as KPIs.",
                "Turn this bullet-point strategy summary into a clean, one-page visual page.",
            ]),
            ("\U0001f4b6", "Finance & administration", [
                "Build a small calculator that estimates travel expense reimbursement from distance and rate.",
                "Create a simple form to log recurring expenses with a running total.",
                "Generate a sortable table from the data I'll paste in below.",
            ]),
        ],
    },
    "explorer": {
        "title": "GitHub Copilot use-case explorer",
        "sub": "26 concrete, ready-to-follow use cases across every part of higher education. "
               "Filter by role or by Copilot feature, then open a card for the exact steps.",
        "search_placeholder": "Search a use case (e.g. \u201cquiz\u201d, \u201cbudget\u201d, \u201cchat\u201d)...",
        "persona_filter_label": "Role",
        "feature_filter_label": "Copilot feature",
        "all_label": "All roles",
        "show_steps": "Show the steps",
        "hide_steps": "Hide the steps",
        "result_label": "Result:",
        "further_label": "Go further:",
        "count_prefix": "Showing",
        "count_suffix": "use cases",
        "empty_message": "No use case matches these filters yet \u2014 try clearing a filter or the search box.",
        "personas": [
            ("teaching", "\U0001f393", "Teaching staff"),
            ("students", "\U0001f9d1\u200d\U0001f393", "Students"),
            ("it", "\U0001f5a5\ufe0f", "IT & digital services"),
            ("hr", "\U0001f91d", "HR"),
            ("leadership", "\U0001f9ed", "Leadership & management"),
            ("finance", "\U0001f4b6", "Finance & administration"),
            ("research", "\U0001f52c", "Researchers"),
            ("campus", "\U0001f4da", "Library, comms & campus life"),
        ],
        "features": [
            ("inline", "Inline completions", "Copilot suggests code as you type, right where you're working."),
            ("chat", "Copilot Chat", "Ask questions, request changes, or get code explained in plain language."),
            ("agent", "Agent mode", "Describe a bigger task; Copilot plans and applies several changes at once."),
            ("cli", "Copilot in the CLI", "Describe what you want in your terminal; Copilot suggests the exact command."),
            ("review", "Copilot code review", "AI review suggestions and reviewer focus areas before or during human review."),
            ("cloudagent", "Copilot cloud agent", "Assign an issue or task to Copilot; it works on a branch and opens a pull request."),
            ("spaces", "Copilot Spaces", "Ground Copilot with shareable context such as files, notes, transcripts, and images."),
            ("mcp", "Extensions & MCP", "Connect Copilot to your own tools and data sources."),
        ],
        "usecases": [
            {
                "title": "Build a self-marking quiz in one sitting",
                "persona": "teaching", "features": ["chat", "inline"],
                "situation": "You want a quiz your students can use to revise a chapter, without an external paid tool.",
                "steps": [
                    "Open Copilot Chat and describe your quiz: \u201cBuild an HTML page with a 5-question multiple-choice quiz about [topic], showing a final score.\u201d",
                    "Read the generated code, test it in your browser, then ask one precise change at a time, e.g. \u201cAdd a short explanation under each question once it's answered.\u201d",
                    "Once you're happy with it, ask Copilot to add a \u201crestart quiz\u201d button.",
                ],
                "result": "A working, customized quiz for your course, ready to publish.",
                "further": "Ask Copilot to shuffle the question order on every launch.",
            },
            {
                "title": "Turn a hand-drawn diagram into a digital one with Copilot Spaces",
                "persona": "teaching", "features": ["spaces", "chat"],
                "situation": "You have a photo or screenshot of a diagram or handwritten exercise to digitize.",
                "steps": [
                    "Paste the screenshot directly into Copilot Chat.",
                    "Ask: \u201cDescribe this diagram and turn it into HTML/CSS that reproduces its structure.\u201d",
                    "Refine colours and labels with follow-up requests.",
                ],
                "result": "A digital, editable diagram built from a simple photo.",
                "further": "Use the same method to digitize a handwritten grading rubric.",
            },
            {
                "title": "Generate exercise variants to reduce copying",
                "persona": "teaching", "features": ["chat"],
                "situation": "You want several versions of the same exercise for different student groups.",
                "steps": [
                    "Give Copilot Chat an existing exercise and ask: \u201cGenerate 4 variants of this exercise with different values but the same difficulty.\u201d",
                    "Ask for a shared marking scheme: \u201cAdd a marking scheme explaining each step.\u201d",
                    "Ask Copilot to export everything into one structured document.",
                ],
                "result": "Several ready-to-distribute versions with a consistent marking scheme.",
                "further": "Ask Copilot to also generate an accessible version for screen readers.",
            },
            {
                "title": "Automate a weighted grade calculator with agent mode",
                "persona": "teaching", "features": ["agent", "chat"],
                "situation": "You manage a complex grading spreadsheet and want automatic weighted averages.",
                "steps": [
                    "Describe your grading scheme to agent mode: \u201cBuild a page that calculates a weighted average from these categories: [list].\u201d",
                    "Review the plan the agent proposes before approving it.",
                    "Ask it to add a CSV export to share results with colleagues.",
                ],
                "result": "A reliable calculator matched to your own grading scheme.",
                "further": "Connect it to a real database (see the Advanced track) to reuse it every semester.",
            },
            {
                "title": "Learn to code with Copilot as a tutor, not a crutch",
                "persona": "students", "features": ["inline", "chat"],
                "situation": "You're new to programming and want to understand code, not just copy it.",
                "steps": [
                    "Write a simple function yourself first, even an incomplete one.",
                    "Ask Copilot Chat: \u201cExplain line by line what this code does.\u201d",
                    "Then ask: \u201cQuiz me on one thing to check I understood.\u201d",
                ],
                "result": "Real understanding of the code, not just copy-pasting.",
                "further": "Ask Copilot for a slightly harder exercise on the same concept.",
            },
            {
                "title": "Build a shared revision site for your study group",
                "persona": "students", "features": ["chat", "cli"],
                "situation": "Your study group wants one shared place to revise before the exam.",
                "steps": [
                    "Describe the flashcard app you want to Copilot Chat.",
                    "Use Copilot in the terminal to create the repository: describe what you want to do, Copilot suggests the exact git command.",
                    "Share the GitHub Pages link with the group.",
                ],
                "result": "A free, shared revision tool your whole group controls.",
                "further": "Add a simple upvote system for the best flashcards.",
            },
            {
                "title": "Present your thesis or internship report online",
                "persona": "students", "features": ["chat"],
                "situation": "You need to structure a long document and automate repetitive parts like a table of contents.",
                "steps": [
                    "Ask Copilot to generate a site skeleton to present your thesis online (summary, chapters, appendices).",
                    "Ask for an interactive table of contents built from your section headings.",
                    "Add a contact page to receive feedback.",
                ],
                "result": "An online, presentable version of your thesis, alongside the classic document.",
                "further": "Ask Copilot to add keyword search across the content.",
            },
            {
                "title": "Build a portfolio for your internship or job search",
                "persona": "students", "features": ["chat", "spaces"],
                "situation": "You want a simple site showcasing your projects, without starting from a blank page.",
                "steps": [
                    "Paste a screenshot of a portfolio style you like and ask Copilot Chat to draw inspiration from it.",
                    "Describe your three best projects, one at a time.",
                    "Ask Copilot to add a simple contact form.",
                ],
                "result": "An online portfolio ready to share on your CV.",
                "further": "Publish it with a custom domain name through GitHub Pages.",
            },
            {
                "title": "Prototype an internal tool in one hour",
                "persona": "it", "features": ["agent", "chat"],
                "situation": "A department asks for a small internal tool and you want a working prototype fast, before committing engineering time.",
                "steps": [
                    "Describe the tool's core need to agent mode: \u201cBuild a page where staff can submit a request and see its status.\u201d",
                    "Review the proposed plan and let the agent build a first version.",
                    "Ask for one realistic refinement, like form validation or a status colour code.",
                ],
                "result": "A working prototype in under an hour, to validate the need before a full build.",
                "further": "If it proves useful, plan a proper version with a real database and access control.",
            },
            {
                "title": "Document an existing script automatically",
                "persona": "it", "features": ["chat"],
                "situation": "You've inherited an undocumented internal script and need to understand and document it fast.",
                "steps": [
                    "Open the script and ask Copilot Chat: \u201cExplain what this script does, step by step.\u201d",
                    "Ask: \u201cGenerate a README describing its purpose, inputs, and how to run it.\u201d",
                    "Ask Copilot to flag any risky or unclear parts of the code.",
                ],
                "result": "Clear documentation for a script that previously only one person understood.",
                "further": "Add the generated README directly to the script's repository.",
            },
            {
                "title": "Automate a deployment with GitHub Actions",
                "persona": "it", "features": ["chat", "agent"],
                "situation": "You want a small site or tool to redeploy automatically whenever it changes.",
                "steps": [
                    "Ask Copilot Chat: \u201cGenerate a GitHub Actions workflow that deploys this site to GitHub Pages on every push to main.\u201d",
                    "Add the suggested file to your repository and push a small change to test it.",
                    "Ask Copilot to add a notification step if the deployment fails.",
                ],
                "result": "A site that updates itself automatically, with no manual redeploy step.",
                "further": "Reuse the same workflow file as a template for other internal projects.",
            },
            {
                "title": "Build an interactive onboarding checklist",
                "persona": "hr", "features": ["chat"],
                "situation": "New staff receive a long, static onboarding document that's easy to lose track of.",
                "steps": [
                    "Describe the onboarding steps to Copilot Chat and ask for an interactive checklist page.",
                    "Ask for progress to be saved so people can leave and come back.",
                    "Ask Copilot to add a printable summary for HR records.",
                ],
                "result": "A friendly, trackable onboarding experience for new colleagues.",
                "further": "Personalize the checklist by role using a simple dropdown at the start.",
            },
            {
                "title": "Create a training feedback form in minutes",
                "persona": "hr", "features": ["chat"],
                "situation": "You need a quick way to collect feedback after a training session, without waiting on a survey tool licence.",
                "steps": [
                    "Ask Copilot Chat to build a page with a 1-5 rating and a comments box.",
                    "Ask it to store submissions so you can review them afterwards.",
                    "Ask for a simple summary view showing the average rating.",
                ],
                "result": "A working feedback form, live before the session even ends.",
                "further": "Reuse the same page as a template for every future training session.",
            },
            {
                "title": "Build a leave-balance calculator",
                "persona": "hr", "features": ["chat"],
                "situation": "Staff keep asking HR how many vacation days they have left.",
                "steps": [
                    "Describe your institution's leave policy to Copilot Chat.",
                    "Ask it to build a small calculator that takes a start date and shows remaining days.",
                    "Ask for a clear explanation shown alongside the result, in case of edge cases.",
                ],
                "result": "A self-service tool that reduces repetitive questions to HR.",
                "further": "Link it from the onboarding checklist above.",
            },
            {
                "title": "Run a live poll during a meeting",
                "persona": "leadership", "features": ["chat", "agent"],
                "situation": "You want real-time feedback from staff during a town hall, without a paid polling tool.",
                "steps": [
                    "Describe the question and options to Copilot Chat, following the same pattern as the Quick Poll example in the guided track.",
                    "Test it yourself, then project the link during the meeting.",
                    "Ask Copilot to add a live-updating results view.",
                ],
                "result": "Instant, visible feedback from the room, without any external service.",
                "further": "Reuse the exact same page for every future meeting, just changing the question.",
            },
            {
                "title": "Build a simple KPI dashboard",
                "persona": "leadership", "features": ["chat"],
                "situation": "You want to track three or four numbers over time without a full BI tool.",
                "steps": [
                    "Describe your KPIs to Copilot Chat and paste a few sample numbers.",
                    "Ask it to build a clean, one-page dashboard summarizing them.",
                    "Ask for a simple way to update the numbers each month.",
                ],
                "result": "A lightweight dashboard you fully control and understand.",
                "further": "Ask Copilot to add a small trend chart once you have a few months of data.",
            },
            {
                "title": "Turn a strategy summary into a visual one-pager",
                "persona": "leadership", "features": ["chat", "spaces"],
                "situation": "You have a dense bullet-point strategy document and want something easier to present.",
                "steps": [
                    "Paste your bullet points into Copilot Chat and ask for a clean, visual one-page layout.",
                    "Paste a screenshot of a visual style you like to guide the design.",
                    "Ask for a printable version as well as a web version.",
                ],
                "result": "A clear, shareable one-pager built from existing content.",
                "further": "Reuse the same layout for the next strategic update.",
            },
            {
                "title": "Build a travel expense calculator",
                "persona": "finance", "features": ["chat"],
                "situation": "Staff often ask how much they'll be reimbursed for travel before submitting a claim.",
                "steps": [
                    "Describe your reimbursement rules to Copilot Chat (distance, rate, caps).",
                    "Ask it to build a small calculator based on those rules.",
                    "Ask for a clear breakdown of the calculation shown to the user.",
                ],
                "result": "A self-service estimator that reduces back-and-forth emails.",
                "further": "Link it from the finance team's internal page.",
            },
            {
                "title": "Track a small recurring budget",
                "persona": "finance", "features": ["chat"],
                "situation": "You manage a small, recurring budget line and want a lighter alternative to a full spreadsheet.",
                "steps": [
                    "Describe the budget categories to Copilot Chat.",
                    "Ask for a simple page to log expenses with a running total.",
                    "Ask for a monthly summary view.",
                ],
                "result": "A lightweight tracker tailored to your exact categories.",
                "further": "Export the data to a spreadsheet for the official records.",
            },
            {
                "title": "Turn pasted data into a sortable table",
                "persona": "finance", "features": ["chat"],
                "situation": "You regularly receive data as plain text or copy-pasted rows that are hard to work with.",
                "steps": [
                    "Paste the raw data into Copilot Chat.",
                    "Ask it to generate a clean, sortable HTML table from it.",
                    "Ask for a search box to filter rows.",
                ],
                "result": "A readable, searchable view of data that used to be a wall of text.",
                "further": "Ask Copilot to add a CSV export button.",
            },
            {
                "title": "Clean a messy dataset with Copilot's help",
                "persona": "research", "features": ["chat", "agent"],
                "situation": "You have a dataset full of inconsistencies (typos, missing values, mixed formats) before you can analyze it.",
                "steps": [
                    "Describe the dataset's problems to Copilot Chat and paste a sample.",
                    "Ask for a script that cleans and standardizes it.",
                    "Review each cleaning rule before running it on the full dataset.",
                ],
                "result": "A clean, analysis-ready dataset, with a documented script showing exactly what changed.",
                "further": "Ask Copilot to add a summary report of what was cleaned and why.",
            },
            {
                "title": "Generate a first-pass statistical analysis script",
                "persona": "research", "features": ["chat"],
                "situation": "You want a starting point for a standard analysis without writing boilerplate code from scratch.",
                "steps": [
                    "Describe your data and research question to Copilot Chat.",
                    "Ask for a script that runs the relevant statistical test and prints a clear summary.",
                    "Ask Copilot to explain each step of the script in comments.",
                ],
                "result": "A working analysis script you understand line by line, not a black box.",
                "further": "Ask Copilot to add a simple chart of the results.",
            },
            {
                "title": "Build a results page for your research",
                "persona": "research", "features": ["chat", "spaces"],
                "situation": "You want a clear, public page presenting your findings beyond the academic paper.",
                "steps": [
                    "Describe your key findings to Copilot Chat, one at a time.",
                    "Paste a chart or figure and ask Copilot to build a page section around it.",
                    "Ask for a plain-language summary alongside the technical one.",
                ],
                "result": "An accessible results page you can link from your CV or a conference talk.",
                "further": "Add a contact section for collaboration requests.",
            },
            {
                "title": "Build an interactive resource catalogue",
                "persona": "campus", "features": ["chat"],
                "situation": "You want an easy way for students to browse recommended resources by topic.",
                "steps": [
                    "Describe your resource list and categories to Copilot Chat.",
                    "Ask for a searchable, filterable catalogue page.",
                    "Ask for a simple way to add new resources over time.",
                ],
                "result": "A living catalogue that's easier to browse than a static PDF list.",
                "further": "Ask Copilot to add tags so resources can belong to several categories.",
            },
            {
                "title": "Generate an automatic FAQ page",
                "persona": "campus", "features": ["chat"],
                "situation": "You keep answering the same questions by email and want a public FAQ instead.",
                "steps": [
                    "Paste your most common questions and answers into Copilot Chat.",
                    "Ask for a clean FAQ page with a search box.",
                    "Ask Copilot to group questions into clear categories.",
                ],
                "result": "A self-service FAQ that reduces repetitive emails.",
                "further": "Add a \u201cstill need help\u201d contact link at the bottom.",
            },
            {
                "title": "Build a campus events page",
                "persona": "campus", "features": ["chat", "spaces"],
                "situation": "You want a simple, attractive page listing upcoming campus events.",
                "steps": [
                    "Describe the events and dates to Copilot Chat.",
                    "Paste a screenshot of an events-page style you like for inspiration.",
                    "Ask for events to automatically sort by date, with past ones fading out.",
                ],
                "result": "A lightweight events page that's easy to update each month.",
                "further": "Ask Copilot to add a simple \u201cadd to calendar\u201d button for each event.",
            },
        ],
    },
}

# ------------------------------------------------------------------
# CONTENT — French
# ------------------------------------------------------------------
CONTENT["fr"] = {
    "meta": {
        "html_lang": "fr",
        "site_name": "Vibe Coding Copilot",
        "brand_tagline": "Enseignement Sup\u00e9rieur",
        "title_suffix": "Vibe Coding avec GitHub Copilot pour l'enseignement sup\u00e9rieur",
        "description": "Une formation gratuite pour apprendre le vibe coding avec GitHub Copilot : "
                       "construis, teste et publie tes propres outils num\u00e9riques pour "
                       "l'enseignement sup\u00e9rieur, sans \u00eatre d\u00e9veloppeur.",
    },
    "nav": {
        "home": "Accueil",
        "explorer": "Cas d'usage",
        "basics": "Vibe Coding D\u00e9butant",
        "advanced": "Vibe Coding Avanc\u00e9",
        "expert": "Vibe Coding Expert",
        "best_practices": "Bonnes pratiques",
        "toolkit": "Bo\u00eete \u00e0 outils",
        "about": "\u00c0 propos",
        "all_lessons": "Toutes les le\u00e7ons",
        "view_route": "Voir le parcours complet",
        "exercise_label": "\u00c0 toi de jouer",
    },
    "footer": {
        "text": "Une ressource p\u00e9dagogique ind\u00e9pendante et gratuite pour le vibe coding "
                "dans l'enseignement sup\u00e9rieur, propuls\u00e9e par GitHub Copilot. Non "
                "affili\u00e9e \u00e0 GitHub ni \u00e0 Microsoft et non approuv\u00e9e par eux.",
    },
    "home": {
        "eyebrow": "Formation gratuite \u00b7 Vibe Coding avec GitHub Copilot",
        "h1_line1": "Vibe Coding",
        "h1_line2": "pour l'enseignement sup\u00e9rieur",
        "lede": "Tu n'as pas besoin d'\u00eatre d\u00e9veloppeur ou d\u00e9veloppeuse pour "
                "cr\u00e9er tes propres outils num\u00e9riques. Que tu enseignes, \u00e9tudies, "
                "travailles \u00e0 l'IT, aux RH, en direction ou aux finances, cette formation "
                "gratuite t'apprend, \u00e9tape par \u00e9tape, \u00e0 construire une vraie web "
                "app avec GitHub Copilot. Tu restes l'expert ou l'experte de ton propre "
                "m\u00e9tier : l'IA t'aide \u00e0 construire, et GitHub garde, versionne et "
                "publie le r\u00e9sultat.",
        "cta_primary": "Explorer les cas d'usage",
        "cta_secondary": "Suivre le parcours guid\u00e9",
        "hero_note": "Gratuit. Aucune exp\u00e9rience de programmation requise. Juste GitHub "
                     "Copilot, un peu de curiosit\u00e9 et 25 le\u00e7ons concr\u00e8tes.",
        "personas_title": "Pens\u00e9 pour tous les p\u00f4les de l'institution",
        "personas_sub": "Le vibe coding n'est ni r\u00e9serv\u00e9 aux d\u00e9veloppeurs, ni "
                        "seulement aux enseignants. Voici ce que \u00e7a donne dans chaque service.",
        "personas": [
            ("\U0001f393", "Enseignants", "Construis le petit outil que tu imagines depuis des "
             "ann\u00e9es : un quiz, un syllabus vivant, un assistant de correction.",
             "Exemple :", "Un enseignant de biologie construit un quiz de r\u00e9vision "
             "auto-corrig\u00e9 en une apr\u00e8s-midi."),
            ("\U0001f9d1\u200d\U0001f393", "\u00c9tudiants", "Pas besoin d'un dipl\u00f4me "
             "d'informatique pour vibe coder tes propres outils d'\u00e9tude, ton portfolio ou "
             "le site de ton asso.", "Exemple :", "Un groupe d'\u00e9tudiants construit une "
             "appli de flashcards partag\u00e9e pour r\u00e9viser ensemble avant les examens."),
            ("\U0001f5a5\ufe0f", "Services IT", "Prototype des outils internes en quelques "
             "heures au lieu de plusieurs mois, puis gouverne-les proprement avec GitHub "
             "Enterprise.", "Exemple :", "L'IT construit un outil de r\u00e9servation de salle "
             "en libre-service et g\u00e8re les acc\u00e8s de mani\u00e8re centralis\u00e9e."),
            ("\U0001f91d", "RH", "Transforme un processus d'onboarding ou de formation "
             "r\u00e9p\u00e9titif en une petite application simple et conviviale.", "Exemple :",
             "Les RH construisent une check-list d'int\u00e9gration interactive pour les "
             "nouveaux collaborateurs."),
            ("\U0001f9ed", "Direction", "Obtiens un vrai outil de feedback ou un tableau de "
             "bord construit en quelques jours, sans attendre un projet IT complet.",
             "Exemple :", "Un responsable de d\u00e9partement construit un sondage en direct "
             "pour recueillir des avis pendant une r\u00e9union."),
            ("\U0001f4b6", "Finances", "Automatise une petite t\u00e2che r\u00e9p\u00e9titive : "
             "un calculateur de budget, un formulaire de notes de frais, un suivi simple.",
             "Exemple :", "L'\u00e9quipe finance construit un petit calculateur de "
             "remboursement de frais de d\u00e9placement."),
        ],
        "journey_title": "De l'id\u00e9e de cours \u00e0 l'application publi\u00e9e",
        "journey_sub": "Chaque parcours de cette formation suit le m\u00eame chemin, tr\u00e8s concret.",
        "journey": [
            ("01", "Id\u00e9e", "Pars d'un vrai probl\u00e8me p\u00e9dagogique et transforme-le en id\u00e9e d'application."),
            ("02", "Construire", "Construis une premi\u00e8re version avec GitHub Copilot, sans \u00e9crire tout le code par toi-m\u00eame."),
            ("03", "Publier", "Sauvegarde ton projet sur GitHub et publie-le en ligne pour tes \u00e9tudiants."),
            ("04", "Am\u00e9liorer", "Teste, affine et fais \u00e9voluer ton outil au fil des retours."),
        ],
        "courses_title": "Trois parcours, un seul objectif : vibe coder pour de vrai",
        "courses_sub": "Commence o\u00f9 tu veux : de ta premi\u00e8re application avec Copilot "
                       "jusqu'\u00e0 un vrai outil p\u00e9dagogique complet, h\u00e9berg\u00e9 sur GitHub.",
        "examples_title": "Ce que tu peux vibe coder, quel que soit ton m\u00e9tier",
        "examples_sub": "Des id\u00e9es concr\u00e8tes, r\u00e9alisables en quelques heures avec GitHub Copilot.",
        "examples": [
            ("Quiz de r\u00e9vision interactif", "Un quiz auto-corrig\u00e9 pour r\u00e9viser un "
             "chapitre, que tes \u00e9tudiants utilisent avant l'examen.", "Enseignants"),
            ("Page de cours vivante", "Un syllabus interactif avec FAQ automatique, planning et "
             "ressources centralis\u00e9es.", "Enseignants"),
            ("Appli de flashcards partag\u00e9e", "Des cartes qui se retournent au clic, "
             "construites ensemble par un groupe d'\u00e9tudiants avant les examens.", "\u00c9tudiants"),
            ("Calculateur de note personnalis\u00e9", "Un outil qui estime la note finale selon "
             "le bar\u00e8me propre \u00e0 chaque cours.", "\u00c9tudiants"),
            ("R\u00e9servation de salle en libre-service", "Un outil interne pour r\u00e9server "
             "une salle ou un cr\u00e9neau de labo, avec disponibilit\u00e9 en direct.", "Services IT"),
            ("Check-list d'int\u00e9gration interactive", "Un parcours pas \u00e0 pas qui guide "
             "un nouveau collaborateur pendant ses deux premi\u00e8res semaines.", "RH"),
            ("Sondage en direct pour une r\u00e9union", "Un sondage \u00e9clair qui recueille "
             "l'avis de l'\u00e9quipe en temps r\u00e9el \u2014 essaie la d\u00e9mo en direct de "
             "la le\u00e7on 3 !", "Direction"),
            ("Petit calculateur de frais", "Un outil l\u00e9ger pour estimer et suivre des "
             "d\u00e9penses r\u00e9currentes ou des frais de d\u00e9placement.", "Finances"),
            ("Vitrine de projets \u00e9tudiants", "Une galerie web o\u00f9 chaque \u00e9tudiant "
             "pr\u00e9sente son projet de fin de semestre.", "Enseignants & \u00e9tudiants"),
        ],
        "teaser_title": "Tu ne sais pas par o\u00f9 commencer ? Regarde d'abord les bonnes pratiques.",
        "teaser_desc": "Une check-list en une page pour bien d\u00e9marrer ton premier projet de "
                       "vibe coding, de l'id\u00e9e \u00e0 la publication sur GitHub.",
        "teaser_cta": "Voir les bonnes pratiques",
    },
    "tracks": {
        "basics": {
            "slug": "vibe-basics",
            "tag_class": "tag-basics",
            "level_label": "D\u00e9butant",
            "title": "Vibe Coding D\u00e9butant",
            "subtitle": "Tes premiers pas en vibe coding : transforme une id\u00e9e de cours en "
                       "vraie application, avec GitHub Copilot.",
            "card_desc": "D\u00e9couvre le vibe coding, construis ta premi\u00e8re web app "
                         "p\u00e9dagogique avec Copilot et publie-la en ligne.",
            "meta": "8 le\u00e7ons \u00b7 environ 1h30",
            "lessons": [
                {
                    "title": "Qu'est-ce que le vibe coding ?",
                    "kicker": "Le\u00e7on 1",
                    "paragraphs": [
                        "Le vibe coding, c'est cr\u00e9er une application en d\u00e9crivant ce que "
                        "tu veux \u00e0 une IA plut\u00f4t qu'en \u00e9crivant chaque ligne de "
                        "code toi-m\u00eame. Avec GitHub Copilot, tu expliques ton besoin en "
                        "langage naturel et l'IA propose le code ; toi, tu restes aux "
                        "commandes : tu lis, tu ajustes, tu valides.",
                        "Pour l'enseignement sup\u00e9rieur, cela change tout : tu peux enfin "
                        "construire le petit outil que tu imagines depuis des ann\u00e9es, sans "
                        "attendre un service informatique ou apprendre \u00e0 programmer "
                        "pendant six mois. Ce parcours t'accompagne pas \u00e0 pas, avec un vrai "
                        "projet de cours comme fil rouge.",
                    ],
                    "tip": "Tu n'as pas besoin d'installer quoi que ce soit pour lire ce "
                           "parcours. L'installation de Copilot arrive \u00e0 la le\u00e7on suivante.",
                    "exercise": "Quel que soit ton m\u00e9tier (enseignement, \u00e9tudes, IT, "
                                "RH, direction, finances), \u00e9cris en une phrase la petite "
                                "appli que tu r\u00eaves d'avoir. Tu en construiras une vraie "
                                "d\u00e8s la le\u00e7on 3.",
                },
                {
                    "title": "D'un probl\u00e8me p\u00e9dagogique \u00e0 une id\u00e9e d'application",
                    "kicker": "Le\u00e7on 2",
                    "paragraphs": [
                        "Le meilleur point de d\u00e9part n'est pas une technologie, mais un "
                        "probl\u00e8me r\u00e9el : des \u00e9tudiants qui n'ont pas de moyen "
                        "simple de r\u00e9viser, un planning de cours dispers\u00e9 entre dix "
                        "e-mails, une correction de copies r\u00e9p\u00e9titive. Pars toujours de ce v\u00e9cu concret.",
                        "D\u00e9cris ce probl\u00e8me en une phrase, puis imagine la plus petite "
                        "application possible qui le r\u00e9soudrait. Un quiz, une page, un "
                        "calculateur : garde \u00e7a simple pour commencer, tu pourras toujours l'enrichir plus tard.",
                    ],
                    "tip": "\u00c9cris ton id\u00e9e sous la forme : \u00ab Une application qui "
                           "permet \u00e0 [qui] de [faire quoi] pour [quel b\u00e9n\u00e9fice] \u00bb.",
                    "exercise": "Choisis UN vrai probl\u00e8me dont tu ou une ou un coll\u00e8gue "
                                "se plaint chaque semaine, en classe, au support IT, en "
                                "onboarding ou en r\u00e9union budget, et \u00e9cris ton id\u00e9e "
                                "avec la formule ci-dessus.",
                },
                {
                    "title": "Ta premi\u00e8re web app avec GitHub Copilot",
                    "kicker": "Le\u00e7on 3",
                    "paragraphs": [
                        "C'est la le\u00e7on o\u00f9 tu construis vraiment quelque chose. "
                        "Installe l'extension GitHub Copilot dans Visual Studio Code (ou ouvre "
                        "Copilot Chat directement sur github.com), connecte-toi avec ton compte "
                        "GitHub, puis cr\u00e9e un nouveau fichier index.html.",
                        "Ci-dessous, on construit ensemble un exemple r\u00e9el et fonctionnel : "
                        "un \u00ab Sondage \u00c9clair \u00bb que tu pourrais utiliser en cours, "
                        "en formation, en r\u00e9union d'\u00e9quipe ou pendant une assembl\u00e9e "
                        "g\u00e9n\u00e9rale. Suis les trois \u00e9tapes avec ton propre Copilot, "
                        "puis teste le r\u00e9sultat fini en direct \u00e0 la fin.",
                    ],
                    "extra_html": '''
<div class="step-badge">\u00c9tape 1 \u2014 D\u00e9crire le squelette</div>
<p>Ouvre Copilot Chat et d\u00e9cris la plus petite version possible de ton id\u00e9e. Sois pr\u00e9cis sur ce qui doit apparaitre sur la page.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Cr\u00e9e une page web simple appel\u00e9e "Sondage \u00c9clair" avec une question et quatre boutons comme options de r\u00e9ponse.</div>
    <div class="chat-bubble-ai">Voici un point de d\u00e9part :
      <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Sondage Eclair&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
  &lt;h2&gt;Qu'est-ce qui t'aiderait le plus ce trimestre ?&lt;/h2&gt;
  &lt;button&gt;Des exemples corriges&lt;/button&gt;
  &lt;button&gt;Plus d'exercices&lt;/button&gt;
  &lt;button&gt;Des videos courtes&lt;/button&gt;
  &lt;button&gt;Des seances de questions&lt;/button&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
    </div>
  </div>
</div>
<p>Enregistre ce fichier, ouvre-le dans ton navigateur en double-cliquant dessus. Tu as d\u00e9j\u00e0 une vraie page web, m\u00eame toute simple.</p>

<div class="step-badge">\u00c9tape 2 \u2014 Demander la logique</div>
<p>Une page avec des boutons qui ne font rien n'est pas tr\u00e8s utile. Demande \u00e0 Copilot de faire compter les votes par les boutons.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Quand quelqu'un clique sur un bouton, enregistre un compteur de votes pour cette option dans le navigateur (localStorage), pour qu'il soit retenu si la page se recharge.</div>
    <div class="chat-bubble-ai">J'ai ajout\u00e9 ce script en bas de ta page :
      <pre><code>&lt;script&gt;
  document.querySelectorAll("button").forEach((btn, i) =&gt; {
    btn.addEventListener("click", () =&gt; {
      let votes = JSON.parse(localStorage.getItem("votes")) || [0,0,0,0];
      votes[i]++;
      localStorage.setItem("votes", JSON.stringify(votes));
      alert("Merci pour ton vote !");
    });
  });
&lt;/script&gt;</code></pre>
    </div>
  </div>
</div>
<p>Teste : clique sur un bouton, recharge la page, clique encore \u2014 le compteur continue d'augmenter m\u00eame si tu ne le vois pas encore. C'est la suite.</p>

<div class="step-badge">\u00c9tape 3 \u2014 Afficher les r\u00e9sultats</div>
<p>Demande maintenant \u00e0 Copilot de remplacer ce simple <code>alert()</code> par quelque chose de visible pour tout le monde.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Au lieu d'une alerte, cache les boutons apres le vote et affiche chaque option sous forme de barre de pourcentage basee sur les votes actuels.</div>
    <div class="chat-bubble-ai">Bonne id\u00e9e, c'est bien plus clair pour les votants. J'ai remplac\u00e9 l'alerte par un petit affichage de r\u00e9sultats qui calcule la part de chaque option sur le total des votes et anime une barre pour la repr\u00e9senter. Je peux aussi ajouter un lien "revoter" pour r\u00e9initialiser cette d\u00e9mo, tu veux ?</div>
  </div>
</div>
<p>Continue ainsi \u2014 une petite demande \u00e0 la fois \u2014 jusqu'\u00e0 ce que la page te plaise vraiment.</p>

<div class="step-badge">\u00c9tape 4 \u2014 Teste ce que tu viens de construire</div>
<p>Voici exactement l'application d\u00e9crite ci-dessus, d\u00e9j\u00e0 construite et fonctionnelle. Clique sur une option et regarde les r\u00e9sultats appara\u00eetre : c'est ce que verront tes \u00e9tudiants, coll\u00e8gues ou \u00e9quipe une fois ta version publi\u00e9e (prochaine le\u00e7on).</p>
<div class="demo-frame-wrap">
  <div class="demo-frame-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">sondage-eclair.html</span></div>
  <iframe src="../assets/demo/quick-poll-fr.html" loading="lazy" title="Demo Sondage Eclair"></iframe>
</div>
''',
                    "tip": "Commence toujours par une version minuscule qui fonctionne : "
                           "l'\u00e9tape 1 ci-dessus est d\u00e9j\u00e0 une page complete et "
                           "fonctionnelle \u00e0 elle seule.",
                    "exercise": "Reconstruis toi-m\u00eame exactement ce Sondage \u00c9clair dans "
                                "un nouveau fichier index.html, puis change la question et les "
                                "quatre options pour coller \u00e0 ton propre contexte : un sujet "
                                "de cours, une question d'onboarding, une priorit\u00e9 budget, "
                                "n'importe quoi de r\u00e9el pour toi.",
                },
                {
                    "title": "Sauvegarder et publier avec GitHub",
                    "kicker": "Le\u00e7on 4",
                    "paragraphs": [
                        "Une fois ta premi\u00e8re version fonctionnelle, cr\u00e9e un d\u00e9p\u00f4t "
                        "(repository) sur GitHub et envoie-y ton code : c'est ce qu'on appelle un "
                        "commit. \u00c0 partir de l\u00e0, ton travail est sauvegard\u00e9 en "
                        "ligne, versionn\u00e9, et tu peux toujours revenir \u00e0 une version "
                        "pr\u00e9c\u00e9dente si quelque chose casse.",
                        "Active ensuite GitHub Pages sur ce d\u00e9p\u00f4t : en quelques clics, "
                        "ton application devient accessible via un simple lien, que tu peux "
                        "partager avec tes \u00e9tudiants ou tes coll\u00e8gues, sans aucun serveur \u00e0 g\u00e9rer.",
                    ],
                    "tip": "Un d\u00e9p\u00f4t GitHub, c'est aussi ta sauvegarde : m\u00eame si "
                           "ton ordinateur tombe en panne, ton projet est en s\u00e9curit\u00e9.",
                    "exercise": "Cr\u00e9e un compte GitHub gratuit si tu n'en as pas, pousse "
                                "ton Sondage \u00c9clair dans un tout nouveau d\u00e9p\u00f4t, et "
                                "active GitHub Pages dessus.",
                },
                {
                    "title": "Tester et am\u00e9liorer avec Copilot Chat",
                    "kicker": "Le\u00e7on 5",
                    "paragraphs": [
                        "Fais tester ton application par un ou deux coll\u00e8gues, ou par "
                        "toi-m\u00eame en te mettant \u00e0 la place d'un \u00e9tudiant. Note "
                        "chaque bug ou maladresse, puis d\u00e9cris-les un par un \u00e0 Copilot "
                        "Chat : \u00ab quand je clique sur ce bouton, rien ne se passe, corrige \u00e7a \u00bb.",
                        "Copilot peut aussi t'expliquer le code existant si tu ne le comprends "
                        "pas encore compl\u00e8tement : demande-lui \u00ab explique-moi cette "
                        "partie \u00bb avant de demander une modification.",
                    ],
                    "tip": "Une seule correction \u00e0 la fois : c'est plus facile de "
                           "v\u00e9rifier que \u00e7a fonctionne, et plus facile de revenir en "
                           "arri\u00e8re si besoin.",
                    "exercise": "Envoie ton lien publi\u00e9 \u00e0 deux coll\u00e8gues (ou "
                                "camarades) et demande-leur de cliquer partout. Note chaque "
                                "maladresse qu'ils rencontrent, puis corrige la premi\u00e8re "
                                "avec Copilot Chat.",
                },
                {
                    "title": "Am\u00e9liorer le style et l'apparence",
                    "kicker": "Le\u00e7on 6",
                    "paragraphs": [
                        "Une fois que ton application fonctionne, demande \u00e0 Copilot de "
                        "l'habiller : couleurs de ton \u00e9tablissement, police plus lisible, "
                        "mise en page plus claire pour tes \u00e9tudiants. Tu peux m\u00eame "
                        "coller une capture d'\u00e9cran d'un style que tu aimes et demander de s'en inspirer.",
                        "Pense accessibilit\u00e9 : contraste suffisant, texte lisible, boutons "
                        "assez grands. Demande simplement \u00e0 Copilot de v\u00e9rifier "
                        "l'accessibilit\u00e9 de ta page, il saura quoi corriger.",
                    ],
                    "tip": None,
                    "exercise": "Demande \u00e0 Copilot de restyliser ton Sondage \u00c9clair "
                                "avec deux couleurs de ton institution ou de ton \u00e9quipe, "
                                "puis v\u00e9rifie le rendu sur ton t\u00e9l\u00e9phone aussi.",
                },
                {
                    "title": "Ajouter images, fichiers et documents",
                    "kicker": "Le\u00e7on 7",
                    "paragraphs": [
                        "Beaucoup d'outils de cours ont besoin d'images, de PDF ou de documents "
                        "\u00e0 t\u00e9l\u00e9charger : un support de cours, un sch\u00e9ma, un "
                        "formulaire. Demande \u00e0 Copilot d'ajouter une zone d'affichage "
                        "d'image ou un bouton de t\u00e9l\u00e9chargement, puis d\u00e9pose "
                        "simplement le fichier dans ton d\u00e9p\u00f4t GitHub.",
                        "GitHub h\u00e9berge aussi bien ton code que ces fichiers : pas besoin "
                        "d'un autre outil pour stocker les ressources de ton application.",
                    ],
                    "tip": None,
                    "exercise": "Ajoute une image ou un PDF t\u00e9l\u00e9chargeable (m\u00eame "
                                "un exemple factice) \u00e0 ton Sondage \u00c9clair, commit-le, "
                                "et v\u00e9rifie qu'il s'affiche bien une fois publi\u00e9.",
                },
                {
                    "title": "Synth\u00e8se et vers le parcours Avanc\u00e9",
                    "kicker": "Le\u00e7on 8",
                    "paragraphs": [
                        "Tu sais maintenant transformer une id\u00e9e de cours en application "
                        "r\u00e9elle : construire avec Copilot, sauvegarder et publier avec "
                        "GitHub, tester, am\u00e9liorer le style, ajouter des fichiers. Le "
                        "r\u00e9flexe le plus important : avance toujours par petites \u00e9tapes que tu peux v\u00e9rifier.",
                        "Le parcours Avanc\u00e9 prend le relais pour aller plus loin : "
                        "connecter une vraie base de donn\u00e9es, donner une m\u00e9moire "
                        "durable \u00e0 ton projet, et g\u00e9rer ton code avec GitHub comme un "
                        "vrai projet qui dure dans le temps.",
                    ],
                    "tip": None,
                    "exercise": "\u00c9cris un README de trois lignes pour ton projet : ce qu'il "
                                "fait, pour qui, et comment le rouvrir avec Copilot la prochaine fois.",
                },
            ],
        },
        "advanced": {
            "slug": "vibe-advanced",
            "tag_class": "tag-advanced",
            "level_label": "Avanc\u00e9",
            "title": "Vibe Coding Avanc\u00e9",
            "subtitle": "Connecte une base de donn\u00e9es, donne de la m\u00e9moire \u00e0 ton "
                       "projet et g\u00e8re ton code comme un projet qui dure, avec GitHub.",
            "card_desc": "Base de donn\u00e9es, conception p\u00e9dagogique, m\u00e9moire de "
                         "projet et gestion du code avec GitHub : de quoi construire un vrai outil qui dure.",
            "meta": "9 le\u00e7ons \u00b7 environ 2h",
            "lessons": [
                {
                    "title": "Travailler avec l'agent de Copilot",
                    "kicker": "Le\u00e7on 1",
                    "paragraphs": [
                        "Au-del\u00e0 des suggestions ligne par ligne, Copilot propose un mode "
                        "agent : tu d\u00e9cris une t\u00e2che plus large (\u00ab ajoute un "
                        "formulaire d'inscription \u00e0 mon quiz et v\u00e9rifie qu'il "
                        "fonctionne \u00bb), et Copilot planifie plusieurs modifications, les "
                        "applique et v\u00e9rifie le r\u00e9sultat, avec des points d'\u00e9tape "
                        "que tu valides.",
                        "C'est l'outil id\u00e9al quand ton application grandit et que tu ne "
                        "veux plus d\u00e9crire chaque petite ligne une par une.",
                    ],
                    "tip": "Relis toujours le plan propos\u00e9 avant de laisser l'agent "
                           "travailler : c'est le meilleur moment pour corriger le tir.",
                    "exercise": "D\u00e9cris une t\u00e2che en plusieurs \u00e9tapes au mode "
                                "agent de Copilot (par exemple, ajouter une page de r\u00e9sultats "
                                "\u00e0 ton Sondage \u00c9clair) et relis attentivement son plan "
                                "avant de le laisser l'ex\u00e9cuter.",
                },
                {
                    "title": "Connecter une base de donn\u00e9es \u00e0 ton application",
                    "kicker": "Le\u00e7on 2",
                    "paragraphs": [
                        "D\u00e8s que ton outil doit retenir des informations d'une session "
                        "\u00e0 l'autre (des r\u00e9ponses de quiz, des inscriptions, des "
                        "notes), tu as besoin d'une base de donn\u00e9es. Des services comme "
                        "Supabase permettent d'en cr\u00e9er une gratuitement, sans "
                        "configuration serveur, et Copilot t'aide \u00e0 \u00e9crire le code de connexion.",
                        "D\u00e9cris \u00e0 Copilot ce que tu veux stocker (par exemple : le nom "
                        "de l'\u00e9tudiant et son score), et laisse-le proposer la structure de "
                        "la base et le code n\u00e9cessaire pour lire et \u00e9crire dedans.",
                    ],
                    "tip": None,
                    "exercise": "Cr\u00e9e un projet Supabase gratuit et connecte-le \u00e0 une "
                                "petite page de test qui stocke une seule information, comme un "
                                "nom et un vote.",
                },
                {
                    "title": "Utiliser cette base de donn\u00e9es en toute s\u00e9curit\u00e9",
                    "kicker": "Le\u00e7on 3",
                    "paragraphs": [
                        "Une base de donn\u00e9es mal prot\u00e9g\u00e9e peut exposer les "
                        "donn\u00e9es de tes \u00e9tudiants. Demande syst\u00e9matiquement "
                        "\u00e0 Copilot d'ajouter des r\u00e8gles de s\u00e9curit\u00e9 (qui a "
                        "le droit de lire ou d'\u00e9crire quoi), et ne stocke jamais plus "
                        "d'informations personnelles que n\u00e9cessaire.",
                        "Pense d\u00e8s maintenant \u00e0 la protection des donn\u00e9es de tes "
                        "\u00e9tudiants (RGPD en Europe) : anonymise ce qui peut l'\u00eatre, et "
                        "explique clairement \u00e0 quoi servent les donn\u00e9es que tu collectes.",
                    ],
                    "tip": "En cas de doute, demande \u00e0 Copilot : \u00ab ce code "
                           "respecte-t-il de bonnes pratiques de protection des donn\u00e9es ? \u00bb",
                    "exercise": "Demande \u00e0 Copilot de relire ton code de base de "
                                "donn\u00e9es pour d\u00e9tecter des probl\u00e8mes de "
                                "s\u00e9curit\u00e9, et corrige au moins un point signal\u00e9.",
                },
                {
                    "title": "Concevoir consciemment pour l'apprentissage",
                    "kicker": "Le\u00e7on 4",
                    "paragraphs": [
                        "Un bon outil p\u00e9dagogique n'est pas seulement fonctionnel, il est "
                        "pens\u00e9 pour l'apprentissage : retour imm\u00e9diat apr\u00e8s une "
                        "r\u00e9ponse, progression visible, encouragements plut\u00f4t que "
                        "sanctions. D\u00e9cris ces intentions p\u00e9dagogiques \u00e0 "
                        "Copilot, pas seulement des fonctionnalit\u00e9s techniques.",
                        "Par exemple, plut\u00f4t que \u00ab affiche le score \u00bb, demande "
                        "\u00ab affiche le score avec une explication de chaque erreur, pour que "
                        "l'\u00e9tudiant comprenne pourquoi il s'est tromp\u00e9 \u00bb.",
                    ],
                    "tip": None,
                    "exercise": "Reformule une demande de fonctionnalit\u00e9 pour ton projet "
                                "comme un prompt centr\u00e9 sur l'apprentissage ou "
                                "l'utilisateur, en suivant l'exemple de cette le\u00e7on, plutot "
                                "qu'une demande purement technique.",
                },
                {
                    "title": "Faire un bon plan de construction",
                    "kicker": "Le\u00e7on 5",
                    "paragraphs": [
                        "Avant de demander une grosse fonctionnalit\u00e9 \u00e0 Copilot, "
                        "\u00e9cris toi-m\u00eame un petit plan en quelques lignes : les "
                        "\u00e9tapes, l'ordre logique, ce qui est essentiel et ce qui peut "
                        "attendre. Un bon plan produit de bien meilleures suggestions qu'une demande vague.",
                        "Partage ensuite ce plan avec Copilot Chat avant de commencer \u00e0 "
                        "coder : il pourra te signaler des \u00e9tapes manquantes ou un ordre plus logique.",
                    ],
                    "tip": None,
                    "exercise": "\u00c9cris un plan de construction en cinq lignes pour ta "
                                "prochaine fonctionnalit\u00e9 avant de demander le moindre code "
                                "\u00e0 Copilot, puis partage-le d'abord avec Copilot Chat.",
                },
                {
                    "title": "It\u00e9rer intelligemment sans casser ton application",
                    "kicker": "Le\u00e7on 6",
                    "paragraphs": [
                        "Plus ton projet grandit, plus il est tentant de demander plusieurs "
                        "changements \u00e0 la fois. R\u00e9siste \u00e0 cette tentation : une "
                        "modification, un test, un commit sur GitHub. Si quelque chose casse, tu "
                        "sais exactement quoi annuler.",
                        "GitHub permet de revenir en arri\u00e8re tr\u00e8s simplement gr\u00e2ce "
                        "\u00e0 l'historique des commits : c'est ton filet de s\u00e9curit\u00e9 "
                        "pour oser it\u00e9rer sans stress.",
                    ],
                    "tip": None,
                    "exercise": "Fais trois petits commits s\u00e9par\u00e9s aujourd'hui, "
                                "chacun avec un changement clair et un message de commit clair.",
                },
                {
                    "title": "Donner une m\u00e9moire durable \u00e0 ton projet",
                    "kicker": "Le\u00e7on 7",
                    "paragraphs": [
                        "Sans consigne particuli\u00e8re, Copilot ne se souvient pas "
                        "forc\u00e9ment de tes pr\u00e9f\u00e9rences d'un jour \u00e0 l'autre. "
                        "Cr\u00e9e un fichier copilot-instructions.md dans un dossier .github/ "
                        "de ton d\u00e9p\u00f4t : d\u00e9cris ton style de code pr\u00e9f\u00e9r\u00e9, "
                        "ta charte graphique, ou des r\u00e8gles comme \u00ab toujours \u00e9crire "
                        "les commentaires en fran\u00e7ais \u00bb.",
                        "Ce fichier devient la m\u00e9moire durable de ton projet : chaque "
                        "suggestion future de Copilot en tiendra compte, m\u00eame dans une "
                        "nouvelle session.",
                    ],
                    "tip": "Relis et compl\u00e8te ce fichier au fil du projet : c'est un "
                           "investissement de cinq minutes qui am\u00e9liore toutes tes prochaines sessions.",
                    "exercise": "Cr\u00e9e ton premier fichier copilot-instructions.md avec au "
                                "moins trois r\u00e8gles propres \u00e0 ton projet.",
                },
                {
                    "title": "Utiliser l'IA comme testeuse",
                    "kicker": "Le\u00e7on 8",
                    "paragraphs": [
                        "Avant de montrer ton application \u00e0 de vrais \u00e9tudiants, "
                        "demande \u00e0 Copilot Chat de jouer le r\u00f4le d'un utilisateur "
                        "maladroit ou distrait : \u00ab essaie de faire planter ce formulaire "
                        "\u00bb, \u00ab que se passe-t-il si je laisse ce champ vide ? \u00bb.",
                        "Demande-lui aussi de g\u00e9n\u00e9rer des cas de test : des exemples "
                        "de r\u00e9ponses correctes, incorrectes, ou compl\u00e8tement "
                        "inattendues \u00e0 ton quiz ou ton formulaire.",
                    ],
                    "tip": None,
                    "exercise": "Demande \u00e0 Copilot Chat d'essayer de casser ton application "
                                "de trois mani\u00e8res diff\u00e9rentes, puis corrige ce qu'il trouve.",
                },
                {
                    "title": "G\u00e9rer ton code comme un vrai projet avec GitHub",
                    "kicker": "Le\u00e7on 9",
                    "paragraphs": [
                        "Un projet qui dure a besoin d'une vraie organisation : des commits "
                        "clairs et r\u00e9guliers, des branches pour tester une id\u00e9e sans "
                        "casser la version qui fonctionne, et \u00e9ventuellement GitHub "
                        "Enterprise ou GitHub Education si ton \u00e9tablissement veut "
                        "h\u00e9berger et g\u00e9rer ces projets de fa\u00e7on centralis\u00e9e "
                        "pour plusieurs enseignants.",
                        "C'est aussi ce qui te permet de collaborer : un coll\u00e8gue peut "
                        "proposer des changements via une pull request, que tu relis avant de "
                        "l'accepter, exactement comme le ferait une \u00e9quipe de d\u00e9veloppement.",
                    ],
                    "tip": None,
                    "exercise": "Cr\u00e9e une branche, fais-y un petit changement, et ouvre ta "
                                "premi\u00e8re pull request pour le fusionner dans ta version principale.",
                },
            ],
        },
        "expert": {
            "slug": "vibe-expert",
            "tag_class": "tag-expert",
            "level_label": "Expert",
            "title": "Vibe Coding Expert",
            "subtitle": "Ajoute de l'intelligence artificielle \u00e0 ton application et "
                       "construis un exemple complet, pr\u00eat pour un vrai cours.",
            "card_desc": "Va plus loin : ajoute de l'IA \u00e0 ton application, choisis le bon "
                         "mod\u00e8le, ma\u00eetrise les co\u00fbts, et termine avec un exemple complet.",
            "meta": "8 le\u00e7ons \u00b7 environ 1h30",
            "lessons": [
                {
                    "title": "Ajouter de l'IA \u00e0 ton application p\u00e9dagogique",
                    "kicker": "Le\u00e7on 1",
                    "paragraphs": [
                        "Jusqu'ici, Copilot t'a aid\u00e9 \u00e0 \u00e9crire le code de ton "
                        "application. Cette le\u00e7on va plus loin : ajouter une "
                        "fonctionnalit\u00e9 d'IA directement utilisable par tes \u00e9tudiants, "
                        "comme un bouton \u00ab explique-moi cette notion autrement \u00bb qui "
                        "interroge un mod\u00e8le d'IA en direct.",
                        "Demande \u00e0 Copilot de t'aider \u00e0 cr\u00e9er cette "
                        "int\u00e9gration : un bouton qui envoie une question \u00e0 un "
                        "mod\u00e8le d'IA et affiche la r\u00e9ponse dans ta page.",
                    ],
                    "tip": None,
                    "exercise": "Ajoute un bouton aliment\u00e9 par l'IA \u00e0 un projet "
                                "existant, m\u00eame un simple bouton qui renvoie la question "
                                "telle quelle, pour voir tout le circuit fonctionner.",
                },
                {
                    "title": "Choisir et comparer les mod\u00e8les d'IA",
                    "kicker": "Le\u00e7on 2",
                    "paragraphs": [
                        "Il existe plusieurs familles de mod\u00e8les d'IA (GPT, Claude, "
                        "Gemini, entre autres), avec des diff\u00e9rences de qualit\u00e9, de "
                        "vitesse et de co\u00fbt. Dans Copilot Chat, tu peux d'ailleurs "
                        "d\u00e9j\u00e0 choisir entre plusieurs mod\u00e8les selon la t\u00e2che.",
                        "Pour l'IA int\u00e9gr\u00e9e \u00e0 ton application p\u00e9dagogique, "
                        "commence simple avec un mod\u00e8le \u00e9conomique, et ne passe "
                        "\u00e0 un mod\u00e8le plus puissant que si tu en as vraiment besoin.",
                    ],
                    "tip": None,
                    "exercise": "Pose la m\u00eame question \u00e0 deux mod\u00e8les diff\u00e9rents "
                                "dans Copilot Chat et compare les r\u00e9ponses en qualit\u00e9, "
                                "ton et vitesse.",
                },
                {
                    "title": "Configurer tes cl\u00e9s d'acc\u00e8s en toute s\u00e9curit\u00e9",
                    "kicker": "Le\u00e7on 3",
                    "paragraphs": [
                        "Pour utiliser un mod\u00e8le d'IA dans ton application, tu as besoin "
                        "d'une cl\u00e9 d'acc\u00e8s (API key) : une sorte de mot de passe pour "
                        "ce service. Ne mets jamais cette cl\u00e9 directement dans ton code visible sur GitHub.",
                        "Demande \u00e0 Copilot de t'aider \u00e0 la stocker comme un secret "
                        "prot\u00e9g\u00e9 (variable d'environnement ou secret GitHub) : ton "
                        "\u00e9tablissement ou son service informatique peut t'accompagner sur ce point si besoin.",
                    ],
                    "tip": "Une cl\u00e9 expos\u00e9e par erreur peut \u00eatre utilis\u00e9e "
                           "par d'autres : si cela arrive, r\u00e9g\u00e9n\u00e8re-la imm\u00e9diatement.",
                    "exercise": "Stocke une cl\u00e9 d'API comme secret prot\u00e9g\u00e9 au "
                                "lieu de la mettre directement dans ton code, et v\u00e9rifie "
                                "que ton code fonctionne toujours en la lisant depuis l\u00e0.",
                },
                {
                    "title": "Premier petit projet : un bouton d'explication IA",
                    "kicker": "Le\u00e7on 4",
                    "paragraphs": [
                        "Construis un exemple concret : sur ta page de cours, un bouton \u00ab "
                        "je ne comprends pas \u00bb qui envoie la question de l'\u00e9tudiant "
                        "\u00e0 un mod\u00e8le d'IA et affiche une explication diff\u00e9rente, "
                        "plus simple ou avec un autre exemple.",
                        "Demande \u00e0 Copilot de construire cette fonctionnalit\u00e9 \u00e9tape "
                        "par \u00e9tape, en testant chaque partie avant de passer \u00e0 la suivante.",
                    ],
                    "tip": None,
                    "exercise": "Construis le bouton \u00ab je ne comprends pas \u00bb de bout "
                                "en bout sur une vraie page \u00e0 toi \u2014 ton Sondage "
                                "\u00c9clair ou un autre projet.",
                },
                {
                    "title": "D\u00e9ployer ton int\u00e9gration IA en toute s\u00e9curit\u00e9",
                    "kicker": "Le\u00e7on 5",
                    "paragraphs": [
                        "Une int\u00e9gration IA ne doit jamais exposer ta cl\u00e9 d'acc\u00e8s "
                        "dans le navigateur de l'\u00e9tudiant. Demande \u00e0 Copilot de "
                        "mettre en place une petite fonction c\u00f4t\u00e9 serveur qui re\u00e7oit "
                        "la question, appelle le mod\u00e8le d'IA avec la cl\u00e9 cach\u00e9e, "
                        "et renvoie uniquement la r\u00e9ponse.",
                        "Des plateformes comme Vercel ou Netlify permettent d'h\u00e9berger ce "
                        "genre de fonction gratuitement pour un petit projet, en quelques clics "
                        "depuis ton d\u00e9p\u00f4t GitHub.",
                    ],
                    "tip": None,
                    "exercise": "D\u00e9ploie ta fonctionnalit\u00e9 IA via une petite fonction "
                                "serverless, et v\u00e9rifie dans l'onglet r\u00e9seau de ton "
                                "navigateur que la cl\u00e9 n'y appara\u00eet jamais.",
                },
                {
                    "title": "Construire de fa\u00e7on s\u00fbre et abordable",
                    "kicker": "Le\u00e7on 6",
                    "paragraphs": [
                        "Un mod\u00e8le d'IA a un co\u00fbt \u00e0 chaque question pos\u00e9e. "
                        "Pour un usage p\u00e9dagogique avec un groupe d'\u00e9tudiants, mets "
                        "en place une limite claire (un nombre de questions par jour, par "
                        "exemple) pour \u00e9viter les mauvaises surprises.",
                        "Demande \u00e0 Copilot d'ajouter cette limite directement dans le "
                        "code, et surveille r\u00e9guli\u00e8rement l'usage via le tableau de "
                        "bord du service d'IA que tu utilises.",
                    ],
                    "tip": None,
                    "exercise": "Ajoute une limite d'usage quotidienne \u00e0 ta fonctionnalit\u00e9 "
                                "IA et teste ce qui se passe une fois cette limite atteinte.",
                },
                {
                    "title": "Aller au-del\u00e0 du texte",
                    "kicker": "Le\u00e7on 7",
                    "paragraphs": [
                        "L'IA ne se limite pas au texte : certains mod\u00e8les peuvent "
                        "d\u00e9crire une image, transcrire un enregistrement audio, ou m\u00eame "
                        "g\u00e9n\u00e9rer une image \u00e0 partir d'une description. Pour un "
                        "cours, cela ouvre des possibilit\u00e9s comme corriger un sch\u00e9ma "
                        "dessin\u00e9 \u00e0 la main ou transcrire une intervention orale.",
                        "Ces fonctionnalit\u00e9s demandent un peu plus de pr\u00e9paration, "
                        "mais la m\u00e9thode reste la m\u00eame : d\u00e9cris pr\u00e9cis\u00e9ment "
                        "\u00e0 Copilot ce que tu veux, teste, ajuste.",
                    ],
                    "tip": None,
                    "exercise": "Demande \u00e0 un mod\u00e8le d'IA de d\u00e9crire ou de "
                                "r\u00e9sumer une image ou un enregistrement li\u00e9 \u00e0 ton propre m\u00e9tier.",
                },
                {
                    "title": "Exemple complet et conclusion",
                    "kicker": "Le\u00e7on 8",
                    "paragraphs": [
                        "Pour clore ce parcours, voici un exemple complet que tu peux "
                        "construire de bout en bout : un quiz interactif avec correction "
                        "automatique, sauvegarde des scores dans une base de donn\u00e9es, et un "
                        "bouton d'explication IA pour chaque question rat\u00e9e, le tout "
                        "publi\u00e9 en ligne via GitHub.",
                        "Tu as maintenant tous les outils pour construire, tester, publier et "
                        "faire \u00e9voluer tes propres applications p\u00e9dagogiques. La seule "
                        "vraie limite, d\u00e9sormais, c'est le temps que tu veux y consacrer : "
                        "merci d'avoir suivi ce parcours, et bon vibe coding !",
                    ],
                    "tip": None,
                    "exercise": "\u00c9cris une chose que tu vas construire ensuite avec ce que "
                                "tu as appris dans cette formation \u2014 puis va la construire.",
                },
            ],
        },
    },
    "best_practices": {
        "title": "Bonnes pratiques",
        "sub": "Une check-list en une page pour bien lancer ton projet de vibe coding, de "
               "l'id\u00e9e \u00e0 la publication sur GitHub.",
        "items": [
            ("Pars toujours d'un vrai probl\u00e8me de cours", "La meilleure id\u00e9e "
             "d'application vient d'une frustration concr\u00e8te que tu vis en classe, pas "
             "d'une technologie \u00e0 la mode."),
            ("Commence minuscule", "Une seule fonctionnalit\u00e9 qui marche vaut mieux qu'un "
             "plan ambitieux jamais termin\u00e9. \u00c9largis ensuite, \u00e9tape par \u00e9tape."),
            ("Un changement, un test, un commit", "Ne demande jamais dix modifications \u00e0 "
             "la fois : tu ne saurais plus laquelle a cass\u00e9 quoi."),
            ("Sauvegarde tout sur GitHub d\u00e8s le premier jour", "M\u00eame un projet "
             "minuscule m\u00e9rite un d\u00e9p\u00f4t GitHub : c'est ta sauvegarde et ton "
             "historique de versions."),
            ("Ne stocke jamais de donn\u00e9es sensibles sans r\u00e9fl\u00e9chir", "Demande "
             "toujours \u00e0 Copilot si ton code respecte de bonnes pratiques de protection "
             "des donn\u00e9es avant de collecter des informations sur tes \u00e9tudiants."),
            ("Prot\u00e8ge tes cl\u00e9s d'acc\u00e8s", "Une cl\u00e9 d'API ne doit jamais "
             "appara\u00eetre dans du code visible sur GitHub : utilise toujours un secret prot\u00e9g\u00e9."),
            ("Relis chaque suggestion avant de l'accepter", "Copilot propose, tu disposes : "
             "comprends ce que fait le code avant de l'utiliser avec de vrais \u00e9tudiants."),
            ("Donne une m\u00e9moire \u00e0 ton projet", "Un fichier copilot-instructions.md "
             "fait gagner un temps pr\u00e9cieux sur chaque nouvelle session de travail."),
            ("Fais tester par un vrai coll\u00e8gue ou \u00e9tudiant", "Un regard ext\u00e9rieur "
             "trouve toujours des maladresses que tu ne remarquerais jamais en travaillant en solo."),
            ("Documente ton projet en une page", "Un court README explique \u00e0 un coll\u00e8gue "
             "(ou \u00e0 toi-m\u00eame dans six mois) ce que fait le projet et comment le relancer."),
        ],
    },
    "about": {
        "title": "\u00c0 propos de ce parcours",
        "paragraphs": [
            "Vibe Coding Copilot est une ressource p\u00e9dagogique ind\u00e9pendante et "
            "gratuite pour toute personne travaillant ou \u00e9tudiant dans l'enseignement "
            "sup\u00e9rieur : enseignantes et enseignants, \u00e9tudiantes et \u00e9tudiants, services IT, RH, "
            "direction, finances et administration, qui souhaite construire ses propres "
            "outils num\u00e9riques sans \u00eatre d\u00e9veloppeur ou d\u00e9veloppeuse.",
            "Ce site n'est ni affili\u00e9, ni approuv\u00e9, ni sponsoris\u00e9 par GitHub ou "
            "Microsoft. Tous les noms de produits et marques cit\u00e9s appartiennent \u00e0 "
            "leurs propri\u00e9taires respectifs ; ce site explique simplement comment bien "
            "les utiliser dans un contexte institutionnel.",
        ],
        "sections": [
            ("Pourquoi ce parcours existe", [
                "Beaucoup d'excellentes id\u00e9es, en classe, au support IT, aux RH ou en "
                "finances, restent bloqu\u00e9es faute de comp\u00e9tences en programmation ou "
                "de budget pour un d\u00e9veloppement sur mesure. Le vibe coding, avec des "
                "outils comme GitHub Copilot, change cette \u00e9quation : tu deviens capable "
                "de construire toi-m\u00eame, en gardant le contr\u00f4le sur ton propre domaine.",
            ]),
            ("Pourquoi GitHub en particulier", [
                "Construire une application avec l'IA n'est que la moiti\u00e9 du chemin : "
                "encore faut-il la sauvegarder, la faire \u00e9voluer sans la casser, et la "
                "publier quelque part. GitHub (et GitHub Enterprise ou GitHub Education pour "
                "les \u00e9tablissements) r\u00e9pond exactement \u00e0 ce besoin, et "
                "s'int\u00e8gre nativement \u00e0 GitHub Copilot.",
            ]),
            ("Retours", [
                "Ce parcours est un document vivant. S'il te manque un exemple, une le\u00e7on "
                "ou une explication, traite-le comme n'importe quel autre document "
                "p\u00e9dagogique : propose une am\u00e9lioration.",
            ]),
        ],
    },
    "toolkit": {
        "title": "Bo\u00eete \u00e0 outils \u2014 biblioth\u00e8que de prompts",
        "sub": "Des prompts Copilot pr\u00eats \u00e0 l'emploi, organis\u00e9s par m\u00e9tier. "
               "Copie-en un, adapte les d\u00e9tails entre crochets, et colle-le dans Copilot Chat.",
        "groups": [
            ("\U0001f393", "Enseignants", [
                "Cr\u00e9e un quiz auto-corrig\u00e9 sur [sujet] avec 5 questions \u00e0 choix "
                "multiple et un retour instantan\u00e9.",
                "Ajoute un bouton qui permet aux \u00e9tudiants de t\u00e9l\u00e9charger leurs "
                "r\u00e9sultats de quiz en PDF.",
                "Transforme les notes de cours que je vais coller ci-dessous en une fiche de "
                "r\u00e9vision structur\u00e9e et imprimable.",
            ]),
            ("\U0001f9d1\u200d\U0001f393", "\u00c9tudiants", [
                "Cr\u00e9e une appli de flashcards pour [mati\u00e8re] o\u00f9 les cartes se "
                "retournent au clic et peuvent \u00eatre marqu\u00e9es comme \u00ab sues \u00bb.",
                "Ajoute un minuteur \u00e0 ma page de r\u00e9vision qui se relance toutes les 25 minutes.",
                "Cr\u00e9e une page de portfolio simple listant mes trois meilleurs projets "
                "avec liens et captures d'\u00e9cran.",
            ]),
            ("\U0001f5a5\ufe0f", "Services IT", [
                "Cr\u00e9e un outil interne simple o\u00f9 le personnel peut demander une "
                "r\u00e9servation de salle et voir la disponibilit\u00e9 en direct.",
                "Ajoute une v\u00e9rification pour que seules les adresses email [domaine] "
                "puissent soumettre ce formulaire.",
                "G\u00e9n\u00e8re un workflow GitHub Actions qui d\u00e9ploie ce site sur "
                "GitHub Pages \u00e0 chaque push.",
            ]),
            ("\U0001f91d", "RH", [
                "Cr\u00e9e une check-list d'int\u00e9gration interactive avec suivi de la "
                "progression pour les nouveaux collaborateurs.",
                "Cr\u00e9e un formulaire de feedback pour une formation avec une note de 1 "
                "\u00e0 5 et un champ de commentaire.",
                "Ajoute une page qui calcule le nombre de jours de cong\u00e9s restants \u00e0 "
                "partir d'une date de d\u00e9but que je saisis.",
            ]),
            ("\U0001f9ed", "Direction", [
                "Cr\u00e9e une page de sondage en direct o\u00f9 le personnel peut voter sur "
                "une question et voir les r\u00e9sultats se mettre \u00e0 jour instantan\u00e9ment.",
                "Cr\u00e9e un tableau de bord simple qui r\u00e9sume les trois indicateurs "
                "que je vais coller comme KPI.",
                "Transforme ce r\u00e9sum\u00e9 strat\u00e9gique en points en une page visuelle claire.",
            ]),
            ("\U0001f4b6", "Finances", [
                "Cr\u00e9e un petit calculateur qui estime le remboursement de frais de "
                "d\u00e9placement \u00e0 partir d'une distance et d'un tarif.",
                "Cr\u00e9e un formulaire simple pour enregistrer des d\u00e9penses r\u00e9currentes "
                "avec un total qui se met \u00e0 jour.",
                "G\u00e9n\u00e8re un tableau triable \u00e0 partir des donn\u00e9es que je vais coller ci-dessous.",
            ]),
        ],
    },
    "explorer": {
        "title": "Explorateur de cas d'usage GitHub Copilot",
        "sub": "26 cas d'usage concrets et pr\u00eats \u00e0 suivre, pour tous les p\u00f4les de "
               "l'enseignement sup\u00e9rieur. Filtre par m\u00e9tier ou par fonctionnalit\u00e9 "
               "Copilot, puis ouvre une carte pour voir les \u00e9tapes exactes.",
        "search_placeholder": "Cherche un cas d'usage (« quiz », « budget », « chat »...)",
        "persona_filter_label": "M\u00e9tier",
        "feature_filter_label": "Fonctionnalit\u00e9 Copilot",
        "all_label": "Tous les m\u00e9tiers",
        "show_steps": "Voir les \u00e9tapes",
        "hide_steps": "Masquer les \u00e9tapes",
        "result_label": "R\u00e9sultat :",
        "further_label": "Pour aller plus loin :",
        "count_prefix": "Affichage de",
        "count_suffix": "cas d'usage",
        "empty_message": "Aucun cas d'usage ne correspond encore \u00e0 ces filtres : essaie "
                         "d'en retirer un ou de vider la recherche.",
        "personas": [
            ("teaching", "\U0001f393", "Enseignantes et enseignants"),
            ("students", "\U0001f9d1\u200d\U0001f393", "\u00c9tudiantes et \u00e9tudiants"),
            ("it", "\U0001f5a5\ufe0f", "Services IT et num\u00e9riques"),
            ("hr", "\U0001f91d", "Ressources humaines"),
            ("leadership", "\U0001f9ed", "Direction et pilotage"),
            ("finance", "\U0001f4b6", "Finances et administration"),
            ("research", "\U0001f52c", "Chercheuses et chercheurs"),
            ("campus", "\U0001f4da", "Biblioth\u00e8que, communication et vie de campus"),
        ],
        "features": [
            ("inline", "Compl\u00e9tions en ligne", "Copilot sugg\u00e8re du code au fil de ta "
             "frappe, directement l\u00e0 o\u00f9 tu travailles."),
            ("chat", "Copilot Chat", "Pose des questions, demande des modifications, ou fais "
             "expliquer du code en langage naturel."),
            ("agent", "Mode Agent", "D\u00e9cris une t\u00e2che plus large ; Copilot planifie "
             "et applique plusieurs changements d'un coup."),
            ("cli", "Copilot en ligne de commande", "D\u00e9cris ce que tu veux dans ton "
             "terminal ; Copilot propose la commande exacte."),
            ("review", "Copilot code review", "Copilot propose des suggestions de revue "
             "et des points d'attention avant ou pendant la relecture humaine."),
            ("cloudagent", "Copilot cloud agent", "Assigne une issue ou une t\u00e2che \u00e0 Copilot ; "
             "il travaille sur une branche puis ouvre une pull request."),
            ("spaces", "Copilot Spaces", "Ancre Copilot avec un contexte partageable : "
             "fichiers, notes, transcriptions et images."),
            ("mcp", "Extensions et MCP", "Connecte Copilot \u00e0 tes propres outils et sources de donn\u00e9es."),
        ],
        "usecases": [
            {
                "title": "Construire un quiz auto-corrig\u00e9 en une seule s\u00e9ance",
                "persona": "teaching", "features": ["chat", "inline"],
                "situation": "Tu veux un quiz que tes \u00e9tudiantes et \u00e9tudiants peuvent "
                            "utiliser pour r\u00e9viser un chapitre, sans passer par un outil externe payant.",
                "steps": [
                    "Ouvre Copilot Chat et d\u00e9cris ton quiz : « Cr\u00e9e une page HTML "
                    "avec un quiz de 5 questions \u00e0 choix multiple sur [sujet], affichant "
                    "un score final. »",
                    "Lis le code g\u00e9n\u00e9r\u00e9, teste-le dans ton navigateur, puis "
                    "demande un ajustement pr\u00e9cis \u00e0 la fois, par exemple : « Ajoute "
                    "une courte explication sous chaque question une fois qu'elle est r\u00e9pondue. »",
                    "Une fois le r\u00e9sultat satisfaisant, demande \u00e0 Copilot d'ajouter "
                    "un bouton « recommencer le quiz ».",
                ],
                "result": "Un quiz fonctionnel et personnalis\u00e9 pour ton cours, pr\u00eat \u00e0 publier.",
                "further": "Demande \u00e0 Copilot de m\u00e9langer l'ordre des questions \u00e0 chaque lancement.",
            },
            {
                "title": "Transformer un sch\u00e9ma dessin\u00e9 \u00e0 la main en version "
                         "num\u00e9rique avec Copilot Spaces",
                "persona": "teaching", "features": ["spaces", "chat"],
                "situation": "Tu as une photo ou une capture d'\u00e9cran d'un sch\u00e9ma ou "
                            "d'un exercice manuscrit \u00e0 num\u00e9riser.",
                "steps": [
                    "Colle la capture d'\u00e9cran directement dans Copilot Chat.",
                    "Demande : « D\u00e9cris ce sch\u00e9ma et transforme-le en HTML/CSS qui "
                    "reproduit sa structure. »",
                    "Affine les couleurs et les l\u00e9gendes avec des demandes successives.",
                ],
                "result": "Un sch\u00e9ma num\u00e9rique et modifiable construit \u00e0 partir d'une simple photo.",
                "further": "Utilise la m\u00eame m\u00e9thode pour num\u00e9riser une grille de correction manuscrite.",
            },
            {
                "title": "G\u00e9n\u00e9rer des variantes d'exercices pour limiter la copie",
                "persona": "teaching", "features": ["chat"],
                "situation": "Tu veux plusieurs versions d'un m\u00eame exercice pour "
                            "diff\u00e9rents groupes d'\u00e9tudiantes et \u00e9tudiants.",
                "steps": [
                    "Donne \u00e0 Copilot Chat un exercice existant et demande : « G\u00e9n\u00e8re "
                    "4 variantes de cet exercice avec des valeurs diff\u00e9rentes mais la "
                    "m\u00eame difficult\u00e9. »",
                    "Demande une grille de correction commune : « Ajoute une grille de "
                    "correction expliquant chaque \u00e9tape. »",
                    "Demande \u00e0 Copilot d'exporter le tout dans un seul document structur\u00e9.",
                ],
                "result": "Plusieurs versions pr\u00eates \u00e0 distribuer, avec une correction coh\u00e9rente.",
                "further": "Demande \u00e0 Copilot de g\u00e9n\u00e9rer aussi une version "
                          "accessible pour les lecteurs d'\u00e9cran.",
            },
            {
                "title": "Automatiser un calculateur de moyenne pond\u00e9r\u00e9e avec le mode Agent",
                "persona": "teaching", "features": ["agent", "chat"],
                "situation": "Tu g\u00e8res un tableau de notation complexe et tu veux calculer "
                            "automatiquement des moyennes pond\u00e9r\u00e9es.",
                "steps": [
                    "D\u00e9cris ton bar\u00e8me au mode Agent : « Cr\u00e9e une page qui calcule "
                    "une moyenne pond\u00e9r\u00e9e \u00e0 partir de ces cat\u00e9gories : [liste]. »",
                    "Relis le plan propos\u00e9 par l'agent avant de l'approuver.",
                    "Demande-lui d'ajouter un export CSV pour partager les r\u00e9sultats avec tes coll\u00e8gues.",
                ],
                "result": "Un calculateur fiable, adapt\u00e9 \u00e0 ton propre bar\u00e8me de notation.",
                "further": "Connecte-le \u00e0 une vraie base de donn\u00e9es (voir le parcours "
                          "Avanc\u00e9) pour le r\u00e9utiliser chaque semestre.",
            },
            {
                "title": "Apprendre \u00e0 coder avec Copilot comme tuteur, pas comme b\u00e9quille",
                "persona": "students", "features": ["inline", "chat"],
                "situation": "Tu d\u00e9butes en programmation et tu veux comprendre le code, "
                            "pas seulement le copier.",
                "steps": [
                    "\u00c9cris d'abord une fonction simple toi-m\u00eame, m\u00eame incompl\u00e8te.",
                    "Demande \u00e0 Copilot Chat : « Explique-moi ligne par ligne ce que fait ce code. »",
                    "Demande ensuite : « Interroge-moi sur un point pour v\u00e9rifier que j'ai compris. »",
                ],
                "result": "Une vraie compr\u00e9hension du code, pas seulement un copier-coller.",
                "further": "Demande \u00e0 Copilot un exercice l\u00e9g\u00e8rement plus difficile sur la m\u00eame notion.",
            },
            {
                "title": "Construire un site de r\u00e9vision partag\u00e9 pour ton groupe d'\u00e9tude",
                "persona": "students", "features": ["chat", "cli"],
                "situation": "Ton groupe d'\u00e9tude veut un espace commun pour r\u00e9viser avant l'examen.",
                "steps": [
                    "D\u00e9cris \u00e0 Copilot Chat l'application de flashcards que vous voulez.",
                    "Utilise Copilot dans le terminal pour cr\u00e9er le d\u00e9p\u00f4t : "
                    "d\u00e9cris ce que tu veux faire, Copilot propose la commande git exacte.",
                    "Partagez le lien GitHub Pages avec le groupe.",
                ],
                "result": "Un outil de r\u00e9vision gratuit et partag\u00e9, sous le contr\u00f4le du groupe.",
                "further": "Ajoutez un syst\u00e8me de vote simple pour les meilleures fiches.",
            },
            {
                "title": "Pr\u00e9senter ton m\u00e9moire ou ton rapport de stage en ligne",
                "persona": "students", "features": ["chat"],
                "situation": "Tu dois structurer un long document et automatiser des t\u00e2ches "
                            "r\u00e9p\u00e9titives comme la table des mati\u00e8res.",
                "steps": [
                    "Demande \u00e0 Copilot de g\u00e9n\u00e9rer un squelette de site pour "
                    "pr\u00e9senter ton m\u00e9moire en ligne (r\u00e9sum\u00e9, chapitres, annexes).",
                    "Demande une table des mati\u00e8res interactive construite \u00e0 partir "
                    "des titres de tes sections.",
                    "Ajoute une page de contact pour recevoir des retours.",
                ],
                "result": "Une version en ligne et pr\u00e9sentable de ton m\u00e9moire, en "
                         "plus du document classique.",
                "further": "Demande \u00e0 Copilot d'ajouter une recherche par mot-cl\u00e9 dans le contenu.",
            },
            {
                "title": "Construire un portfolio pour ta recherche de stage ou d'emploi",
                "persona": "students", "features": ["chat", "spaces"],
                "situation": "Tu veux un site simple qui pr\u00e9sente tes projets, sans "
                            "repartir d'une page blanche.",
                "steps": [
                    "Colle une capture d'\u00e9cran d'un style de portfolio que tu aimes et "
                    "demande \u00e0 Copilot Chat de s'en inspirer.",
                    "D\u00e9cris tes trois meilleurs projets, un par un.",
                    "Demande \u00e0 Copilot d'ajouter un formulaire de contact simple.",
                ],
                "result": "Un portfolio en ligne pr\u00eat \u00e0 partager sur ton CV.",
                "further": "Publie-le avec un nom de domaine personnalis\u00e9 via GitHub Pages.",
            },
            {
                "title": "Prototyper un outil interne en une heure",
                "persona": "it", "features": ["agent", "chat"],
                "situation": "Un service demande un petit outil interne et tu veux un "
                            "prototype fonctionnel rapidement, avant d'investir du temps d'ing\u00e9nierie.",
                "steps": [
                    "D\u00e9cris le besoin principal de l'outil au mode Agent : « Cr\u00e9e une "
                    "page o\u00f9 le personnel peut soumettre une demande et voir son statut. »",
                    "Relis le plan propos\u00e9 et laisse l'agent construire une premi\u00e8re version.",
                    "Demande un affinement r\u00e9aliste, comme une validation de formulaire "
                    "ou un code couleur de statut.",
                ],
                "result": "Un prototype fonctionnel en moins d'une heure, pour valider le "
                         "besoin avant un vrai d\u00e9veloppement.",
                "further": "S'il se r\u00e9v\u00e8le utile, planifie une version compl\u00e8te "
                          "avec une vraie base de donn\u00e9es et une gestion des acc\u00e8s.",
            },
            {
                "title": "Documenter automatiquement un script existant",
                "persona": "it", "features": ["chat"],
                "situation": "Tu as h\u00e9rit\u00e9 d'un script interne non document\u00e9 et "
                            "tu dois le comprendre et le documenter rapidement.",
                "steps": [
                    "Ouvre le script et demande \u00e0 Copilot Chat : « Explique-moi ce que "
                    "fait ce script, \u00e9tape par \u00e9tape. »",
                    "Demande : « G\u00e9n\u00e8re un README d\u00e9crivant son objectif, ses "
                    "entr\u00e9es et comment l'ex\u00e9cuter. »",
                    "Demande \u00e0 Copilot de signaler les parties du code risqu\u00e9es ou peu claires.",
                ],
                "result": "Une documentation claire pour un script que seule une personne comprenait auparavant.",
                "further": "Ajoute le README g\u00e9n\u00e9r\u00e9 directement dans le d\u00e9p\u00f4t du script.",
            },
            {
                "title": "Automatiser un d\u00e9ploiement avec GitHub Actions",
                "persona": "it", "features": ["chat", "agent"],
                "situation": "Tu veux qu'un petit site ou outil se red\u00e9ploie "
                            "automatiquement \u00e0 chaque modification.",
                "steps": [
                    "Demande \u00e0 Copilot Chat : « G\u00e9n\u00e8re un workflow GitHub "
                    "Actions qui d\u00e9ploie ce site sur GitHub Pages \u00e0 chaque push sur main. »",
                    "Ajoute le fichier propos\u00e9 \u00e0 ton d\u00e9p\u00f4t et pousse un "
                    "petit changement pour tester.",
                    "Demande \u00e0 Copilot d'ajouter une notification en cas d'\u00e9chec du d\u00e9ploiement.",
                ],
                "result": "Un site qui se met \u00e0 jour tout seul, sans \u00e9tape manuelle de red\u00e9ploiement.",
                "further": "R\u00e9utilise le m\u00eame fichier de workflow comme mod\u00e8le pour d'autres projets internes.",
            },
            {
                "title": "Construire une check-list d'int\u00e9gration interactive",
                "persona": "hr", "features": ["chat"],
                "situation": "Les nouvelles recrues re\u00e7oivent un long document "
                            "d'int\u00e9gration statique, facile \u00e0 perdre de vue.",
                "steps": [
                    "D\u00e9cris les \u00e9tapes d'int\u00e9gration \u00e0 Copilot Chat et "
                    "demande une page de check-list interactive.",
                    "Demande que la progression soit sauvegard\u00e9e pour que la personne "
                    "puisse reprendre plus tard.",
                    "Demande \u00e0 Copilot d'ajouter un r\u00e9sum\u00e9 imprimable pour les dossiers RH.",
                ],
                "result": "Une exp\u00e9rience d'int\u00e9gration conviviale et suivie pour les nouveaux coll\u00e8gues.",
                "further": "Personnalise la check-list par m\u00e9tier gr\u00e2ce \u00e0 un simple menu d\u00e9roulant au d\u00e9part.",
            },
            {
                "title": "Cr\u00e9er un formulaire de feedback de formation en quelques minutes",
                "persona": "hr", "features": ["chat"],
                "situation": "Tu as besoin d'un moyen rapide de recueillir des retours "
                            "apr\u00e8s une formation, sans attendre la licence d'un outil de sondage.",
                "steps": [
                    "Demande \u00e0 Copilot Chat de construire une page avec une note de 1 "
                    "\u00e0 5 et un champ de commentaire.",
                    "Demande que les r\u00e9ponses soient enregistr\u00e9es pour \u00eatre consult\u00e9es ensuite.",
                    "Demande une vue de synth\u00e8se affichant la note moyenne.",
                ],
                "result": "Un formulaire de feedback fonctionnel, en ligne avant m\u00eame la fin de la session.",
                "further": "R\u00e9utilise la m\u00eame page comme mod\u00e8le pour chaque future formation.",
            },
            {
                "title": "Construire un calculateur de solde de cong\u00e9s",
                "persona": "hr", "features": ["chat"],
                "situation": "Le personnel demande r\u00e9guli\u00e8rement aux RH combien de "
                            "jours de cong\u00e9s il lui reste.",
                "steps": [
                    "D\u00e9cris la politique de cong\u00e9s de ton \u00e9tablissement \u00e0 Copilot Chat.",
                    "Demande-lui de construire un petit calculateur qui prend une date de "
                    "d\u00e9but et affiche les jours restants.",
                    "Demande une explication claire affich\u00e9e \u00e0 c\u00f4t\u00e9 du "
                    "r\u00e9sultat, en cas de cas particulier.",
                ],
                "result": "Un outil en libre-service qui r\u00e9duit les questions r\u00e9p\u00e9titives aux RH.",
                "further": "Relie-le \u00e0 la check-list d'int\u00e9gration ci-dessus.",
            },
            {
                "title": "Lancer un sondage en direct pendant une r\u00e9union",
                "persona": "leadership", "features": ["chat", "agent"],
                "situation": "Tu veux un retour en temps r\u00e9el du personnel pendant une "
                            "assembl\u00e9e g\u00e9n\u00e9rale, sans outil de sondage payant.",
                "steps": [
                    "D\u00e9cris la question et les options \u00e0 Copilot Chat, en suivant le "
                    "m\u00eame sch\u00e9ma que l'exemple du Sondage \u00c9clair du parcours guid\u00e9.",
                    "Teste-le toi-m\u00eame, puis projette le lien pendant la r\u00e9union.",
                    "Demande \u00e0 Copilot d'ajouter un affichage des r\u00e9sultats mis \u00e0 jour en direct.",
                ],
                "result": "Un retour instantan\u00e9 et visible de la salle, sans aucun service externe.",
                "further": "R\u00e9utilise exactement la m\u00eame page pour chaque future r\u00e9union, en changeant simplement la question.",
            },
            {
                "title": "Construire un tableau de bord simple d'indicateurs cl\u00e9s",
                "persona": "leadership", "features": ["chat"],
                "situation": "Tu veux suivre trois ou quatre chiffres dans le temps sans un outil de BI complet.",
                "steps": [
                    "D\u00e9cris tes indicateurs \u00e0 Copilot Chat et colle quelques chiffres d'exemple.",
                    "Demande-lui de construire un tableau de bord clair, sur une seule page, qui les r\u00e9sume.",
                    "Demande un moyen simple de mettre \u00e0 jour les chiffres chaque mois.",
                ],
                "result": "Un tableau de bord l\u00e9ger, que tu contr\u00f4les et comprends enti\u00e8rement.",
                "further": "Demande \u00e0 Copilot d'ajouter un petit graphique de tendance une "
                          "fois quelques mois de donn\u00e9es r\u00e9unis.",
            },
            {
                "title": "Transformer un r\u00e9sum\u00e9 strat\u00e9gique en page visuelle",
                "persona": "leadership", "features": ["chat", "spaces"],
                "situation": "Tu as un document strat\u00e9gique dense en points, et tu veux "
                            "quelque chose de plus facile \u00e0 pr\u00e9senter.",
                "steps": [
                    "Colle tes points dans Copilot Chat et demande une mise en page visuelle "
                    "claire, sur une seule page.",
                    "Colle une capture d'\u00e9cran d'un style visuel que tu aimes pour orienter le design.",
                    "Demande une version imprimable en plus de la version web.",
                ],
                "result": "Une page claire et partageable, construite \u00e0 partir d'un contenu d\u00e9j\u00e0 existant.",
                "further": "R\u00e9utilise la m\u00eame mise en page pour la prochaine mise \u00e0 jour strat\u00e9gique.",
            },
            {
                "title": "Construire un calculateur de frais de d\u00e9placement",
                "persona": "finance", "features": ["chat"],
                "situation": "Le personnel demande souvent combien il sera rembours\u00e9 pour "
                            "un d\u00e9placement avant de soumettre une note de frais.",
                "steps": [
                    "D\u00e9cris tes r\u00e8gles de remboursement \u00e0 Copilot Chat (distance, tarif, plafonds).",
                    "Demande-lui de construire un petit calculateur bas\u00e9 sur ces r\u00e8gles.",
                    "Demande un d\u00e9tail clair du calcul affich\u00e9 \u00e0 la personne qui l'utilise.",
                ],
                "result": "Un estimateur en libre-service qui r\u00e9duit les \u00e9changes d'e-mails.",
                "further": "Relie-le \u00e0 la page interne de l'\u00e9quipe finances.",
            },
            {
                "title": "Suivre un petit budget r\u00e9current",
                "persona": "finance", "features": ["chat"],
                "situation": "Tu g\u00e8res une petite ligne budg\u00e9taire r\u00e9currente et "
                            "tu veux une alternative plus l\u00e9g\u00e8re qu'un tableur complet.",
                "steps": [
                    "D\u00e9cris les cat\u00e9gories de ton budget \u00e0 Copilot Chat.",
                    "Demande une page simple pour enregistrer les d\u00e9penses avec un total qui se met \u00e0 jour.",
                    "Demande une vue de synth\u00e8se mensuelle.",
                ],
                "result": "Un suivi l\u00e9ger, adapt\u00e9 exactement \u00e0 tes propres cat\u00e9gories.",
                "further": "Exporte les donn\u00e9es vers un tableur pour les registres officiels.",
            },
            {
                "title": "Transformer des donn\u00e9es coll\u00e9es en tableau triable",
                "persona": "finance", "features": ["chat"],
                "situation": "Tu re\u00e7ois r\u00e9guli\u00e8rement des donn\u00e9es en texte "
                            "brut ou en lignes copi\u00e9es-coll\u00e9es, difficiles \u00e0 exploiter.",
                "steps": [
                    "Colle les donn\u00e9es brutes dans Copilot Chat.",
                    "Demande-lui de g\u00e9n\u00e9rer un tableau HTML clair et triable \u00e0 partir de ces donn\u00e9es.",
                    "Demande une barre de recherche pour filtrer les lignes.",
                ],
                "result": "Une vue lisible et cherchable de donn\u00e9es qui \u00e9taient auparavant un mur de texte.",
                "further": "Demande \u00e0 Copilot d'ajouter un bouton d'export CSV.",
            },
            {
                "title": "Nettoyer un jeu de donn\u00e9es d\u00e9sordonn\u00e9 avec l'aide de Copilot",
                "persona": "research", "features": ["chat", "agent"],
                "situation": "Tu as un jeu de donn\u00e9es plein d'incoh\u00e9rences (fautes, "
                            "valeurs manquantes, formats m\u00e9lang\u00e9s) avant de pouvoir l'analyser.",
                "steps": [
                    "D\u00e9cris les probl\u00e8mes du jeu de donn\u00e9es \u00e0 Copilot Chat et colle un \u00e9chantillon.",
                    "Demande un script qui le nettoie et le standardise.",
                    "Relis chaque r\u00e8gle de nettoyage avant de l'appliquer \u00e0 l'ensemble des donn\u00e9es.",
                ],
                "result": "Un jeu de donn\u00e9es propre et pr\u00eat pour l'analyse, avec un "
                         "script document\u00e9 montrant exactement ce qui a chang\u00e9.",
                "further": "Demande \u00e0 Copilot d'ajouter un rapport r\u00e9sumant ce qui a \u00e9t\u00e9 nettoy\u00e9 et pourquoi.",
            },
            {
                "title": "G\u00e9n\u00e9rer un premier script d'analyse statistique",
                "persona": "research", "features": ["chat"],
                "situation": "Tu veux un point de d\u00e9part pour une analyse standard sans "
                            "r\u00e9\u00e9crire du code r\u00e9p\u00e9titif \u00e0 chaque fois.",
                "steps": [
                    "D\u00e9cris tes donn\u00e9es et ta question de recherche \u00e0 Copilot Chat.",
                    "Demande un script qui ex\u00e9cute le test statistique pertinent et "
                    "affiche une synth\u00e8se claire.",
                    "Demande \u00e0 Copilot d'expliquer chaque \u00e9tape du script en commentaires.",
                ],
                "result": "Un script d'analyse que tu comprends ligne par ligne, pas une bo\u00eete noire.",
                "further": "Demande \u00e0 Copilot d'ajouter un graphique simple des r\u00e9sultats.",
            },
            {
                "title": "Construire une page de pr\u00e9sentation de tes r\u00e9sultats de recherche",
                "persona": "research", "features": ["chat", "spaces"],
                "situation": "Tu veux une page claire et publique pr\u00e9sentant tes "
                            "r\u00e9sultats, au-del\u00e0 de l'article acad\u00e9mique.",
                "steps": [
                    "D\u00e9cris tes principaux r\u00e9sultats \u00e0 Copilot Chat, un par un.",
                    "Colle un graphique ou une figure et demande \u00e0 Copilot de construire "
                    "une section de page autour.",
                    "Demande un r\u00e9sum\u00e9 en langage clair \u00e0 c\u00f4t\u00e9 de la version technique.",
                ],
                "result": "Une page de r\u00e9sultats accessible, \u00e0 partager depuis ton "
                         "CV ou lors d'une conf\u00e9rence.",
                "further": "Ajoute une section de contact pour les demandes de collaboration.",
            },
            {
                "title": "Construire un catalogue de ressources interactif",
                "persona": "campus", "features": ["chat"],
                "situation": "Tu veux un moyen simple pour les \u00e9tudiantes et \u00e9tudiants "
                            "de parcourir des ressources recommand\u00e9es par sujet.",
                "steps": [
                    "D\u00e9cris ta liste de ressources et tes cat\u00e9gories \u00e0 Copilot Chat.",
                    "Demande une page de catalogue avec recherche et filtres.",
                    "Demande un moyen simple d'ajouter de nouvelles ressources au fil du temps.",
                ],
                "result": "Un catalogue vivant, plus facile \u00e0 parcourir qu'une liste PDF statique.",
                "further": "Demande \u00e0 Copilot d'ajouter des \u00e9tiquettes pour que les "
                          "ressources appartiennent \u00e0 plusieurs cat\u00e9gories.",
            },
            {
                "title": "G\u00e9n\u00e9rer une page de FAQ automatique",
                "persona": "campus", "features": ["chat"],
                "situation": "Tu r\u00e9ponds sans cesse aux m\u00eames questions par e-mail "
                            "et tu veux une FAQ publique \u00e0 la place.",
                "steps": [
                    "Colle tes questions et r\u00e9ponses les plus fr\u00e9quentes dans Copilot Chat.",
                    "Demande une page de FAQ claire avec une barre de recherche.",
                    "Demande \u00e0 Copilot de regrouper les questions par cat\u00e9gories claires.",
                ],
                "result": "Une FAQ en libre-service qui r\u00e9duit les e-mails r\u00e9p\u00e9titifs.",
                "further": "Ajoute un lien de contact « besoin d'aide en plus » en bas de page.",
            },
            {
                "title": "Construire une page des \u00e9v\u00e9nements de campus",
                "persona": "campus", "features": ["chat", "spaces"],
                "situation": "Tu veux une page simple et attrayante listant les prochains \u00e9v\u00e9nements du campus.",
                "steps": [
                    "D\u00e9cris les \u00e9v\u00e9nements et les dates \u00e0 Copilot Chat.",
                    "Colle une capture d'\u00e9cran d'un style de page d'\u00e9v\u00e9nements que tu aimes, pour inspiration.",
                    "Demande que les \u00e9v\u00e9nements se trient automatiquement par date, "
                    "les pass\u00e9s s'effa\u00e7ant progressivement.",
                ],
                "result": "Une page d'\u00e9v\u00e9nements l\u00e9g\u00e8re, facile \u00e0 mettre \u00e0 jour chaque mois.",
                "further": "Demande \u00e0 Copilot d'ajouter un bouton « ajouter \u00e0 mon agenda » pour chaque \u00e9v\u00e9nement.",
            },
        ],
    },
}

# ------------------------------------------------------------------
# CONTENT — Dutch
# ------------------------------------------------------------------
CONTENT["nl"] = {
    "meta": {
        "html_lang": "nl",
        "site_name": "Vibe Coding Copilot",
        "brand_tagline": "Hoger Onderwijs",
        "title_suffix": "Vibe Coding met GitHub Copilot voor het hoger onderwijs",
        "description": "Een gratis training om vibe coding te leren met GitHub Copilot: bouw, "
                       "test en publiceer je eigen digitale tools voor het hoger onderwijs, "
                       "zonder ontwikkelaar te zijn.",
    },
    "nav": {
        "home": "Home",
        "explorer": "Use cases",
        "basics": "Vibe Coding Basis",
        "advanced": "Vibe Coding Gevorderd",
        "expert": "Vibe Coding Expert",
        "best_practices": "Best practices",
        "toolkit": "Toolkit",
        "about": "Over dit project",
        "all_lessons": "Alle lessen",
        "view_route": "Bekijk het volledige traject",
        "exercise_label": "Aan de slag",
    },
    "footer": {
        "text": "Een onafhankelijke, gratis leerbron voor vibe coding in het hoger onderwijs, "
                "aangedreven door GitHub Copilot. Niet verbonden aan of goedgekeurd door "
                "GitHub of Microsoft.",
    },
    "home": {
        "eyebrow": "Gratis training \u00b7 Vibe Coding met GitHub Copilot",
        "h1_line1": "Vibe Coding",
        "h1_line2": "voor het hoger onderwijs",
        "lede": "Je hoeft geen ontwikkelaar te zijn om je eigen digitale tools te maken. Of je "
                "nu lesgeeft, studeert, bij IT werkt, mensen aanstuurt, een dienst leidt of de "
                "begroting beheert: deze gratis training leert je stap voor stap een echte "
                "webapp bouwen met GitHub Copilot. Jij blijft de expert in je eigen vakgebied: "
                "AI helpt je bouwen, en GitHub bewaart, versioneert en publiceert het resultaat.",
        "cta_primary": "Ontdek de use cases",
        "cta_secondary": "Volg het begeleide traject",
        "hero_note": "Gratis. Geen programmeerervaring vereist. Gewoon GitHub Copilot, een "
                     "beetje nieuwsgierigheid en 25 praktische lessen.",
        "personas_title": "Gemaakt voor elk onderdeel van de instelling",
        "personas_sub": "Vibe coding is niet alleen voor ontwikkelaars, of alleen voor "
                        "docenten. Dit is wat het overal op de campus oplevert.",
        "personas": [
            ("\U0001f393", "Docenten", "Bouw het kleine hulpmiddel dat je al jaren voor ogen "
             "hebt: een quiz, een levende cursushandleiding, een nakijkhulp.", "Voorbeeld:",
             "Een docent biologie bouwt in \u00e9\u00e9n namiddag een zelfnakijkende herhalingsquiz."),
            ("\U0001f9d1\u200d\U0001f393", "Studenten", "Je hebt geen informaticadiploma nodig "
             "om je eigen studietools, portfolio of verenigingswebsite te vibe coden.",
             "Voorbeeld:", "Een groep studenten bouwt samen een gedeelde flashcard-app om "
             "samen te herhalen v\u00f3\u00f3r de examens."),
            ("\U0001f5a5\ufe0f", "IT-diensten", "Prototype interne tools in enkele uren in "
             "plaats van maanden, en beheer ze daarna netjes met GitHub Enterprise.",
             "Voorbeeld:", "IT bouwt een zelfbedieningstool voor zaalreservaties en beheert de "
             "toegang centraal via GitHub."),
            ("\U0001f91d", "HR", "Zet een repetitief onboarding- of opleidingsproces om in een "
             "eenvoudige, gebruiksvriendelijke webapp.", "Voorbeeld:", "HR bouwt een "
             "interactieve onboardingchecklist voor nieuwe medewerkers."),
            ("\U0001f9ed", "Directie", "Krijg een echte feedbacktool of dashboard binnen enkele "
             "dagen gebouwd, zonder te wachten op een volledig IT-project.", "Voorbeeld:", "Een "
             "diensthoofd bouwt een live peiling om feedback te verzamelen tijdens een personeelsvergadering."),
            ("\U0001f4b6", "Financi\u00ebn", "Automatiseer een kleine, repetitieve taak: een "
             "budgetcalculator, een onkostenformulier, een eenvoudige tracker.", "Voorbeeld:",
             "Het financeteam bouwt een kleine calculator voor reiskostenvergoeding."),
        ],
        "journey_title": "Van lesidee tot gepubliceerde app",
        "journey_sub": "Elk traject in deze training volgt hetzelfde, heel concrete pad.",
        "journey": [
            ("01", "Idee", "Vertrek van een echt onderwijsprobleem en vertaal het naar een app-idee."),
            ("02", "Bouwen", "Bouw een eerste versie met GitHub Copilot, zonder zelf alle code te schrijven."),
            ("03", "Publiceren", "Bewaar je project op GitHub en publiceer het online voor je studenten."),
            ("04", "Verbeteren", "Test, verfijn en laat je tool groeien op basis van echte feedback."),
        ],
        "courses_title": "Drie trajecten, \u00e9\u00e9n doel: echt vibe coden",
        "courses_sub": "Begin waar je bent: van je eerste app met Copilot tot een volledige "
                       "onderwijstool, gehost op GitHub.",
        "examples_title": "Wat je kunt vibe coden, welk vakgebied je ook hebt",
        "examples_sub": "Concrete idee\u00ebn die je in een paar uur kunt bouwen met GitHub Copilot.",
        "examples": [
            ("Interactieve herhalingsquiz", "Een zelfnakijkende quiz om een hoofdstuk te "
             "herhalen, die je studenten gebruiken voor het examen.", "Docenten"),
            ("Een levende cursuspagina", "Een interactieve cursushandleiding met automatische "
             "FAQ, planning en gecentraliseerde bronnen.", "Docenten"),
            ("Gedeelde flashcard-app", "Kaartjes die omdraaien bij een klik, samen gebouwd door "
             "een groep studenten om te herhalen v\u00f3\u00f3r de examens.", "Studenten"),
            ("Aangepaste puntencalculator", "Een tool die het eindcijfer schat volgens de "
             "eigen puntenverdeling van elk vak.", "Studenten"),
            ("Zaalreservatie in zelfbediening", "Een interne tool om een zaal of labo-slot te "
             "boeken, met live beschikbaarheid en een goedkeuringsstap.", "IT-diensten"),
            ("Interactieve onboardingchecklist", "Een stap-voor-stap checklist die nieuwe "
             "medewerkers begeleidt tijdens hun eerste twee weken.", "HR"),
            ("Live peiling voor een vergadering", "Een snelle peiling die in real time feedback "
             "verzamelt van personeel \u2014 probeer de live demo in les 3!", "Directie"),
            ("Kleine onkostencalculator", "Een lichte tool om terugkerende kosten of reiskosten "
             "te schatten en bij te houden.", "Financi\u00ebn"),
            ("Studentenprojectvitrine", "Een webgalerij waarin elke student zijn of haar "
             "eindproject van het semester presenteert.", "Docenten & studenten"),
        ],
        "teaser_title": "Niet zeker waar te beginnen? Lees eerst de best practices.",
        "teaser_desc": "Een checklist van \u00e9\u00e9n pagina om je eerste vibe-codingproject "
                       "goed te starten, van idee tot publicatie op GitHub.",
        "teaser_cta": "Bekijk de best practices",
    },
    "tracks": {
        "basics": {
            "slug": "vibe-basics",
            "tag_class": "tag-basics",
            "level_label": "Basis",
            "title": "Vibe Coding Basis",
            "subtitle": "Je eerste stappen in vibe coding: verander een lesidee in een echte "
                       "app, met GitHub Copilot.",
            "card_desc": "Ontdek vibe coding, bouw je eerste onderwijs-webapp met Copilot en "
                         "publiceer hem online.",
            "meta": "8 lessen \u00b7 ongeveer 1,5 uur",
            "lessons": [
                {
                    "title": "Wat is vibe coding?",
                    "kicker": "Les 1",
                    "paragraphs": [
                        "Vibe coding betekent een applicatie bouwen door aan een AI te "
                        "beschrijven wat je wilt, in plaats van elke regel code zelf te "
                        "schrijven. Met GitHub Copilot leg je je behoefte uit in gewone taal en "
                        "stelt de AI de code voor; jij blijft aan het stuur: je leest, past aan "
                        "en keurt goed.",
                        "Voor het hoger onderwijs verandert dit alles: je kunt eindelijk het "
                        "kleine hulpmiddel bouwen dat je al jaren voor ogen hebt, zonder te "
                        "wachten op een IT-dienst of zes maanden te leren programmeren. Dit "
                        "traject begeleidt je stap voor stap, met \u00e9\u00e9n echt lesproject als rode draad.",
                    ],
                    "tip": "Je hoeft niets te installeren om dit traject te lezen. Copilot "
                           "installeer je in de volgende les.",
                    "exercise": "Welk vakgebied je ook hebt (onderwijs, studie, IT, HR, "
                                "directie, financi\u00ebn): schrijf in \u00e9\u00e9n zin de "
                                "kleine app die je zou willen hebben. In les 3 bouw je er echt \u00e9\u00e9n.",
                },
                {
                    "title": "Van een onderwijsprobleem naar een app-idee",
                    "kicker": "Les 2",
                    "paragraphs": [
                        "Het beste vertrekpunt is nooit een technologie, maar een echt "
                        "probleem: studenten die geen eenvoudige manier hebben om te herhalen, "
                        "een lesrooster verspreid over tien e-mails, repetitief nakijkwerk. "
                        "Vertrek altijd vanuit die concrete, doorleefde ervaring.",
                        "Beschrijf het probleem in \u00e9\u00e9n zin en bedenk dan de kleinst "
                        "mogelijke app die het zou oplossen. Een quiz, een pagina, een "
                        "rekentool: houd het simpel om te beginnen, je kunt het later altijd uitbreiden.",
                    ],
                    "tip": "Schrijf je idee als: \u201cEen app waarmee [wie] [wat] kan doen, "
                           "zodat [welk voordeel]\u201d.",
                    "exercise": "Kies \u00c9\u00e9N echt probleem waar jij of een collega elke "
                                "week over klaagt \u2014 in de les, aan de helpdesk, bij "
                                "onboarding, in een budgetvergadering \u2014 en schrijf je "
                                "idee met de zin hierboven.",
                },
                {
                    "title": "Je eerste webapp met GitHub Copilot",
                    "kicker": "Les 3",
                    "paragraphs": [
                        "Dit is de les waarin je echt iets bouwt. Installeer de GitHub "
                        "Copilot-extensie in Visual Studio Code (of open Copilot Chat "
                        "rechtstreeks op github.com), meld je aan met je GitHub-account en maak "
                        "een nieuw bestand index.html aan.",
                        "Hieronder bouwen we samen een echt, werkend voorbeeld: een \u201cSnelle "
                        "Peiling\u201d die je kan gebruiken in een les, een opleiding, een "
                        "teamvergadering of een personeelsvergadering. Volg de drie stappen met "
                        "je eigen Copilot, en probeer aan het einde het afgewerkte resultaat live uit.",
                    ],
                    "extra_html": '''
<div class="step-badge">Stap 1 \u2014 Beschrijf het skelet</div>
<p>Open Copilot Chat en beschrijf de kleinst mogelijke versie van je idee. Wees specifiek over wat er op de pagina moet staan.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Bouw een eenvoudige webpagina genaamd "Snelle Peiling" met een vraag en vier knoppen als antwoordopties.</div>
    <div class="chat-bubble-ai">Hier is een startpunt:
      <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Snelle Peiling&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
  &lt;h2&gt;Wat zou jou dit semester het meest helpen?&lt;/h2&gt;
  &lt;button&gt;Uitgewerkte voorbeelden&lt;/button&gt;
  &lt;button&gt;Meer oefeningen&lt;/button&gt;
  &lt;button&gt;Korte video's&lt;/button&gt;
  &lt;button&gt;Live vraag-en-antwoord&lt;/button&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
    </div>
  </div>
</div>
<p>Bewaar dit bestand en open het in je browser door erop te dubbelklikken. Je hebt nu een echte, weliswaar eenvoudige, webpagina.</p>

<div class="step-badge">Stap 2 \u2014 Vraag om de logica</div>
<p>Een pagina met knoppen die niets doen is nog niet erg nuttig. Vraag Copilot om de knoppen stemmen te laten tellen.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Sla, wanneer iemand op een knop klikt, een stemteller voor die optie op in de browser (localStorage), zodat die onthouden wordt als de pagina herlaadt.</div>
    <div class="chat-bubble-ai">Ik heb dit script onderaan je pagina toegevoegd:
      <pre><code>&lt;script&gt;
  document.querySelectorAll("button").forEach((btn, i) =&gt; {
    btn.addEventListener("click", () =&gt; {
      let votes = JSON.parse(localStorage.getItem("votes")) || [0,0,0,0];
      votes[i]++;
      localStorage.setItem("votes", JSON.stringify(votes));
      alert("Bedankt voor je stem!");
    });
  });
&lt;/script&gt;</code></pre>
    </div>
  </div>
</div>
<p>Test het: klik op een knop, herlaad de pagina, klik opnieuw \u2014 de teller blijft groeien, ook al zie je dat nog niet. Dat komt hierna.</p>

<div class="step-badge">Stap 3 \u2014 Toon de resultaten</div>
<p>Vraag Copilot nu om die simpele <code>alert()</code> te vervangen door iets dat mensen echt kunnen zien.</p>
<div class="chat-mockup">
  <div class="chat-head">Copilot Chat</div>
  <div class="chat-body">
    <div class="chat-bubble-user">Verberg in plaats van een alert de knoppen na het stemmen en toon elke optie als een percentagebalk op basis van de stemmen tot nu toe.</div>
    <div class="chat-bubble-ai">Goed idee, dat is veel duidelijker voor wie stemt. Ik heb de alert vervangen door een kleine resultatenweergave die het aandeel van elke optie berekent op basis van het totaal aantal stemmen en er een balk voor animeert. Wil je ook een "opnieuw stemmen"-link zodat je deze demo kunt resetten?</div>
  </div>
</div>
<p>Ga zo door \u2014 \u00e9\u00e9n kleine vraag tegelijk \u2014 tot de pagina er precies zo uitziet en aanvoelt als jij wilt.</p>

<div class="step-badge">Stap 4 \u2014 Probeer wat je net gebouwd hebt</div>
<p>Dit is precies de hierboven beschreven app, al gebouwd en hieronder live. Klik op een optie en bekijk hoe de resultaten verschijnen: dit is wat je studenten, collega's of team zullen zien zodra jouw versie gepubliceerd is (volgende les).</p>
<div class="demo-frame-wrap">
  <div class="demo-frame-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">snelle-peiling.html</span></div>
  <iframe src="../assets/demo/quick-poll-nl.html" loading="lazy" title="Snelle Peiling live demo"></iframe>
</div>
''',
                    "tip": "Begin altijd met een minuscule werkende versie voordat je functies "
                           "toevoegt: stap 1 hierboven is al een complete, werkende pagina op zich.",
                    "exercise": "Bouw deze exacte Snelle Peiling zelf opnieuw in een nieuw "
                                "bestand index.html, en pas dan de vraag en de vier opties aan "
                                "je eigen context aan: een lesonderwerp, een onboardingvraag, "
                                "een budgetprioriteit, iets echts voor jou.",
                },
                {
                    "title": "Bewaren en publiceren met GitHub",
                    "kicker": "Les 4",
                    "paragraphs": [
                        "Zodra je eerste versie werkt, maak je een repository aan op GitHub en "
                        "stuur je je code ernaartoe: dat heet een commit. Vanaf dat moment is je "
                        "werk online opgeslagen, geversioneerd, en kun je altijd terug naar een "
                        "vorige versie als er iets misgaat.",
                        "Zet daarna GitHub Pages aan voor die repository: in een paar klikken "
                        "wordt je app bereikbaar via een simpele link, die je kunt delen met "
                        "studenten of collega's, zonder een server te beheren.",
                    ],
                    "tip": "Een GitHub-repository is ook je back-up: zelfs als je computer "
                           "crasht, is je project veilig.",
                    "exercise": "Maak een gratis GitHub-account aan als je er nog geen hebt, "
                                "push je Snelle Peiling naar een gloednieuwe repository, en zet "
                                "er GitHub Pages voor aan.",
                },
                {
                    "title": "Testen en verbeteren met Copilot Chat",
                    "kicker": "Les 5",
                    "paragraphs": [
                        "Laat een of twee collega's je app uitproberen, of test het zelf door je "
                        "in de plaats van een student te stellen. Noteer elke bug of onhandigheid "
                        "en beschrijf ze een voor een aan Copilot Chat: \u201cals ik op deze knop "
                        "klik, gebeurt er niets, los dit op\u201d.",
                        "Copilot kan ook bestaande code uitleggen die je nog niet volledig "
                        "begrijpt: vraag \u201cleg dit deel aan me uit\u201d voordat je om een wijziging vraagt.",
                    ],
                    "tip": "\u00c9\u00e9n aanpassing tegelijk: makkelijker te controleren of het "
                           "werkt, en makkelijker terug te draaien indien nodig.",
                    "exercise": "Stuur je gepubliceerde link naar twee collega's (of "
                                "medestudenten) en vraag hen overal doorheen te klikken. Noteer "
                                "elke onhandigheid die ze tegenkomen, en los de eerste op met "
                                "Copilot Chat.",
                },
                {
                    "title": "Stijl en uitstraling verbeteren",
                    "kicker": "Les 6",
                    "paragraphs": [
                        "Zodra je app werkt, vraag je Copilot om ze aan te kleden: de kleuren "
                        "van je instelling, een leesbaarder lettertype, een duidelijkere lay-out "
                        "voor je studenten. Je kunt zelfs een screenshot van een stijl die je "
                        "mooi vindt plakken en vragen om zich daarop te bas\u00e9ren.",
                        "Denk ook aan toegankelijkheid: voldoende contrast, leesbare tekst, "
                        "groot genoege knoppen. Vraag Copilot gewoon om de toegankelijkheid van "
                        "je pagina te controleren, het weet wat er te verbeteren valt.",
                    ],
                    "tip": None,
                    "exercise": "Vraag Copilot om je Snelle Peiling opnieuw te stylen met twee "
                                "kleuren van je instelling of team, en bekijk het resultaat ook "
                                "op je telefoon.",
                },
                {
                    "title": "Afbeeldingen, bestanden en documenten toevoegen",
                    "kicker": "Les 7",
                    "paragraphs": [
                        "Veel lestools hebben afbeeldingen, pdf's of downloadbare documenten "
                        "nodig: een cursusnota, een schema, een formulier. Vraag Copilot om een "
                        "afbeeldingsweergave of een downloadknop toe te voegen, en zet het "
                        "bestand vervolgens gewoon in je GitHub-repository.",
                        "GitHub host zowel je code als deze bestanden: geen ander hulpmiddel "
                        "nodig om de bronnen van je app op te slaan.",
                    ],
                    "tip": None,
                    "exercise": "Voeg een afbeelding of downloadbare pdf toe aan je Snelle "
                                "Peiling (zelfs een placeholder), commit het, en controleer of "
                                "het correct laadt op de gepubliceerde pagina.",
                },
                {
                    "title": "Samenvatting en op naar het traject Gevorderd",
                    "kicker": "Les 8",
                    "paragraphs": [
                        "Je weet nu hoe je een lesidee omzet in een echte app: bouwen met "
                        "Copilot, bewaren en publiceren met GitHub, testen, stijl verbeteren, "
                        "bestanden toevoegen. De belangrijkste gewoonte: ga altijd vooruit in "
                        "kleine, controleerbare stapjes.",
                        "Het traject Gevorderd pakt hier de draad op om verder te gaan: een "
                        "echte database koppelen, je project een blijvend geheugen geven, en je "
                        "code beheren met GitHub als een echt project dat standhoudt.",
                    ],
                    "tip": None,
                    "exercise": "Schrijf een README van drie regels voor je project: wat het "
                                "doet, voor wie, en hoe je het de volgende keer opnieuw opent met Copilot.",
                },
            ],
        },
        "advanced": {
            "slug": "vibe-advanced",
            "tag_class": "tag-advanced",
            "level_label": "Gevorderd",
            "title": "Vibe Coding Gevorderd",
            "subtitle": "Koppel een database, geef je project geheugen en beheer je code als "
                       "een project dat standhoudt, met GitHub.",
            "card_desc": "Database, onderwijskundig ontwerp, projectgeheugen en codebeheer met "
                         "GitHub: alles om een echte tool te bouwen die standhoudt.",
            "meta": "9 lessen \u00b7 ongeveer 2 uur",
            "lessons": [
                {
                    "title": "Werken met de agent-modus van Copilot",
                    "kicker": "Les 1",
                    "paragraphs": [
                        "Naast suggesties regel voor regel biedt Copilot een agent-modus: je "
                        "beschrijft een grotere taak (\u201cvoeg een inschrijfformulier toe aan "
                        "mijn quiz en controleer of het werkt\u201d), en Copilot plant "
                        "meerdere wijzigingen, voert ze uit en controleert het resultaat, met "
                        "controlepunten die jij goedkeurt.",
                        "Dit is het ideale hulpmiddel zodra je app groeit en je niet langer elke "
                        "kleine regel apart wilt beschrijven.",
                    ],
                    "tip": "Bekijk altijd eerst het voorgestelde plan voordat je de agent laat "
                           "werken: dat is het beste moment om bij te sturen.",
                    "exercise": "Beschrijf een taak in meerdere stappen aan Copilots agent-modus "
                                "(bijvoorbeeld een resultatenpagina toevoegen aan je Snelle "
                                "Peiling) en bekijk zijn plan zorgvuldig voordat je het laat uitvoeren.",
                },
                {
                    "title": "Een database koppelen aan je app",
                    "kicker": "Les 2",
                    "paragraphs": [
                        "Zodra je tool informatie moet onthouden van de ene sessie naar de "
                        "andere (quizantwoorden, inschrijvingen, cijfers), heb je een database "
                        "nodig. Diensten zoals Supabase laten je er gratis \u00e9\u00e9n "
                        "aanmaken, zonder serverconfiguratie, en Copilot helpt je de "
                        "verbindingscode te schrijven.",
                        "Beschrijf aan Copilot wat je wilt opslaan (bijvoorbeeld: de naam van "
                        "de student en zijn of haar score), en laat het de databasestructuur en "
                        "de nodige code voorstellen om erin te lezen en te schrijven.",
                    ],
                    "tip": None,
                    "exercise": "Maak een gratis Supabase-project en koppel het aan een kleine "
                                "testpagina die \u00e9\u00e9n stukje informatie opslaat, zoals "
                                "een naam en een stem.",
                },
                {
                    "title": "Die database veilig gebruiken",
                    "kicker": "Les 3",
                    "paragraphs": [
                        "Een slecht beveiligde database kan de gegevens van je studenten "
                        "blootleggen. Vraag Copilot systematisch om beveiligingsregels toe te "
                        "voegen (wie mag wat lezen of schrijven), en sla nooit meer persoonlijke "
                        "gegevens op dan nodig.",
                        "Denk vanaf nu al aan de bescherming van je studentgegevens (AVG in "
                        "Europa): anonimiseer wat kan, en leg duidelijk uit waarvoor de "
                        "gegevens die je verzamelt dienen.",
                    ],
                    "tip": "Bij twijfel, vraag Copilot: \u201cvolgt deze code goede praktijken "
                           "voor gegevensbescherming?\u201d",
                    "exercise": "Vraag Copilot om je databasecode te controleren op "
                                "veiligheidsproblemen, en los minstens \u00e9\u00e9n gesignaleerd punt op.",
                },
                {
                    "title": "Bewust ontwerpen voor leren",
                    "kicker": "Les 4",
                    "paragraphs": [
                        "Een goede onderwijstool is niet alleen functioneel, hij is ontworpen "
                        "voor leren: onmiddellijke feedback na een antwoord, zichtbare "
                        "vooruitgang, aanmoediging in plaats van straf. Beschrijf deze "
                        "onderwijskundige intenties aan Copilot, niet alleen technische functies.",
                        "Vraag bijvoorbeeld niet \u201ctoon de score\u201d, maar \u201ctoon de "
                        "score met een uitleg bij elke fout, zodat de student begrijpt waarom "
                        "hij of zij het fout had\u201d.",
                    ],
                    "tip": None,
                    "exercise": "Herschrijf \u00e9\u00e9n functieverzoek voor je project als een "
                                "leer- of gebruikersgerichte prompt, volgens het voorbeeld "
                                "hierboven, in plaats van een zuiver technische vraag.",
                },
                {
                    "title": "Een goed bouwplan maken",
                    "kicker": "Les 5",
                    "paragraphs": [
                        "Voordat je Copilot om een grote functie vraagt, schrijf je zelf een "
                        "kort plan in een paar regels: de stappen, de logische volgorde, wat "
                        "essentieel is en wat kan wachten. Een goed plan levert veel betere "
                        "suggesties op dan een vage vraag.",
                        "Deel dit plan vervolgens met Copilot Chat voordat je begint te coderen: "
                        "het kan ontbrekende stappen of een logischere volgorde signaleren.",
                    ],
                    "tip": None,
                    "exercise": "Schrijf een bouwplan van vijf regels voor je volgende functie "
                                "voordat je Copilot om code vraagt, en deel het eerst met Copilot Chat.",
                },
                {
                    "title": "Slim itereren zonder je app te breken",
                    "kicker": "Les 6",
                    "paragraphs": [
                        "Hoe groter je project wordt, hoe verleidelijker het is om meerdere "
                        "wijzigingen tegelijk te vragen. Weersta die verleiding: \u00e9\u00e9n "
                        "wijziging, \u00e9\u00e9n test, \u00e9\u00e9n commit op GitHub. Als er "
                        "iets breekt, weet je precies wat je moet terugdraaien.",
                        "GitHub laat je heel eenvoudig terugkeren dankzij de commitgeschiedenis: "
                        "dat is je vangnet om zonder stress te blijven itereren.",
                    ],
                    "tip": None,
                    "exercise": "Doe vandaag drie kleine, aparte commits, elk met \u00e9\u00e9n "
                                "duidelijke wijziging en \u00e9\u00e9n duidelijk commitbericht.",
                },
                {
                    "title": "Je project een blijvend geheugen geven",
                    "kicker": "Les 7",
                    "paragraphs": [
                        "Zonder specifieke instructies onthoudt Copilot je voorkeuren niet "
                        "noodzakelijk van de ene dag op de andere. Maak een bestand "
                        "copilot-instructions.md aan in een map .github/ van je repository: "
                        "beschrijf je gewenste codeerstijl, je huisstijl, of regels zoals "
                        "\u201caltijd commentaar in het Nederlands schrijven\u201d.",
                        "Dit bestand wordt het blijvende geheugen van je project: elke "
                        "toekomstige suggestie van Copilot houdt er rekening mee, zelfs in een gloednieuwe sessie.",
                    ],
                    "tip": "Bekijk en vul dit bestand aan naarmate het project groeit: het is "
                           "een investering van vijf minuten die elke volgende sessie verbetert.",
                    "exercise": "Maak je eerste copilot-instructions.md-bestand met minstens "
                                "drie regels specifiek voor jouw project.",
                },
                {
                    "title": "AI gebruiken als tester",
                    "kicker": "Les 8",
                    "paragraphs": [
                        "Voordat je je app aan echte studenten laat zien, vraag je Copilot Chat "
                        "om een onhandige of afgeleide gebruiker te spelen: \u201cprobeer dit "
                        "formulier te laten crashen\u201d, \u201cwat gebeurt er als ik dit veld "
                        "leeg laat?\u201d.",
                        "Vraag het ook om testgevallen te genereren: voorbeelden van correcte, "
                        "onjuiste of volledig onverwachte antwoorden op je quiz of formulier.",
                    ],
                    "tip": None,
                    "exercise": "Vraag Copilot Chat om je app op drie verschillende manieren te "
                                "proberen breken, en los daarna op wat het vindt.",
                },
                {
                    "title": "Je code beheren als een echt project met GitHub",
                    "kicker": "Les 9",
                    "paragraphs": [
                        "Een project dat standhoudt heeft echte organisatie nodig: duidelijke, "
                        "regelmatige commits, branches om een idee uit te proberen zonder de "
                        "werkende versie te breken, en eventueel GitHub Enterprise of GitHub "
                        "Education als je instelling deze projecten centraal wil hosten en "
                        "beheren voor meerdere docenten.",
                        "Dit is ook wat samenwerking mogelijk maakt: een collega kan wijzigingen "
                        "voorstellen via een pull request, die jij bekijkt voordat je ze "
                        "accepteert, precies zoals een ontwikkelteam dat zou doen.",
                    ],
                    "tip": None,
                    "exercise": "Maak een branch aan, doe er een kleine wijziging op, en open "
                                "je eerste pull request om die terug te voegen in je hoofdversie.",
                },
            ],
        },
        "expert": {
            "slug": "vibe-expert",
            "tag_class": "tag-expert",
            "level_label": "Expert",
            "title": "Vibe Coding Expert",
            "subtitle": "Voeg kunstmatige intelligentie toe aan je app en bouw een volledig "
                       "voorbeeld, klaar voor een echt vak.",
            "card_desc": "Ga verder: voeg AI toe aan je app, kies het juiste model, houd de "
                         "kosten onder controle en sluit af met een volledig voorbeeld.",
            "meta": "8 lessen \u00b7 ongeveer 1,5 uur",
            "lessons": [
                {
                    "title": "AI toevoegen aan je onderwijsapp",
                    "kicker": "Les 1",
                    "paragraphs": [
                        "Tot nu toe heeft Copilot je geholpen de code van je app te schrijven. "
                        "Deze les gaat verder: een AI-functie toevoegen die je studenten "
                        "rechtstreeks kunnen gebruiken, zoals een \u201cleg dit anders uit\u201d "
                        "-knop die live een AI-model raadpleegt.",
                        "Vraag Copilot om je te helpen deze integratie te bouwen: een knop die "
                        "een vraag naar een AI-model stuurt en het antwoord op je pagina toont.",
                    ],
                    "tip": None,
                    "exercise": "Voeg \u00e9\u00e9n AI-gestuurde knop toe aan een bestaand "
                                "project, al is het maar een placeholder die de vraag gewoon "
                                "teruggeeft, om het hele circuit te zien werken.",
                },
                {
                    "title": "AI-modellen kiezen en vergelijken",
                    "kicker": "Les 2",
                    "paragraphs": [
                        "Er bestaan meerdere families AI-modellen (GPT, Claude, Gemini, onder "
                        "andere), met verschillen in kwaliteit, snelheid en kosten. In Copilot "
                        "Chat kun je trouwens al kiezen tussen meerdere modellen, afhankelijk van de taak.",
                        "Begin voor de AI in je onderwijsapp eenvoudig met een goedkoop model, "
                        "en stap pas over naar een krachtiger model als je dat echt nodig hebt.",
                    ],
                    "tip": None,
                    "exercise": "Stel dezelfde vraag aan twee verschillende modellen in Copilot "
                                "Chat en vergelijk de antwoorden op kwaliteit, toon en snelheid.",
                },
                {
                    "title": "Je toegangssleutels veilig instellen",
                    "kicker": "Les 3",
                    "paragraphs": [
                        "Om een AI-model in je app te gebruiken, heb je een toegangssleutel "
                        "(API key) nodig: een soort wachtwoord voor die dienst. Zet deze sleutel "
                        "nooit rechtstreeks in code die zichtbaar is op GitHub.",
                        "Vraag Copilot om je te helpen ze op te slaan als een beschermd geheim "
                        "(omgevingsvariabele of GitHub-secret): de IT-dienst van je instelling "
                        "kan je hierbij helpen indien nodig.",
                    ],
                    "tip": "Een per ongeluk blootgestelde sleutel kan door anderen worden "
                           "gebruikt: gebeurt dit toch, genereer ze dan onmiddellijk opnieuw.",
                    "exercise": "Sla \u00e9\u00e9n API-sleutel op als beschermd geheim in plaats "
                                "van rechtstreeks in je code, en controleer of je code nog werkt "
                                "als hij ze vandaar leest.",
                },
                {
                    "title": "Eerste klein project: een AI-uitlegknop",
                    "kicker": "Les 4",
                    "paragraphs": [
                        "Bouw een concreet voorbeeld: op je cursuspagina een knop \u201cik "
                        "begrijp het niet\u201d die de vraag van de student naar een AI-model "
                        "stuurt en een andere uitleg toont, eenvoudiger of met een ander voorbeeld.",
                        "Vraag Copilot om deze functie stap voor stap te bouwen, waarbij je elk "
                        "onderdeel test voordat je verdergaat.",
                    ],
                    "tip": None,
                    "exercise": "Bouw de knop \u201cik begrijp het niet\u201d helemaal af op een "
                                "echte pagina van jezelf \u2014 je Snelle Peiling of een ander project.",
                },
                {
                    "title": "Je AI-integratie veilig implementeren",
                    "kicker": "Les 5",
                    "paragraphs": [
                        "Een AI-integratie mag nooit je toegangssleutel blootleggen in de "
                        "browser van de student. Vraag Copilot om een kleine "
                        "server-side-functie op te zetten die de vraag ontvangt, het AI-model "
                        "aanroept met de verborgen sleutel, en enkel het antwoord teruggeeft.",
                        "Platformen zoals Vercel of Netlify laten je dit soort functie gratis "
                        "hosten voor een klein project, in een paar klikken rechtstreeks vanuit "
                        "je GitHub-repository.",
                    ],
                    "tip": None,
                    "exercise": "Implementeer je AI-functie via een kleine serverless functie, "
                                "en controleer in het netwerktabblad van je browser dat de "
                                "sleutel er nooit verschijnt.",
                },
                {
                    "title": "Veilig en betaalbaar bouwen",
                    "kicker": "Les 6",
                    "paragraphs": [
                        "Een AI-model kost geld bij elke gestelde vraag. Stel voor onderwijsgebruik "
                        "met een groep studenten een duidelijke limiet in (bijvoorbeeld een "
                        "aantal vragen per dag) om onaangename verrassingen te vermijden.",
                        "Vraag Copilot om deze limiet rechtstreeks in de code toe te voegen, en "
                        "controleer regelmatig het gebruik via het dashboard van de AI-dienst die je gebruikt.",
                    ],
                    "tip": None,
                    "exercise": "Voeg een dagelijkse gebruikslimiet toe aan je AI-functie en "
                                "test wat er gebeurt zodra die limiet bereikt is.",
                },
                {
                    "title": "Verder dan tekst gaan",
                    "kicker": "Les 7",
                    "paragraphs": [
                        "AI beperkt zich niet tot tekst: sommige modellen kunnen een "
                        "afbeelding beschrijven, een audio-opname transcriberen, of zelfs een "
                        "afbeelding genereren op basis van een beschrijving. Voor een vak "
                        "opent dit mogelijkheden zoals een met de hand getekend schema "
                        "nakijken of een mondelinge presentatie transcriberen.",
                        "Deze functies vragen wat meer voorbereiding, maar de methode blijft "
                        "dezelfde: beschrijf precies aan Copilot wat je wilt, test, pas aan.",
                    ],
                    "tip": None,
                    "exercise": "Vraag een AI-model om \u00e9\u00e9n afbeelding of opname die "
                                "relevant is voor jouw eigen vakgebied te beschrijven of samen te vatten.",
                },
                {
                    "title": "Volledig voorbeeld en afsluiting",
                    "kicker": "Les 8",
                    "paragraphs": [
                        "Om dit traject af te sluiten, hier een volledig voorbeeld dat je "
                        "helemaal zelf kunt bouwen: een interactieve quiz met automatische "
                        "verbetering, scores opgeslagen in een database, en een AI-uitlegknop "
                        "voor elke gemiste vraag, alles online gepubliceerd via GitHub.",
                        "Je hebt nu alle hulpmiddelen om je eigen onderwijsapps te bouwen, te "
                        "testen, te publiceren en te laten groeien. De enige echte grens is nu "
                        "de tijd die je eraan wilt besteden: bedankt om dit traject te volgen, "
                        "en veel plezier met vibe coden!",
                    ],
                    "tip": None,
                    "exercise": "Schrijf op wat je hierna gaat bouwen met alles wat je in deze "
                                "training hebt geleerd \u2014 en ga het dan ook echt bouwen.",
                },
            ],
        },
    },
    "best_practices": {
        "title": "Best practices",
        "sub": "Een checklist van \u00e9\u00e9n pagina om je vibe-codingproject goed te "
               "starten, van idee tot publicatie op GitHub.",
        "items": [
            ("Vertrek altijd van een echt lesprobleem", "Het beste app-idee komt uit een "
             "concrete frustratie die je in de klas ervaart, niet uit een trendy technologie."),
            ("Begin minuscuul", "\u00c9\u00e9n functie die werkt is beter dan een ambitieus "
             "plan dat nooit af raakt. Breid daarna stap voor stap uit."),
            ("\u00c9\u00e9n wijziging, \u00e9\u00e9n test, \u00e9\u00e9n commit", "Vraag nooit "
             "tien wijzigingen tegelijk: je zou niet meer weten welke wijziging wat heeft gebroken."),
            ("Bewaar alles op GitHub vanaf dag \u00e9\u00e9n", "Zelfs een minuscuul project "
             "verdient een GitHub-repository: het is je back-up en je versiegeschiedenis."),
            ("Sla nooit zomaar gevoelige gegevens op", "Vraag Copilot altijd of je code goede "
             "praktijken voor gegevensbescherming volgt voordat je informatie over je "
             "studenten verzamelt."),
            ("Bescherm je toegangssleutels", "Een API-sleutel mag nooit verschijnen in code die "
             "zichtbaar is op GitHub: gebruik altijd een beschermd geheim."),
            ("Bekijk elke suggestie voordat je ze accepteert", "Copilot stelt voor, jij "
             "beslist: begrijp wat de code doet voordat je ze met echte studenten gebruikt."),
            ("Geef je project een geheugen", "Een bestand copilot-instructions.md bespaart "
             "kostbare tijd in elke nieuwe werksessie."),
            ("Laat een echte collega of student testen", "Een blik van buitenaf vindt altijd "
             "onhandigheden die je zelf nooit zou opmerken."),
            ("Documenteer je project in \u00e9\u00e9n pagina", "Een korte README legt aan een "
             "collega (of aan jezelf over zes maanden) uit wat het project doet en hoe je het opnieuw opstart."),
        ],
    },
    "about": {
        "title": "Over dit traject",
        "paragraphs": [
            "Vibe Coding Copilot is een onafhankelijke, gratis leerbron voor iedereen die "
            "werkt of studeert in het hoger onderwijs: docenten, studenten, IT- en digitale "
            "diensten, HR, directie, financi\u00ebn en administratie, die hun eigen digitale "
            "tools willen bouwen zonder ontwikkelaar te zijn.",
            "Deze site is niet verbonden aan, goedgekeurd door of gesponsord door GitHub of "
            "Microsoft. Alle vermelde productnamen en merken zijn eigendom van hun "
            "respectievelijke eigenaren; deze site legt alleen uit hoe je ze goed gebruikt in "
            "een institutionele context.",
        ],
        "sections": [
            ("Waarom dit traject bestaat", [
                "Veel uitstekende idee\u00ebn, in een klaslokaal, aan een helpdesk, bij HR of "
                "in een financeteam, blijven vastzitten door een gebrek aan "
                "programmeervaardigheden of budget voor maatwerk. Vibe coding, met tools zoals "
                "GitHub Copilot, verandert die vergelijking: je wordt in staat om het zelf te "
                "bouwen, terwijl je de controle over je eigen vakgebied behoudt.",
            ]),
            ("Waarom specifiek GitHub", [
                "Een app bouwen met AI is maar de helft van de weg: je moet hem nog bewaren, "
                "laten groeien zonder hem te breken, en ergens publiceren. GitHub (en GitHub "
                "Enterprise of GitHub Education voor instellingen) beantwoordt precies aan die "
                "behoefte, en integreert native met GitHub Copilot.",
            ]),
            ("Feedback", [
                "Dit traject is een levend document. Mis je een voorbeeld, een les of een "
                "uitleg, behandel het dan zoals elk ander lesmateriaal: stel een verbetering voor.",
            ]),
        ],
    },
    "toolkit": {
        "title": "Toolkit \u2014 promptbibliotheek",
        "sub": "Kant-en-klare Copilot-prompts, gegroepeerd per vakgebied. Kopieer er \u00e9\u00e9n, "
               "pas de details tussen haakjes aan, en plak hem in Copilot Chat.",
        "groups": [
            ("\U0001f393", "Docenten", [
                "Bouw een zelfnakijkende quiz over [onderwerp] met 5 meerkeuzevragen en "
                "directe feedback.",
                "Voeg een knop toe waarmee studenten hun quizresultaten als pdf kunnen downloaden.",
                "Zet de collegenota's die ik hieronder plak om in een gestructureerde, "
                "afdrukbare samenvatting.",
            ]),
            ("\U0001f9d1\u200d\U0001f393", "Studenten", [
                "Bouw een flashcard-app voor [vak] waarbij kaartjes omdraaien bij een klik en "
                "gemarkeerd kunnen worden als \u201cgekend\u201d.",
                "Voeg een afteltimer toe aan mijn studiepagina die elke 25 minuten opnieuw start.",
                "Maak een eenvoudige portfoliopagina met mijn drie beste projecten, met links "
                "en screenshots.",
            ]),
            ("\U0001f5a5\ufe0f", "IT-diensten", [
                "Bouw een eenvoudige interne tool waarmee personeel een zaal kan reserveren en "
                "de beschikbaarheid live kan zien.",
                "Voeg een controle toe zodat alleen e-mailadressen van [domein] dit formulier "
                "kunnen indienen.",
                "Genereer een GitHub Actions-workflow die deze site bij elke push naar GitHub "
                "Pages deployt.",
            ]),
            ("\U0001f91d", "HR", [
                "Bouw een interactieve onboardingchecklist met voortgangstracking voor nieuwe medewerkers.",
                "Maak een feedbackformulier voor een opleiding met een score van 1 tot 5 en "
                "een opmerkingenveld.",
                "Voeg een pagina toe die berekent hoeveel vakantiedagen er nog over zijn op "
                "basis van een startdatum die ik invoer.",
            ]),
            ("\U0001f9ed", "Directie", [
                "Bouw een live peilingpagina waar personeel op \u00e9\u00e9n vraag kan stemmen "
                "en de resultaten meteen ziet bijwerken.",
                "Maak een eenvoudig dashboard dat de drie cijfers samenvat die ik als KPI's zal plakken.",
                "Zet deze puntsgewijze strategische samenvatting om in een overzichtelijke, "
                "visuele pagina.",
            ]),
            ("\U0001f4b6", "Financi\u00ebn", [
                "Bouw een kleine calculator die de vergoeding voor reiskosten schat op basis "
                "van afstand en tarief.",
                "Maak een eenvoudig formulier om terugkerende kosten bij te houden met een "
                "lopend totaal.",
                "Genereer een sorteerbare tabel op basis van de gegevens die ik hieronder plak.",
            ]),
        ],
    },
    "explorer": {
        "title": "GitHub Copilot use-case explorer",
        "sub": "26 concrete, direct bruikbare use cases voor elk onderdeel van het hoger "
               "onderwijs. Filter op functie of op Copilot-feature, en open een kaart voor de exacte stappen.",
        "search_placeholder": "Zoek een use case (\u201cquiz\u201d, \u201cbudget\u201d, \u201cchat\u201d...)",
        "persona_filter_label": "Functie",
        "feature_filter_label": "Copilot-feature",
        "all_label": "Alle functies",
        "show_steps": "Toon de stappen",
        "hide_steps": "Verberg de stappen",
        "result_label": "Resultaat:",
        "further_label": "Ga verder:",
        "count_prefix": "Weergave van",
        "count_suffix": "use cases",
        "empty_message": "Geen enkele use case past nog bij deze filters \u2014 probeer een "
                         "filter te verwijderen of het zoekveld te wissen.",
        "personas": [
            ("teaching", "\U0001f393", "Docenten"),
            ("students", "\U0001f9d1\u200d\U0001f393", "Studenten"),
            ("it", "\U0001f5a5\ufe0f", "IT- en digitale diensten"),
            ("hr", "\U0001f91d", "HR"),
            ("leadership", "\U0001f9ed", "Directie en beleid"),
            ("finance", "\U0001f4b6", "Financi\u00ebn en administratie"),
            ("research", "\U0001f52c", "Onderzoekers"),
            ("campus", "\U0001f4da", "Bibliotheek, communicatie & campusleven"),
        ],
        "features": [
            ("inline", "Inline-aanvullingen", "Copilot stelt code voor terwijl je typt, "
             "precies waar je werkt."),
            ("chat", "Copilot Chat", "Stel vragen, vraag wijzigingen, of laat code uitleggen in gewone taal."),
            ("agent", "Agent-modus", "Beschrijf een grotere taak; Copilot plant en voert "
             "meteen meerdere wijzigingen door."),
            ("cli", "Copilot in de CLI", "Beschrijf wat je wilt in je terminal; Copilot stelt "
             "het exacte commando voor."),
            ("review", "Copilot code review", "Copilot geeft AI-reviewsuggesties en "
             "aandachtspunten v\u00f3\u00f3r of tijdens menselijke review."),
            ("cloudagent", "Copilot cloud agent", "Wijs een issue of taak toe aan Copilot; "
             "die werkt op een branch en opent daarna een pull request."),
            ("spaces", "Copilot Spaces", "Veranker Copilot met deelbare context zoals "
             "bestanden, notities, transcripties en afbeeldingen."),
            ("mcp", "Extensies & MCP", "Verbind Copilot met je eigen tools en gegevensbronnen."),
        ],
        "usecases": [
            {
                "title": "Bouw in \u00e9\u00e9n sessie een zelfnakijkende quiz",
                "persona": "teaching", "features": ["chat", "inline"],
                "situation": "Je wilt een quiz die je studenten kunnen gebruiken om een "
                            "hoofdstuk te herhalen, zonder een externe betaalde tool.",
                "steps": [
                    "Open Copilot Chat en beschrijf je quiz: \u201cBouw een HTML-pagina met "
                    "een quiz van 5 meerkeuzevragen over [onderwerp], met een eindscore.\u201d",
                    "Lees de gegenereerde code, test ze in je browser, en vraag daarna "
                    "telkens \u00e9\u00e9n precieze aanpassing, bijvoorbeeld: \u201cVoeg een "
                    "korte uitleg toe onder elke vraag zodra ze beantwoord is.\u201d",
                    "Zodra het resultaat je bevalt, vraag je Copilot om een knop \u201cquiz "
                    "herstarten\u201d toe te voegen.",
                ],
                "result": "Een werkende, aangepaste quiz voor je vak, klaar om te publiceren.",
                "further": "Vraag Copilot om de vraagvolgorde bij elke start te schudden.",
            },
            {
                "title": "Zet een met de hand getekend schema om in een digitale versie met Copilot Spaces",
                "persona": "teaching", "features": ["spaces", "chat"],
                "situation": "Je hebt een foto of screenshot van een schema of een "
                            "handgeschreven oefening die je wilt digitaliseren.",
                "steps": [
                    "Plak de screenshot rechtstreeks in Copilot Chat.",
                    "Vraag: \u201cBeschrijf dit schema en zet het om in HTML/CSS dat de "
                    "structuur ervan weergeeft.\u201d",
                    "Verfijn kleuren en labels met opeenvolgende vragen.",
                ],
                "result": "Een digitaal, aanpasbaar schema gebouwd vanuit een eenvoudige foto.",
                "further": "Gebruik dezelfde methode om een handgeschreven correctiemodel te digitaliseren.",
            },
            {
                "title": "Genereer varianten van oefeningen om overschrijven te beperken",
                "persona": "teaching", "features": ["chat"],
                "situation": "Je wilt meerdere versies van dezelfde oefening voor "
                            "verschillende groepen studenten.",
                "steps": [
                    "Geef Copilot Chat een bestaande oefening en vraag: \u201cGenereer 4 "
                    "varianten van deze oefening met andere waarden maar dezelfde "
                    "moeilijkheidsgraad.\u201d",
                    "Vraag om een gedeeld correctiemodel: \u201cVoeg een correctiemodel toe "
                    "dat elke stap uitlegt.\u201d",
                    "Vraag Copilot om alles te exporteren naar \u00e9\u00e9n gestructureerd document.",
                ],
                "result": "Meerdere klaar-om-te-verspreiden versies, met een consistent correctiemodel.",
                "further": "Vraag Copilot om ook een toegankelijke versie te genereren voor schermlezers.",
            },
            {
                "title": "Automatiseer een gewogen-gemiddelde calculator met de agent-modus",
                "persona": "teaching", "features": ["agent", "chat"],
                "situation": "Je beheert een complex puntenoverzicht en wilt automatisch "
                            "gewogen gemiddelden berekenen.",
                "steps": [
                    "Beschrijf je puntensysteem aan de agent-modus: \u201cBouw een pagina die "
                    "een gewogen gemiddelde berekent op basis van deze categorie\u00ebn: [lijst].\u201d",
                    "Bekijk het voorgestelde plan van de agent voordat je het goedkeurt.",
                    "Vraag om een CSV-export toe te voegen om resultaten met collega's te delen.",
                ],
                "result": "Een betrouwbare calculator, afgestemd op jouw eigen puntensysteem.",
                "further": "Koppel hem aan een echte database (zie het traject Gevorderd) om "
                          "hem elk semester te hergebruiken.",
            },
            {
                "title": "Leer coderen met Copilot als tutor, niet als kruk",
                "persona": "students", "features": ["inline", "chat"],
                "situation": "Je begint met programmeren en wilt code begrijpen, niet enkel kopi\u00ebren.",
                "steps": [
                    "Schrijf eerst zelf een eenvoudige functie, ook al is ze onvolledig.",
                    "Vraag Copilot Chat: \u201cLeg regel voor regel uit wat deze code doet.\u201d",
                    "Vraag daarna: \u201cOverhoor me over \u00e9\u00e9n punt om te "
                    "controleren of ik het begrepen heb.\u201d",
                ],
                "result": "Een echt begrip van de code, niet zomaar kopi\u00ebren en plakken.",
                "further": "Vraag Copilot om een iets moeilijkere oefening over hetzelfde concept.",
            },
            {
                "title": "Bouw een gedeelde herhalingssite voor je studiegroep",
                "persona": "students", "features": ["chat", "cli"],
                "situation": "Je studiegroep wil \u00e9\u00e9n gedeelde plek om samen te herhalen voor het examen.",
                "steps": [
                    "Beschrijf de flashcard-app die jullie willen aan Copilot Chat.",
                    "Gebruik Copilot in de terminal om de repository aan te maken: beschrijf "
                    "wat je wilt doen, Copilot stelt het exacte git-commando voor.",
                    "Deel de GitHub Pages-link met de groep.",
                ],
                "result": "Een gratis, gedeeld herhalingsinstrument onder controle van de groep.",
                "further": "Voeg een eenvoudig stemsysteem toe voor de beste fiches.",
            },
            {
                "title": "Presenteer je thesis of stageverslag online",
                "persona": "students", "features": ["chat"],
                "situation": "Je moet een lang document structureren en repetitieve delen "
                            "zoals een inhoudstafel automatiseren.",
                "steps": [
                    "Vraag Copilot om een sitestructuur te genereren om je thesis online te "
                    "presenteren (samenvatting, hoofdstukken, bijlagen).",
                    "Vraag om een interactieve inhoudstafel opgebouwd uit je sectietitels.",
                    "Voeg een contactpagina toe om feedback te ontvangen.",
                ],
                "result": "Een online, presenteerbare versie van je thesis, naast het klassieke document.",
                "further": "Vraag Copilot om zoeken op trefwoord toe te voegen aan de inhoud.",
            },
            {
                "title": "Bouw een portfolio voor je stage- of jobzoektocht",
                "persona": "students", "features": ["chat", "spaces"],
                "situation": "Je wilt een eenvoudige site die je projecten toont, zonder van nul te beginnen.",
                "steps": [
                    "Plak een screenshot van een portfoliostijl die je mooi vindt en vraag "
                    "Copilot Chat om zich erop te bas\u00e9ren.",
                    "Beschrijf je drie beste projecten, \u00e9\u00e9n voor \u00e9\u00e9n.",
                    "Vraag Copilot om een eenvoudig contactformulier toe te voegen.",
                ],
                "result": "Een online portfolio klaar om te delen op je cv.",
                "further": "Publiceer het met een aangepaste domeinnaam via GitHub Pages.",
            },
            {
                "title": "Prototype een interne tool in \u00e9\u00e9n uur",
                "persona": "it", "features": ["agent", "chat"],
                "situation": "Een dienst vraagt om een kleine interne tool en je wilt snel een "
                            "werkend prototype, voordat je engineeringtijd investeert.",
                "steps": [
                    "Beschrijf de kernbehoefte van de tool aan de agent-modus: \u201cBouw een "
                    "pagina waar personeel een aanvraag kan indienen en de status kan zien.\u201d",
                    "Bekijk het voorgestelde plan en laat de agent een eerste versie bouwen.",
                    "Vraag om een realistische verfijning, zoals formuliervalidatie of een statuskleurcode.",
                ],
                "result": "Een werkend prototype in minder dan een uur, om de behoefte te "
                         "valideren v\u00f3\u00f3r een volledige bouw.",
                "further": "Als het nuttig blijkt, plan dan een volwaardige versie met een "
                          "echte database en toegangsbeheer.",
            },
            {
                "title": "Documenteer een bestaand script automatisch",
                "persona": "it", "features": ["chat"],
                "situation": "Je hebt een niet-gedocumenteerd intern script ge\u00ebrfd en "
                            "moet het snel begrijpen en documenteren.",
                "steps": [
                    "Open het script en vraag Copilot Chat: \u201cLeg stap voor stap uit wat dit script doet.\u201d",
                    "Vraag: \u201cGenereer een README die het doel, de invoer en de "
                    "uitvoering beschrijft.\u201d",
                    "Vraag Copilot om risicovolle of onduidelijke delen van de code te signaleren.",
                ],
                "result": "Duidelijke documentatie voor een script dat voorheen maar \u00e9\u00e9n persoon begreep.",
                "further": "Voeg de gegenereerde README rechtstreeks toe aan de repository van het script.",
            },
            {
                "title": "Automatiseer een deployment met GitHub Actions",
                "persona": "it", "features": ["chat", "agent"],
                "situation": "Je wilt dat een kleine site of tool automatisch opnieuw wordt "
                            "uitgerold bij elke wijziging.",
                "steps": [
                    "Vraag Copilot Chat: \u201cGenereer een GitHub Actions-workflow die deze "
                    "site bij elke push naar main naar GitHub Pages deployt.\u201d",
                    "Voeg het voorgestelde bestand toe aan je repository en push een kleine "
                    "wijziging om te testen.",
                    "Vraag Copilot om een melding toe te voegen bij een mislukte deployment.",
                ],
                "result": "Een site die zichzelf automatisch bijwerkt, zonder handmatige herdeployment.",
                "further": "Hergebruik hetzelfde workflow-bestand als sjabloon voor andere interne projecten.",
            },
            {
                "title": "Bouw een interactieve onboardingchecklist",
                "persona": "hr", "features": ["chat"],
                "situation": "Nieuwe medewerkers krijgen een lang, statisch onboardingdocument "
                            "dat makkelijk uit het oog verloren wordt.",
                "steps": [
                    "Beschrijf de onboardingstappen aan Copilot Chat en vraag om een "
                    "interactieve checklistpagina.",
                    "Vraag dat de voortgang bewaard wordt zodat iemand later kan verdergaan.",
                    "Vraag Copilot om een afdrukbare samenvatting toe te voegen voor het HR-dossier.",
                ],
                "result": "Een vriendelijke, opvolgbare onboardingervaring voor nieuwe collega's.",
                "further": "Personaliseer de checklist per functie met een eenvoudig keuzemenu vooraf.",
            },
            {
                "title": "Maak in enkele minuten een opleidingsfeedbackformulier",
                "persona": "hr", "features": ["chat"],
                "situation": "Je hebt snel een manier nodig om feedback te verzamelen na een "
                            "opleiding, zonder te wachten op een licentie voor een enqu\u00eatetool.",
                "steps": [
                    "Vraag Copilot Chat om een pagina te bouwen met een score van 1 tot 5 en "
                    "een opmerkingenveld.",
                    "Vraag dat de antwoorden worden opgeslagen zodat je ze achteraf kunt bekijken.",
                    "Vraag om een eenvoudig overzicht dat de gemiddelde score toont.",
                ],
                "result": "Een werkend feedbackformulier, live nog v\u00f3\u00f3r het einde van de sessie.",
                "further": "Hergebruik dezelfde pagina als sjabloon voor elke volgende opleiding.",
            },
            {
                "title": "Bouw een calculator voor het verlofsaldo",
                "persona": "hr", "features": ["chat"],
                "situation": "Personeel vraagt HR voortdurend hoeveel vakantiedagen er nog over zijn.",
                "steps": [
                    "Beschrijf het verlofbeleid van je instelling aan Copilot Chat.",
                    "Vraag om een kleine calculator te bouwen die een startdatum neemt en de "
                    "resterende dagen toont.",
                    "Vraag om een duidelijke uitleg naast het resultaat, voor bijzondere gevallen.",
                ],
                "result": "Een zelfbedieningstool die repetitieve vragen aan HR vermindert.",
                "further": "Koppel hem aan de onboardingchecklist hierboven.",
            },
            {
                "title": "Organiseer een live peiling tijdens een vergadering",
                "persona": "leadership", "features": ["chat", "agent"],
                "situation": "Je wilt real-time feedback van het personeel tijdens een "
                            "personeelsvergadering, zonder betaalde peilingtool.",
                "steps": [
                    "Beschrijf de vraag en de opties aan Copilot Chat, volgens hetzelfde "
                    "stramien als het voorbeeld van de Snelle Peiling in het begeleide traject.",
                    "Test ze zelf, en projecteer daarna de link tijdens de vergadering.",
                    "Vraag Copilot om een live bijgewerkte resultatenweergave toe te voegen.",
                ],
                "result": "Directe, zichtbare feedback uit de zaal, zonder externe dienst.",
                "further": "Hergebruik exact dezelfde pagina voor elke volgende vergadering, "
                          "en verander enkel de vraag.",
            },
            {
                "title": "Bouw een eenvoudig KPI-dashboard",
                "persona": "leadership", "features": ["chat"],
                "situation": "Je wilt drie of vier cijfers in de tijd opvolgen zonder een volledige BI-tool.",
                "steps": [
                    "Beschrijf je KPI's aan Copilot Chat en plak enkele voorbeeldcijfers.",
                    "Vraag om een overzichtelijk dashboard op \u00e9\u00e9n pagina dat ze samenvat.",
                    "Vraag om een eenvoudige manier om de cijfers elke maand bij te werken.",
                ],
                "result": "Een licht dashboard dat je volledig zelf beheert en begrijpt.",
                "further": "Vraag Copilot om een kleine trendgrafiek toe te voegen zodra je "
                          "enkele maanden gegevens hebt.",
            },
            {
                "title": "Zet een strategische samenvatting om in een visuele pagina",
                "persona": "leadership", "features": ["chat", "spaces"],
                "situation": "Je hebt een dicht, puntsgewijs strategiedocument en wilt iets "
                            "dat makkelijker te presenteren is.",
                "steps": [
                    "Plak je bulletpoints in Copilot Chat en vraag om een overzichtelijke, "
                    "visuele lay-out op \u00e9\u00e9n pagina.",
                    "Plak een screenshot van een visuele stijl die je mooi vindt om het ontwerp te sturen.",
                    "Vraag om zowel een afdrukbare versie als een webversie.",
                ],
                "result": "Een duidelijke, deelbare pagina, gebouwd vanuit bestaande inhoud.",
                "further": "Hergebruik dezelfde lay-out voor de volgende strategische update.",
            },
            {
                "title": "Bouw een calculator voor reiskosten",
                "persona": "finance", "features": ["chat"],
                "situation": "Personeel vraagt vaak hoeveel het terugbetaald krijgt voor een "
                            "verplaatsing v\u00f3\u00f3r het indienen van een onkostennota.",
                "steps": [
                    "Beschrijf je terugbetalingsregels aan Copilot Chat (afstand, tarief, plafonds).",
                    "Vraag om een kleine calculator te bouwen op basis van die regels.",
                    "Vraag om een duidelijke uitsplitsing van de berekening te tonen aan de gebruiker.",
                ],
                "result": "Een zelfbedieningsschatter die e-mailverkeer vermindert.",
                "further": "Koppel hem aan de interne pagina van het financeteam.",
            },
            {
                "title": "Volg een klein terugkerend budget op",
                "persona": "finance", "features": ["chat"],
                "situation": "Je beheert een kleine, terugkerende budgetlijn en wilt een "
                            "lichter alternatief voor een volledig rekenblad.",
                "steps": [
                    "Beschrijf de budgetcategorie\u00ebn aan Copilot Chat.",
                    "Vraag om een eenvoudige pagina om uitgaven te loggen met een bijgewerkt totaal.",
                    "Vraag om een maandelijks overzicht.",
                ],
                "result": "Een lichte tracker, afgestemd op precies jouw eigen categorie\u00ebn.",
                "further": "Exporteer de gegevens naar een rekenblad voor de offici\u00eble registers.",
            },
            {
                "title": "Zet geplakte gegevens om in een sorteerbare tabel",
                "persona": "finance", "features": ["chat"],
                "situation": "Je krijgt regelmatig gegevens als platte tekst of gekopieerde "
                            "rijen die moeilijk te verwerken zijn.",
                "steps": [
                    "Plak de ruwe gegevens in Copilot Chat.",
                    "Vraag om er een overzichtelijke, sorteerbare HTML-tabel van te maken.",
                    "Vraag om een zoekbalk om rijen te filteren.",
                ],
                "result": "Een leesbare, doorzoekbare weergave van gegevens die voorheen een "
                         "muur van tekst waren.",
                "further": "Vraag Copilot om een CSV-exportknop toe te voegen.",
            },
            {
                "title": "Ruim een rommelige dataset op met hulp van Copilot",
                "persona": "research", "features": ["chat", "agent"],
                "situation": "Je hebt een dataset vol inconsistenties (typfouten, ontbrekende "
                            "waarden, gemengde formaten) voordat je ze kunt analyseren.",
                "steps": [
                    "Beschrijf de problemen van de dataset aan Copilot Chat en plak een voorbeeld.",
                    "Vraag om een script dat ze opschoont en standaardiseert.",
                    "Bekijk elke opschoningsregel voordat je ze op de volledige dataset toepast.",
                ],
                "result": "Een propere, analyseklare dataset, met een gedocumenteerd script "
                         "dat precies toont wat er veranderd is.",
                "further": "Vraag Copilot om een samenvattend rapport toe te voegen van wat er "
                          "is opgeschoond en waarom.",
            },
            {
                "title": "Genereer een eerste statistisch analysescript",
                "persona": "research", "features": ["chat"],
                "situation": "Je wilt een startpunt voor een standaardanalyse zonder telkens "
                            "standaardcode te herschrijven.",
                "steps": [
                    "Beschrijf je gegevens en onderzoeksvraag aan Copilot Chat.",
                    "Vraag om een script dat de relevante statistische toets uitvoert en een "
                    "duidelijke samenvatting toont.",
                    "Vraag Copilot om elke stap van het script toe te lichten in commentaar.",
                ],
                "result": "Een analysescript dat je regel voor regel begrijpt, geen zwarte doos.",
                "further": "Vraag Copilot om een eenvoudige grafiek van de resultaten toe te voegen.",
            },
            {
                "title": "Bouw een presentatiepagina voor je onderzoeksresultaten",
                "persona": "research", "features": ["chat", "spaces"],
                "situation": "Je wilt een duidelijke, publieke pagina die je bevindingen "
                            "toont, naast het academische artikel.",
                "steps": [
                    "Beschrijf je belangrijkste bevindingen aan Copilot Chat, \u00e9\u00e9n voor \u00e9\u00e9n.",
                    "Plak een grafiek of figuur en vraag Copilot om er een paginasectie rond te bouwen.",
                    "Vraag om een samenvatting in gewone taal naast de technische versie.",
                ],
                "result": "Een toegankelijke resultatenpagina die je kunt linken vanaf je cv of een conferentie.",
                "further": "Voeg een contactsectie toe voor samenwerkingsverzoeken.",
            },
            {
                "title": "Bouw een interactieve bronnencatalogus",
                "persona": "campus", "features": ["chat"],
                "situation": "Je wilt een eenvoudige manier voor studenten om aanbevolen "
                            "bronnen per onderwerp te doorbladeren.",
                "steps": [
                    "Beschrijf je bronnenlijst en categorie\u00ebn aan Copilot Chat.",
                    "Vraag om een doorzoekbare, filterbare cataloguspagina.",
                    "Vraag om een eenvoudige manier om na verloop van tijd nieuwe bronnen toe te voegen.",
                ],
                "result": "Een levende catalogus, makkelijker te doorbladeren dan een statische pdf-lijst.",
                "further": "Vraag Copilot om labels toe te voegen zodat bronnen tot meerdere "
                          "categorie\u00ebn kunnen behoren.",
            },
            {
                "title": "Genereer een automatische FAQ-pagina",
                "persona": "campus", "features": ["chat"],
                "situation": "Je beantwoordt steeds dezelfde vragen per e-mail en wilt in "
                            "plaats daarvan een publieke FAQ.",
                "steps": [
                    "Plak je meest voorkomende vragen en antwoorden in Copilot Chat.",
                    "Vraag om een overzichtelijke FAQ-pagina met een zoekbalk.",
                    "Vraag Copilot om vragen te groeperen in duidelijke categorie\u00ebn.",
                ],
                "result": "Een zelfbedienings-FAQ die repetitieve e-mails vermindert.",
                "further": "Voeg onderaan een contactlink \u201cnog hulp nodig\u201d toe.",
            },
            {
                "title": "Bouw een campusevenementenpagina",
                "persona": "campus", "features": ["chat", "spaces"],
                "situation": "Je wilt een eenvoudige, aantrekkelijke pagina met aankomende campusevenementen.",
                "steps": [
                    "Beschrijf de evenementen en data aan Copilot Chat.",
                    "Plak een screenshot van een evenementenpaginastijl die je mooi vindt, ter inspiratie.",
                    "Vraag dat evenementen automatisch op datum sorteren, met voorbije "
                    "evenementen die vervagen.",
                ],
                "result": "Een lichte evenementenpagina die je makkelijk elke maand kunt bijwerken.",
                "further": "Vraag Copilot om bij elk evenement een knop \u201ctoevoegen aan agenda\u201d toe te voegen.",
            },
        ],
    },
}

TRACK_ORDER = ["basics", "advanced", "expert"]


def esc(s):
    """Minimal HTML escaping for plain text values (titles, paragraphs)."""
    if s is None:
        return ""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def other_langs(lang):
    return [l for l in LANGS if l != lang]


def lang_switch_html(lang, page_key):
    """page_key is one of: home, basics, advanced, expert, best_practices, about"""
    links = []
    for l in LANGS:
        href = page_href(l, page_key)
        cls = "active" if l == lang else ""
        links.append(f'<a class="{cls}" href="{href}">{LANG_LABEL[l]}</a>')
    return '<div class="lang-switch desktop-only">' + "".join(links) + "</div>"


def page_href(lang, page_key):
    if page_key == "home":
        return f"../{lang}/index.html"
    if page_key == "explorer":
        return f"../{lang}/cas-usage.html"
    if page_key in TRACK_ORDER:
        slug = CONTENT[lang]["tracks"][page_key]["slug"]
        return f"../{lang}/{slug}.html"
    if page_key == "best_practices":
        return f"../{lang}/best-practices.html"
    if page_key == "toolkit":
        return f"../{lang}/toolkit.html"
    if page_key == "about":
        return f"../{lang}/about.html"
    return f"../{lang}/index.html"


def local_href(page_key, lang):
    """Href relative to the current lang folder (no ../lang/ prefix)."""
    if page_key == "home":
        return "index.html"
    if page_key == "explorer":
        return "cas-usage.html"
    if page_key in TRACK_ORDER:
        return CONTENT[lang]["tracks"][page_key]["slug"] + ".html"
    if page_key == "best_practices":
        return "best-practices.html"
    if page_key == "toolkit":
        return "toolkit.html"
    if page_key == "about":
        return "about.html"
    return "index.html"


def nav_course_group_html(lang, track_key):
    track = CONTENT[lang]["tracks"][track_key]
    nav = CONTENT[lang]["nav"]
    href = local_href(track_key, lang)
    items = "".join(
        f'<li><a href="{href}#lesson-{i+1}"><span>{i+1}</span>'
        f'<strong>{esc(lesson["title"])}</strong></a></li>'
        for i, lesson in enumerate(track["lessons"])
    )
    return f'''<div class="nav-course-group">
      <a class="nav-trigger" href="{href}">{esc(nav[track_key])}</a>
      <div class="nav-lesson-panel">
        <div class="nav-lesson-panel-head"><span>{esc(nav["all_lessons"])}</span><strong>{esc(track["level_label"])}</strong></div>
        <ol class="nav-lesson-list">{items}</ol>
        <a class="nav-lesson-overview" href="{href}">{esc(nav["view_route"])}<span aria-hidden="true">\u2192</span></a>
      </div>
    </div>'''


def mobile_course_group_html(lang, track_key):
    track = CONTENT[lang]["tracks"][track_key]
    nav = CONTENT[lang]["nav"]
    href = local_href(track_key, lang)
    items = "".join(
        f'<li><a href="{href}#lesson-{i+1}"><span>{i+1}</span>'
        f'<strong>{esc(lesson["title"])}</strong></a></li>'
        for i, lesson in enumerate(track["lessons"])
    )
    return f'''<details class="mobile-course-details">
      <summary class="mobile-course-summary"><span>{esc(nav[track_key])}</span></summary>
      <div class="mobile-course-body">
        <ol class="nav-lesson-list">{items}</ol>
        <a class="nav-lesson-overview" href="{href}">{esc(nav["view_route"])}<span aria-hidden="true">\u2192</span></a>
      </div>
    </details>'''


def header_html(lang, current_page):
    nav = CONTENT[lang]["nav"]
    meta = CONTENT[lang]["meta"]
    course_groups = "".join(nav_course_group_html(lang, t) for t in TRACK_ORDER)
    mobile_groups = "".join(mobile_course_group_html(lang, t) for t in TRACK_ORDER)
    home_href = local_href("home", lang)
    explorer_href = local_href("explorer", lang)
    bp_href = local_href("best_practices", lang)
    toolkit_href = local_href("toolkit", lang)
    about_href = local_href("about", lang)
    return f'''<header class="site-header">
  <div class="container header-inner">
    <a class="brand-mark" href="{home_href}" aria-label="{esc(meta["site_name"])}">
      <svg width="26" height="26" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0a8 8 0 0 0-2.53 15.59c.4.07.55-.17.55-.38l-.01-1.49c-2.01.44-2.43-.97-2.43-.97-.33-.83-.8-1.05-.8-1.05-.66-.45.05-.44.05-.44.72.05 1.1.74 1.1.74.64 1.1 1.68.78 2.09.6.07-.46.25-.78.46-.96-1.6-.18-3.29-.8-3.29-3.57 0-.79.28-1.43.74-1.93-.07-.18-.32-.92.07-1.92 0 0 .61-.19 1.99.74a6.9 6.9 0 0 1 3.63 0c1.38-.93 1.99-.74 1.99-.74.39 1 .14 1.74.07 1.92.46.5.74 1.14.74 1.93 0 2.78-1.69 3.39-3.3 3.57.26.22.49.66.49 1.33l-.01 1.97c0 .21.14.45.55.38A8 8 0 0 0 8 0Z"/></svg>
      <span class="brand-text"><span class="b1">{esc(meta["site_name"])}</span><span class="b2">{esc(meta.get("brand_tagline", "GitHub Copilot"))}</span></span>
    </a>
    <nav class="desktop-nav" aria-label="Main">
      <span><a class="nav-trigger" href="{explorer_href}" style="color:var(--accent-purple);">{esc(nav.get("explorer", "Cas d'usage"))}</a></span>
      {course_groups}
      <span><a class="nav-trigger" href="{toolkit_href}">{esc(nav.get("toolkit", "Toolkit"))}</a></span>
      <span><a class="nav-trigger" href="{bp_href}">{esc(nav["best_practices"])}</a></span>
      <span><a class="nav-trigger" href="{about_href}">{esc(nav["about"])}</a></span>
    </nav>
    <div class="header-actions">
      {lang_switch_html(lang, current_page)}
      <details class="mobile-nav">
        <summary class="mobile-nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></summary>
      </details>
    </div>
  </div>
  <div class="mobile-nav-panel container" style="display:none;">
    <div class="lang-switch" style="margin-bottom:14px;">{lang_switch_html(lang, current_page)}</div>
    <a href="{explorer_href}" style="display:block;padding:10px 0;color:var(--accent-purple);font-weight:700;">{esc(nav.get("explorer", "Cas d'usage"))}</a>
    {mobile_groups}
    <a href="{toolkit_href}" style="display:block;padding:10px 0;">{esc(nav.get("toolkit", "Toolkit"))}</a>
    <a href="{bp_href}" style="display:block;padding:10px 0;">{esc(nav["best_practices"])}</a>
    <a href="{about_href}" style="display:block;padding:10px 0;">{esc(nav["about"])}</a>
  </div>
</header>'''


def footer_html(lang):
    nav = CONTENT[lang]["nav"]
    footer = CONTENT[lang]["footer"]
    meta = CONTENT[lang]["meta"]
    year = 2026
    return f'''<footer class="site-footer">
  <div class="container footer-inner">
    <p>&copy; {year} {esc(meta["site_name"])}. {esc(footer["text"])}</p>
    <div class="footer-links">
      <a href="{local_href("home", lang)}">{esc(nav["home"])}</a>
      <a href="{local_href("explorer", lang)}">{esc(nav.get("explorer", "Cas d'usage"))}</a>
      <a href="{local_href("best_practices", lang)}">{esc(nav["best_practices"])}</a>
      <a href="{local_href("about", lang)}">{esc(nav["about"])}</a>
    </div>
  </div>
</footer>'''


def page_shell(lang, current_page, title, description, body_html):
    meta = CONTENT[lang]["meta"]
    full_title = f"{title} \u2014 {meta['site_name']}"
    return f'''<!DOCTYPE html>
<html lang="{meta["html_lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
{header_html(lang, current_page)}
{body_html}
{footer_html(lang)}
<script src="../assets/script.js"></script>
</body>
</html>'''


def render_home(lang):
    home = CONTENT[lang]["home"]
    nav = CONTENT[lang]["nav"]
    meta = CONTENT[lang]["meta"]

    journey_cards = "".join(
        f'''<div class="journey-card"><div class="num">{num}</div><h3>{esc(title)}</h3><p>{esc(desc)}</p></div>'''
        for num, title, desc in home["journey"]
    )

    course_cards = ""
    for t in TRACK_ORDER:
        track = CONTENT[lang]["tracks"][t]
        href = local_href(t, lang)
        course_cards += f'''<a class="course-card" href="{href}" style="text-decoration:none;">
      <span class="level-tag {track["tag_class"]}">{esc(track["level_label"])}</span>
      <h3>{esc(track["title"])}</h3>
      <p>{esc(track["card_desc"])}</p>
      <div class="meta">{esc(track["meta"])}</div>
      <div class="cta">{esc(nav["view_route"])} \u2192</div>
    </a>'''

    example_cards = ""
    for item in home.get("examples", []):
        title, desc = item[0], item[1]
        persona = item[2] if len(item) > 2 else None
        pill = f'<span class="persona-pill">{esc(persona)}</span>' if persona else ""
        example_cards += f'<div class="example-card">{pill}<h3>{esc(title)}</h3><p>{esc(desc)}</p></div>'

    persona_cards = "".join(
        f'''<div class="persona-card">
      <div class="persona-icon">{icon}</div>
      <h3>{esc(role)}</h3>
      <p class="persona-pitch">{esc(pitch)}</p>
      <p class="persona-example"><strong>{esc(example_label)}</strong> {esc(example_text)}</p>
    </div>'''
        for icon, role, pitch, example_label, example_text in home.get("personas", [])
    )

    body = f'''<main>
<section class="hero">
  <div class="container">
    <span class="eyebrow">{esc(home["eyebrow"])}</span>
    <h1><span class="grad">{esc(home["h1_line1"])}</span><br>{esc(home["h1_line2"])}</h1>
    <p class="lede">{esc(home["lede"])}</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="{local_href("explorer", lang)}">{esc(home["cta_primary"])}</a>
      <a class="btn btn-ghost" href="{local_href("basics", lang)}">{esc(home["cta_secondary"])}</a>
    </div>
    <p class="hero-note">{esc(home["hero_note"])}</p>
  </div>
</section>

<section class="personas">
  <div class="container">
    <div class="section-head">
      <h2>{esc(home["personas_title"])}</h2>
      <p>{esc(home["personas_sub"])}</p>
    </div>
    <div class="persona-grid">{persona_cards}</div>
  </div>
</section>

<section class="journey">
  <div class="container">
    <div class="section-head">
      <h2>{esc(home["journey_title"])}</h2>
      <p>{esc(home["journey_sub"])}</p>
    </div>
    <div class="journey-grid">{journey_cards}</div>
  </div>
</section>

<section class="examples">
  <div class="container">
    <div class="section-head">
      <h2>{esc(home["examples_title"])}</h2>
      <p>{esc(home["examples_sub"])}</p>
    </div>
    <div class="examples-grid">{example_cards}</div>
  </div>
</section>

<section class="courses">
  <div class="container">
    <div class="section-head">
      <h2>{esc(home["courses_title"])}</h2>
      <p>{esc(home["courses_sub"])}</p>
    </div>
    <div class="course-grid">{course_cards}</div>
  </div>
</section>

<div class="teaser">
  <div>
    <h3>{esc(home["teaser_title"])}</h3>
    <p>{esc(home["teaser_desc"])}</p>
  </div>
  <a class="btn btn-primary" href="{local_href("best_practices", lang)}">{esc(home["teaser_cta"])}</a>
</div>
</main>'''
    return page_shell(lang, "home", meta["title_suffix"], meta["description"], body)


def render_course(lang, track_key):
    track = CONTENT[lang]["tracks"][track_key]
    nav = CONTENT[lang]["nav"]

    toc_items = "".join(
        f'<li><a href="#lesson-{i+1}">{esc(lesson["title"])}</a></li>'
        for i, lesson in enumerate(track["lessons"])
    )

    lesson_blocks = ""
    n = len(track["lessons"])
    for i, lesson in enumerate(track["lessons"]):
        paras = "".join(f"<p>{esc(p)}</p>" for p in lesson["paragraphs"])
        extra = lesson.get("extra_html") or ""
        tip = ""
        if lesson.get("tip"):
            tip = f'<div class="tip-box"><strong>Tip</strong><span>{esc(lesson["tip"])}</span></div>'
        exercise = ""
        if lesson.get("exercise"):
            exercise = (
                f'<div class="exercise-box"><strong>{esc(nav.get("exercise_label", "Exercise"))}</strong>'
                f'<span>{esc(lesson["exercise"])}</span></div>'
            )
        prev_link = ""
        next_link = ""
        if i > 0:
            prev_link = f'<a href="#lesson-{i}">\u2190 {esc(track["lessons"][i-1]["title"])}</a>'
        else:
            prev_link = "<span></span>"
        if i < n - 1:
            next_link = f'<a href="#lesson-{i+2}">{esc(track["lessons"][i+1]["title"])} \u2192</a>'
        else:
            next_link = "<span></span>"
        lesson_blocks += f'''<article class="lesson" id="lesson-{i+1}">
      <div class="lesson-kicker">{esc(lesson["kicker"])}</div>
      <h2>{esc(lesson["title"])}</h2>
      {paras}
      {extra}
      {tip}
      {exercise}
      <div class="lesson-nav">{prev_link}{next_link}</div>
    </article>'''

    body = f'''<main>
<section class="course-hero">
  <div class="container">
    <span class="level-tag {track["tag_class"]}">{esc(track["level_label"])}</span>
    <h1>{esc(track["title"])}</h1>
    <p>{esc(track["subtitle"])}</p>
  </div>
</section>
<div class="container course-layout">
  <aside class="toc">
    <h4>{esc(nav["all_lessons"])}</h4>
    <ol>{toc_items}</ol>
  </aside>
  <div class="lessons">{lesson_blocks}</div>
</div>
</main>'''
    return page_shell(lang, track_key, track["title"], track["subtitle"], body)


def render_best_practices(lang):
    bp = CONTENT[lang]["best_practices"]
    items_html = ""
    for i, (title, desc) in enumerate(bp["items"]):
        items_html += f'''<div class="bp-item">
      <span class="idx">{i+1:02d}</span>
      <h3>{esc(title)}</h3>
      <p>{esc(desc)}</p>
    </div>'''
    body = f'''<main>
<section class="bp-page">
  <div class="container">
    <div class="section-head">
      <h1>{esc(bp["title"])}</h1>
      <p>{esc(bp["sub"])}</p>
    </div>
    <div class="bp-grid">{items_html}</div>
  </div>
</section>
</main>'''
    return page_shell(lang, "best_practices", bp["title"], bp["sub"], body)


def render_about(lang):
    about = CONTENT[lang]["about"]
    paras = "".join(f"<p>{esc(p)}</p>" for p in about["paragraphs"])
    sections_html = ""
    for h2, ps in about["sections"]:
        sections_html += f"<h2>{esc(h2)}</h2>" + "".join(f"<p>{esc(p)}</p>" for p in ps)
    body = f'''<main>
<section class="about-page">
  <div class="container about-body">
    <h1>{esc(about["title"])}</h1>
    {paras}
    {sections_html}
  </div>
</section>
</main>'''
    return page_shell(lang, "about", about["title"], about["paragraphs"][0][:150], body)


def render_explorer(lang):
    exp = CONTENT[lang]["explorer"]
    nav = CONTENT[lang]["nav"]

    feature_label = {key: label for key, label, _desc in exp["features"]}

    persona_pills = '<button type="button" class="filter-pill active" data-persona="all">' + esc(exp["all_label"]) + '</button>'
    for key, icon, label in exp["personas"]:
        persona_pills += f'<button type="button" class="filter-pill" data-persona="{key}">{icon} {esc(label)}</button>'

    feature_pills = ""
    for key, label, _desc in exp["features"]:
        feature_pills += f'<button type="button" class="filter-pill" data-feature="{key}">{esc(label)}</button>'

    legend_items = "".join(
        f'''<div class="feature-legend-item"><span class="feature-chip">{esc(label)}</span><p>{esc(desc)}</p></div>'''
        for _key, label, desc in exp["features"]
    )

    persona_lookup = {key: (icon, label) for key, icon, label in exp["personas"]}

    cards_html = ""
    for uc in exp["usecases"]:
        p_icon, p_label = persona_lookup[uc["persona"]]
        feature_chips = "".join(
            f'<span class="feature-chip">{esc(feature_label[f])}</span>' for f in uc["features"]
        )
        steps_html = "".join(f"<li>{esc(s)}</li>" for s in uc["steps"])
        search_blob = esc((uc["title"] + " " + uc["situation"]).lower())
        cards_html += f'''<div class="usecase-card" data-persona="{uc["persona"]}" data-features="{' '.join(uc["features"])}" data-search="{search_blob}">
      <div class="usecase-top">
        <span class="persona-chip">{p_icon} {esc(p_label)}</span>
        {feature_chips}
      </div>
      <h3>{esc(uc["title"])}</h3>
      <p class="usecase-situation">{esc(uc["situation"])}</p>
      <button type="button" class="usecase-toggle" data-label-show="{esc(exp['show_steps'])}" data-label-hide="{esc(exp['hide_steps'])}">
        <span class="toggle-label">{esc(exp["show_steps"])}</span><span class="chevron" aria-hidden="true">\u25be</span>
      </button>
      <div class="usecase-details" hidden>
        <ol class="usecase-steps">{steps_html}</ol>
        <p class="usecase-result"><strong>{esc(exp["result_label"])}</strong> {esc(uc["result"])}</p>
        <p class="usecase-further"><strong>{esc(exp["further_label"])}</strong> {esc(uc["further"])}</p>
      </div>
    </div>'''

    body = f'''<main>
<section class="explorer-page">
  <div class="container">
    <div class="section-head">
      <h1>{esc(exp["title"])}</h1>
      <p>{esc(exp["sub"])}</p>
    </div>

    <div class="feature-legend">{legend_items}</div>

    <div class="explorer-toolbar">
      <div class="explorer-search">
        <input type="text" placeholder="{esc(exp['search_placeholder'])}">
      </div>
      <div class="filter-row">
        <span class="filter-label">{esc(exp["persona_filter_label"])}</span>
        {persona_pills}
      </div>
      <div class="filter-row">
        <span class="filter-label">{esc(exp["feature_filter_label"])}</span>
        {feature_pills}
      </div>
    </div>

    <p class="explorer-count">{esc(exp["count_prefix"])} <strong>{len(exp["usecases"])}</strong> {esc(exp["count_suffix"])}</p>

    <div class="usecase-grid">{cards_html}</div>
    <div class="explorer-empty">{esc(exp["empty_message"])}</div>
  </div>
</section>
</main>'''
    return page_shell(lang, "explorer", exp["title"], exp["sub"], body)


def render_toolkit(lang):
    toolkit = CONTENT[lang]["toolkit"]
    groups_html = ""
    for icon, role, prompts in toolkit["groups"]:
        prompt_items = "".join(
            f'<div class="prompt-item"><span class="quote-mark">&gt;</span><span>{esc(p)}</span></div>'
            for p in prompts
        )
        groups_html += f'''<div class="toolkit-group">
      <div class="toolkit-group-head">
        <div class="persona-icon">{icon}</div>
        <h2>{esc(role)}</h2>
      </div>
      <div class="prompt-list">{prompt_items}</div>
    </div>'''
    body = f'''<main>
<section class="toolkit-page">
  <div class="container">
    <div class="section-head">
      <h1>{esc(toolkit["title"])}</h1>
      <p>{esc(toolkit["sub"])}</p>
    </div>
    {groups_html}
  </div>
</section>
</main>'''
    return page_shell(lang, "toolkit", toolkit["title"], toolkit["sub"], body)


def render_root_index():
    links = "".join(
        f'<a class="btn btn-primary" style="margin:6px;" href="{l}/index.html">{LANG_LABEL[l]}</a>'
        for l in LANGS
    )
    brand = CONTENT["en"]["meta"]["site_name"]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=en/index.html">
<title>{esc(brand)}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="container" style="padding:120px 0; text-align:center;">
  <h1>{esc(brand)}</h1>
  <p style="color:var(--text-muted); margin-bottom:28px;">Choose your language / Choisissez votre langue / Kies je taal</p>
  {links}
</div>
</body>
</html>'''


def main():
    site_refresh.generate_site(CONTENT, ROOT, LANGS, LANG_LABEL)


if __name__ == "__main__":
    main()

