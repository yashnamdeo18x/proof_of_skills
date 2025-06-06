let's start.....


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>GitProofiX - Prove Your Developer Skills</title>
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {
      --primary: #4da6ff;
      --primary-dark: #1a73e8;
      --secondary: #000000;
      --accent: #000000;
      --dark: #0a0e17;
      --darker: #060913;
      --glass-bg: rgba(255, 255, 255, 0.05);
      --glass-border: rgba(255, 255, 255, 0.1);
      --text-light: #ffffff;
      --text-lighter: rgba(255, 255, 255, 0.9);
      --text-muted: rgba(255, 255, 255, 0.6);
      --gradient-primary: linear-gradient(135deg, var(--primary), var(--primary-dark));
      --gradient-accent: linear-gradient(135deg, var(--secondary), var(--accent));
      --gradient-dark: linear-gradient(135deg, var(--darker), var(--dark));
      --section-spacing: 120px;
      --border-radius: 16px;
      --box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
      --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.1);
      --glass-effect: backdrop-filter: blur(12px) saturate(180%);
      -webkit-backdrop-filter: blur(12px) saturate(180%);
      --leetcode-dark: #282828;
      --leetcode-light: #3a3a3a;
      --leetcode-green: #00b8a3;
      --leetcode-yellow: #ffc01e;
      --leetcode-red: #ff375f;
      --python-blue: #3776ab;
      --javascript-yellow: #f0db4f;
      --cpp-blue: #00599c;
      --css-orange: #2965f1;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      scroll-behavior: smooth;
    }

    body, html {
      height: 100%;
      overflow-x: hidden;
      color: var(--text-light);
      font-family: 'Poppins', sans-serif;
      background-color: var(--darker);
      background-image: 
        radial-gradient(circle at 25% 25%, rgba(77, 166, 255, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 75% 75%, rgba(255, 77, 141, 0.15) 0%, transparent 50%);
    }

    h1, h2, h3, h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 1.5rem;
    }

    h1 {
      font-size: clamp(2.5rem, 5vw, 4rem);
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      display: inline-block;
    }

    h2 {
      font-size: clamp(2rem, 4vw, 3rem);
      text-align: center;
      margin-bottom: 2.5rem;
      position: relative;
    }

    h2::after {
      content: '';
      display: block;
      width: 100px;
      height: 5px;
      background: var(--gradient-primary);
      margin: 1.5rem auto 0;
      border-radius: 5px;
    }

    h3 {
      font-size: clamp(1.5rem, 3vw, 2rem);
      margin-bottom: 1.25rem;
      color: var(--primary);
    }

    p {
      color: var(--text-lighter);
      margin-bottom: 1.5rem;
      font-weight: 300;
      font-size: 1.1rem;
      line-height: 1.7;
    }

    .text-center {
      text-align: center;
    }

    .container {
      max-width: 1300px;
      margin: 0 auto;
      padding: 0 30px;
    }

    section {
      padding: var(--section-spacing) 0;
      position: relative;
    }

    .section {
      background: var(--gradient-dark);
      position: relative;
      overflow: hidden;
    }

    .proof-section {
      background: var(--gradient-primary);
      text-align: center;
      color: white;
    }

    .navbar {
      background: rgba(10, 14, 23, 0.9);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      padding: 20px 50px;
      position: sticky;
      top: 0;
      z-index: 1000;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      border-bottom: 1px solid var(--glass-border);
      transition: var(--transition);
    }

    .navbar.scrolled {
      padding: 15px 50px;
      box-shadow: var(--box-shadow);
    }

    .hero-logo a {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--text-light);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .math-logo img {
      height: 43px;
      vertical-align: middle;
      margin-right: 1px;
      margin-bottom: 8px;
      margin-top: 2px;
    }

    .list {
      display: flex;
      list-style: none;
      gap: 30px;
    }

    .list a {
      color: var(--text-lighter);
      text-decoration: none;
      font-weight: 500;
      transition: var(--transition);
      position: relative;
      font-size: 1.1rem;
    }

    .list a::after {
      content: '';
      position: absolute;
      bottom: -5px;
      left: 0;
      width: 0;
      height: 2px;
      background: var(--primary);
      transition: var(--transition);
    }

    .list a:hover {
      color: var(--primary);
    }

    .list a:hover::after {
      width: 100%;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 14px 28px;
      border-radius: 50px;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      border: none;
      cursor: pointer;
      gap: 10px;
      font-size: 1.1rem;
      position: relative;
      overflow: hidden;
    }

    .btn::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(rgba(255,255,255,0.1), rgba(255,255,255,0));
      opacity: 0;
      transition: var(--transition);
    }

    .btn:hover::after {
      opacity: 1;
    }

    .btn-primary {
      background: var(--gradient-primary);
      color: white;
      box-shadow: 0 4px 20px rgba(77, 166, 255, 0.4);
    }

    .btn-primary:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 25px rgba(77, 166, 255, 0.6);
    }

    .btn-secondary {
      background: var(--gradient-accent);
      color: white;
      box-shadow: 0 4px 20px rgba(255, 77, 141, 0.4);
    }

    .btn-secondary:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 25px rgba(255, 77, 141, 0.6);
    }

    .btn-outline {
      background: transparent;
      color: var(--primary);
      border: 2px solid var(--primary);
    }

    .btn-outline:hover {
      background: var(--primary);
      color: white;
      box-shadow: 0 4px 20px rgba(77, 166, 255, 0.4);
    }

    .github-login-btn {
      background: #333;
      color: white;
      padding: 14px 28px;
      border-radius: 50px;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 1.1rem;
    }

    .github-login-btn:hover {
      background: #444;
      transform: translateY(-3px);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .hero-buttons {
      display: flex;
      gap: 20px;
      margin-top: 40px;
      flex-wrap: wrap;
    }

    .hero {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 100vh;
      padding: 0 50px;
      position: relative;
      overflow: hidden;
    }

    .hero::before {
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 800px;
      height: 800px;
      background: radial-gradient(circle, rgba(77, 166, 255, 0.15) 0%, rgba(77, 166, 255, 0) 70%);
      z-index: -1;
    }

    .hero-text {
      max-width: 600px;
      z-index: 1;
    }

    .hero-text p {
      font-size: 1.25rem;
      margin-bottom: 40px;
      color: var(--text-lighter);
    }

    #typed {
      display: block;
      min-height: 60px;
      font-size: 1.5rem;
      margin-bottom: 30px;
      color: var(--primary);
    }

    .hero-animation {
      width: 100%;
      max-width: none;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .features-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin-top: 60px;
    }

    .feature-card {
      background: var(--glass-bg);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border-radius: var(--border-radius);
      padding: 40px 30px;
      border: 1px solid var(--glass-border);
      transition: var(--transition);
      text-align: center;
      opacity: 0;
      transform: translateY(30px);
      box-shadow: var(--box-shadow);
    }

    .feature-card.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .feature-card:hover {
      transform: translateY(-10px) scale(1.02);
      box-shadow: 0 20px 40px rgba(77, 166, 255, 0.3);
      border-color: var(--primary);
    }

    .feature-animation {
      width: 100%;
      max-width: 200px;
      margin: 0 auto 30px;
      transition: var(--transition);
      filter: drop-shadow(0 5px 15px rgba(77, 166, 255, 0.2));
    }

    .feature-animation:hover {
      transform: translateY(-10px);
    }

    .pulse-animation {
      animation: pulse 3s infinite ease-in-out;
    }

    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }

    .float-animation {
      animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
      0% {
        transform: translateY(0px);
      }
      50% {
        transform: translateY(-15px);
      }
      100% {
        transform: translateY(0px);
      }
    }

    .animated-img {
      width: 800px;
      max-width: 90%;
      display: block;
      margin: auto;
    }

    .badge-rotate {
      animation: rotateBadge 10s linear infinite;
    }

    @keyframes rotateBadge {
      0% { transform: rotateY(0deg); }
      100% { transform: rotateY(360deg); }
    }

    .career-animation {
      animation: careerFloat 6s ease-in-out infinite;
    }

    @keyframes careerFloat {
      0% { transform: translateY(0px) rotate(0deg); }
      25% { transform: translateY(-15px) rotate(2deg); }
      50% { transform: translateY(0px) rotate(0deg); }
      75% { transform: translateY(-10px) rotate(-2deg); }
      100% { transform: translateY(0px) rotate(0deg); }
    }

    .skill-animation {
      animation: skillPulse 4s infinite ease-in-out;
    }

    @keyframes skillPulse {
      0% { transform: scale(1) rotate(0deg); }
      25% { transform: scale(1.03) rotate(1deg); }
      50% { transform: scale(1) rotate(0deg); }
      75% { transform: scale(1.02) rotate(-1deg); }
      100% { transform: scale(1) rotate(0deg); }
    }

    .analyzer-form {
      max-width: 600px;
      margin: 40px auto 0;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    input[type="text"] {
      width: 100%;
      padding: 18px 25px;
      border-radius: 50px;
      border: none;
      background: rgba(255, 255, 255, 0.1);
      color: white;
      font-size: 1.1rem;
      border: 1px solid rgba(255, 255, 255, 0.2);
      transition: var(--transition);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    input[type="text"]:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(77, 166, 255, 0.3);
    }

    input[type="text"]::placeholder {
      color: var(--text-muted);
    }

    .code-editor-preview {
      background: #1e1e1e;
      border-radius: var(--border-radius);
      padding: 20px;
      margin: 30px auto;
      max-width: 800px;
      box-shadow: var(--box-shadow);
      position: relative;
      overflow: hidden;
    }

    .editor-header {
      display: flex;
      gap: 8px;
      margin-bottom: 15px;
    }

    .editor-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }

    .editor-dot.red {
      background: #ff5f56;
    }

    .editor-dot.yellow {
      background: #ffbd2e;
    }

    .editor-dot.green {
      background: #27c93f;
    }

    .editor-content {
      font-family: 'Courier New', monospace;
      color: #d4d4d4;
      font-size: 0.9rem;
      line-height: 1.6;
      overflow-x: auto;
    }

    .editor-line {
      display: flex;
    }

    .line-number {
      color: #858585;
      min-width: 40px;
      text-align: right;
      padding-right: 10px;
      user-select: none;
    }

    .code-keyword {
      color: #569cd6;
    }

    .code-function {
      color: #dcdcaa;
    }

    .code-string {
      color: #ce9178;
    }

    .code-comment {
      color: #6a9955;
    }

    .badge-showcase {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 20px;
      margin: 40px auto;
      max-width: 800px;
    }

    .badge-item {
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--border-radius);
      padding: 20px;
      text-align: center;
      transition: var(--transition);
      border: 1px solid var(--glass-border);
    }

    .badge-item:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }

    .badge-icon {
      width: 80px;
      height: 80px;
      margin: 0 auto 15px;
      background: var(--gradient-primary);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
    }

    .badge-name {
      font-weight: 600;
      margin-bottom: 5px;
    }

    .badge-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .stats-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 40px auto;
      max-width: 800px;
    }

    .stat-card {
      background: rgba(255, 255, 255, 0.05);
      border-radius: var(--border-radius);
      padding: 30px 20px;
      text-align: center;
      border: 1px solid var(--glass-border);
    }

    .stat-value {
      font-size: 2.5rem;
      font-weight: 700;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      margin-bottom: 10px;
    }

    .stat-label {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    footer {
      background: var(--dark);
      padding: 50px 0 30px;
      text-align: center;
      border-top: 1px solid var(--glass-border);
      position: relative;
    }

    footer::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: url('https://assets-global.website-files.com/5f16d3f9836e6e4fbade7c9a/62b218b8a0d52b0b8b9d2b1a_noise.png') center/cover;
      opacity: 0.05;
      pointer-events: none;
    }

    footer p {
      margin-bottom: 20px;
      position: relative;
    }

    .social-links {
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-top: 30px;
      position: relative;
    }

    .social-links a {
      color: var(--text-lighter);
      width: 50px;
      height: 50px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.1);
      transition: var(--transition);
      font-size: 1.3rem;
    }

    .social-links a:hover {
      color: var(--primary);
      transform: translateY(-5px);
      background: rgba(77, 166, 255, 0.1);
      box-shadow: 0 5px 15px rgba(77, 166, 255, 0.2);
    }

    .blob {
      position: absolute;
      border-radius: 50%;
      filter: blur(60px);
      opacity: 0.2;
      z-index: -1;
    }

    .blob-1 {
      width: 500px;
      height: 500px;
      background: var(--primary);
      top: -200px;
      right: -200px;
    }

    .blob-2 {
      width: 400px;
      height: 400px;
      background: var(--secondary);
      bottom: -100px;
      left: -100px;
    }

    /* LeetCode-style Challenge Interface */
    .challenge-container {
      display: flex;
      flex-direction: column;
      max-width: 1200px;
      margin: 0 auto;
      background: var(--leetcode-dark);
      border-radius: var(--border-radius);
      overflow: hidden;
      box-shadow: var(--box-shadow);
    }

    .challenge-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      background: var(--leetcode-light);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .challenge-title {
      font-size: 1.5rem;
      font-weight: 600;
      color: var(--text-light);
    }

    .challenge-difficulty {
      padding: 5px 15px;
      border-radius: 20px;
      font-weight: 600;
      font-size: 0.9rem;
    }

    .difficulty-easy {
      background-color: rgba(0, 184, 163, 0.1);
      color: var(--leetcode-green);
    }

    .difficulty-medium {
      background-color: rgba(255, 192, 30, 0.1);
      color: var(--leetcode-yellow);
    }

    .difficulty-hard {
      background-color: rgba(255, 55, 95, 0.1);
      color: var(--leetcode-red);
    }

    .challenge-content {
      display: flex;
      min-height: 600px;
    }

    .problem-panel {
      flex: 1;
      padding: 20px;
      overflow-y: auto;
      border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    .problem-description {
      line-height: 1.6;
      color: var(--text-lighter);
    }

    .problem-description h3 {
      margin-top: 20px;
      color: var(--text-light);
    }

    .problem-description pre {
      background: rgba(0, 0, 0, 0.3);
      padding: 15px;
      border-radius: 5px;
      overflow-x: auto;
      margin: 15px 0;
    }

    .problem-description code {
      font-family: 'Courier New', monospace;
      font-size: 0.9rem;
    }

    .editor-panel {
      flex: 1;
      display: flex;
      flex-direction: column;
    }

    .code-editor {
      flex: 1;
      background: #1e1e1e;
      position: relative;
    }

    .editor-tabs {
      display: flex;
      background: #252526;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .editor-tab {
      padding: 10px 20px;
      cursor: pointer;
      color: var(--text-muted);
      font-size: 0.9rem;
      border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    .editor-tab.active {
      background: #1e1e1e;
      color: var(--text-light);
    }

    .editor-area {
      height: 100%;
      padding: 15px;
      font-family: 'Courier New', monospace;
      color: #d4d4d4;
      font-size: 0.95rem;
      line-height: 1.5;
      outline: none;
      white-space: pre;
      overflow: auto;
    }

    .editor-footer {
      background: #252526;
      padding: 15px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .language-selector {
      background: rgba(0, 0, 0, 0.3);
      color: var(--text-light);
      border: none;
      padding: 8px 15px;
      border-radius: 4px;
      font-size: 0.9rem;
    }

    .action-buttons {
      display: flex;
      gap: 10px;
    }

    .run-btn, .submit-btn {
      padding: 8px 20px;
      border-radius: 4px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      font-size: 0.9rem;
      transition: var(--transition);
    }

    .run-btn {
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-light);
    }

    .run-btn:hover {
      background: rgba(255, 255, 255, 0.2);
    }

    .submit-btn {
      background: var(--leetcode-green);
      color: white;
    }

    .submit-btn:hover {
      background: #00a893;
    }

    .test-cases {
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding: 15px;
      background: #252526;
    }

    .test-cases-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }

    .test-cases-title {
      font-weight: 600;
    }

    .test-case {
      background: rgba(0, 0, 0, 0.3);
      padding: 10px;
      border-radius: 4px;
      margin-bottom: 10px;
    }

    .test-case-title {
      font-weight: 600;
      margin-bottom: 5px;
      color: var(--text-light);
    }

    .test-case-content {
      font-family: 'Courier New', monospace;
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .test-case-result {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 5px;
      font-size: 0.85rem;
    }

    .result-success {
      color: var(--leetcode-green);
    }

    .result-failure {
      color: var(--leetcode-red);
    }

    /* Challenge List */
    .challenges-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 40px;
    }

    .challenge-card {
      background: var(--glass-bg);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border-radius: var(--border-radius);
      padding: 20px;
      border: 1px solid var(--glass-border);
      transition: var(--transition);
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }

    .challenge-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(77, 166, 255, 0.2);
    }

    .challenge-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 3px;
      height: 100%;
      background: var(--primary);
      transition: var(--transition);
    }

    .challenge-card:hover::before {
      width: 5px;
    }

    .challenge-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
    }

    .challenge-card-title {
      font-weight: 600;
      font-size: 1.1rem;
    }

    .challenge-card-difficulty {
      font-size: 0.8rem;
      padding: 3px 10px;
      border-radius: 20px;
    }

    .challenge-card-language {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-bottom: 10px;
      font-size: 0.9rem;
    }

    .challenge-card-description {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 15px;
    }

    .challenge-card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .challenge-card-stats {
      display: flex;
      gap: 15px;
    }

    .challenge-stat {
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .challenge-card-btn {
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 0.8rem;
      background: rgba(77, 166, 255, 0.1);
      color: var(--primary);
      border: none;
      cursor: pointer;
      transition: var(--transition);
    }

    .challenge-card-btn:hover {
      background: rgba(77, 166, 255, 0.2);
    }

    /* Language Tabs */
    .language-tabs {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 30px;
      flex-wrap: wrap;
    }

    .language-tab {
      padding: 10px 20px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: var(--text-lighter);
      cursor: pointer;
      transition: var(--transition);
      font-weight: 500;
    }

    .language-tab:hover {
      background: rgba(77, 166, 255, 0.2);
    }

    .language-tab.active {
      background: var(--primary);
      color: white;
      box-shadow: 0 4px 15px rgba(77, 166, 255, 0.3);
    }

    /* Language-specific colors */
    .python .challenge-card-language {
      color: var(--python-blue);
    }

    .javascript .challenge-card-language {
      color: var(--javascript-yellow);
    }

    .cpp .challenge-card-language {
      color: var(--cpp-blue);
    }

    .css .challenge-card-language {
      color: var(--css-orange);
    }

    .python:hover {
      border-color: var(--python-blue);
    }

    .javascript:hover {
      border-color: var(--javascript-yellow);
    }

    .cpp:hover {
      border-color: var(--cpp-blue);
    }

    .css:hover {
      border-color: var(--css-orange);
    }

    /* Output tab styling */
    #output-tab-content {
      display: none;
      padding: 15px;
      background: #1e1e1e;
      color: #d4d4d4;
      font-family: 'Courier New', monospace;
      white-space: pre-wrap;
      min-height: 200px;
      max-height: 300px;
      overflow-y: auto;
    }

    /* Responsive styles */
    @media (max-width: 1200px) {
      :root {
        --section-spacing: 100px;
      }
    }

    @media (max-width: 992px) {
      .hero {
        flex-direction: column;
        text-align: center;
        padding: 120px 30px 80px;
        min-height: auto;
      }

      .hero-text {
        margin-bottom: 60px;
        max-width: 100%;
      }

      .hero-buttons {
        justify-content: center;
      }

      .hero-animation {
        width: 100%;
        max-width: 450px;
      }

      .navbar {
        padding: 15px 30px;
      }

      .list {
        gap: 20px;
      }

      .challenge-content {
        flex-direction: column;
      }

      .problem-panel {
        border-right: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      }
    }

    @media (max-width: 768px) {
      :root {
        --section-spacing: 80px;
        --border-radius: 12px;
      }

      .navbar {
        flex-direction: column;
        gap: 15px;
        padding: 15px 20px;
      }

      .list {
        gap: 15px;
        flex-wrap: wrap;
        justify-content: center;
      }

      .hero {
        padding: 100px 20px 60px;
      }

      .hero-text p {
        font-size: 1.1rem;
      }

      #typed {
        font-size: 1.3rem;
        min-height: 50px;
      }

      .hero-buttons {
        flex-direction: column;
        gap: 15px;
      }

      .btn, .github-login-btn {
        width: 100%;
        justify-content: center;
      }

      .features-container {
        grid-template-columns: 1fr;
      }

      .badge-showcase {
        grid-template-columns: repeat(3, 1fr);
      }

      .challenges-list {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 480px) {
      :root {
        --section-spacing: 60px;
      }

      h1 {
        font-size: 2.2rem;
      }

      h2 {
        font-size: 1.8rem;
      }

      h2::after {
        width: 60px;
        height: 4px;
      }

      .container {
        padding: 0 20px;
      }

      .badge-showcase {
        grid-template-columns: repeat(2, 1fr);
      }
      
      .hero-logo a {
        font-size: 1.5rem;
      }
      
      .math-logo {
        font-size: 1.5rem;
      }

      .editor-footer {
        flex-direction: column;
        gap: 10px;
        align-items: flex-start;
      }

      .action-buttons {
        width: 100%;
      }

      .run-btn, .submit-btn {
        flex: 1;
      }

      .language-tabs {
        gap: 5px;
      }

      .language-tab {
        padding: 8px 15px;
        font-size: 0.9rem;
      }
    }
  </style>
</head>

<body>
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>

  <nav class="navbar" id="navbar">
    <div class="hero-logo">
      <a href="#">
        <span class="math-logo">
          <img src="static/image/logogit.png" alt="logo">
        </span>
        GitProofiX
      </a>
    </div>    
    
    <ul class="list">
      <li><a href="#home">Home</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#how-it-works">How It Works</a></li>
      <li><a href="#challenges">Challenges</a></li>
      <li><a href="#profile-demo">Profile</a></li>
      <li><a href="#about">About</a></li>
    </ul>
    
    <a href="{% url 'social:begin' 'github' %}" class="github-login-btn">
      <i class="fab fa-github"></i> Login with GitHub
    </a>
  </nav>

  <section class="hero" id="home">
    <div class="hero-text">
      <h1>Elevate Your Developer Profile</h1>
      <p>GitProofiX transforms your GitHub activity into verifiable credentials and NFT badges that prove your real-world coding skills. Stand out in the competitive tech industry with blockchain-verified proof of your abilities.</p>
      <span id="typed"></span>
      <div class="hero-buttons">
        <a href="#features" class="btn btn-primary"><i class="fas fa-rocket"></i> Explore Features</a>
        <a href="{% url 'social:begin' 'github' %}" class="btn btn-secondary"><i class="fab fa-github"></i> Connect GitHub</a>
      </div>
    </div>
    <div class="hero-animation float-animation">
      <img src="static/image/side.png" alt="Developer Scene" class="animated-img">
    </div>    
  </section>

  <section class="section" id="features">
    <div class="container">
      <h2>Developer Credentials Reimagined</h2>
      <p class="text-center">GitProofiX helps developers prove their skills through verifiable achievements and blockchain technology</p>
      
      <div class="features-container">
        <div class="feature-card">
          <div class="feature-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_vybwn7df.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>GitHub Verification</h3>
          <p>Submit any GitHub repository for analysis. Our system evaluates code quality, complexity, and originality. Verified repos earn NFT badges that prove your development skills.</p>
          <a href="#analyzer-demo" class="btn btn-outline" style="margin-top: 15px;">Try Analyzer</a>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_5tkzkblw.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>Coding Challenges</h3>
          <p>Compete in real-time coding battles against other developers. Solve problems under time pressure to demonstrate your problem-solving skills and earn ranking points.</p>
          <a href="#challenges" class="btn btn-outline" style="margin-top: 15px;">Join Battle</a>
        </div>
      
        <div class="feature-card">
          <div class="feature-animation skill-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_uk2g9zkh.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>Skill Assessment</h3>
          <p>Complete our curated coding challenges in various technologies. Earn skill badges and GITProofiX points that showcase your expertise in specific programming languages.</p>
          <a href="#skill-demo" class="btn btn-outline" style="margin-top: 15px;">Test Skills</a>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation">
            <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_1a8dx7zj.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>NFT Achievements</h3>
          <p>Mint unique NFT badges for your verified accomplishments. These blockchain-based credentials serve as tamper-proof evidence of your development skills.</p>
          <a href="#badges-demo" class="btn btn-outline" style="margin-top: 15px;">View Badges</a>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_2cwDXD.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>Developer Portfolio</h3>
          <p>Showcase your verified skills, badges, and achievements in a professional portfolio. Share your profile with employers or clients as proof of your abilities.</p>
          <a href="#profile-demo" class="btn btn-outline" style="margin-top: 15px;">See Profile</a>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation career-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_5ifqtlsi.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>Career Opportunities</h3>
          <p>Get matched with tech companies looking for developers with your verified skill set. Your GitProofiX profile serves as a trusted credential for job applications.</p>
          <a href="#contact" class="btn btn-outline" style="margin-top: 15px;">Find Jobs</a>
        </div>
      </div>
    </div>
  </section>

  <section class="proof-section" id="how-it-works">
    <div class="container">
      <h2>How GitProofiX Works</h2>
      <p class="text-center" style="max-width: 800px; margin: 0 auto 40px;">
        Our four-step process makes it easy to verify your skills and build your developer reputation
      </p>
      
      <div class="features-container">
        <div class="feature-card">
          <div class="feature-animation pulse-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_5tkzkblw.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>1. Connect GitHub</h3>
          <p>Securely link your GitHub account to analyze your repositories and contribution history. We only request read access to evaluate your public work.</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation pulse-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_vybwn7df.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>2. Verify Skills</h3>
          <p>Our system evaluates your code quality, complexity, and project impact. We check for originality and meaningful contributions to prevent gaming the system.</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation pulse-animation">
            <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_1a8dx7zj.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>3. Earn Badges</h3>
          <p>Receive verifiable credentials and NFT badges for your achievements. Each badge represents a specific skill or accomplishment you've demonstrated.</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-animation pulse-animation">
            <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_2cwDXD.json" background="transparent" speed="1" loop autoplay></lottie-player>
          </div>
          <h3>4. Showcase Talent</h3>
          <p>Build your professional portfolio and share your verified skills. Export your profile as HTML, JSON, or an image to include in resumes or applications.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Enhanced Coding Challenges Section -->
  <section class="section" id="challenges">
    <div class="container">
      <h2>Coding Challenges</h2>
      <p class="text-center">Test your skills with our curated coding challenges across multiple languages</p>
      
      <!-- Language Selector Tabs -->
      <div class="language-tabs">
        <button class="language-tab active" onclick="filterChallenges('all')">All Languages</button>
        <button class="language-tab" onclick="filterChallenges('python')"><i class="fab fa-python"></i> Python</button>
        <button class="language-tab" onclick="filterChallenges('javascript')"><i class="fab fa-js"></i> JavaScript</button>
        <button class="language-tab" onclick="filterChallenges('cpp')"><i class="fas fa-code"></i> C++</button>
        <button class="language-tab" onclick="filterChallenges('css')"><i class="fab fa-css3-alt"></i> CSS</button>
      </div>
      
      <!-- Challenge List -->
      <div class="challenges-list">
        <!-- Python Challenges -->
        <div class="challenge-card python" onclick="loadPythonChallenge(1)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Sum of Two Numbers</div>
            <div class="challenge-card-difficulty difficulty-easy">Easy</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-python"></i> Python
          </div>
          <div class="challenge-card-description">
            Write a function that takes two numbers and returns their sum.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 92% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 100 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card python" onclick="loadPythonChallenge(2)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">List Comprehension</div>
            <div class="challenge-card-difficulty difficulty-medium">Medium</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-python"></i> Python
          </div>
          <div class="challenge-card-description">
            Create a list comprehension that squares even numbers and cubes odd numbers from 1 to 20.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 68% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 250 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card python" onclick="loadPythonChallenge(3)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Decorator Performance</div>
            <div class="challenge-card-difficulty difficulty-hard">Hard</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-python"></i> Python
          </div>
          <div class="challenge-card-description">
            Create a decorator that logs the execution time of any function and caches its results.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 42% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 500 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <!-- JavaScript Challenges -->
        <div class="challenge-card javascript" onclick="loadJSChallenge(1)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Array Manipulation</div>
            <div class="challenge-card-difficulty difficulty-easy">Easy</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-js"></i> JavaScript
          </div>
          <div class="challenge-card-description">
            Write a function to remove duplicates from an array and return the new length.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 88% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 150 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card javascript" onclick="loadJSChallenge(2)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Promise Chain</div>
            <div class="challenge-card-difficulty difficulty-medium">Medium</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-js"></i> JavaScript
          </div>
          <div class="challenge-card-description">
            Implement a promise chain that fetches data from 3 different APIs sequentially.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 55% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 300 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card javascript" onclick="loadJSChallenge(3)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Custom Observable</div>
            <div class="challenge-card-difficulty difficulty-hard">Hard</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-js"></i> JavaScript
          </div>
          <div class="challenge-card-description">
            Implement a custom Observable class with subscribe, next, and complete methods.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 35% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 550 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <!-- C++ Challenges -->
        <div class="challenge-card cpp" onclick="loadCppChallenge(1)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Basic I/O</div>
            <div class="challenge-card-difficulty difficulty-easy">Easy</div>
          </div>
          <div class="challenge-card-language">
            <i class="fas fa-code"></i> C++
          </div>
          <div class="challenge-card-description">
            Write a program that reads two integers and prints their sum, difference, product, and quotient.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 90% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 120 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card cpp" onclick="loadCppChallenge(2)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Class Inheritance</div>
            <div class="challenge-card-difficulty difficulty-medium">Medium</div>
          </div>
          <div class="challenge-card-language">
            <i class="fas fa-code"></i> C++
          </div>
          <div class="challenge-card-description">
            Implement a base Shape class with derived Circle and Rectangle classes calculating area.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 60% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 350 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card cpp" onclick="loadCppChallenge(3)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Smart Pointer</div>
            <div class="challenge-card-difficulty difficulty-hard">Hard</div>
          </div>
          <div class="challenge-card-language">
            <i class="fas fa-code"></i> C++
          </div>
          <div class="challenge-card-description">
            Implement a custom smart pointer class with reference counting and ownership transfer.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 30% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 600 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <!-- CSS Challenges -->
        <div class="challenge-card css" onclick="loadCSSChallenge(1)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Center Elements</div>
            <div class="challenge-card-difficulty difficulty-easy">Easy</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-css3-alt"></i> CSS
          </div>
          <div class="challenge-card-description">
            Center a div both horizontally and vertically using 3 different CSS methods.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 85% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 100 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card css" onclick="loadCSSChallenge(2)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">Grid Layout</div>
            <div class="challenge-card-difficulty difficulty-medium">Medium</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-css3-alt"></i> CSS
          </div>
          <div class="challenge-card-description">
            Create a responsive photo gallery using CSS Grid with specific breakpoints.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 58% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 250 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
        
        <div class="challenge-card css" onclick="loadCSSChallenge(3)">
          <div class="challenge-card-header">
            <div class="challenge-card-title">3D Animation</div>
            <div class="challenge-card-difficulty difficulty-hard">Hard</div>
          </div>
          <div class="challenge-card-language">
            <i class="fab fa-css3-alt"></i> CSS
          </div>
          <div class="challenge-card-description">
            Create a 3D cube that rotates on hover using only CSS transforms and transitions.
          </div>
          <div class="challenge-card-footer">
            <div class="challenge-card-stats">
              <div class="challenge-stat">
                <i class="fas fa-users"></i> 38% solved
              </div>
              <div class="challenge-stat">
                <i class="fas fa-star"></i> 400 points
              </div>
            </div>
            <button class="challenge-card-btn">Solve Challenge</button>
          </div>
        </div>
      </div>
      
      <!-- Challenge Editor (hidden by default) -->
      <div id="challenge-editor" style="display: none; margin-top: 50px;">
        <div class="challenge-container">
          <div class="challenge-header">
            <div class="challenge-title" id="challenge-title">Challenge Title</div>
            <div class="challenge-difficulty" id="challenge-difficulty">Easy</div>
          </div>
          
          <div class="challenge-content">
            <div class="problem-panel">
              <div class="problem-description" id="problem-description">
                <!-- Problem description will be loaded here -->
              </div>
            </div>
            
            <div class="editor-panel">
              <div class="editor-tabs">
                <div class="editor-tab active" id="solution-tab">Solution</div>
                <div class="editor-tab" id="output-tab">Output</div>
              </div>
              
              <div class="code-editor">
                <div class="editor-area" id="code-editor" contenteditable="true">
                  <!-- Code editor content will be loaded here -->
                </div>
                <div id="output-tab-content">
                  <!-- Output will be displayed here -->
                </div>
              </div>
              
              <div class="editor-footer">
                <select class="language-selector" id="language-selector">
                  <option value="python">Python</option>
                  <option value="javascript">JavaScript</option>
                  <option value="cpp">C++</option>
                  <option value="css">CSS</option>
                </select>
                
                <div class="action-buttons">
                  <button class="run-btn"><i class="fas fa-play"></i> Run</button>
                  <button class="submit-btn"><i class="fas fa-check"></i> Submit</button>
                </div>
              </div>
              
              <div class="test-cases">
                <div class="test-cases-header">
                  <div class="test-cases-title">Test Cases</div>
                </div>
                
                <div id="test-cases-container">
                  <!-- Test cases will be loaded here -->
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="hero-buttons" style="justify-content: center; margin-top: 30px;">
          <button class="btn btn-outline" onclick="backToChallenges()">
            <i class="fas fa-arrow-left"></i> Back to Challenges
          </button>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="analyzer-demo">
    <div class="container">
      <h2>GitHub Repository Analyzer</h2>
      <p class="text-center">Submit your GitHub repository for comprehensive analysis and earn your first verified badge</p>
      
      <div class="feature-animation float-animation" style="max-width: 400px; margin: 0 auto;">
        <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_vybwn7df.json" background="transparent" speed="1" loop autoplay></lottie-player>
      </div>
      
      <div class="analyzer-form">
        <input type="text" placeholder="https://github.com/username/repository" />
        <button class="btn btn-primary" style="width: 100%;">
          <i class="fas fa-search"></i> Analyze Repository
        </button>
      </div>
      
      <div class="features-container" style="margin-top: 60px;">
        <div class="feature-card">
          <i class="fas fa-code" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Code Quality</h3>
          <p>We evaluate readability, structure, and best practices in your codebase. Our analysis considers maintainability, documentation, and adherence to language conventions.</p>
        </div>
        
        <div class="feature-card">
          <i class="fas fa-project-diagram" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Project Complexity</h3>
          <p>Analysis of architecture, dependencies, and technical sophistication. We assess how your project demonstrates real-world development skills beyond simple tutorials.</p>
        </div>
        
        <div class="feature-card">
          <i class="fas fa-users" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Collaboration</h3>
          <p>Assessment of your teamwork through issues, PRs, and code reviews. Open source contributions and collaborative projects earn higher verification scores.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="skill-demo">
    <div class="container">
      <h2>Skill Assessment Arena</h2>
      <p class="text-center">Test your skills with our curated coding challenges and earn points</p>
      
      <div class="feature-animation skill-animation" style="max-width: 400px; margin: 0 auto;">
        <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_uk2g9zkh.json" background="transparent" speed="1" loop autoplay></lottie-player>
      </div>
      
      <div class="features-container" style="margin-top: 60px;">
        <div class="feature-card">
          <i class="fas fa-laptop-code" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Language-Specific Tests</h3>
          <p>Choose from challenges in JavaScript, Python, Java, C++, and more. Each test is designed to evaluate your proficiency in the selected language.</p>
        </div>
        
        <div class="feature-card">
          <i class="fas fa-layer-group" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Difficulty Levels</h3>
          <p>Problems range from beginner to expert level. Start with easier challenges and work your way up as you improve your skills and confidence.</p>
        </div>
        
        <div class="feature-card">
          <i class="fas fa-star" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 15px;"></i>
          <h3>Earn Points</h3>
          <p>Complete challenges to earn GitProofiX points. More difficult problems award more points, helping you climb the leaderboard faster.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="badges-demo">
    <div class="container">
      <h2>Verifiable Developer Credentials</h2>
      <p class="text-center">Your achievements, permanently recorded on the blockchain</p>
      
      <div class="feature-animation badge-rotate" style="max-width: 300px; margin: 0 auto;">
        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_1a8dx7zj.json" background="transparent" speed="1" loop autoplay></lottie-player>
      </div>
      
      <div class="hero-buttons" style="justify-content: center; margin: 40px auto;">
        <a href="#" class="btn btn-primary"><i class="fas fa-image"></i> View Badge Gallery</a>
        <a href="#" class="btn btn-outline"><i class="fas fa-share-alt"></i> Share Your Profile</a>
      </div>
      
      <div class="badge-showcase">
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fas fa-code"></i>
          </div>
          <div class="badge-name">Code Quality</div>
          <div class="badge-desc">Awarded for clean, maintainable code</div>
        </div>
        
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fas fa-brain"></i>
          </div>
          <div class="badge-name">Algorithm Expert</div>
          <div class="badge-desc">For solving complex problems</div>
        </div>
        
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fas fa-users"></i>
          </div>
          <div class="badge-name">Team Player</div>
          <div class="badge-desc">Great collaboration skills</div>
        </div>
        
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fas fa-trophy"></i>
          </div>
          <div class="badge-name">Battle Champion</div>
          <div class="badge-desc">Won coding competitions</div>
        </div>
        
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fab fa-js"></i>
          </div>
          <div class="badge-name">JavaScript Pro</div>
          <div class="badge-desc">Advanced JS skills</div>
        </div>
        
        <div class="badge-item">
          <div class="badge-icon">
            <i class="fas fa-server"></i>
          </div>
          <div class="badge-name">Backend Expert</div>
          <div class="badge-desc">Server-side mastery</div>
        </div>
      </div>
    </div>
  </section>

  <section class="proof-section" id="profile-demo">
    <div class="container">
      <h2>Your Developer Profile</h2>
      <p class="text-center">Showcase your verified skills and achievements to potential employers</p>
      
      <div class="feature-animation" style="max-width: 400px; margin: 0 auto;">
        <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_2cwDXD.json" background="transparent" speed="1" loop autoplay></lottie-player>
      </div>
      
      <div class="stats-container">
        <div class="stat-card">
          <div class="stat-value">24</div>
          <div class="stat-label">Repos Analyzed</div>
        </div>
        
        <div class="stat-card">
          <div class="stat-value">15</div>
          <div class="stat-label">NFT Badges</div>
        </div>
        
        <div class="stat-card">
          <div class="stat-value">8</div>
          <div class="stat-label">Battles Won</div>
        </div>
        
        <div class="stat-card">
          <div class="stat-value">1,245</div>
          <div class="stat-label">GitProofiX Points</div>
        </div>
      </div>
      
      <div class="hero-buttons" style="justify-content: center; margin-top: 40px;">
        <a href="#" class="btn btn-primary"><i class="fas fa-file-export"></i> Export Profile</a>
        <a href="#" class="btn btn-secondary"><i class="fas fa-eye"></i> View Public Profile</a>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="container">
      <h2>About GitProofiX</h2>
      <p class="text-center" style="max-width: 800px; margin: 0 auto 50px;">
        We're revolutionizing how developers prove their skills in an era where traditional credentials often fail to capture real-world abilities. 
        Our platform combines GitHub analysis, coding challenges, and blockchain technology to create verifiable proof of your development expertise.
      </p>
      
      <div class="features-container">
        <div class="feature-card">
          <h3>Our Mission</h3>
          <p>To create a more meritocratic tech industry where developers are recognized for their actual skills rather than just their resumes. We believe talent should be measured by output, not pedigree.</p>
        </div>
        
        <div class="feature-card">
          <h3>The Problem</h3>
          <p>Traditional hiring processes often overlook talented developers who don't fit conventional molds or have non-traditional backgrounds. Degrees and certifications don't always reflect real coding ability.</p>
        </div>
        
        <div class="feature-card">
          <h3>The Solution</h3>
          <p>Objective, verifiable credentials based on actual code and problem-solving abilities rather than self-reported skills. GitProofiX provides tangible proof of what you can do, not just what you say you can do.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="proof-section" id="contact">
    <div class="container">
      <h2>Ready to Prove Your Skills?</h2>
      <p class="text-center" style="max-width: 600px; margin: 0 auto 30px;">
        Join thousands of developers who are building verifiable portfolios with GitProofiX. Start showcasing your real skills today.
      </p>
      
      <div class="hero-buttons" style="justify-content: center;">
        <a href="{% url 'social:begin' 'github' %}" class="btn btn-primary" style="font-size: 1.2rem; padding: 18px 36px;">
          <i class="fab fa-github"></i> Connect GitHub & Get Started
        </a>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <p>&copy; 2025 GitProofiX. All rights reserved.</p>
      <div class="social-links">
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-discord"></i></a>
        <a href="#"><i class="fab fa-github"></i></a>
        <a href="#"><i class="fab fa-linkedin"></i></a>
      </div>
    </div>
  </footer>

  <script>
    var typed = new Typed("#typed", {
      strings: [
        "Analyze your GitHub repositories.",
        "Compete in coding challenges.",
        "Earn verifiable NFT badges.",
        "Build your developer reputation.",
        "Stand out to employers.",
        "Prove your skills objectively."
      ],
      typeSpeed: 50,
      backSpeed: 25,
      loop: true,
      smartBackspace: true,
      showCursor: true,
      cursorChar: '|'
    });

    window.addEventListener('scroll', function() {
      const navbar = document.getElementById('navbar');
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });

    document.addEventListener('DOMContentLoaded', function() {
      const featureCards = document.querySelectorAll('.feature-card');
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
          if (entry.isIntersecting) {
            setTimeout(() => {
              entry.target.classList.add('visible');
            }, index * 150);
          }
        });
      }, { 
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
      });
      
      featureCards.forEach(card => {
        observer.observe(card);
      });

      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
          e.preventDefault();
          const target = document.querySelector(this.getAttribute('href'));
          if (target) {
            window.scrollTo({
              top: target.offsetTop - 80,
              behavior: 'smooth'
            });
          }
        });
      });
    });

    // Challenge filtering function
    function filterChallenges(language) {
      const challenges = document.querySelectorAll('.challenge-card');
      const tabs = document.querySelectorAll('.language-tab');
      
      // Update active tab
      tabs.forEach(tab => {
        if (tab.textContent.includes(language.charAt(0).toUpperCase() + language.slice(1)) || 
            (language === 'all' && tab.textContent.includes('All'))) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });
      
      // Show/hide challenges based on language filter
      challenges.forEach(challenge => {
        if (language === 'all' || challenge.classList.contains(language)) {
          challenge.style.display = 'block';
        } else {
          challenge.style.display = 'none';
        }
      });
    }

    // Challenge loading functions for each language
    function loadPythonChallenge(challengeId) {
      const challengesList = document.querySelector('.challenges-list');
      const challengeEditor = document.getElementById('challenge-editor');
      
      // Update challenge details based on ID
      if (challengeId === 1) {
        document.getElementById('challenge-title').textContent = 'Sum of Two Numbers';
        document.getElementById('challenge-difficulty').textContent = 'Easy';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-easy';
        document.getElementById('problem-description').innerHTML = `
          <p>Write a function called <code>sum_two_numbers</code> that takes two numbers as arguments and returns their sum.</p>
          
          <h3>Example 1:</h3>
          <pre>Input: a = 5, b = 3
Output: 8</pre>
          
          <h3>Example 2:</h3>
          <pre>Input: a = -2, b = 7
Output: 5</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li><code>-10<sup>9</sup> &lt;= a, b &lt;= 10<sup>9</sup></code></li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `def sum_two_numbers(a, b):
    # Your code here
    pass`;
        
        // Set up test cases
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Input: a = 5, b = 3</div>
            <div class="test-case-content">Expected Output: 8</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Input: a = -2, b = 7</div>
            <div class="test-case-content">Expected Output: 5</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 3</div>
            <div class="test-case-content">Input: a = 0, b = 0</div>
            <div class="test-case-content">Expected Output: 0</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 2) {
        document.getElementById('challenge-title').textContent = 'List Comprehension';
        document.getElementById('challenge-difficulty').textContent = 'Medium';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-medium';
        document.getElementById('problem-description').innerHTML = `
          <p>Create a list comprehension that generates a list of numbers from 1 to 20 where:</p>
          <ul>
            <li>Even numbers are squared</li>
            <li>Odd numbers are cubed</li>
          </ul>
          
          <h3>Example Output:</h3>
          <pre>[1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400]</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Must be done in a single list comprehension</li>
            <li>No external functions or libraries</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `# Write your list comprehension here
result = None`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Check for correct transformation of numbers 1-20</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 3) {
        document.getElementById('challenge-title').textContent = 'Decorator Performance';
        document.getElementById('challenge-difficulty').textContent = 'Hard';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-hard';
        document.getElementById('problem-description').innerHTML = `
          <p>Create a decorator called <code>timed_cache</code> that:</p>
          <ol>
            <li>Logs the execution time of the decorated function</li>
            <li>Caches the results for 5 seconds</li>
            <li>Returns cached results if available and not expired</li>
          </ol>
          
          <h3>Example Usage:</h3>
          <pre>@timed_cache
def expensive_operation(x):
    time.sleep(1)  # Simulate slow operation
    return x * x</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Must work with functions that have any number of positional arguments</li>
            <li>Cache should be per-function and per-arguments</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `import time
from functools import wraps

def timed_cache(func):
    # Your decorator implementation here
    pass`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Check that same inputs return cached results within 5 seconds</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify execution time is logged</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      }
      
      // Set language selector to Python
      document.getElementById('language-selector').value = 'python';
      
      challengesList.style.display = 'none';
      challengeEditor.style.display = 'block';
      
      // Scroll to challenge editor
      window.scrollTo({
        top: challengeEditor.offsetTop - 80,
        behavior: 'smooth'
      });
    }

    function loadJSChallenge(challengeId) {
      const challengesList = document.querySelector('.challenges-list');
      const challengeEditor = document.getElementById('challenge-editor');
      
      // Update challenge details based on ID
      if (challengeId === 1) {
        document.getElementById('challenge-title').textContent = 'Array Manipulation';
        document.getElementById('challenge-difficulty').textContent = 'Easy';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-easy';
        document.getElementById('problem-description').innerHTML = `
          <p>Write a function called <code>removeDuplicates</code> that takes an array and returns a new array with duplicates removed.</p>
          
          <h3>Example 1:</h3>
          <pre>Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]</pre>
          
          <h3>Example 2:</h3>
          <pre>Input: ['a', 'b', 'a', 'c', 'b']
Output: ['a', 'b', 'c']</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Must maintain original order of first occurrences</li>
            <li>Should work with any data type</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `function removeDuplicates(arr) {
    // Your code here
}`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Input: [1, 2, 2, 3, 4, 4, 5]</div>
            <div class="test-case-content">Expected Output: [1, 2, 3, 4, 5]</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Input: ['a', 'b', 'a', 'c', 'b']</div>
            <div class="test-case-content">Expected Output: ['a', 'b', 'c']</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 2) {
        document.getElementById('challenge-title').textContent = 'Promise Chain';
        document.getElementById('challenge-difficulty').textContent = 'Medium';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-medium';
        document.getElementById('problem-description').innerHTML = `
          <p>Implement a function called <code>fetchSequentially</code> that:</p>
          <ol>
            <li>Takes an array of API URLs</li>
            <li>Fetches data from each API one after another (not in parallel)</li>
            <li>Returns a promise that resolves with an array of results in the same order</li>
          </ol>
          
          <h3>Example Usage:</h3>
          <pre>fetchSequentially([
  'https://api.example.com/data/1',
  'https://api.example.com/data/2',
  'https://api.example.com/data/3'
]).then(results => {
  console.log(results); // Array of responses in order
});</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Must use native fetch (no libraries)</li>
            <li>Must handle errors gracefully (skip failed requests but maintain order)</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `function fetchSequentially(urls) {
    // Your implementation here
}`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify sequential execution and order preservation</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 3) {
        document.getElementById('challenge-title').textContent = 'Custom Observable';
        document.getElementById('challenge-difficulty').textContent = 'Hard';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-hard';
        document.getElementById('problem-description').innerHTML = `
          <p>Implement an <code>Observable</code> class with the following methods:</p>
          <ul>
            <li><code>subscribe(observer)</code> - Registers an observer</li>
            <li><code>next(value)</code> - Notifies all observers with a value</li>
            <li><code>complete()</code> - Notifies observers that the stream is complete</li>
          </ul>
          
          <h3>Example Usage:</h3>
          <pre>const observable = new Observable();
observable.subscribe({
  next: val => console.log('Got:', val),
  complete: () => console.log('Done')
});

observable.next(1);
observable.next(2);
observable.complete();</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Should support multiple observers</li>
            <li>Should ignore calls to next() after complete()</li>
            <li>Observers should be objects with next and complete methods</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `class Observable {
    // Your implementation here
}`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify notification to multiple observers</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Check complete() behavior</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      }
      
      // Set language selector to JavaScript
      document.getElementById('language-selector').value = 'javascript';
      
      challengesList.style.display = 'none';
      challengeEditor.style.display = 'block';
      
      // Scroll to challenge editor
      window.scrollTo({
        top: challengeEditor.offsetTop - 80,
        behavior: 'smooth'
      });
    }

    function loadCppChallenge(challengeId) {
      const challengesList = document.querySelector('.challenges-list');
      const challengeEditor = document.getElementById('challenge-editor');
      
      // Update challenge details based on ID
      if (challengeId === 1) {
        document.getElementById('challenge-title').textContent = 'Basic I/O';
        document.getElementById('challenge-difficulty').textContent = 'Easy';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-easy';
        document.getElementById('problem-description').innerHTML = `
          <p>Write a program that:</p>
          <ol>
            <li>Reads two integers from standard input</li>
            <li>Prints their sum, difference, product, and quotient</li>
          </ol>
          
          <h3>Example Input:</h3>
          <pre>10 2</pre>
          
          <h3>Example Output:</h3>
          <pre>Sum: 12
Difference: 8
Product: 20
Quotient: 5</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Handle division by zero gracefully</li>
            <li>Use only standard C++ libraries</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `#include <iostream>
using namespace std;

int main() {
    // Your code here
    return 0;
}`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Input: 10 2</div>
            <div class="test-case-content">Expected Output: Sum: 12, Difference: 8, Product: 20, Quotient: 5</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Input: 5 0</div>
            <div class="test-case-content">Expected Output: Sum: 5, Difference: 5, Product: 0, Quotient: undefined (handle error)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 2) {
        document.getElementById('challenge-title').textContent = 'Class Inheritance';
        document.getElementById('challenge-difficulty').textContent = 'Medium';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-medium';
        document.getElementById('problem-description').innerHTML = `
          <p>Implement a class hierarchy for geometric shapes:</p>
          <ol>
            <li>Base <code>Shape</code> class with pure virtual <code>area()</code> method</li>
            <li><code>Circle</code> class that inherits from <code>Shape</code> and implements <code>area()</code></li>
            <li><code>Rectangle</code> class that inherits from <code>Shape</code> and implements <code>area()</code></li>
          </ol>
          
          <h3>Example Usage:</h3>
          <pre>Circle c(5.0);
Rectangle r(4.0, 6.0);
cout << "Circle area: " << c.area() << endl;
cout << "Rectangle area: " << r.area() << endl;</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Use proper access modifiers</li>
            <li>Implement constructors for each class</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `#include <iostream>
#include <cmath>
using namespace std;

// Your class implementations here`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify Circle area calculation (radius = 5)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify Rectangle area calculation (4x6)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 3) {
        document.getElementById('challenge-title').textContent = 'Smart Pointer';
        document.getElementById('challenge-difficulty').textContent = 'Hard';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-hard';
        document.getElementById('problem-description').innerHTML = `
          <p>Implement a simplified <code>SmartPointer</code> class with:</p>
          <ol>
            <li>Reference counting</li>
            <li>Ownership transfer semantics</li>
            <li>Proper copy constructor and assignment operator</li>
          </ol>
          
          <h3>Example Usage:</h3>
          <pre>SmartPointer<int> p1(new int(42));
SmartPointer<int> p2 = p1; // Reference count increases
SmartPointer<int> p3;
p3 = p2; // Reference count increases
// When all go out of scope, memory is freed</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Must handle all memory management correctly</li>
            <li>Should prevent memory leaks</li>
            <li>Implement move semantics</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `template <typename T>
class SmartPointer {
    // Your implementation here
};`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify reference counting</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify memory cleanup</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      }
      
      // Set language selector to C++
      document.getElementById('language-selector').value = 'cpp';
      
      challengesList.style.display = 'none';
      challengeEditor.style.display = 'block';
      
      // Scroll to challenge editor
      window.scrollTo({
        top: challengeEditor.offsetTop - 80,
        behavior: 'smooth'
      });
    }

    function loadCSSChallenge(challengeId) {
      const challengesList = document.querySelector('.challenges-list');
      const challengeEditor = document.getElementById('challenge-editor');
      
      // Update challenge details based on ID
      if (challengeId === 1) {
        document.getElementById('challenge-title').textContent = 'Center Elements';
        document.getElementById('challenge-difficulty').textContent = 'Easy';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-easy';
        document.getElementById('problem-description').innerHTML = `
          <p>Implement three different methods to center a div both horizontally and vertically:</p>
          <ol>
            <li>Using Flexbox</li>
            <li>Using Grid</li>
            <li>Using Position and Transform</li>
          </ol>
          
          <h3>HTML Structure:</h3>
          <pre>&lt;div class="container"&gt;
  &lt;div class="centered-box"&gt;Content&lt;/div&gt;
&lt;/div&gt;</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Container should fill the viewport</li>
            <li>Centered box should be 200px × 200px with visible border</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `/* Flexbox Solution */
.container-flex {
  /* Your code here */
}

/* Grid Solution */
.container-grid {
  /* Your code here */
}

/* Position Solution */
.container-position {
  /* Your code here */
}`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify Flexbox centering</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify Grid centering</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 3</div>
            <div class="test-case-content">Verify Position centering</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 2) {
        document.getElementById('challenge-title').textContent = 'Grid Layout';
        document.getElementById('challenge-difficulty').textContent = 'Medium';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-medium';
        document.getElementById('problem-description').innerHTML = `
          <p>Create a responsive photo gallery using CSS Grid with the following requirements:</p>
          <ol>
            <li>3 columns on desktop (> 992px)</li>
            <li>2 columns on tablet (768px - 992px)</li>
            <li>1 column on mobile (< 768px)</li>
            <li>Gap between items should be 20px</li>
            <li>Images should maintain aspect ratio and fill their containers</li>
          </ol>
          
          <h3>HTML Structure:</h3>
          <pre>&lt;div class="gallery"&gt;
  &lt;div class="gallery-item"&gt;&lt;img src="image1.jpg"&gt;&lt;/div&gt;
  &lt;div class="gallery-item"&gt;&lt;img src="image2.jpg"&gt;&lt;/div&gt;
  &lt;!-- More items --&gt;
&lt;/div&gt;</pre>
        `;
        document.getElementById('code-editor').innerHTML = `.gallery {
  /* Your grid implementation here */
}

/* Add media queries for responsiveness */`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify desktop layout (3 columns)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify tablet layout (2 columns)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 3</div>
            <div class="test-case-content">Verify mobile layout (1 column)</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      } else if (challengeId === 3) {
        document.getElementById('challenge-title').textContent = '3D Animation';
        document.getElementById('challenge-difficulty').textContent = 'Hard';
        document.getElementById('challenge-difficulty').className = 'challenge-difficulty difficulty-hard';
        document.getElementById('problem-description').innerHTML = `
          <p>Create a 3D cube that:</p>
          <ol>
            <li>Has 6 faces with different colors</li>
            <li>Rotates continuously on the Y-axis</li>
            <li>Pauses rotation on hover</li>
            <li>Has a smooth transition when interaction changes</li>
          </ol>
          
          <h3>HTML Structure:</h3>
          <pre>&lt;div class="scene"&gt;
  &lt;div class="cube"&gt;
    &lt;div class="face front"&gt;Front&lt;/div&gt;
    &lt;div class="face back"&gt;Back&lt;/div&gt;
    &lt;!-- More faces --&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>
          
          <h3>Constraints:</h3>
          <ul>
            <li>Use only CSS (no JavaScript)</li>
            <li>Cube should be 200px × 200px × 200px</li>
          </ul>
        `;
        document.getElementById('code-editor').innerHTML = `.scene {
  /* Your 3D scene setup here */
}

.cube {
  /* Your cube transformation here */
}

/* Define faces and animations */`;
        
        document.getElementById('test-cases-container').innerHTML = `
          <div class="test-case">
            <div class="test-case-title">Case 1</div>
            <div class="test-case-content">Verify 3D cube structure with 6 faces</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 2</div>
            <div class="test-case-content">Verify continuous rotation</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
          <div class="test-case">
            <div class="test-case-title">Case 3</div>
            <div class="test-case-content">Verify hover pause effect</div>
            <div class="test-case-result">
              <i class="fas fa-clock"></i> Not Run
            </div>
          </div>
        `;
      }
      
      // Set language selector to CSS
      document.getElementById('language-selector').value = 'css';
      
      challengesList.style.display = 'none';
      challengeEditor.style.display = 'block';
      
      // Scroll to challenge editor
      window.scrollTo({
        top: challengeEditor.offsetTop - 80,
        behavior: 'smooth'
      });
    }

    function backToChallenges() {
      const challengesList = document.querySelector('.challenges-list');
      const challengeEditor = document.getElementById('challenge-editor');
      
      challengesList.style.display = 'grid';
      challengeEditor.style.display = 'none';
      
      // Scroll to challenges section
      window.scrollTo({
        top: document.getElementById('challenges').offsetTop - 80,
        behavior: 'smooth'
      });
    }

    // Tab switching in editor
    document.getElementById('solution-tab').addEventListener('click', function() {
      document.getElementById('solution-tab').classList.add('active');
      document.getElementById('output-tab').classList.remove('active');
      document.getElementById('code-editor').style.display = 'block';
      document.getElementById('output-tab-content').style.display = 'none';
    });

    document.getElementById('output-tab').addEventListener('click', function() {
      document.getElementById('output-tab').classList.add('active');
      document.getElementById('solution-tab').classList.remove('active');
      document.getElementById('output-tab-content').style.display = 'block';
      document.getElementById('code-editor').style.display = 'none';
    });

    // Add event listeners for editor buttons
    document.querySelector('.run-btn').addEventListener('click', function() {
      // Simulate running the code
      const testCases = document.querySelectorAll('.test-case-result');
      const outputContent = document.getElementById('output-tab-content');
      
      // Show output tab
      document.getElementById('output-tab').click();
      
      // Simulate output
      outputContent.textContent = "Running tests...\n";
      outputContent.textContent += "Test 1: Passed\n";
      outputContent.textContent += "Test 2: Passed\n";
      outputContent.textContent += "Test 3: Passed\n";
      outputContent.textContent += "\nAll tests passed successfully!";
      
      // Update test case results
      testCases.forEach(testCase => {
        testCase.className = 'test-case-result result-success';
        testCase.innerHTML = '<i class="fas fa-check-circle"></i> Passed';
      });
    });

    document.querySelector('.submit-btn').addEventListener('click', function() {
      // Simulate submitting the code
      const currentChallenge = document.getElementById('challenge-title').textContent;
      const difficulty = document.getElementById('challenge-difficulty').textContent;
      let points = 100;
      
      if (difficulty === 'Medium') points = 250;
      else if (difficulty === 'Hard') points = 500;
      
      alert(`Challenge "${currentChallenge}" submitted successfully! You earned ${points} points.`);
      backToChallenges();
    });
    // Initialize with all challenges visible
    filterChallenges('all');
  </script>
</body>
</html> 
