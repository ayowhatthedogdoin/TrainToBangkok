from flask import Flask, render_template, request, redirect, url_for, session
from .forcalculator import searchpath

def createweb():
    web = Flask(__name__)
    web.secret_key = 'secretsomuch'

    @web.route('/')
    def index():
        return render_template('Index.html')
    
    @web.route('/map')
    def map():
        return render_template('Map.html')

    @web.route('/calculator', methods=['POST', 'GET'])
    def calculator():
        if request.method == 'POST':
            current, want = request.form['stations'], request.form['stations2']
            session['current'], session['want'] = current, want
            if current != "stations1" and want != 'stations1':
                return redirect(url_for('calculated'))
            else:
                return render_template('Calculator.html')
        else:
            return render_template('Calculator.html')
        
    @web.route('/the_way')
    def calculated():
        if 'current' in session:
            current = session.pop('current')
            want = session.pop('want')
            station = searchpath(currentstation=current, wantstation=want)
            return render_template('Calculated.html', station=station)
        else:
            return redirect(url_for('calculator'))

    @web.route('/service')
    def service():
        return render_template('Service.html')

    return web
