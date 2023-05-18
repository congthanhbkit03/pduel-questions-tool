
def xay_dung_file_tex(docx_filename, tieude, dscauhoi, dsdapan):
    # tao file - neu co thi xoa va tao lai
    with open(docx_filename + ".tex", 'w', encoding="utf-8") as f:
        # f.write('Create a new text file!')
        f.write("%!TEX xelatex")
        f.write("\n\\documentclass{book}")
        f.write("\n\\usepackage{moodle}")
        f.write("\n\\usepackage{graphicx}")
        f.write("\n\\usepackage{amssymb}")
        f.write("\n\\usepackage{amsmath}")
        f.write("\n\\begin{document}")
        f.write("\n\n")

        #in tieu de cho bai thi
        f.write("\n\\begin{quiz}{" + tieude+"}")
        # duyet qua tung cau hoi va tao trong tex
        for idx, cauhoi in enumerate(dscauhoi):
            f.write("\n\n\\begin{multi}[points=1]{Câu " + str(idx + 1) + "}")
            print(cauhoi.content)
            f.write(("\n" + cauhoi.content))    #noi dung cau hoi
            if dsdapan[idx] == 'A':
                f.write("\n\\item* " + cauhoi.opt1)
            else:
                f.write("\n\\item " + cauhoi.opt1)
            if dsdapan[idx] == 'B':
                f.write("\n\\item* " + cauhoi.opt2)
            else:
                f.write("\n\\item " + cauhoi.opt2)
            if dsdapan[idx] == 'C':
                f.write("\n\\item* " + cauhoi.opt3)
            else:
                f.write("\n\\item " + cauhoi.opt3)
            if dsdapan[idx] == 'D':
                f.write("\n\\item* " + cauhoi.opt4)
            else:
                f.write("\n\\item " + cauhoi.opt4)
            f.write("\n\\end{multi}")
        f.write("\n\n\\end{quiz}")
        f.write("\n\n\\end{document}")