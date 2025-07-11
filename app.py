from flask import Flask, render_template

app = Flask(__name__)

departments = [
    {"name": "Procurement", "slug": "procurement"},
    {"name": "HR", "slug": "hr"},
    {"name": "Accounts", "slug": "accounts"},
    {"name": "Engineering", "slug": "engineering"},
    {"name": "Spareshop", "slug": "spareshop"},
    {"name": "Mechanical Engineering", "slug": "mechanical-engineering"},
    {"name": "Financial Management", "slug": "financial-management"},
    {"name": "Sales & Marketing", "slug": "sales-marketing"},
    {"name": "Purchase and Payables", "slug": "purchase-payables"},
]

@app.route('/')
def home():
    return render_template('index.html', departments=departments)

@app.route('/about')
def about():
    return render_template('about.html', departments=departments)

@app.route('/services')
def services():
    return render_template('services.html', departments=departments)

@app.route('/analytics')
def analytics():
    return render_template('analytics.html', departments=departments)

@app.route('/contact')
def contact():
    return render_template('contact.html', departments=departments)

@app.route('/department/<slug>')
def department(slug):
    dept = next((d for d in departments if d["slug"] == slug), None)
    if not dept:
        return render_template('404.html'), 404
    return render_template('department.html', department=dept)

@app.route('/blog')
def blog():
    return render_template('blog.html', departments=departments)

if __name__ == '__main__':
    app.run(debug=True)
