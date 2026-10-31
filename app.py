
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AuditPro Dashboard</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #080d1b;
    color: white;
}

.dashboard {
    display: flex;
    min-height: 100vh;
}

.sidebar {
    width: 250px;
    padding: 30px 22px;
    background: #10182b;
    border-right: 1px solid #25304a;
}

.logo {
    font-size: 24px;
    font-weight: bold;
    color: #8b9cff;
    margin-bottom: 55px;
}

.logo span {
    color: white;
}

.menu-label {
    color: #78849f;
    font-size: 12px;
    margin-bottom: 20px;
}

.nav-item {
    padding: 16px;
    margin-bottom: 10px;
    border-radius: 12px;
    color: #a9b4ca;
    cursor: pointer;
    transition: 0.3s;
}

.nav-item:hover,
.nav-item.active {
    background: linear-gradient(110deg, #5148d8, #765cf5);
    color: white;
    transform: translateX(5px);
}

.main {
    flex: 1;
    padding: 35px;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 45px;
    animation: fadeDown 0.8s ease;
}

.topbar p {
    color: #aab5cc;
    font-size: 13px;
    margin-bottom: 8px;
}

.profile {
    background: #18243b;
    padding: 13px 20px;
    border-radius: 30px;
    color: #b9c7e3;
}

.hero {
    padding: 45px;
    border-radius: 24px;
    background: linear-gradient(120deg, #302c91, #5c45d9, #8b5cf6);
    animation: fadeUp 0.9s ease;
    overflow: hidden;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 18px;
}

.hero p {
    color: #e1ddff;
    line-height: 1.8;
    max-width: 600px;
}

.hero button {
    margin-top: 25px;
    padding: 14px 24px;
    border: none;
    border-radius: 9px;
    background: white;
    color: #5145c9;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.hero button:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px #211b7080;
}

.section-title {
    margin: 38px 0 20px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.card {
    background: #131e34;
    border: 1px solid #263653;
    padding: 25px;
    border-radius: 17px;
    transition: 0.3s;
    animation: fadeUp 1s ease;
}

.card:hover {
    transform: translateY(-7px);
    border-color: #7668ff;
    box-shadow: 0 12px 30px #00000040;
}

.icon {
    font-size: 30px;
    margin-bottom: 20px;
}

.card h2 {
    font-size: 30px;
    color: #a99bff;
    margin-bottom: 10px;
}

.card p {
    color: #9baac4;
    font-size: 14px;
}

.status {
    display: inline-block;
    margin-top: 17px;
    color: #5ee6ae;
    font-size: 12px;
    background: #123c35;
    padding: 8px 12px;
    border-radius: 20px;
}

.footer {
    margin-top: 45px;
    color: #75839e;
    font-size: 12px;
    text-align: center;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 800px) {
    .sidebar {
        display: none;
    }

    .main {
        padding: 20px;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 30px 22px;
    }

    .hero h1 {
        font-size: 27px;
    }
}
</style>
</head>

<body>

<div class="dashboard">

    <aside class="sidebar">
        <div class="logo">Audit<span>Pro</span></div>

        <div class="menu-label">MAIN MENU</div>

        <div class="nav-item active">▦ Dashboard</div>
        <div class="nav-item">◈ Audit Overview</div>
        <div class="nav-item">▤ Reports</div>
        <div class="nav-item">✓ Compliance</div>
        <div class="nav-item">⚙ Settings</div>
    </aside>

    <main class="main">

        <header class="topbar">
            <div>
                <p>INTERNAL AUDIT MANAGEMENT</p>
                <h2>Dashboard Overview</h2>
            </div>

            <div class="profile">● Administrator</div>
        </header>

        <section class="hero">
            <h1>Welcome to AuditPro 👋</h1>

            <p>
                Take control of your organization's audit operations.
                Monitor compliance, track audit activities, and explore
                insights through your centralized audit dashboard.
            </p>

            <button onclick="document.getElementById('overview').scrollIntoView({behavior:'smooth'})">
                Explore Dashboard →
            </button>
        </section>

        <h2 class="section-title" id="overview">
            Audit Performance Overview
        </h2>

        <section class="cards">

            <div class="card">
                <div class="icon">📋</div>
                <h2>24</h2>
                <p>Total Audit Activities</p>
                <span class="status">● System Active</span>
            </div>

            <div class="card">
                <div class="icon">🛡️</div>
                <h2>92%</h2>
                <p>Compliance Score</p>
                <span class="status">● Demo Metric</span>
            </div>

            <div class="card">
                <div class="icon">📊</div>
                <h2>18</h2>
                <p>Completed Reports</p>
                <span class="status">● Demo Metric</span>
            </div>

        </section>

        <footer class="footer">
            © 2026 AuditPro | Internal Audit Management System
            <br><br>
            Secure • Reliable • Transparent
        </footer>

    </main>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

