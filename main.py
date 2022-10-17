from flask import Flask, redirect, url_for, render_template
from application_vlados import *

app = Flask(__name__)


@app.route('/')
@app.route('/report/')
def report():
    structured_info = processing_data('files/start.log', 'files/end.log', 'files/abbreviations.txt')
    prepared_info_for_report = build_report(structured_info, 'asc')
    number_of_valid_racers = len([None for racer in prepared_info_for_report if racer.lap_time])
    racer_number_sequence = iter(range(1, number_of_valid_racers + 1))
    info_for_output = []
    for racer in prepared_info_for_report:
        if racer.lap_time:
            racers_number = next(racer_number_sequence)
            info_for_output.append((racers_number, racer.name, racer.team, racer.lap_time_str))
        else:
            info_for_output.append(('-', racer.name, racer.team, racer.lap_time_str))
    return render_template('report.html', info_for_output=info_for_output)


@app.route('/report/desc')
def report_desc():
    structured_info = processing_data('files/start.log', 'files/end.log', 'files/abbreviations.txt')
    prepared_info_for_report = build_report(structured_info, 'desc')
    number_of_valid_racers = len([None for racer in prepared_info_for_report if racer.lap_time])
    racer_number_sequence = iter(range(number_of_valid_racers, 0, -1))
    info_for_output = []
    for racer in prepared_info_for_report:
        if racer.lap_time:
            racers_number = next(racer_number_sequence)
            info_for_output.append((racers_number, racer.name, racer.team, racer.lap_time_str))
        else:
            info_for_output.append(('-', racer.name, racer.team, racer.lap_time_str))
    return render_template('report_desc.html', info_for_output=info_for_output)


@app.route('/report/drivers/')
def drivers():
    structured_info = processing_data('files/start.log', 'files/end.log', 'files/abbreviations.txt')
    prepared_info_for_report = build_report(structured_info, 'asc')
    number_of_valid_racers = len([None for racer in prepared_info_for_report if racer.lap_time])
    racer_number_sequence = iter(range(1, number_of_valid_racers + 1))
    info_for_output = []
    for racer in prepared_info_for_report:
        if racer.lap_time:
            racers_number = next(racer_number_sequence)
            info_for_output.append((racers_number, racer.name, racer.team, racer.lap_time_str, racer.abbreviation))
        else:
            info_for_output.append(('-', racer.name, racer.team, racer.lap_time_str, racer.abbreviation))
    return render_template('drivers.html', info_for_output=info_for_output)


@app.route('/report/drivers/desc')
def drivers_desc():
    structured_info = processing_data('files/start.log', 'files/end.log', 'files/abbreviations.txt')
    prepared_info_for_report = build_report(structured_info, 'desc')
    number_of_valid_racers = len([None for racer in prepared_info_for_report if racer.lap_time])
    racer_number_sequence = iter(range(number_of_valid_racers, 0, -1))
    info_for_output = []
    for racer in prepared_info_for_report:
        if racer.lap_time:
            racers_number = next(racer_number_sequence)
            info_for_output.append((racers_number, racer.name, racer.team, racer.lap_time_str, racer.abbreviation))
        else:
            info_for_output.append(('-', racer.name, racer.team, racer.lap_time_str, racer.abbreviation))
    return render_template('drivers_desc.html', info_for_output=info_for_output)


@app.route('/report/drivers/<abbreviation>')
def driver(abbreviation):
    structured_info = processing_data('files/start.log', 'files/end.log', 'files/abbreviations.txt')
    return render_template('driver.html', racer=structured_info[abbreviation])


if __name__ == '__main__':
    app.run(debug=True)