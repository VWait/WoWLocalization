import xlrd


def search_card(text, cards):
    ids = []
    return ids


def parse_card_xls_to_sql(model_card):
    workbook = xlrd.open_workbook('main/static/xls/cards.xls')
    worksheet = workbook.sheet_by_index(0)

    args_names = worksheet.row_values(0, 0)
    rows_count = len(worksheet.col(0)) - 1
    rows_values = [worksheet.row_values(i, 0) for i in range(1, rows_count + 1)]

    for row in rows_values:
        card = model_card()
        for i in range(len(args_names)):
            if row[i] == '-':
                row[i] = None
            setattr(card, args_names[i], row[i])
        card.save()
