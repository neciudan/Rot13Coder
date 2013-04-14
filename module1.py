#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     07/10/2012
# Copyright:   (c) Dan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs=dict((m[:3].lower(),m)for m in months)

def valid_month(month):
    if month:
        short_month=month[:3].lower()
        return month_abbvs.get(short_month)
def valid_day(day):
    if day and day.isdigit():
        day=int(day)
        if day>0 and day<=31:
            return day
def valid_year(year):
    if year and year.isdigit():
        year=int(year)
        if year>1900 and year<=2020:
            return year

print valid_month('feb')
print valid_day('10,')

def escape_html(s):
    for(i,o) in (("&","&amp;"),(">","&gt;"),("<","&lt;"),('"',"&quote;")):
        s=s.replace(i,o)
    return s
print escape_html("<b>what</b>")