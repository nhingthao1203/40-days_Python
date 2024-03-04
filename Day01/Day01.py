def calculate_can_chi_calendar(year):
    can_list =["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính", "Đinh","Mậu","Kỷ"]
    chi_list =["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mẹo","Thìn","Tỵ","Ngọ","Mùi"]
    result = can_list[year%10] + ' '+chi_list[year%12]
    return result

print(calculate_can_chi_calendar(2003))
