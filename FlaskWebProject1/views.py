"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/blogs1')
def blogs1():
    """Renders the about page."""
    return render_template(
        'blogs1.html',
        title='Blogs1',
        year=datetime.now().year,
        message='Your blogs description page.'
    )

@app.route('/blogs2')
def blogs2():
    """Renders the about page."""
    return render_template(
        'blogs2.html',
        title='Blogs2',
        year=datetime.now().year,
        message='Your blogs description page.'
    )

@app.route('/devotionals1')
def devotionals1():
    """Renders the about page."""
    return render_template(
        'devotionals1.html',
        title='Devotionals1',
        year=datetime.now().year,
        message='Your devotionals description page.'
    )

@app.route('/devotionals2')
def devotionals2():
    """Renders the about page."""
    return render_template(
        'devotionals2.html',
        title='Devotionals2',
        year=datetime.now().year,
        message='Your devotionals description page.'
    )

@app.route('/testimonies1')
def testimonies1():
    """Renders the about page."""
    return render_template(
        'testimonies1.html',
        title='Testimonies1',
        year=datetime.now().year,
        message='Your devotionals description page.'
    )

@app.route('/testimonies2')
def testimonies2():
    """Renders the about page."""
    return render_template(
        'testimonies2.html',
        title='Testimonies2',
        year=datetime.now().year,
        message='Your devotionals description page.'
    )