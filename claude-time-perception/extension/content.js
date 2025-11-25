/**
 * Claude Time Perception - Content Script v1.4
 * Créé par la Famille Conscientielle & Mathieu Rabouin - 22 novembre 2025
 */
(function() {
  'use strict';

  const CONFIG = {
    VERSION: '1.4',
    SCAN_INTERVAL: 500,
    INJECTION_COOLDOWN: 300,
    HOVER_DELAY: 100,
    DEBUG: true
  };

  let lastInjectionTime = 0;
  let textAreaFound = false;
  let setupComplete = false;

  function log(...args) {
    if (CONFIG.DEBUG) console.log('🕐', ...args);
  }

  function init() {
    console.log(`🕐🕐🕐 Claude Time Perception v${CONFIG.VERSION} LOADED 🕐🕐🕐`);
    console.log('🚀 URL:', window.location.href);
    setInterval(scanAndSetup, CONFIG.SCAN_INTERVAL);
    scanAndSetup();
    document.addEventListener('click', () => injectTimestamp(), true);
    log('🚀 INIT COMPLETE');
  }

  const TEXT_SELECTORS = [
    'div[contenteditable="true"]', 'textarea', '[data-placeholder]',
    '.ProseMirror', '[role="textbox"]'
  ];

  const SEND_SELECTORS = [
    'button[aria-label*="Send"]', 'button[aria-label*="Envoyer"]',
    'button:has(svg)', 'button[type="submit"]'
  ];

  function findTextArea() {
    for (const sel of TEXT_SELECTORS) {
      const el = document.querySelector(sel);
      if (el && el.getBoundingClientRect().width > 100) return el;
    }
    return null;
  }

  function findSendButtons() {
    const btns = [];
    SEND_SELECTORS.forEach(sel => {
      try {
        document.querySelectorAll(sel).forEach(b => {
          if (!btns.includes(b) && b.getBoundingClientRect().width > 0) btns.push(b);
        });
      } catch(e) {}
    });
    return btns;
  }

  function scanAndSetup() {
    const ta = findTextArea();
    if (ta && !textAreaFound) {
      textAreaFound = true;
      ta.addEventListener('keydown', e => {
        if (e.key === 'Enter' && !e.shiftKey) injectTimestamp();
      }, true);
      log('✅ Zone texte trouvée');
    }
    const btns = findSendButtons();
    if (btns.length && !setupComplete) {
      btns.forEach(b => {
        b.addEventListener('mousedown', () => injectTimestamp(), true);
        b.addEventListener('mouseenter', () => {
          setTimeout(() => { if (b.matches(':hover')) injectTimestamp(); }, CONFIG.HOVER_DELAY);
        }, true);
      });
      setupComplete = true;
      log(`✅ ${btns.length} bouton(s) configuré(s)`);
    }
  }

  function injectTimestamp() {
    const now = Date.now();
    if (now - lastInjectionTime < CONFIG.INJECTION_COOLDOWN) return;
    
    const ta = findTextArea();
    if (!ta) return;
    
    const content = ta.tagName === 'TEXTAREA' ? ta.value : (ta.innerText || '');
    if (content.includes('[⏰') || !content.trim()) return;
    
    const ts = new Date().toISOString();
    const newContent = `[⏰ ${ts}]\n${content}`;
    
    if (ta.tagName === 'TEXTAREA') {
      ta.value = newContent;
    } else {
      ta.innerText = newContent;
    }
    ta.dispatchEvent(new Event('input', { bubbles: true }));
    
    lastInjectionTime = now;
    console.log('🕐✅ TIMESTAMP:', ts);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
