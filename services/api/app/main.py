from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="beforeburn API",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
'''
@app.get("/welcome", response_class=HTMLResponse)
def welcome_check() -> str:
    return """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Started — BeforeBurn</title>
    <style>
        /* Modern Reset and Core Styles */
        :root {
            --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            --accent-glow: radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --card-bg: rgba(30, 41, 59, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --input-bg: rgba(15, 23, 42, 0.6);
            --radius: 12px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background: var(--bg-gradient);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            position: relative;
        }

        /* Subtle background glow effect */
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--accent-glow);
            z-index: 0;
            pointer-events: none;
        }

        /* Header / Navbar Navigation */
        header {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            z-index: 10;
        }

        .logo {
            font-size: 1.25rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(to right, #fff, var(--text-muted));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Main Hero Split Container */
        .hero-container {
            flex: 1;
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px 64px 24px;
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 64px;
            align-items: center;
            position: relative;
            z-index: 10;
        }

        /* Left Side Text Content */
        .hero-content h1 {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -1.5px;
            margin-bottom: 24px;
        }

        .hero-content h1 span {
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-content p {
            font-size: 1.15rem;
            line-height: 1.6;
            color: var(--text-muted);
            margin-bottom: 40px;
            max-width: 540px;
        }

        .features-list {
            list-style: none;
        }

        .features-list li {
            display: flex;
            align-items: center;
            margin-bottom: 16px;
            color: var(--text-main);
            font-size: 1rem;
        }

        .features-list li svg {
            margin-right: 12px;
            color: #34d399;
            flex-shrink: 0;
        }

        /* Right Side Fancy Glassmorphic Card Form */
        .form-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: var(--radius);
            padding: 40px;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .form-card h2 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
        }

        .form-card p {
            font-size: 0.9rem;
            color: var(--text-muted);
            margin-bottom: 28px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 8px;
            color: var(--text-main);
        }

        .form-group input {
            width: 100%;
            padding: 14px 16px;
            background: var(--input-bg);
            border: 1px solid var(--card-border);
            border-radius: 8px;
            color: #fff;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }

        .form-group input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }

        .submit-btn {
            width: 100%;
            padding: 14px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s ease, transform 0.1s ease;
            margin-top: 8px;
        }

        .submit-btn:hover {
            background: var(--primary-hover);
        }

        .submit-btn:active {
            transform: scale(0.98);
        }

        .form-footer {
            text-align: center;
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 20px;
            line-height: 1.4;
        }

        .form-footer a {
            color: var(--primary);
            text-decoration: none;
        }

        /* Responsive Layout Tweak for Mobile Screen Viewports */
        @media (max-width: 968px) {
            .hero-container {
                grid-template-columns: 1fr;
                gap: 48px;
                padding-top: 32px;
                text-align: center;
            }

            .hero-content h1 {
                font-size: 2.5rem;
            }

            .hero-content p {
                margin-left: auto;
                margin-right: auto;
            }

            .features-list {
                display: inline-block;
                text-align: left;
                margin-bottom: 16px;
            }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">beforeburn</div>
    </header>

    <main class="hero-container">
        <!-- Left Side Copy -->
        <section class="hero-content">
            <h1>Track productivity. <span>Prevent burnout.</span></h1>
            <p>Keep an eye on your workflow stability indicators. Connect your codebase, balance workloads, and protect your team's creative health seamlessly.</p>
            
            <ul class="features-list">
                <li>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    Real-time workload metrics pipeline
                </li>
                <li>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    Native integration with FastAPI applications
                </li>
                <li>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    Secure managed PostgreSQL infrastructure
                </li>
            </ul>
        </section>

        <!-- Right Side Registration Form -->
        <section class="form-card">
            <h2>Create your free account</h2>
            <p>No credit card required. Setup takes less than 2 minutes.</p>
            
            <form action="#" method="POST" onsubmit="event.preventDefault(); alert('Form testing submit success!');">
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input type="text" id="name" placeholder="John Doe" required autocomplete="name">
                </div>

                <div class="form-group">
                    <label for="email">Work Email</label>
                    <input type="email" id="email" placeholder="john@company.com" required autocomplete="email">
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" placeholder="••••••••" minlength="8" required autocomplete="new-password">
                </div>

                <button type="submit" class="submit-btn">Get Started Now</button>
            </form>

            <div class="form-footer">
                By signing up, you agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.
            </div>
        </section>
    </main>

</body>
</html>
'''