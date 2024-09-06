from flask import Flask, render_template, redirect, url_for, request
from modules import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    loaded_data = read_from_json()
    total_hours = get_total_hours()
    todays_date = get_date()
    return render_template('index.html', totalHours=total_hours, loadedData=loaded_data, todaysDate=todays_date)


@app.route('/remove/<id_to_remove>', methods=['GET'])
def remove(id_to_remove):
    remove_id(id_to_remove)
    return redirect(url_for('home'))


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        start_time = request.form['start-time']
        end_time = request.form['end-time']
        break_time = request.form['break-time']
        shift_date = request.form['shift-date']

        hours = calculate_hours(start_time, end_time, break_time)
        shift = f"{start_time}-{end_time}({break_time})"

        id_to_write = get_id()

        data = {
            'id': id_to_write,
            'hours': hours,
            'shift': shift,
            'date': shift_date,
        }
        save_to_json(data)

    return redirect(url_for('home'))


@app.route("/reset", methods=['GET'])
def reset():
    clear_json_file()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
