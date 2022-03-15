def exam(update, context):
    found = 0
    chat_id = update.message.chat.id
    text = ''
    text_old = ''
    id = (context.args[0]).upper()

    file = open('Exam_timetable2.csv', 'r')
    if 'ccn' in id.lower():
        text_old = '走啦死老野'
    for row in csv.reader(file):
        if row[0] == id and found == 1:
            text = str(row[1] + '\n日期 : ' + row[2] +
                       '(' + row[3] + ') \n時間 : ' + row[4])
        if row[0] == id and found == 0:
            text = str(row[1] + '\n日期 : ' + row[2] +
                       '(' + row[3] + ') \n時間 : ' + row[4])
            found = 1
    if found == 0:
        context.bot.sendMessage(chat_id=chat_id, text='冇呢一科牙 ' + text_old)
    else:
        context.bot.sendMessage(
            chat_id=chat_id, text=text, parse_mode='Markdown')
