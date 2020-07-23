import PySimpleGUI as sg

var = {'front': [], 'back': [], 'decimal': False, 'x_val': 0.0, 'y_val': 0.0, 'result': 0.0, 'operator': ''}


def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def update_display(display_value):
    try:
        calculator['_display_'].update(value="{:,.2f}".format(display_value))
    except:
        calculator['_display_'].update(value=display_value)


def number_click(event):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())


def clear_click():
    #CE or C button click event
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operator_click(event: str):
    #+ - / * button click event
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


def calculate_click():
    #Equals button click event
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()
    except:
        update_display("ERROR!")
        clear_click()


n = {'size': (5, 2), 'font': ('Arial', 14), 'button_color': ('Black', 'LightCyan')}
f = {'size': (5, 2), 'font': ('Arial', 14)}

layout = [
    [sg.Text('0.0', size=(9, 1), justification='right', font=('Arial', 37, 'bold'), background_color='black', key='_display_')],
    [sg.Button('CE', **f), sg.Button('<<', **f), sg.Button('%', **f), sg.Button('/', **f)],
    [sg.Button('7', **n), sg.Button('8', **n), sg.Button('9', **n), sg.Button('*', **f)],
    [sg.Button('4', **n), sg.Button('5', **n), sg.Button('6', **n), sg.Button('+', **f)],
    [sg.Button('1', **n), sg.Button('2', **n), sg.Button('3', **n), sg.Button('-', **f)],
    [sg.Button('0', **n), sg.Button('.', **n), sg.Button('+/-',  **n), sg.Button('=', **f, focus=True)]
]

calculator = sg.Window('Calculator', background_color='#696969', layout=layout)

while True:
    event, values = calculator.read()
    print(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        number_click(event)
    if event in ['Escape:27', 'CE', '<<']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+', '-', '*', '/']:
        operator_click(event)
    '''if event == '+/-':
        posneg_click()'''
    if event == '.':
        var['decimal'] = True
    if event == '=':
        calculate_click()
    if event == '%':
        update_display(var['result'] / 100.0)
    if event == sg.WIN_CLOSED:
        break
calculator.close()
