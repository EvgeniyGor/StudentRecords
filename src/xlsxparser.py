import xlrd
import json
def XLSXSheduleParser(schedulefilepath= '/home/nick1/PycharmProjects/untitled/etu/parser/FKTI_3(1).xlsx'):
    rb = xlrd.open_workbook(schedulefilepath,encoding_override="ascii") #,formatting_info=True
    sheet = rb.sheet_by_index(0)
    start_col = 3   #Can be various at different faculties
    start_row = 6   #Can be various at different faculties

    #day = 24+1 cells
    #lecture = 4 cells

    for groupNum in range(start_col,sheet.ncols):
        if sheet.cell_type(start_row-2,groupNum) == 0:
            continue
        group = {
            "Timetable": [
                {
                    "DayOfWeek": "Monday",
                    "IsFirstWeek": True,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Tuesday",
                    "IsFirstWeek": True,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Wednesday",
                    "IsFirstWeek": True,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Thursday",
                    "IsFirstWeek": True,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Friday",
                    "IsFirstWeek": True,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Monday",
                    "IsFirstWeek": False,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Tuesday",
                    "IsFirstWeek": False,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Wednesday",
                    "IsFirstWeek": False,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Thursday",
                    "IsFirstWeek": False,
                    "Lectures": []
                },
                {
                    "DayOfWeek": "Friday",
                    "IsFirstWeek": False,
                    "Lectures": []
                }
            ]

        }
        group['Group'] = int(sheet.cell_value(start_row-2,groupNum))
        for week in range(2):
            for day in range(5):
                for clock in range(6):
                    number = start_row + day * 25 + clock * 4 + week * 2
                    if sheet.cell_type(start_row + day * 25 + clock * 4 + week * 3,groupNum) == 0: continue
                    if sheet.cell_type(start_row + day * 25 + clock * 4 + week * 2, groupNum) != 0:
                        s1 = sheet.cell_value(start_row + day * 25 + clock * 4 + week * 2,groupNum)
                        group["Timetable"][day + week * 5]["Lectures"].append({"title": s1, "Number": clock})
                    else:
                        s1 = sheet.cell_value(start_row + day * 25 + clock * 4, groupNum)
                        group["Timetable"][day + week * 5]["Lectures"].append({"title": s1, "Number": clock})
        f = open('/home/nick1/PycharmProjects/untitled/etu/parser/' + str(group['Group']) + '.json', 'w')
        json.dump(group, f, indent=2)
        f.close()


XLSXSheduleParser()

