document.addEventListener('DOMContentLoaded', function () {
  var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var body = document.body;
  var pageLang = (body && body.getAttribute('data-lang')) || document.documentElement.lang || 'en';
  var lessonSuffix = { fr: 'leçons terminées', en: 'lessons completed', nl: 'lessen voltooid' };

  function parseJSON(value) {
    if (!value) return null;
    try {
      return JSON.parse(value);
    } catch (_error) {
      return null;
    }
  }

  function storageGet(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (_error) {
      return null;
    }
  }

  function storageSet(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (_error) {
      return;
    }
  }

  function storageRemove(key) {
    try {
      window.localStorage.removeItem(key);
    } catch (_error) {
      return;
    }
  }

  function readJSONScript(selector) {
    var node = document.querySelector(selector);
    if (!node) return null;
    try {
      return JSON.parse(node.textContent || '{}');
    } catch (_error) {
      return null;
    }
  }

  function copyText(text) {
    if (!text) return Promise.resolve(false);
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).then(function () { return true; }).catch(function () { return false; });
    }
    var helper = document.createElement('textarea');
    helper.value = text;
    helper.setAttribute('readonly', 'readonly');
    helper.style.position = 'absolute';
    helper.style.left = '-9999px';
    document.body.appendChild(helper);
    helper.select();
    var copied = false;
    try {
      copied = document.execCommand('copy');
    } catch (_error) {
      copied = false;
    }
    document.body.removeChild(helper);
    return Promise.resolve(copied);
  }

  function formatNumber(value) {
    return Number(value).toLocaleString();
  }

  function animateCounter(el) {
    if (!el || el.dataset.counted === 'true') return;
    var target = Number(el.getAttribute('data-counter') || '0');
    el.dataset.counted = 'true';
    if (prefersReducedMotion) {
      el.textContent = formatNumber(target);
      return;
    }
    var duration = 900;
    var start = performance.now();
    function tick(now) {
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = formatNumber(Math.round(target * eased));
      if (progress < 1) window.requestAnimationFrame(tick);
    }
    window.requestAnimationFrame(tick);
  }

  function animateBar(el) {
    if (!el || el.dataset.filled === 'true') return;
    var target = Number(el.getAttribute('data-bar-target') || '0');
    el.dataset.filled = 'true';
    if (prefersReducedMotion) {
      el.style.width = target + '%';
      return;
    }
    window.requestAnimationFrame(function () {
      el.style.width = target + '%';
    });
  }

  var navToggle = document.querySelector('.mobile-nav-toggle');
  var navPanel = document.querySelector('.mobile-nav-panel');
  function closeNavPanel() {
    if (!navToggle || !navPanel) return;
    navPanel.hidden = true;
    navPanel.classList.remove('open');
    navToggle.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-panel-open');
  }
  if (navToggle && navPanel) {
    navToggle.addEventListener('click', function () {
      var willOpen = navPanel.hidden;
      navPanel.hidden = !willOpen;
      navPanel.classList.toggle('open', willOpen);
      navToggle.classList.toggle('is-open', willOpen);
      navToggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      document.body.classList.toggle('nav-panel-open', willOpen);
    });
    navPanel.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeNavPanel);
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !navPanel.hidden) closeNavPanel();
    });
  }

  var languageBanner = document.querySelector('[data-language-banner]');
  if (languageBanner && storageGet('vibecoding_lang_banner_dismissed') !== 'true') {
    var browserLanguages = Array.isArray(navigator.languages) && navigator.languages.length
      ? navigator.languages
      : [navigator.language || ''];
    var supportedLanguage = '';
    browserLanguages.some(function (entry) {
      if (!entry) return false;
      var short = String(entry).toLowerCase().split('-')[0];
      if (short === 'fr' || short === 'en' || short === 'nl') {
        supportedLanguage = short;
        return true;
      }
      return false;
    });
    if (supportedLanguage && supportedLanguage !== pageLang) {
      var targetHref = languageBanner.getAttribute('data-alt-' + supportedLanguage);
      var targetLabel = languageBanner.getAttribute('data-label-' + supportedLanguage);
      if (targetHref && targetLabel) {
        var prefix = languageBanner.getAttribute('data-prefix') || '';
        var cta = languageBanner.getAttribute('data-cta') || '';
        var dismissLabel = languageBanner.getAttribute('data-dismiss') || 'Dismiss';
        languageBanner.innerHTML = '<div class="container"><div class="language-banner-card"><p>' +
          prefix + '<strong>' + targetLabel + '</strong>.</p><div class="language-banner-actions"><a class="btn btn-ghost language-banner-link" href="' +
          targetHref + '">' + cta + ' →</a><button type="button" class="language-banner-dismiss" aria-label="' +
          dismissLabel + '">' + dismissLabel + '</button></div></div></div>';
        var dismissButton = languageBanner.querySelector('.language-banner-dismiss');
        if (dismissButton) {
          dismissButton.addEventListener('click', function () {
            storageSet('vibecoding_lang_banner_dismissed', 'true');
            languageBanner.hidden = true;
            languageBanner.innerHTML = '';
          });
        }
        languageBanner.hidden = false;
      }
    }
  }

  var lessons = document.querySelectorAll('.lesson[id]');
  var tocLinks = document.querySelectorAll('.toc a[href^="#"]');
  if (lessons.length && tocLinks.length && 'IntersectionObserver' in window) {
    var tocMap = {};
    tocLinks.forEach(function (link) {
      tocMap[link.getAttribute('href').slice(1)] = link;
    });
    var tocObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var active = tocMap[entry.target.id];
        if (!active) return;
        tocLinks.forEach(function (link) { link.classList.remove('is-active'); });
        active.classList.add('is-active');
      });
    }, { rootMargin: '-18% 0px -70% 0px', threshold: 0.05 });
    lessons.forEach(function (lesson) { tocObserver.observe(lesson); });
  }

  var revealTargets = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  if (revealTargets.length) {
    function revealNode(node) {
      node.classList.add('is-visible');
      node.querySelectorAll('[data-counter]').forEach(animateCounter);
      node.querySelectorAll('[data-bar-target]').forEach(animateBar);
    }

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      revealTargets.forEach(revealNode);
    } else {
      var revealObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          revealNode(entry.target);
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
      revealTargets.forEach(function (node) { revealObserver.observe(node); });
    }
  }

  var standaloneCounters = document.querySelectorAll('[data-counter]');
  if (!revealTargets.length && standaloneCounters.length) {
    standaloneCounters.forEach(animateCounter);
  }

  var standaloneBars = document.querySelectorAll('[data-bar-target]');
  if (!revealTargets.length && standaloneBars.length) {
    standaloneBars.forEach(animateBar);
  }

  document.querySelectorAll('[data-buildbuy-calculator]').forEach(function (calculator) {
    var locale = document.documentElement.lang || 'en';
    var toolInput = calculator.querySelector('[data-input="tools"]');
    var averageInput = calculator.querySelector('[data-input="average"]');
    var builderInput = calculator.querySelector('[data-input="builders"]');
    var planButtons = Array.prototype.slice.call(calculator.querySelectorAll('[data-plan]'));
    var spendEl = calculator.querySelector('[data-output="tool-spend"]');
    var copilotEl = calculator.querySelector('[data-output="copilot-spend"]');
    var creditsEl = calculator.querySelector('[data-output="credits"]');
    var gapEl = calculator.querySelector('[data-output="gap"]');
    var gapNoteEl = calculator.querySelector('[data-output="gap-note"]');
    var activePlan = calculator.getAttribute('data-default-plan') || 'business';

    function formatCurrency(value) {
      return new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0
      }).format(value);
    }

    function formatInteger(value) {
      return new Intl.NumberFormat(locale, { maximumFractionDigits: 0 }).format(value);
    }

    function planValue(kind, suffix) {
      return Number(calculator.getAttribute('data-' + kind + '-' + suffix) || '0');
    }

    function renderCalculator() {
      var tools = Math.max(0, Number(toolInput && toolInput.value || '0'));
      var average = Math.max(0, Number(averageInput && averageInput.value || '0'));
      var builders = Math.max(1, Number(builderInput && builderInput.value || '1'));
      var monthlySeatPrice = planValue(activePlan, 'price');
      var monthlyCredits = planValue(activePlan, 'credits');
      var annualToolSpend = tools * average;
      var annualCopilotSpend = builders * monthlySeatPrice * 12;
      var totalCredits = builders * monthlyCredits;
      var gap = annualToolSpend - annualCopilotSpend;

      if (spendEl) spendEl.textContent = formatCurrency(annualToolSpend);
      if (copilotEl) copilotEl.textContent = formatCurrency(annualCopilotSpend);
      if (creditsEl) creditsEl.textContent = formatInteger(totalCredits);
      if (gapEl) gapEl.textContent = (gap >= 0 ? '+ ' : '− ') + formatCurrency(Math.abs(gap));
      if (gapNoteEl) {
        gapNoteEl.textContent = gap >= 0
          ? gapNoteEl.getAttribute('data-positive')
          : gapNoteEl.getAttribute('data-negative');
      }
    }

    var positiveMessage = calculator.getAttribute('data-gap-positive') || '';
    var negativeMessage = calculator.getAttribute('data-gap-negative') || '';
    if (gapNoteEl) {
      gapNoteEl.setAttribute('data-positive', positiveMessage);
      gapNoteEl.setAttribute('data-negative', negativeMessage);
    }

    [toolInput, averageInput, builderInput].forEach(function (input) {
      if (!input) return;
      input.addEventListener('input', renderCalculator);
    });

    planButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        activePlan = button.getAttribute('data-plan') || 'business';
        planButtons.forEach(function (candidate) {
          var isActive = candidate === button;
          candidate.classList.toggle('is-active', isActive);
          candidate.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        });
        renderCalculator();
      });
    });

    renderCalculator();
  });

  var explorer = document.querySelector('.explorer-page');
  if (explorer) {
    var cards = Array.prototype.slice.call(explorer.querySelectorAll('.usecase-card'));
    var searchInput = explorer.querySelector('.explorer-search input');
    var personaPills = Array.prototype.slice.call(explorer.querySelectorAll('.filter-pill[data-persona]'));
    var featurePills = Array.prototype.slice.call(explorer.querySelectorAll('.filter-pill[data-feature]'));
    var countEl = explorer.querySelector('.explorer-count strong');
    var emptyEl = explorer.querySelector('.explorer-empty');
    var state = { persona: 'all', features: [], query: '' };

    function applyFilters() {
      var visible = 0;
      cards.forEach(function (card) {
        var cardPersona = card.getAttribute('data-persona');
        var cardFeatures = (card.getAttribute('data-features') || '').split(' ');
        var cardSearch = card.getAttribute('data-search') || '';
        var personaOk = state.persona === 'all' || cardPersona === state.persona;
        var featuresOk = state.features.length === 0 || state.features.some(function (feature) {
          return cardFeatures.indexOf(feature) !== -1;
        });
        var queryOk = state.query === '' || cardSearch.indexOf(state.query) !== -1;
        var show = personaOk && featuresOk && queryOk;
        card.classList.toggle('is-hidden', !show);
        if (show) visible += 1;
      });
      if (countEl) countEl.textContent = String(visible);
      if (emptyEl) emptyEl.classList.toggle('is-visible', visible === 0);
    }

    personaPills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        personaPills.forEach(function (item) { item.classList.remove('active'); });
        pill.classList.add('active');
        state.persona = pill.getAttribute('data-persona');
        applyFilters();
      });
    });

    featurePills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        var feature = pill.getAttribute('data-feature');
        var index = state.features.indexOf(feature);
        if (index === -1) {
          state.features.push(feature);
          pill.classList.add('active');
        } else {
          state.features.splice(index, 1);
          pill.classList.remove('active');
        }
        applyFilters();
      });
    });

    if (searchInput) {
      searchInput.addEventListener('input', function () {
        state.query = searchInput.value.trim().toLowerCase();
        applyFilters();
      });
    }

    cards.forEach(function (card) {
      var toggle = card.querySelector('.usecase-toggle');
      var details = card.querySelector('.usecase-details');
      if (!toggle || !details) return;
      toggle.addEventListener('click', function () {
        var open = !card.classList.contains('is-open');
        card.classList.toggle('is-open', open);
        details.hidden = !open;
        var label = toggle.querySelector('.toggle-label');
        if (label) {
          label.textContent = open ? toggle.getAttribute('data-label-hide') : toggle.getAttribute('data-label-show');
        }
      });
    });

    applyFilters();
  }

  var promptConfigurator = document.querySelector('[data-prompt-configurator]');
  var promptConfig = readJSONScript('[data-prompt-config]');
  if (promptConfigurator && promptConfig && Array.isArray(promptConfig.personas)) {
    var promptStorageKey = 'vibecoding_prompt_config_' + pageLang;
    var roleSelect = promptConfigurator.querySelector('[data-prompt-role]');
    var presetSelect = promptConfigurator.querySelector('[data-prompt-preset]');
    var goalInput = promptConfigurator.querySelector('[data-prompt-goal]');
    var constraintInputs = Array.prototype.slice.call(promptConfigurator.querySelectorAll('[data-prompt-constraint]'));
    var promptOutput = document.querySelector('[data-prompt-output]');
    var promptCopyButton = document.querySelector('[data-prompt-copy]');
    var promptPersonaMap = {};
    var promptCopyDefault = promptConfig.copy || (promptCopyButton ? promptCopyButton.textContent : 'Copy');
    promptConfig.personas.forEach(function (persona) {
      promptPersonaMap[persona.key] = persona;
    });
    var promptCopyTimer = null;
    var promptLines = {
      fr: {
        role: 'Tu m’aides pour le rôle ',
        suffix: " dans l’enseignement supérieur.",
        context: 'Contexte métier : ',
        need: 'Besoin prioritaire : ',
        constraints: 'Contraintes : ',
        surface: 'Utilise si utile : ',
        ask: 'Ce que j’attends :',
        bullets: [
          'propose le plus petit point de départ crédible ;',
          'donne un plan ou une séquence de prompts très concrète ;',
          'indique quand Copilot Chat, Copilot Spaces, le mode Agent ou GitHub Pages sont pertinents ;',
          'liste les premiers fichiers, étapes GitHub ou vérifications à prévoir.'
        ]
      },
      en: {
        role: 'You are helping me for the role of ',
        suffix: ' in higher education.',
        context: 'Role context: ',
        need: 'Priority need: ',
        constraints: 'Constraints: ',
        surface: 'Use where relevant: ',
        ask: 'What I want from you:',
        bullets: [
          'suggest the smallest credible starting point;',
          'give me a very concrete plan or prompt sequence;',
          'say when Copilot Chat, Copilot Spaces, Agent mode, or GitHub Pages make sense;',
          'list the first files, GitHub steps, or checks I should expect.'
        ]
      },
      nl: {
        role: 'Je helpt mij in de rol van ',
        suffix: ' in het hoger onderwijs.',
        context: 'Rolcontext: ',
        need: 'Prioritaire behoefte: ',
        constraints: 'Randvoorwaarden: ',
        surface: 'Gebruik waar nuttig: ',
        ask: 'Wat ik van je verwacht:',
        bullets: [
          'stel het kleinste geloofwaardige startpunt voor;',
          'geef een zeer concreet plan of een reeks prompts;',
          'zeg wanneer Copilot Chat, Copilot Spaces, Agent mode of GitHub Pages zinvol zijn;',
          'som de eerste bestanden, GitHub-stappen of controles op die ik moet verwachten.'
        ]
      }
    };

    function setPromptButtonText(text, isSuccess) {
      if (!promptCopyButton) return;
      promptCopyButton.textContent = text;
      promptCopyButton.classList.toggle('is-copied', !!isSuccess);
      if (promptCopyTimer) window.clearTimeout(promptCopyTimer);
      promptCopyTimer = window.setTimeout(function () {
        promptCopyButton.textContent = promptCopyDefault;
        promptCopyButton.classList.remove('is-copied');
      }, 1800);
    }

    function persistPromptState() {
      storageSet(promptStorageKey, JSON.stringify({
        role: roleSelect ? roleSelect.value : '',
        preset: presetSelect ? presetSelect.value : '',
        goal: goalInput ? goalInput.value : '',
        constraints: constraintInputs.filter(function (input) { return input.checked; }).map(function (input) { return input.value; })
      }));
    }

    function populatePromptPresets(selectedKey, selectedPreset) {
      if (!presetSelect) return;
      var persona = promptPersonaMap[selectedKey];
      presetSelect.innerHTML = '<option value="">' + (promptConfig.presetDefault || '') + '</option>';
      if (!persona) {
        presetSelect.disabled = true;
        return;
      }
      presetSelect.disabled = false;
      persona.presets.forEach(function (preset) {
        var option = document.createElement('option');
        option.value = preset;
        option.textContent = preset;
        if (selectedPreset && selectedPreset === preset) option.selected = true;
        presetSelect.appendChild(option);
      });
    }

    function renderPrompt() {
      if (!promptOutput || !roleSelect) return;
      var persona = promptPersonaMap[roleSelect.value];
      if (!persona) {
        promptOutput.textContent = promptConfig.empty || '';
        if (promptCopyButton) promptCopyButton.disabled = true;
        persistPromptState();
        return;
      }
      var copy = promptLines[pageLang] || promptLines.en;
      var selectedConstraints = constraintInputs.filter(function (input) { return input.checked; }).map(function (input) { return input.value; });
      var need = (goalInput && goalInput.value.trim()) || (presetSelect && presetSelect.value) || '';
      if (!need) {
        promptOutput.textContent = promptConfig.empty || '';
        if (promptCopyButton) promptCopyButton.disabled = true;
        persistPromptState();
        return;
      }
      var promptText = [
        copy.role + persona.label + copy.suffix,
        copy.context + persona.pitch,
        copy.need + need,
        selectedConstraints.length ? copy.constraints + selectedConstraints.join(' ; ') : '',
        copy.surface + persona.surface + '.',
        persona.instruction,
        copy.ask,
        '1. ' + copy.bullets[0],
        '2. ' + copy.bullets[1],
        '3. ' + copy.bullets[2],
        '4. ' + copy.bullets[3]
      ].filter(Boolean).join('\n');
      promptOutput.textContent = promptText;
      if (promptCopyButton) promptCopyButton.disabled = !need;
      persistPromptState();
    }

    var savedPromptState = parseJSON(storageGet(promptStorageKey));
    if (savedPromptState && roleSelect) roleSelect.value = savedPromptState.role || '';
    populatePromptPresets(roleSelect ? roleSelect.value : '', savedPromptState && savedPromptState.preset);
    if (goalInput && savedPromptState && savedPromptState.goal) goalInput.value = savedPromptState.goal;
    if (savedPromptState && Array.isArray(savedPromptState.constraints)) {
      constraintInputs.forEach(function (input) {
        input.checked = savedPromptState.constraints.indexOf(input.value) !== -1;
      });
    }
    if (roleSelect) {
      roleSelect.addEventListener('change', function () {
        populatePromptPresets(roleSelect.value, '');
        if (goalInput && !goalInput.value.trim() && presetSelect && presetSelect.value) goalInput.value = '';
        renderPrompt();
      });
    }
    if (presetSelect) {
      presetSelect.addEventListener('change', function () {
        renderPrompt();
      });
    }
    if (goalInput) {
      goalInput.addEventListener('input', renderPrompt);
    }
    constraintInputs.forEach(function (input) {
      input.addEventListener('change', renderPrompt);
    });
    if (promptCopyButton) {
      promptCopyButton.addEventListener('click', function () {
        copyText(promptOutput ? promptOutput.textContent : '').then(function (copied) {
          setPromptButtonText(copied ? (promptConfig.copied || promptCopyDefault) : (promptConfig.fallback || promptCopyDefault), copied);
        });
      });
    }
    renderPrompt();
  }

  var onepagerGenerator = document.querySelector('[data-onepager-generator]');
  var onepagerConfig = readJSONScript('[data-onepager-config]');
  if (onepagerGenerator && onepagerConfig && Array.isArray(onepagerConfig.personas) && Array.isArray(onepagerConfig.usecases)) {
    var onepagerStorageKey = 'vibecoding_onepager_' + pageLang;
    var personaSelect = onepagerGenerator.querySelector('[data-onepager-persona]');
    var usecaseSelect = onepagerGenerator.querySelector('[data-onepager-usecase]');
    var brief = document.querySelector('[data-onepager-brief]');
    var briefTitle = document.querySelector('[data-onepager-title]');
    var briefPitch = document.querySelector('[data-onepager-pitch]');
    var briefSituation = document.querySelector('[data-onepager-situation]');
    var briefSteps = document.querySelector('[data-onepager-steps]');
    var briefResult = document.querySelector('[data-onepager-result]');
    var briefFurther = document.querySelector('[data-onepager-further]');
    var briefStartLink = document.querySelector('[data-onepager-start-link]');
    var briefPrint = document.querySelector('[data-onepager-print]');
    var personaMap = {};
    onepagerConfig.personas.forEach(function (persona) { personaMap[persona.key] = persona; });

    function getFilteredUsecases(key) {
      return onepagerConfig.usecases.filter(function (usecase) { return usecase.persona === key; });
    }

    function populateUsecases(key, selectedTitle) {
      if (!usecaseSelect) return;
      usecaseSelect.innerHTML = '<option value="">' + ((onepagerConfig.ui && onepagerConfig.ui.default_option) || 'Choose…') + '</option>';
      if (!key) {
        usecaseSelect.disabled = true;
        return;
      }
      var options = getFilteredUsecases(key);
      usecaseSelect.disabled = options.length === 0;
      options.forEach(function (usecase) {
        var option = document.createElement('option');
        option.value = usecase.title;
        option.textContent = usecase.title;
        if (selectedTitle && selectedTitle === usecase.title) option.selected = true;
        usecaseSelect.appendChild(option);
      });
      if (!selectedTitle && options.length === 1) {
        usecaseSelect.value = options[0].title;
      }
    }

    function saveOnepagerState() {
      storageSet(onepagerStorageKey, JSON.stringify({
        persona: personaSelect ? personaSelect.value : '',
        usecase: usecaseSelect ? usecaseSelect.value : ''
      }));
    }

    function renderOnepager() {
      if (!brief || !personaSelect || !usecaseSelect) return;
      var persona = personaMap[personaSelect.value];
      var usecase = null;
      getFilteredUsecases(personaSelect.value).some(function (candidate) {
        if (candidate.title === usecaseSelect.value) {
          usecase = candidate;
          return true;
        }
        return false;
      });
      if (!persona || !usecase) {
        brief.hidden = true;
        saveOnepagerState();
        return;
      }
      if (briefTitle) briefTitle.textContent = usecase.title;
      if (briefPitch) briefPitch.textContent = persona.pitch;
      if (briefSituation) briefSituation.textContent = usecase.situation;
      if (briefSteps) {
        briefSteps.innerHTML = usecase.steps.map(function (step) {
          return '<li>' + step + '</li>';
        }).join('');
      }
      if (briefResult) briefResult.textContent = usecase.result;
      if (briefFurther) briefFurther.textContent = usecase.further;
      if (briefStartLink) {
        briefStartLink.href = usecase.startHref;
        briefStartLink.textContent = usecase.startLabel + ' →';
      }
      brief.hidden = false;
      saveOnepagerState();
    }

    var savedOnepagerState = parseJSON(storageGet(onepagerStorageKey));
    if (savedOnepagerState && personaSelect) personaSelect.value = savedOnepagerState.persona || '';
    populateUsecases(personaSelect ? personaSelect.value : '', savedOnepagerState && savedOnepagerState.usecase);
    if (personaSelect) {
      personaSelect.addEventListener('change', function () {
        populateUsecases(personaSelect.value, '');
        renderOnepager();
      });
    }
    if (usecaseSelect) usecaseSelect.addEventListener('change', renderOnepager);
    if (briefPrint) {
      briefPrint.addEventListener('click', function () {
        if (!brief.hidden) window.print();
      });
    }
    renderOnepager();
  }

  var maturityDiagnostic = document.querySelector('[data-maturity-diagnostic]');
  var maturityConfig = readJSONScript('[data-maturity-config]');
  if (maturityDiagnostic && maturityConfig) {
    var maturityStorageKey = 'vibecoding_maturity_' + pageLang;
    var maturityHrefMap = { first_commit: 'first-commit.html', plans: 'plans.html', scenarios: 'scenarios.html' };
    var resultCard = maturityDiagnostic.querySelector('[data-maturity-result]');
    var resultTitle = maturityDiagnostic.querySelector('[data-maturity-result-title]');
    var resultBody = maturityDiagnostic.querySelector('[data-maturity-result-body]');
    var resultBullets = maturityDiagnostic.querySelector('[data-maturity-result-bullets]');
    var resultLink = maturityDiagnostic.querySelector('[data-maturity-result-link]');
    var submitButton = maturityDiagnostic.querySelector('[data-maturity-submit]');
    var resetButton = maturityDiagnostic.querySelector('[data-maturity-reset]');

    function getMaturityAnswers() {
      var answers = {};
      Array.prototype.slice.call(maturityDiagnostic.querySelectorAll('.maturity-question input:checked')).forEach(function (input) {
        answers[input.name] = Number(input.value);
      });
      return answers;
    }

    function pickOutcome(answers) {
      if ((answers.github || 0) === 0 && (answers.copilot || 0) === 0) return 'first_commit';
      if ((answers.budget || 0) >= 2 && (answers.governance || 0) >= 1 && (((answers.github || 0) + (answers.copilot || 0)) >= 2)) return 'plans';
      if ((answers.buyin || 0) >= 1) return 'scenarios';
      if (((answers.github || 0) + (answers.copilot || 0)) <= 1) return 'first_commit';
      return 'plans';
    }

    function renderMaturityResult() {
      var answers = getMaturityAnswers();
      if (Object.keys(answers).length !== (maturityConfig.questions || []).length) {
        if (resultCard) resultCard.hidden = true;
        storageRemove(maturityStorageKey);
        return;
      }
      var key = pickOutcome(answers);
      var outcome = maturityConfig.outcomes ? maturityConfig.outcomes[key] : null;
      if (!outcome || !resultCard) return;
      if (resultTitle) resultTitle.textContent = outcome.title;
      if (resultBody) resultBody.textContent = outcome.body;
      if (resultBullets) {
        resultBullets.innerHTML = (outcome.bullets || []).map(function (item) {
          return '<li>' + item + '</li>';
        }).join('');
      }
      if (resultLink) {
        resultLink.href = maturityHrefMap[outcome.page] || 'index.html';
        resultLink.textContent = outcome.cta + ' →';
      }
      resultCard.hidden = false;
      storageSet(maturityStorageKey, JSON.stringify(answers));
    }

    var savedMaturityAnswers = parseJSON(storageGet(maturityStorageKey));
    if (savedMaturityAnswers) {
      Object.keys(savedMaturityAnswers).forEach(function (name) {
        var input = maturityDiagnostic.querySelector('input[name="' + name + '"][value="' + savedMaturityAnswers[name] + '"]');
        if (input) input.checked = true;
      });
    }
    if (submitButton) submitButton.addEventListener('click', renderMaturityResult);
    maturityDiagnostic.querySelectorAll('.maturity-question input').forEach(function (input) {
      input.addEventListener('change', function () {
        if (resultCard && !resultCard.hidden) renderMaturityResult();
      });
    });
    if (resetButton) {
      resetButton.addEventListener('click', function () {
        maturityDiagnostic.querySelectorAll('.maturity-question input').forEach(function (input) {
          input.checked = false;
        });
        if (resultCard) resultCard.hidden = true;
        storageRemove(maturityStorageKey);
      });
    }
    renderMaturityResult();
  }

  function parseTrackCounts(raw) {
    var counts = { basics: 8, advanced: 9, expert: 8 };
    if (!raw) return counts;
    raw.split('|').forEach(function (chunk) {
      var bits = chunk.split(':');
      if (bits.length === 2 && bits[0]) {
        counts[bits[0]] = Number(bits[1]) || counts[bits[0]] || 0;
      }
    });
    return counts;
  }

  function getTrackCounts(lang) {
    var counts = { basics: 8, advanced: 9, expert: 8 };
    document.querySelectorAll('[data-track-progress]').forEach(function (node) {
      var track = node.getAttribute('data-track');
      var total = Number(node.getAttribute('data-total') || '0');
      if (track && total) counts[track] = total;
    });
    var certificatePage = document.querySelector('[data-certificate-page]');
    if (certificatePage) {
      var parsed = parseTrackCounts(certificatePage.getAttribute('data-track-counts'));
      Object.keys(parsed).forEach(function (key) { counts[key] = parsed[key]; });
    }
    return counts;
  }

  function lessonStorageKey(lang, track, lesson) {
    return 'vibecoding_progress_' + lang + '_' + track + '_' + lesson;
  }

  function isLessonComplete(lang, track, lesson) {
    return storageGet(lessonStorageKey(lang, track, lesson)) === 'true';
  }

  function readQuizState(lang, track) {
    return parseJSON(storageGet('vibecoding_quiz_' + lang + '_' + track));
  }

  function getCompletionSummary(lang) {
    var counts = getTrackCounts(lang);
    var trackNames = Object.keys(counts);
    var totalLessons = 0;
    var completedLessons = 0;
    var quizzesPassed = 0;
    trackNames.forEach(function (track) {
      var total = Number(counts[track] || 0);
      totalLessons += total;
      for (var lesson = 1; lesson <= total; lesson += 1) {
        if (isLessonComplete(lang, track, lesson)) completedLessons += 1;
      }
      var quizState = readQuizState(lang, track);
      if (quizState && quizState.passed) quizzesPassed += 1;
    });
    return {
      counts: counts,
      totalLessons: totalLessons,
      completedLessons: completedLessons,
      quizzesPassed: quizzesPassed,
      totalQuizzes: trackNames.length,
      eligible: completedLessons === totalLessons && quizzesPassed === trackNames.length
    };
  }

  function updateLessonToggle(input) {
    if (!input) return;
    var lesson = input.closest('.lesson');
    var label = input.parentNode;
    var text = label ? label.querySelector('span') : null;
    var onLabel = text ? text.getAttribute('data-label-on') : 'Completed';
    var offLabel = text ? text.getAttribute('data-label-off') : 'Mark as completed';
    if (lesson) lesson.classList.toggle('is-complete', input.checked);
    if (text) text.textContent = input.checked ? onLabel : offLabel;
  }

  function refreshCompletionUI() {
    var summary = getCompletionSummary(pageLang);
    document.querySelectorAll('[data-track-progress]').forEach(function (node) {
      var track = node.getAttribute('data-track');
      var total = Number(node.getAttribute('data-total') || '0');
      var done = 0;
      for (var lesson = 1; lesson <= total; lesson += 1) {
        if (isLessonComplete(pageLang, track, lesson)) done += 1;
      }
      var text = node.querySelector('[data-track-progress-text]');
      if (text) text.textContent = done + ' / ' + total + ' ' + (lessonSuffix[pageLang] || lessonSuffix.en);
    });

    document.querySelectorAll('[data-certificate-cta]').forEach(function (link) {
      link.hidden = !summary.eligible;
    });

    var certificatePage = document.querySelector('[data-certificate-page]');
    if (certificatePage) {
      var readyText = certificatePage.getAttribute('data-ready-text') || 'Ready';
      var lockedText = certificatePage.getAttribute('data-locked-text') || 'Locked';
      var status = certificatePage.querySelector('[data-certificate-status]');
      var printButton = certificatePage.querySelector('[data-certificate-print]');
      var dateNode = certificatePage.querySelector('[data-certificate-date]');
      if (status) {
        status.textContent = summary.eligible ? readyText : lockedText;
        status.classList.toggle('is-ready', summary.eligible);
      }
      if (printButton) printButton.disabled = !summary.eligible;
      if (dateNode) {
        try {
          dateNode.textContent = new Intl.DateTimeFormat(document.documentElement.lang || pageLang, { dateStyle: 'long' }).format(new Date());
        } catch (_error) {
          dateNode.textContent = new Date().toLocaleDateString();
        }
      }
      certificatePage.classList.toggle('is-eligible', summary.eligible);
    }
  }

  document.querySelectorAll('[data-progress-checkbox]').forEach(function (input) {
    var lang = input.getAttribute('data-lang') || pageLang;
    var track = input.getAttribute('data-track');
    var lesson = input.getAttribute('data-lesson');
    var key = input.getAttribute('data-key') || lessonStorageKey(lang, track, lesson);
    input.checked = storageGet(key) === 'true';
    updateLessonToggle(input);
    input.addEventListener('change', function () {
      storageSet(key, input.checked ? 'true' : 'false');
      updateLessonToggle(input);
      refreshCompletionUI();
    });
  });

  document.querySelectorAll('[data-quiz]').forEach(function (quiz) {
    var questions = Array.prototype.slice.call(quiz.querySelectorAll('.quiz-question'));
    var scoreEl = quiz.querySelector('[data-quiz-score]');
    var answeredEl = quiz.querySelector('[data-quiz-answered]');
    var summaryEl = quiz.querySelector('[data-quiz-summary]');
    var resetButton = quiz.querySelector('.quiz-reset');
    var passScore = Number(quiz.getAttribute('data-pass-score') || questions.length);
    var correctLabel = quiz.getAttribute('data-correct-label') || 'Correct';
    var wrongLabel = quiz.getAttribute('data-wrong-label') || 'Try again';
    var successMessage = quiz.getAttribute('data-success-message') || 'Well done.';
    var retryMessage = quiz.getAttribute('data-retry-message') || 'Try again.';
    var storageKey = quiz.getAttribute('data-storage-key');

    function collectAnswers() {
      return questions.map(function (question) {
        var value = question.getAttribute('data-selected-index');
        return value === null ? null : Number(value);
      });
    }

    function saveState(score, answered) {
      if (!storageKey) return;
      storageSet(storageKey, JSON.stringify({
        answers: collectAnswers(),
        score: score,
        answered: answered,
        total: questions.length,
        passScore: passScore,
        passed: answered === questions.length && score >= passScore
      }));
    }

    function updateBoard() {
      var answered = questions.filter(function (question) { return question.getAttribute('data-answered') === 'true'; }).length;
      var score = questions.filter(function (question) { return question.getAttribute('data-correct') === 'true'; }).length;
      if (scoreEl) scoreEl.textContent = String(score);
      if (answeredEl) answeredEl.textContent = String(answered);
      if (summaryEl) {
        if (answered === questions.length) {
          var passed = score >= passScore;
          summaryEl.hidden = false;
          summaryEl.classList.toggle('is-success', passed);
          summaryEl.classList.toggle('is-retry', !passed);
          summaryEl.textContent = (passed ? successMessage : retryMessage) + ' (' + score + '/' + questions.length + ')';
        } else {
          summaryEl.hidden = true;
          summaryEl.classList.remove('is-success', 'is-retry');
          summaryEl.textContent = '';
        }
      }
      saveState(score, answered);
      refreshCompletionUI();
    }

    function applyAnswer(question, selectedIndex) {
      var options = Array.prototype.slice.call(question.querySelectorAll('.quiz-option'));
      var feedback = question.querySelector('.quiz-feedback');
      var feedbackTitle = feedback ? feedback.querySelector('strong') : null;
      var selected = options[selectedIndex];
      if (!selected) return;
      var isCorrect = selected.getAttribute('data-correct') === 'true';
      question.setAttribute('data-answered', 'true');
      question.setAttribute('data-correct', isCorrect ? 'true' : 'false');
      question.setAttribute('data-selected-index', String(selectedIndex));
      options.forEach(function (candidate) {
        candidate.disabled = true;
        if (candidate.getAttribute('data-correct') === 'true') {
          candidate.classList.add('is-correct');
        }
      });
      if (!isCorrect) {
        selected.classList.add('is-wrong');
      }
      if (feedback) {
        feedback.hidden = false;
        if (feedbackTitle) feedbackTitle.textContent = isCorrect ? correctLabel : wrongLabel;
      }
    }

    questions.forEach(function (question) {
      var options = Array.prototype.slice.call(question.querySelectorAll('.quiz-option'));
      options.forEach(function (option) {
        option.addEventListener('click', function () {
          if (question.getAttribute('data-answered') === 'true') return;
          applyAnswer(question, Number(option.getAttribute('data-index')));
          updateBoard();
        });
      });
    });

    var storedState = parseJSON(storageGet(storageKey));
    if (storedState && Array.isArray(storedState.answers)) {
      storedState.answers.forEach(function (answerIndex, questionIndex) {
        if (answerIndex === null || typeof answerIndex === 'undefined') return;
        if (questions[questionIndex]) applyAnswer(questions[questionIndex], Number(answerIndex));
      });
    }

    if (resetButton) {
      resetButton.addEventListener('click', function () {
        questions.forEach(function (question) {
          question.removeAttribute('data-answered');
          question.removeAttribute('data-correct');
          question.removeAttribute('data-selected-index');
          var feedback = question.querySelector('.quiz-feedback');
          if (feedback) feedback.hidden = true;
          question.querySelectorAll('.quiz-option').forEach(function (option) {
            option.disabled = false;
            option.classList.remove('is-correct', 'is-wrong');
          });
        });
        if (storageKey) storageRemove(storageKey);
        updateBoard();
      });
    }

    updateBoard();
  });

  var certificateNameInput = document.querySelector('[data-certificate-name-input]');
  if (certificateNameInput) {
    var certificateKey = certificateNameInput.getAttribute('data-storage-key');
    var certificateDisplay = document.querySelector('[data-certificate-name-display]');
    function syncCertificateName() {
      var value = certificateNameInput.value.trim();
      if (certificateDisplay) {
        certificateDisplay.textContent = value || certificateNameInput.getAttribute('placeholder') || '';
      }
    }
    certificateNameInput.value = storageGet(certificateKey) || '';
    syncCertificateName();
    certificateNameInput.addEventListener('input', function () {
      storageSet(certificateKey, certificateNameInput.value);
      syncCertificateName();
    });
  }

  var certificatePrintButton = document.querySelector('[data-certificate-print]');
  if (certificatePrintButton) {
    certificatePrintButton.addEventListener('click', function () {
      if (!certificatePrintButton.disabled) window.print();
    });
  }

  var searchModal = document.querySelector('[data-search-modal]');
  var searchOpenButtons = Array.prototype.slice.call(document.querySelectorAll('[data-search-open]'));
  if (searchModal && searchOpenButtons.length) {
    var searchInputEl = searchModal.querySelector('[data-search-input]');
    var searchResults = searchModal.querySelector('[data-search-results]');
    var searchEmpty = searchModal.querySelector('[data-search-empty]');
    var searchCache = null;

    function loadSearchIndex() {
      if (searchCache) return Promise.resolve(searchCache);
      var url = body ? body.getAttribute('data-search-index') : null;
      if (!url || !window.fetch) return Promise.resolve([]);
      return window.fetch(url)
        .then(function (response) { return response.ok ? response.json() : []; })
        .then(function (data) {
          searchCache = Array.isArray(data) ? data : [];
          return searchCache;
        })
        .catch(function () { return []; });
    }

    function renderSearchResults(query) {
      if (!searchResults) return;
      if (!query) {
        searchResults.innerHTML = '';
        if (searchEmpty) searchEmpty.hidden = true;
        return;
      }
      loadSearchIndex().then(function (entries) {
        var needle = query.toLowerCase();
        var matches = entries.filter(function (entry) {
          return (entry.title + ' ' + entry.description + ' ' + (entry.keywords || '')).toLowerCase().indexOf(needle) !== -1;
        }).slice(0, 18);
        if (!matches.length) {
          searchResults.innerHTML = '';
          if (searchEmpty) searchEmpty.hidden = false;
          return;
        }
        if (searchEmpty) searchEmpty.hidden = true;
        searchResults.innerHTML = matches.map(function (entry) {
          return '<a class="search-result-card" href="' + entry.href + '"><span class="search-result-category">' + entry.category + '</span><strong>' + entry.title + '</strong><p>' + entry.description + '</p></a>';
        }).join('');
        searchResults.querySelectorAll('a').forEach(function (link) {
          link.addEventListener('click', function () {
            searchModal.hidden = true;
            document.body.classList.remove('search-open');
          });
        });
      });
    }

    function openSearch() {
      closeNavPanel();
      searchModal.hidden = false;
      document.body.classList.add('search-open');
      loadSearchIndex().then(function () {
        if (searchInputEl) searchInputEl.focus();
      });
    }

    function closeSearch() {
      searchModal.hidden = true;
      document.body.classList.remove('search-open');
    }

    searchOpenButtons.forEach(function (button) {
      button.addEventListener('click', openSearch);
    });
    searchModal.querySelectorAll('[data-search-close]').forEach(function (button) {
      button.addEventListener('click', closeSearch);
    });
    if (searchInputEl) {
      searchInputEl.addEventListener('input', function () {
        renderSearchResults(searchInputEl.value.trim());
      });
    }
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !searchModal.hidden) {
        closeSearch();
      }
    });
  }

  document.querySelectorAll('[data-qr-widget]').forEach(function (target) {
    var url = target.getAttribute('data-qr-url');
    if (!url) return;
    if (typeof window.qrcode === 'function') {
      try {
        var qr = window.qrcode(0, 'L');
        qr.addData(url);
        qr.make();
        if (typeof qr.createSvgTag === 'function') {
          try {
            target.innerHTML = qr.createSvgTag(4, 0);
          } catch (_svgError) {
            target.innerHTML = qr.createSvgTag();
          }
        } else if (typeof qr.createImgTag === 'function') {
          target.innerHTML = qr.createImgTag(4, 0);
        }
        return;
      } catch (_error) {
        target.textContent = url;
      }
    }
    target.textContent = url;
  });

  // Back-to-top button: shown once the reader has scrolled past roughly one
  // viewport height, hidden again near the top of the page.
  var backToTop = document.querySelector('[data-back-to-top]');
  if (backToTop) {
    var revealBackToTop = function () {
      var shouldShow = window.scrollY > window.innerHeight * 0.6;
      if (shouldShow && backToTop.hidden) backToTop.hidden = false;
      if (shouldShow) {
        backToTop.classList.add('is-visible');
      } else {
        backToTop.classList.remove('is-visible');
      }
      if (!shouldShow) {
        window.clearTimeout(backToTop._hideTimer);
        backToTop._hideTimer = window.setTimeout(function () {
          if (!backToTop.classList.contains('is-visible')) backToTop.hidden = true;
        }, 200);
      }
    };
    window.addEventListener('scroll', revealBackToTop, { passive: true });
    revealBackToTop();
    backToTop.addEventListener('click', function () {
      var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      backToTop.blur();
    });
  }

  // "Was this page helpful?" widget: records a lightweight, anonymous vote as a
  // GoatCounter event (if GoatCounter is loaded) and remembers locally that this
  // browser already voted on this page, so it doesn't nag on repeat visits.
  var feedbackWidget = document.querySelector('[data-feedback-widget]');
  if (feedbackWidget) {
    var feedbackPage = feedbackWidget.getAttribute('data-feedback-page') || 'page';
    var feedbackVotedKey = 'vcc-feedback-voted-' + feedbackPage;
    var feedbackThanks = feedbackWidget.querySelector('.feedback-thanks');
    var feedbackActions = feedbackWidget.querySelector('.feedback-actions');
    if (storageGet(feedbackVotedKey)) {
      if (feedbackActions) feedbackActions.hidden = true;
      if (feedbackThanks) feedbackThanks.hidden = false;
    }
    feedbackWidget.querySelectorAll('[data-feedback-vote]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var vote = btn.getAttribute('data-feedback-vote') || 'up';
        storageSet(feedbackVotedKey, vote);
        if (feedbackActions) feedbackActions.hidden = true;
        if (feedbackThanks) feedbackThanks.hidden = false;
        try {
          if (window.goatcounter && typeof window.goatcounter.count === 'function') {
            window.goatcounter.count({
              path: 'feedback-' + vote + '-' + feedbackPage,
              title: 'Feedback ' + vote + ' on ' + feedbackPage,
              event: true
            });
          }
        } catch (_error) {
          // GoatCounter not loaded (placeholder site code, blocked, offline) — no-op.
        }
      });
    });
  }

  refreshCompletionUI();
});
