from .tool.func import *

def vote_2(conn):
    curs = conn.cursor()

    sql_num_1 = int(number_check(flask.request.args.get('num', '1')))
    sql_num = (sql_num_1 * 50 - 50) if sql_num_1 * 50 > 0 else 0

    data = ''
    if flask.request.args.get('close', 'n') == 'n':
        data += '<a href="/vote?close=y">(' + load_lang('close_vote_list') + ')</a>'
        sub = 0
        curs.execute(db_change('select name, id, type from vote where type = "open" or type = "n_open" limit ?, 50'), [sql_num])
    else:
        data += '<a href="/vote">(' + load_lang('open_vote_list') + ')</a>'
        sub = '(' + load_lang('closed') + ')'
        curs.execute(db_change('select name, id, type from vote where type = "close" or type = "n_close" limit ?, 50'), [sql_num])

    data += '<ul>'

    data_list = curs.fetchall()
    for i in data_list:
        if flask.request.args.get('close', 'n') == 'n':
            open_select = load_lang('open_vote') if i[2] == 'open' else load_lang('not_open_vote')
        else:
            open_select = load_lang('open_vote') if i[2] == 'close' else load_lang('not_open_vote')

        data += '<li><a href="/vote/' + i[1] + '">' + html.escape(i[0]) + ' (' + open_select + ')</a></li>'

    data += '</ul>'
    if flask.request.args.get('close', 'n') == 'n':
        data += ('<a href="/add_vote">(' + load_lang('add_vote') + ')</a>') if admin_check() == 1 else ''
        data += next_fix('/vote?num=', sql_num_1, data_list)
    else:
        data += next_fix('/vote?close=y&num=', sql_num_1, data_list)

    return easy_minify(flask.render_template(skin_check(),
        imp = [load_lang('vote_list'), wiki_set(), custom(), other2([sub, 0])],
        data = data,
        menu = [['other', load_lang('return')]]
    ))