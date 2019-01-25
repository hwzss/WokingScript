# encoding: utf8

# 将目录下的所有指定代码文件里的代码写入一个文件，用于软件著作权时需要特定页数的代码，代替手工一页一页复制代码到文件中
import os
 
code_file_path = "/Users/kaifa/Desktop/code.txt"  #代码汇总的文件的路径
files_dir_path = "/Users/kaifa/Desktop/Working/GitLab/express-ios/MC_Express/MC_Express/Classes"  #代码文件目录
pageLines = 50 #每页代码行数
maxPage = 60 #代码页数
code_file_suffix = ".m" #代码文件后缀

code_file = open(code_file_path, 'w')  
lineNum = 0
for parent, dirnames, filenames in os.walk(files_dir_path) :
	print ("gg", parent)                                  
	for filename in filenames :
		if os.path.splitext(filename)[1] == code_file_suffix :
			print (filename)
			abspath = os.path.join(parent, filename)
			f = open(abspath, 'r')
			for lines in f.readlines() :
				if lines.split() : 	            		
						lineNum += 1
						pageNum = lineNum / pageLines
						if pageNum > maxPage :	            			
								print ("end..., the page num is ", pageNum)
								code_file.close
								os._exit(0)
						code_file.write(lines)
			f.close			
